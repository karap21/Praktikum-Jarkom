# WebServer.py
import socket
import sys
import mimetypes
from pathlib import Path

HOST = ''                 # bind ke semua interface
PORT = 6789
BASE_DIR = Path.cwd()     # direktori kerja saat menjalankan server

def build_response_header(status_code, content_type, content_length):
    return f"HTTP/1.1 {status_code}\r\nContent-Type: {content_type}\r\nContent-Length: {content_length}\r\n\r\n".encode()

def handle_client(conn, addr):
    try:
        request = conn.recv(4096).decode(errors='ignore')
        if not request:
            print(f"[{addr}] Empty request, closing")
            conn.close()
            return

        # ambil baris request pertama dengan aman
        lines = request.splitlines()
        request_line = lines[0] if lines else ''
        print(f"[{addr}] Request line: {request_line}")

        parts = request_line.split()
        if len(parts) < 2:
            # kirim 400 Bad Request jika format salah
            body = b"<html><body><h1>400 Bad Request</h1></body></html>"
            header = build_response_header("400 Bad Request", "text/html", len(body))
            conn.sendall(header + body)
            conn.close()
            return

        method, path = parts[0], parts[1]
        if method != 'GET':
            body = b"<html><body><h1>405 Method Not Allowed</h1></body></html>"
            header = build_response_header("405 Method Not Allowed", "text/html", len(body))
            conn.sendall(header + body)
            conn.close()
            return

        # normalisasi path
        if path == '/':
            path = '/index.html'
        rel_path = path.lstrip('/')
        file_path = BASE_DIR / rel_path

        # fallback ke folder assets jika tidak ditemukan langsung
        if not file_path.exists():
            alt = BASE_DIR / 'assets' / rel_path
            if alt.exists():
                file_path = alt

        if file_path.exists() and file_path.is_file():
            content = file_path.read_bytes()
            content_type = mimetypes.guess_type(str(file_path))[0] or 'application/octet-stream'
            header = build_response_header("200 OK", content_type, len(content))
            conn.sendall(header + content)
            print(f"[{addr}] 200 OK -> {file_path}")
        else:
            body = b"<html><body><h1>404 Not Found</h1></body></html>"
            header = build_response_header("404 Not Found", "text/html", len(body))
            conn.sendall(header + body)
            print(f"[{addr}] 404 Not Found -> {rel_path}")

    except Exception as e:
        print(f"[{addr}] Exception:", e)
        body = b"<html><body><h1>500 Internal Server Error</h1></body></html>"
        header = build_response_header("500 Internal Server Error", "text/html", len(body))
        try:
            conn.sendall(header + body)
        except:
            pass
    finally:
        conn.close()

def run_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen(5)
        print(f"Server ready on port {PORT}...")
        try:
            while True:
                conn, addr = server.accept()
                # single-threaded handler, cukup untuk praktikum
                handle_client(conn, addr)
        except KeyboardInterrupt:
            print("\nServer dihentikan oleh user.")
        except Exception as e:
            print("Error server:", e)

if __name__ == "__main__":
    run_server()
