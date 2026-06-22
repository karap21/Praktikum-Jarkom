Pertama kita mengunjungi link disediakan dibawah ini, bertujuan unutuk memantau aktifitas jaringan ketika membuka link http dibawah.
![Screenshot Jarkom](Gambar/Screenshot%202026-06-22%20180720.png)

Setelah dibuka, link http berisi halaman seperti yang dapat dilihat dibawah. 
![Screenshot Jarkom](Gambar/Screenshot%202026-06-22%20180242.png)

 Buka Wireshark anda. Disini  kita akan menekan Wi-Fi karena kita menggunakan jairngan nirkabel, yaitu Wi-Fi kampus
 ![Screenshot Jarkom](Gambar/Screenshot%202026-06-22%20180253.png)
 ![Screenshot Jarkom](Gambar/Screenshot%202026-06-22%20180303.png)

 Ketika kita membuka Wi-Fi tersebut maka kita akan melihat banyak sekali lalu lintas jaringan yang terjadi dikomputer kita. Dipraktikum ini kita menggunakan protocol jaringan http, sesuai link yang kita buka baru saja, jadi kita filter menjadi http 
![Screenshot Jarkom](Gambar/Screenshot%202026-06-22%20180319.png)

Disini kita dapat melihat ada 4 aktifitas jaringan yang ada. Link yang baru saja kita buka, dapat kita lihat di paket 718 yang Dimana ip kita mengirim permintaan atau request kepada link wireshark tersebut yang berisikan file html, dan direspon oleh link, dengan mengirim file html  tersebut ke web kita yang ditandai dengan 200 ok. Smentara yang dibawha itu adlaah aktifitas yang berbeda.
![Screenshot Jarkom](Gambar/Screenshot%202026-06-22%20180335.png)