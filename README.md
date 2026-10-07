# GameZone Center

## 1. Deskripsi Program

GameZone Center merupakan program penyewaan konsol dan game yang dibuat menggunakan bahasa pemrograman Python dengan pendekatan Object-Oriented Programming (OOP).

Program ini digunakan untuk mengelola data konsol, game, pelanggan, serta transaksi penyewaan. Program juga memiliki fitur pengelolaan stok konsol, saldo pelanggan, validasi data, perhitungan biaya sewa, dan perhitungan denda keterlambatan.

Program dibuat dengan menerapkan materi OOP yang telah dipelajari, yaitu Class & Object, Atribut & Method, serta Encapsulation & Property.

## 2. Tujuan Program

Tujuan pembuatan program ini adalah:

* Menerapkan konsep Class dan Object dalam Python.
* Menerapkan atribut dan method pada setiap class.
* Menerapkan encapsulation menggunakan atribut private.
* Menggunakan property sebagai getter dan setter.
* Menerapkan instance method, class method, dan static method.
* Melakukan validasi terhadap data yang dimasukkan.
* Mengelola proses penyewaan konsol dan game.

## 3. Struktur Class

Program memiliki empat class utama, yaitu `Konsol`, `Game`, `Pelanggan`, dan `Penyewaan`.

### 3.1 Class Konsol

Class `Konsol` digunakan untuk menyimpan data konsol yang tersedia di GameZone Center.

**Atribut yang digunakan:**

* `nama_konsol` : nama konsol.
* `tipe_konsol` : tipe konsol seperti PS4 atau PS5.
* `__stok` : stok konsol yang bersifat private.
* `total_konsol_terdaftar` : jumlah objek konsol yang dibuat.
* `nama_game_center` : nama tempat.
* `harga_sewa_per_jam` : harga sewa konsol per jam.

**Method yang digunakan:**

* `tampilkan_info()` : menampilkan informasi konsol.
* `ubah_harga_sewa()` : class method untuk mengubah harga sewa.
* `validasi_tipe_konsol()` : static method untuk memvalidasi tipe konsol.
* `stok` : property untuk mengakses dan mengubah stok dengan validasi.

### 3.2 Class Game

Class `Game` digunakan untuk menyimpan data game yang tersedia.

**Atribut yang digunakan:**

* `judul` : judul game.
* `genre` : genre game.
* `__rating_usia` : rating usia yang bersifat private.
* `total_game_terdaftar` : jumlah objek game yang dibuat.

**Method yang digunakan:**

* `tampilkan_info()` : menampilkan informasi game.
* `validasi_genre()` : static method untuk memvalidasi genre.
* `rating_usia` : property untuk mengakses dan mengubah rating dengan validasi.

### 3.3 Class Pelanggan

Class `Pelanggan` digunakan untuk menyimpan data pelanggan dan saldo pelanggan.

**Atribut yang digunakan:**

* `nama` : nama pelanggan.
* `no_hp` : nomor handphone pelanggan.
* `__saldo` : saldo pelanggan yang bersifat private.
* `total_pelanggan` : jumlah objek pelanggan yang dibuat.
* `nama_tempat` : nama tempat.

**Method yang digunakan:**

* `top_up_saldo()` : menambahkan saldo pelanggan.
* `tampilkan_saldo()` : menampilkan informasi saldo pelanggan.
* `validasi_no_hp()` : static method untuk memvalidasi nomor handphone.
* `saldo` : property untuk mengakses dan mengubah saldo dengan validasi.

### 3.4 Class Penyewaan

Class `Penyewaan` digunakan untuk mengatur transaksi penyewaan antara pelanggan, konsol, dan game.

**Atribut yang digunakan:**

* `pelanggan` : objek pelanggan yang melakukan penyewaan.
* `konsol` : objek konsol yang disewa.
* `game` : objek game yang dimainkan.
* `durasi_jam` : durasi penyewaan.
* `__total_bayar` : total biaya penyewaan yang bersifat private.
* `total_transaksi` : jumlah transaksi yang dibuat.
* `nama_toko` : nama tempat penyewaan.
* `denda_telat_per_jam` : denda keterlambatan per jam.

**Method yang digunakan:**

* `hitung_total()` : menghitung total biaya sewa.
* `bayar()` : melakukan proses pembayaran penyewaan.
* `hitung_denda()` : menghitung denda keterlambatan.
* `cek_durasi_valid()` : static method untuk memvalidasi durasi penyewaan.
* `total_bayar` : property untuk mengakses total biaya penyewaan.

## 4. Konsep OOP yang Digunakan

### 4.1 Class dan Object

Program memiliki empat class utama, yaitu `Konsol`, `Game`, `Pelanggan`, dan `Penyewaan`.

Object dibuat dari masing-masing class. Contohnya:

```python
konsol1 = Konsol("Playstation 5", "PS5", 5)
konsol2 = Konsol("Playstation 4", "PS4", 3)
```

Object `konsol1` dan `konsol2` merupakan object dari class `Konsol`.

Selain itu, class `Penyewaan` menggunakan object dari class lain, yaitu object `Pelanggan`, `Konsol`, dan `Game`. Hal ini digunakan untuk menghubungkan data pelanggan, konsol, dan game dalam satu transaksi penyewaan.

### 4.2 Atribut

Program menggunakan atribut kelas dan atribut instance.

Atribut kelas digunakan untuk menyimpan data yang digunakan bersama oleh object. Contohnya:

```python
harga_sewa_per_jam = 10000
```

Sedangkan atribut instance memiliki nilai yang berbeda untuk setiap object, contohnya:

```python
self.nama_konsol = nama_konsol
self.tipe_konsol = tipe_konsol
```

Program juga menggunakan atribut public dan private. Atribut private ditandai dengan dua underscore, contohnya:

```python
self.__stok = stok
```

### 4.3 Method

Program menggunakan tiga jenis method.

**Instance method** digunakan untuk mengolah data object. Contohnya `top_up_saldo()`, `tampilkan_info()`, dan `bayar()`.

**Class method** menggunakan decorator `@classmethod` dan parameter `cls`. Contohnya:

```python
@classmethod
def ubah_harga_sewa(cls, harga_baru):
    cls.harga_sewa_per_jam = harga_baru
```

Method tersebut digunakan untuk mengubah harga sewa yang merupakan atribut kelas.

**Static method** menggunakan decorator `@staticmethod` dan tidak menggunakan `self` maupun `cls`. Contohnya:

```python
@staticmethod
def validasi_tipe_konsol(tipe):
    tipe_valid = ["PS4", "PS5", "Nintendo Switch"]
    return tipe in tipe_valid
```

Method tersebut digunakan untuk melakukan validasi tipe konsol.

### 4.4 Encapsulation dan Property

Encapsulation diterapkan dengan membuat beberapa atribut menjadi private, seperti `__stok`, `__rating_usia`, `__saldo`, dan `__total_bayar`.

Atribut private tersebut diakses menggunakan `@property` sebagai getter dan `@nama_property.setter` sebagai setter.

Setter juga memiliki validasi. Contohnya pada stok konsol:

```python
@stok.setter
def stok(self, stok_baru):
    if stok_baru < 0:
        print("Peringatan : stok tidak boleh negatif!")
    else:
        self.__stok = stok_baru
```

Jika stok yang diberikan bernilai negatif, perubahan data ditolak.

## 5. Cara Menjalankan Program

1. Pastikan Python sudah terinstall pada komputer.
2. Buka folder program melalui Visual Studio Code atau terminal.
3. Buka file Python program.
4. Jalankan program menggunakan terminal dengan perintah:

```bash
python 2509106076_MuhammadFachriAkbar_PT1.py
```

5. Program akan menampilkan data konsol, game, pelanggan, pengujian setter, pengujian method, transaksi penyewaan, dan denda.

## 6. Pengujian Program

### 6.1 Pengujian Setter

Pengujian setter dilakukan dengan memberikan data valid dan tidak valid.

**Data valid:**

* Stok konsol diubah menjadi `7`.
* Saldo Pari diubah menjadi `150000`.
* Rating usia game diubah menjadi `"T"`.

**Data tidak valid:**

* Stok diubah menjadi `-5`.
* Saldo diubah menjadi `-10000`.
* Rating usia diubah menjadi `"X"`.

Program akan menolak data yang tidak memenuhi validasi.

### 6.2 Pengujian Instance Method

Instance method diuji melalui method `top_up_saldo()` dan `tampilkan_saldo()`.

Saldo Pari ditambahkan sebesar Rp50.000 dan kemudian saldo ditampilkan kembali.

### 6.3 Pengujian Class Method

Class method diuji melalui:

```python
Konsol.ubah_harga_sewa(15000)
```

Harga sewa awal sebesar Rp10.000 per jam kemudian diubah menjadi Rp15.000 per jam.

### 6.4 Pengujian Static Method

Static method digunakan untuk melakukan validasi tanpa membutuhkan object tertentu.

Pengujian dilakukan terhadap:

* Tipe konsol.
* Genre game.
* Nomor handphone.
* Durasi penyewaan.

Data yang valid menghasilkan `True`, sedangkan data yang tidak valid menghasilkan `False`.

### 6.5 Pengujian Penyewaan

Dibuat dua transaksi penyewaan:

* Pari menyewa Playstation 5 dan memainkan EA Sports FC26 selama 2 jam.
* Akbar menyewa Playstation 4 dan memainkan Resident Evil Requiem selama 5 jam.

Setelah harga sewa diubah menjadi Rp15.000 per jam, biaya Pari adalah Rp30.000 dan biaya Akbar adalah Rp75.000.

Saldo Pari mencukupi sehingga pembayaran berhasil, sedangkan saldo Akbar tidak mencukupi.

### 6.6 Pengujian Denda

Pengujian denda dilakukan dengan:

* Keterlambatan 2 jam menghasilkan denda Rp10.000.
* Keterlambatan 0 jam menghasilkan denda Rp0.

## 7. Kesimpulan

Program GameZone Center telah menerapkan konsep Object-Oriented Programming menggunakan Python. Program memiliki empat class utama yang saling berinteraksi dan menerapkan Class & Object, Atribut & Method, serta Encapsulation & Property.

Program juga telah melakukan pengujian terhadap instance method, class method, static method, getter, setter, validasi data, transaksi penyewaan, dan perhitungan denda.


---

# Posttest 2 — Penambahan Relasi UML & Inheritance

## 8. Deskripsi Tambahan

Pada posttest kedua ini, program GameZone Center dikembangkan dengan menambahkan dua konsep baru, yaitu Relasi UML (Asosiasi, Agregasi, Komposisi) dan Inheritance (Pewarisan).

## 9. Relasi UML

### 9.1 Asosiasi

Relasi asosiasi diterapkan antara class `Pelanggan` dan class `Game` melalui atribut `game_favorit`.

Pelanggan dapat menunjuk ke sebuah objek `Game` sebagai game favoritnya melalui method `pilih_game_favorit()`. Kedua objek tetap independen satu sama lain; objek `Game` tetap dapat digunakan meskipun tidak dijadikan favorit oleh pelanggan manapun, dan objek `Pelanggan` tetap dapat digunakan meskipun belum memilih game favorit.

```python
def pilih_game_favorit(self, game):
    self.game_favorit = game
```

### 9.2 Agregasi

Relasi agregasi diterapkan antara class `Konsol` dan class `Game` melalui atribut `daftar_game`.

Objek `Game` dibuat secara terpisah di luar class `Konsol`, kemudian "dititipkan" ke konsol melalui method `tambah_game()`. Objek `Game` tersebut tetap dapat berdiri sendiri meskipun konsolnya dihapus atau diganti.

```python
def tambah_game(self, game):
    self.daftar_game.append(game)
```

### 9.3 Komposisi

Relasi komposisi diterapkan antara class `Penyewaan` dan class `NotaPembayaran`.

Objek `NotaPembayaran` hanya dibuat di dalam method `bayar()` milik class `Penyewaan`, dan tidak pernah dibuat secara terpisah dari luar. Objek nota ini bersifat eksklusif, hanya ada selama transaksi penyewaannya ada.

```python
self.nota = NotaPembayaran(self.pelanggan.nama, self.__total_bayar)
```

## 10. Inheritance

### 10.1 Superclass dan Subclass

Class `Konsol` dijadikan superclass (parent class), dengan dua subclass (child class) yaitu `KonsolPlayStation` dan `KonsolNintendo`.

* `KonsolPlayStation` memiliki atribut tambahan `jumlah_controller`.
* `KonsolNintendo` memiliki atribut tambahan `mode_portable`.

### 10.2 Penggunaan super()

Setiap subclass memanggil constructor superclass menggunakan `super().__init__()` sebelum menambahkan atribut miliknya sendiri.

```python
def __init__(self, nama_konsol, tipe_konsol, stok, kode_servis, jumlah_controller):
    super().__init__(nama_konsol, tipe_konsol, stok, kode_servis)
    self.jumlah_controller = jumlah_controller
```

### 10.3 Method Overriding

Method `tampilkan_info()` pada superclass `Konsol` di-override pada kedua subclass untuk menampilkan informasi tambahan yang berbeda-beda, dengan tetap memanggil method superclass menggunakan `super().tampilkan_info()`.

### 10.4 Tingkat Akses pada Pewarisan

Atribut `_stok` pada superclass `Konsol` dibuat protected agar dapat diakses dan dimanipulasi langsung oleh subclass, seperti pada method `servis_konsol()` milik `KonsolPlayStation`.

Atribut `__kode_servis` dibuat private karena bersifat rahasia dan hanya digunakan di dalam superclass melalui method `cek_kode_servis()`.

## 11. Pengujian Tambahan

### 11.1 Pengujian Inheritance

Objek `konsol1` dibuat dari subclass `KonsolPlayStation` dan `konsol2` dari subclass `KonsolNintendo`. Kedua objek tetap dikenali sebagai instance dari superclass `Konsol` melalui pengujian `isinstance()`.

### 11.2 Pengujian Akses Protected pada Subclass

Method `servis_konsol()` pada `KonsolPlayStation` mengakses dan mengubah atribut protected `_stok` milik superclass secara langsung, membuktikan bahwa subclass dapat memanipulasi data protected tanpa melalui property.

### 11.3 Pengujian Relasi UML

* Asosiasi diuji dengan memanggil `pilih_game_favorit()` pada objek `Pelanggan`.
* Agregasi diuji dengan memanggil `tambah_game()` pada objek `Konsol`.
* Komposisi diuji dengan memanggil `bayar()` pada objek `Penyewaan`, yang secara otomatis membuat objek `NotaPembayaran`.

## 12. Kesimpulan Tambahan

Program GameZone Center pada posttest kedua ini telah menerapkan konsep Relasi UML berupa Asosiasi, Agregasi, dan Komposisi, serta konsep Inheritance berupa superclass, subclass, penggunaan `super()`, method overriding, dan pengaturan tingkat akses protected dan private pada pewarisan.