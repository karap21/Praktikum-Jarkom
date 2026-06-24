### Laporan Praktikum Modul 9 — Ringkas (README.md)

```markdown
# Laporan Praktikum Jaringan Komputer Modul 9

**Praktikan:** **Haniel Juanta Sembiring**  
**NIM:** **103072400145**  
**Kelas:** **IF-04-01**

### Tujuan
Membuat web server sederhana menggunakan Python socket, memahami format HTTP request/response, menangani file request dan error 404, serta menguji menggunakan browser dan `curl`.

### Struktur File
```
modul09/
├── WebServer.py
├── HelloWorld.html        # atau assets/HelloWorld.html
├── Readme.md
└── Gambar/
    ├── 1.png
    ├── 2.png
    ├── 3.png
    └── 4.png
```

### Cara Menjalankan Server
1. Buka terminal di folder `modul09`:
   ```bash
   cd /path/to/modul09
   python WebServer.py
   ```
2. Pastikan muncul: **Server ready on port 6789...**
3. Akses halaman:
   - Jika `HelloWorld.html` di root:
     ```
     http://localhost:6789/HelloWorld.html
     ```
   - Jika di folder `assets`:
     ```
     http://localhost:6789/assets/HelloWorld.html
     ```

### Screenshot untuk Laporan
- **1. Kode HTML HelloWorld**  
  `![](Gambar/1.png)`  
  *Ambil setelah membuka HelloWorld.html di editor (menunjukkan identitas: Nama, NIM, Kelas).*

- **2. Tampilan Halaman di Browser (200 OK)**  
  `![](Gambar/2.png)`  
  *Ambil saat browser menampilkan halaman HelloWorld.html sukses.*

- **3. Terminal Server Menjalankan dan Log Request**  
  `![](Gambar/3.png)`  
  *Ambil saat server menampilkan `Server ready on port 6789...` dan log `Request line` serta `200 OK`.*

- **4. Browser Menampilkan 404 Not Found**  
  `![](Gambar/4.png)`  
  *Ambil saat mengakses file yang tidak ada untuk menunjukkan response 404.*

### Hasil Singkat
- Server berhasil melayani request dan mengembalikan **200 OK** untuk file yang ada.  
- Server mengembalikan **404 Not Found** untuk file yang tidak ada.  
- `Content-Type: text/html` dan body HTML dikirim sesuai standar.

### Kesimpulan
Web server sederhana berjalan baik pada port **6789**. Dokumentasi dilengkapi dengan empat screenshot: kode HTML, tampilan browser 200, log terminal, dan tampilan 404.

```

