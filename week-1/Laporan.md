# Laporan Praktikum Jaringan Komputer - Modul 2
## Pengenalan Tools dan Test Run Wireshark

### Identitas Praktikan
| Item | Keterangan |
|------|------------|
| **Nama** | Haniel Juanta Sembiring |
| **NIM** | [103072400145] |
| **Kelas** | [IF-04-01] |

---

## 1. Tujuan Praktikum
Berdasarkan modul praktikum Jaringan Komputer, tujuan dari Modul 2 adalah:
1. Mahasiswa dapat melakukan instalasi tool yang digunakan (Wireshark).
2. Mahasiswa dapat menggunakan tool (Wireshark) untuk menangkap dan mengidentifikasi paket data.

---

## 2. Persiapan Tools
Sebelum memulai praktikum, dilakukan pengecekan tools yang wajib digunakan untuk melakukan *packet sniffing*.

### 2.1 Wireshark
Wireshark adalah aplikasi *packet analyzer* gratis yang digunakan untuk mengamati pesan yang bertukar antara entitas protokol dalam jaringan.
- **Status:** Terinstall
- **Link Download:** [www.wireshark.org](http://www.wireshark.org/download.html)

---

## 3. Langkah Kerja
Berikut adalah langkah-langkah utama yang dilakukan selama praktikum Modul 2 untuk melakukan *test run* penangkapan jaringan:
1. Menyiapkan aplikasi Wireshark dan *web browser*.
2. Memilih *interface* jaringan yang aktif dan memulai proses tangkap jaringan (*capture*).
3. Mengakses tautan HTTP spesifik untuk memicu pertukaran paket data.
4. Menghentikan proses *capture* dan menganalisis paket yang berhasil ditangkap.

---

## 4. Hasil dan Pembahasan

### 4.1 Mengakses Tautan Target
Pertama, kita mengunjungi tautan yang disediakan di bawah ini. Tujuannya adalah untuk memantau aktivitas jaringan ketika membuka tautan HTTP tersebut.

![Screenshot Tautan Target](Gambar/Screenshot%202026-06-22%20180720.png)

Setelah dibuka, tautan HTTP tersebut akan menampilkan halaman seperti pada gambar di bawah ini.

![Screenshot Halaman Web](Gambar/Screenshot%202026-06-22%20180242.png)

### 4.2 Memilih Interface pada Wireshark
Selanjutnya, buka aplikasi **Wireshark**. Di sini kita akan memilih *interface* **Wi-Fi** karena kita menggunakan jaringan nirkabel (Wi-Fi kampus).

![Screenshot Interface Wi-Fi 1](Gambar/Screenshot%202026-06-22%20180253.png)

![Screenshot Interface Wi-Fi 2](Gambar/Screenshot%202026-06-22%20180303.png)

### 4.3 Memfilter Protokol HTTP
Setelah memilih *interface* Wi-Fi tersebut, kita akan melihat banyak sekali lalu lintas jaringan yang sedang berjalan di komputer. Pada praktikum ini, kita secara spesifik memantau protokol HTTP sesuai dengan tautan yang baru saja kita buka. Oleh karena itu, kita perlu memfilternya dengan mengetikkan `http` pada kolom filter.

![Screenshot Filter HTTP](Gambar/Screenshot%202026-06-22%20180319.png)

### 4.4 Analisis Paket Data
Pada hasil *filter*, dapat dilihat bahwa terdapat **4 aktivitas jaringan HTTP**. Aktivitas dari tautan yang baru saja kita buka dapat dilihat pada **paket 718**. 

> 🔍 **Analisis Paket 718:** > IP komputer kita mengirimkan permintaan (*HTTP GET request*) kepada *server* tautan Wireshark yang berisikan file HTML. *Server* kemudian merespons dengan mengirimkan file HTML tersebut ke *web browser* kita, yang ditandai dengan status pesan **`200 OK`**. 

Sementara itu, paket-paket yang berada di bawahnya merupakan aktivitas jaringan yang berbeda.

![Screenshot Analisis Paket](Gambar/Screenshot%202026-06-22%20180335.png)

---

## 5. Kesimpulan
Berdasarkan praktikum Modul 2 ini, dapat disimpulkan bahwa:
1. Praktikan telah berhasil memahami fungsi utama dari Wireshark sebagai *Packet Sniffer* dan *Packet Analyzer*.
2. Praktikan mampu melakukan proses *capture* lalu lintas jaringan menggunakan *interface* yang tepat (Wi-Fi/Ethernet).
3. Praktikan berhasil memancing lalu lintas data spesifik menggunakan protokol HTTP dengan mengakses tautan target yang telah disediakan, yang mana data tersebut kemudian berhasil direkam oleh Wireshark.