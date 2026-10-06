# MINPRO-2-DDP-Sistem Manajemen Pengelolaan Kamar Hotel

Nama : Brian Hotlan Sitompul

NIM : 2609116035

Kelas : A

# Penjelasan Singkat
Sistem Manajemen Pengelolaan Kamar Hotel adalah sistem yang memudahkan admin untuk mengelola kamar hotel dan memudahkan user untuk memesan kamar hotel. Isi dari project ini ada CRUD admin dan CRUD user

# Flowchart Login

<img width="713" height="538" alt="LoginFixBanget drawio" src="https://github.com/user-attachments/assets/35ffcc91-4026-4023-8198-6f35fa3464f5" />

Flowchart halaman utama mulai dari proses login. Setelah berhasil login sistem membedakan Akses yang dimiliki oleh Admin dan User

# FLowchart Admin

<img width="1520" height="1159" alt="AdminFixBanget drawio" src="https://github.com/user-attachments/assets/920db688-c2ca-4dc1-89f1-b05d80a69594" />

### Penjelasan Flowchart - Halaman Admin
Flowchart ini menggambarkan seluruh alur kerja dan logika pada halaman Admin, mulai dari menampilkan menu utama hingga proses pengolahan data kamar yang dilengkapi dengan sistem perulangan.

Menampilkan Menu Admin
Setelah berhasil masuk dari login Admin, sistem akan menampilkan daftar opsi menu utama Admin. Seluruh keluaran dari Pilihan 1 sampai 4, termasuk pesan sukses, pesan error, serta opsi input yang tidak valid, akan diputar kembali ke menu utama Admin sampai pengguna memutuskan untuk keluar.

### Rincian Alur 

Pada Pilihan 1 untuk Lihat Data Kamar, sistem akan memanggil dan menampilkan seluruh data kamar hotel yang tersimpan, kemudian alur langsung kembali ke Menu Admin.

Pada Pilihan 2 untuk Tambah Data Kamar, Admin menginput nomor kamar baru. Jika nomor kamar valid, data akan disimpan dan sistem menampilkan pesan bahwa data berhasil ditambahkan. Sebaliknya, jika nomor tidak valid atau sudah ada, sistem menampilkan pesan data tidak ditemukan, lalu alur kembali ke Menu Admin.

Pada Pilihan 3 untuk Ubah Data Kamar, Admin menginput nomor kamar yang ingin diperbarui. Jika nomor kamar valid, sistem menampilkan detail data kamar terkini, lalu Admin memasukkan tipe kamar baru dan status kamar baru. Sistem akan menetapkan harga secara otomatis berdasarkan tipe yang dipilih dan menampilkan pesan bahwa data berhasil diperbarui. Jika nomor kamar tidak valid, muncul pesan bahwa data tidak ditemukan, dan alur berputar kembali ke Menu Admin.

Pada Pilihan 4 untuk Hapus Data Kamar, Admin menginput nomor kamar yang akan dihapus. Jika nomor kamar valid, data dihapus dari database dan sistem menampilkan pesan bahwa data berhasil dihapus. Jika nomor tidak valid, muncul pesan data tidak ditemukan, kemudian alur kembali ke Menu Admin.

Pada Pilihan 5 untuk Keluar, jika Admin memilih opsi ini, sistem akan menghentikan perulangan menu Admin, mengembalikan akses ke Menu Utama, dan mengakhiri sesi. Jika Admin memasukkan angka di luar opsi 1 sampai 5, alur secara otomatis diputar kembali ke tampilan Menu Admin.

# Flowchart User

<img width="2747" height="1180" alt="UserFixBanget drawio (1)" src="https://github.com/user-attachments/assets/1bc966b4-6b5c-4666-a805-47dbe7fb10ef" />


### Penjelasan Flowchart - Halaman User

Flowchart ini menggambarkan alur kerja dan logika pada halaman User, mulai dari akses menu utama, pemesanan kamar, perubahan pesanan, transaksi pembayaran, hingga alur keluar dari sistem.

**Menampilkan Menu User**
Setelah memilih opsi User, sistem akan menampilkan daftar menu yang dapat diakses oleh pelanggan. Setiap selesai menjalankan sebuah proses pada pilihan menu atau ketika input yang dimasukkan tidak valid, alur sistem akan berputar kembali ke tampilan Menu User.

**Rincian Alur Menu**

Pada Pilihan 1 untuk Lihat Data Kamar, sistem memanggil fungsi untuk menampilkan daftar dan status seluruh kamar hotel yang tersedia, kemudian alur langsung kembali ke Menu User.

Pada Pilihan 2 untuk Booking Kamar, sistem terlebih dahulu menampilkan data kamar lalu meminta pengguna menginput nomor kamar yang ingin dipesan. Sistem mengecek apakah nomor kamar valid dan apakah status kamar dalam keadaan kosong. Jika nomor kamar tidak valid atau status kamar terisi, sistem menampilkan pesan peringatan dan meminta input ulang. Jika kamar valid dan kosong, pengguna menginput durasi menginap, sistem menghitung total harga, menampilkan rincian detail pesanan, lalu alur kembali ke Menu User.

Pada Pilihan 3 untuk Ubah Pesanan, sistem menampilkan rincian pesanan saat ini. Pengguna dapat memilih untuk mengubah durasi atau mengganti kamar. Jika memilih ubah durasi, pengguna memasukkan durasi baru dan sistem menampilkan rincian pesanan yang telah diperbarui. Jika memilih ganti kamar, pengguna menginput nomor kamar baru, sistem melakukan validasi nomor dan ketersediaan status kamar, lalu pengguna memasukkan durasi menginap, sistem menghitung total harga baru, menampilkan detail pesanan, dan alur kembali ke Menu User.

Pada Pilihan 4 untuk Pembayaran, sistem mengecek terlebih dahulu apakah pengguna sudah melakukan booking kamar. Jika belum, sistem menampilkan pesan bahwa pengguna belum memiliki pesanan lalu kembali ke menu utama. Jika sudah ada pesanan, sistem menampilkan rincian biaya dan meminta nominal pembayaran. Sistem memeriksa kecukupan uang pembayaran. Jika pembayaran kurang, transaksi dinyatakan gagal dan pengguna diminta memasukkan nominal kembali. Jika pembayaran cukup, sistem menampilkan pesan transaksi berhasil lalu alur kembali ke Menu User.

Pada Pilihan 5 untuk Keluar, sistem menghentikan perulangan menu User, mengembalikan akses ke Menu Utama, dan mengakhiri sesi. Jika pengguna memasukkan input di luar opsi 1 sampai 5, alur secara otomatis diputar kembali ke tampilan Menu User.


# ALUR PROGRAM ADMIN
### LOGIN ADMIN

<img width="416" height="355" alt="image" src="https://github.com/user-attachments/assets/cc294dc8-b562-4b07-919b-c6a6d2783cf7" />


Output Ketika Berhasil Login sebagai Admin, menggunakan username : admin dan password : admin123
saya menggunakan import pwinput untuk menyembunyikan password


### Fitur Admin
# 1. Tampilkan Daftar Kamar

<img width="625" height="407" alt="image" src="https://github.com/user-attachments/assets/c4d5a31b-85bc-4f02-8b10-4cd7aa501003" />


Berikut Output ketika saya memilih pilihan "1" akan muncul daftar kamar - kamar yang tersedia

# 2. Tambah Data Kamar

<img width="662" height="220" alt="image" src="https://github.com/user-attachments/assets/a8c9fdc1-c413-488e-a240-c29b4cc3a395" />

Berikut adalah tambah data kamar admin dapat menambahkan data kamar kemudian memasukkan nomor kamar yang valid, setelah itu memilih tipe kamar yang sebelumnya setiap tipe kamar sudah memiliki harga masing - masing (Biasa : Rp.100.000), (Bagus : Rp. 200.000) dan (VIP : 300.000)

<img width="380" height="248" alt="image" src="https://github.com/user-attachments/assets/608f2a20-8385-483e-91ae-a220e3bdd80c" />

Berikut adalah output ketika data kamar sudah ada dalam tabel

# 3. Ubah Data Kamar

<img width="798" height="715" alt="image" src="https://github.com/user-attachments/assets/7c13ed56-9ee0-4230-9f42-f52738db7f39" />

Berikut adalah Output Ubah Data Kamar. Pertama admin harus menginput nomor kamar yang valid dan tersedia di tabel, jika sudah valid akan tampil data kamar yang dipilih dengan rincian sebelum diubah. Setelah itu admin dapat memilih tipe kamar baru, admin dapat mengubah sesuka hati mulai dari Biasa, Bagus, dan VIP setelah memilih tipe admin dapat memilih status kamar baru antara Kosong, Terisi dan Dibooking atau admin juga bisa menekan enter langsung jika tidak ingin mengubah status kamar.

# 4. Hapus Data Kamar

<img width="737" height="515" alt="image" src="https://github.com/user-attachments/assets/b965ea60-74ba-4040-95e8-a26259a0897b" />

Output ketika admin memilih pilihan = 4 yaitu menghapus data kamar, admin harus menginput nomor kamar yang valid jika ingin menghapus data kamar, jika valid maka data berhasil dihapus.

<img width="455" height="95" alt="image" src="https://github.com/user-attachments/assets/537e313f-5271-4cfa-9fd7-e7e6d36330d4" />

Output jika admin menginput nomor kamar tidak valid

# 5. Keluar

<img width="656" height="443" alt="image" src="https://github.com/user-attachments/assets/0a26e76a-41ba-4e06-9284-7175bf7e36f1" />


Output jika sudah selesai menggunakan layanan akan muncul kata "Terimakasih Telah Menggunakan Layanan Kami" dan admin melakukan log out

# ALUR PROGRAM USER
### LOGIN USER

<img width="417" height="383" alt="image" src="https://github.com/user-attachments/assets/9e5c7c57-f5b4-420b-bb23-1ed2a7b88f87" />

Output ketika berhasil dengan role User. Login menggunakan user = user dan password = user123

### Fitur User
# 1. Tampilkan Daftar Kamar

<img width="626" height="477" alt="image" src="https://github.com/user-attachments/assets/dd48614d-440c-437e-a944-4b5c017e57d2" />

Output ketika user menginput = 1 akan muncul daftar - daftar kamar hotel yang tersedia

# 2. Booking Kamar

<img width="632" height="601" alt="image" src="https://github.com/user-attachments/assets/fe63481b-abb9-4a19-a65c-f648839ddf72" />

Output ketika user menginput = 2 (Booking Kamar). User memilih nomor kamar dan wajib 'kosong' kemudian mengisi durasi menginap dalam hitungan hari dan sistem akan menentukan total harga. 

<img width="676" height="292" alt="image" src="https://github.com/user-attachments/assets/fb382f01-f2b7-40a3-9ff2-ca4159969052" />

Output ketika user memilih kamar yang 'terisi'

# 3. Lihat / Ubah Pesanan

<img width="701" height="772" alt="image" src="https://github.com/user-attachments/assets/e96723eb-f44e-4288-9441-21825ebbfdbc" />

Output ketika user menginput = 3 (Lihat/Ubah pesanan) akan muncul detail pesanan yang sudah dibooking sebelumnya serta akan muncul pilihan ubah pesanan dan jika user menginput = 1 (Ubah durasi hari) maka user harus mengisi durasi menginap yang baru berupa angka ketika sudah valid sistem akan mengeluarkan output rincian pesanan yang baru.

<img width="663" height="767" alt="image" src="https://github.com/user-attachments/assets/39d7ba34-58eb-41e8-bbdb-a65c66aad221" />

Output ketika user menginput = 2 (Pilih kamar lain) akan muncul nomor kamar baru yang ingin dibooking. Jika user memilih nomor kamar yang valid, ada di tabel serta status 'kosong' akan lanjut ke durasi penginapan yang baru, user harus mengisi durasi menginap yang baru harus berupa angka. Kemudia jika semua sudah valid akan muncul rincian pesanan terbaru serta nominal pembayaran. 

# 4. Pembayaran

<img width="782" height="655" alt="image" src="https://github.com/user-attachments/assets/aa2cb658-ad00-4e9a-b99a-6616678f589a" />

Output ketika user menginput = 4(Pembayaran). Akan muncul rincian pesanan secara lengkap dan user harus memasukkan nominal uang yang harus dibayarkan ketika pembayaran >= total harga maka transaksi sukses dilakukan dan akan ada struk pembayaran.

<img width="602" height="285" alt="image" src="https://github.com/user-attachments/assets/46994fbb-e4a0-41cd-8e81-ba59bdd3c541" />

Output jika gagal melakukan pembayaran karena nominal pembayaran tidak cukup.

# 5. Keluar

<img width="457" height="280" alt="image" src="https://github.com/user-attachments/assets/4ca20658-c0bb-4694-99fa-ac2905ba9409" />

Output ketika user menginput = 5(Keluar) akan melakukan log out.





















