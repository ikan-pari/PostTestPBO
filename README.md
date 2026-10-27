# GameZone Center — Posttest 4

## 1. Deskripsi Program

GameZone Center adalah program penyewaan konsol dan game yang dibuat dengan Python menggunakan pendekatan Object-Oriented Programming (OOP). Program mengelola data konsol, game, pelanggan, dan transaksi penyewaan, termasuk saldo pelanggan, perhitungan biaya sewa per jenis konsol, nota pembayaran, laporan transaksi, dan denda keterlambatan.

Pada Posttest 4 program dikembangkan dengan menerapkan **Abstraksi (Abstract Base Class)** dan **Polimorfisme** (polimorfisme via pewarisan, duck typing, dan operator overloading), serta tetap memakai konsep Posttest 1 dan 2 (class, atribut, method, encapsulation, relasi UML, inheritance).

## 2. Class Diagram

![Class Diagram GameZone Center](images/class_diagram.png)

### 2.1 Asosiasi — `Pelanggan` → `Game`

Class `Pelanggan` menyimpan atribut `game_favorit` yang menunjuk ke sebuah objek `Game` lewat method `pilih_game_favorit()`. Relasi ini asosiasi karena kedua objek hanya saling "mengenal": `Pelanggan` tetap valid tanpa game favorit dan `Game` tetap ada walaupun tidak dipilih siapa pun.

### 2.2 Agregasi — `Konsol` ◇→ `Game`

Class `Konsol` memiliki atribut `daftar_game` yang berisi objek `Game` yang dibuat di luar `Konsol`, lalu ditambahkan lewat `tambah_game()`. Dipilih agregasi (bukan komposisi) karena `Game` dapat berdiri sendiri dan tetap ada walaupun konsolnya dihapus; satu `Game` bahkan dapat dipasang di lebih dari satu konsol (contoh: Resident Evil Requiem ada di PS5 dan Switch).

### 2.3 Komposisi — `Penyewaan` ◆→ `NotaPembayaran`

Objek `NotaPembayaran` dibuat di dalam method `bayar()` milik `Penyewaan` dan disimpan di atribut `nota`. Dipilih komposisi (bukan agregasi) karena nota hanya berarti untuk satu transaksi: ia tidak pernah dibuat dari luar dan tidak punya makna tanpa `Penyewaan` yang memilikinya.

### 2.4 Relasi lain pada diagram

* **Pewarisan**: `KonsolPlayStation`, `KonsolNintendo`, dan `KonsolXbox` mewarisi `Konsol`.
* **Asosiasi**: `Penyewaan` menyimpan objek `Pelanggan`, `Konsol`, dan `Game`.

## 3. Abstraksi

* **Abstract class**: `Konsol(ABC)`.
* **Abstract method** (2): `hitung_biaya_sewa(durasi_jam)` dan `info_spesifik()`.
* **Subclass** yang mengimplementasikan seluruh abstract method: `KonsolPlayStation`, `KonsolNintendo`, `KonsolXbox`.
* **Method konkret** yang dipakai bersama semua subclass: `tampilkan_info()`, `tambah_game()`, `cek_kode_servis()`.
* **Inheritance tetap dipakai**: setiap subclass memanggil `super().__init__(...)` dan punya atribut unik (`jumlah_controller`, `mode_portable`, `punya_game_pass`). Atribut `_stok` bersifat protected (diakses langsung oleh `KonsolPlayStation.servis_konsol()`), sedangkan `__kode_servis` bersifat private khusus superclass.
* **Bukti abstract class tidak bisa diinstansiasi**: lihat bagian screenshot (`TypeError`).

## 4. Polimorfisme

* **Polimorfisme via pewarisan**: method `hitung_biaya_sewa()` dan `info_spesifik()` di-override oleh tiga subclass dengan perilaku berbeda (PS: tambahan biaya per controller, Nintendo: diskon portable, Xbox: biaya Game Pass). Dipanggil dalam satu loop atas list berisi objek `KonsolPlayStation`, `KonsolNintendo`, dan `KonsolXbox`. `Penyewaan.hitung_total()` juga memanggil `self.konsol.hitung_biaya_sewa()` tanpa pengecekan jenis konsol.
* **Duck typing**: `NotaPembayaran` dan `LaporanTransaksi` tidak berhubungan lewat pewarisan, tetapi sama-sama punya method `cetak()`. Keduanya dipanggil lewat fungsi yang sama, `proses_cetak(dokumen)`.
* **Operator overloading**: `Konsol.__len__()` (jumlah game pada konsol), `Game.__str__()` (representasi teks game), dan `Penyewaan.__lt__()` (membandingkan penyewaan berdasarkan total biaya sehingga dapat diurutkan dengan `sorted()`).
* **Tanpa anti-pattern**: tidak ada rantai `if/elif` yang mengecek `type()` atau string jenis konsol; perilaku ditentukan oleh method tiap objek.

## 5. Penerapan SOLID (Nilai Plus)

* **OCP (Open/Closed Principle)**: class `KonsolXbox` ditambahkan sebagai subclass baru tanpa mengubah kode `Penyewaan` maupun subclass lain. Jenis konsol baru cukup dibuat dengan mengimplementasikan abstract method `Konsol`.
* **DIP (Dependency Inversion Principle)**: `Penyewaan` bergantung pada abstraksi `Konsol` (objek konsol diberikan lewat constructor), bukan pada subclass konkret tertentu.

## 6. Cara Menjalankan Program

1. Pastikan Python sudah terinstall.
2. Buka folder program di Visual Studio Code atau terminal.
3. Jalankan:

```bash
python 2509106076_MuhammadFachriAkbar_PT4.py
```

## 7. Screenshot Output

### 7.1 Bukti abstract class tidak bisa diinstansiasi

![Bukti Abstraksi](images/output_abstraksi.png)

Output yang muncul:

```text
TypeError: Can't instantiate abstract class Konsol without an implementation for abstract methods 'hitung_biaya_sewa', 'info_spesifik'
```

### 7.2 Polimorfisme via pewarisan

![Polimorfisme](images/output_polimorfisme.png)

### 7.3 Duck typing dan operator overloading

![Duck Typing dan Operator Overloading](images/output_duck_typing.png)

### 7.4 Transaksi penyewaan (komposisi nota)

![Transaksi Penyewaan](images/output_transaksi.png)

## 8. Kesimpulan

Program GameZone Center telah menerapkan Abstraksi melalui abstract class `Konsol` dengan tiga subclass, serta Polimorfisme melalui pewarisan, duck typing, dan operator overloading. Relasi asosiasi, agregasi, dan komposisi benar-benar ada di kode dan digambarkan pada class diagram.