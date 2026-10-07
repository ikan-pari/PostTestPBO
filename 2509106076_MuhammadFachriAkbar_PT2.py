class Konsol:
    total_konsol_terdaftar = 0
    nama_game_center = "GameZone Center"
    harga_sewa_per_jam = 10000

    def __init__(self, nama_konsol, tipe_konsol, stok, kode_servis):
        self.nama_konsol = nama_konsol
        self.tipe_konsol = tipe_konsol
        self._stok = stok                     # protected -- boleh diakses/diubah langsung oleh subclass
        self.__kode_servis = kode_servis       # private -- rahasia, eksklusif untuk superclass

        # ===== AGREGASI: Konsol "punya" daftar Game, tapi Game dibuat di LUAR dan tetap independen =====
        self.daftar_game = []

        Konsol.total_konsol_terdaftar += 1

    @property
    def stok(self):
        return self._stok

    @stok.setter
    def stok(self, stok_baru):
        if stok_baru < 0:
            print("Peringatan : stok tidak boleh negatif!")
        else:
            self._stok = stok_baru

    def tambah_game(self, game):
        """Agregasi: menambahkan objek Game yang SUDAH ADA ke daftar game konsol ini."""
        self.daftar_game.append(game)
        print(f"Game '{game.judul}' ditambahkan ke {self.nama_konsol}.")

    def tampilkan_info(self):
        daftar_judul = ", ".join(g.judul for g in self.daftar_game) if self.daftar_game else "Belum ada game"
        print(f"[{self.nama_konsol}] Tipe: {self.tipe_konsol} | "
            f"Stok: {self._stok} | Sewa: Rp{Konsol.harga_sewa_per_jam}/jam | "
            f"Game tersedia: {daftar_judul}")

    def cek_kode_servis(self):
        print(f"Kode servis internal {self.nama_konsol}: {self.__kode_servis}")

    @classmethod
    def ubah_harga_sewa(cls, harga_baru):
        cls.harga_sewa_per_jam = harga_baru

    @staticmethod
    def validasi_tipe_konsol(tipe):
        tipe_valid = ["PS4", "PS5","Nintendo Switch"]
        return tipe in tipe_valid


class KonsolPlayStation(Konsol):
    def __init__(self, nama_konsol, tipe_konsol, stok, kode_servis, jumlah_controller):
        super().__init__(nama_konsol, tipe_konsol, stok, kode_servis)
        self.jumlah_controller = jumlah_controller   # atribut unik subclass ini

    def tampilkan_info(self):   # method overriding
        super().tampilkan_info()
        print(f"Jumlah controller: {self.jumlah_controller}")

    def servis_konsol(self):
        """Contoh subclass mengakses & mengubah atribut protected milik superclass secara langsung."""
        if self._stok > 0:
            self._stok -= 1
            print(f"{self.nama_konsol} sedang diservis. Stok sementara berkurang menjadi {self._stok}.")
        else:
            print(f"{self.nama_konsol} tidak ada stok untuk diservis.")



class KonsolNintendo(Konsol):
    def __init__(self, nama_konsol, tipe_konsol, stok, kode_servis, mode_portable):
        super().__init__(nama_konsol, tipe_konsol, stok, kode_servis)
        self.mode_portable = mode_portable   # atribut unik subclass ini

    def tampilkan_info(self):   # method overriding
        super().tampilkan_info()
        status = "Bisa dibawa jalan" if self.mode_portable else "Statis di tempat"
        print(f"Mode: {status}")


class Game:
    total_game_terdaftar = 0

    def __init__(self, judul, genre, rating_usia):
        self.judul = judul
        self.genre = genre
        self.__rating_usia = rating_usia
        Game.total_game_terdaftar += 1

    @property
    def rating_usia(self):
        return self.__rating_usia

    @rating_usia.setter
    def rating_usia(self, rating_baru):
        rating_valid = ["E", "T", "M"]
        if rating_baru  not in rating_valid:
            print("Rating usia tidak termasuk!")
        else:
            self.__rating_usia = rating_baru

    def tampilkan_info(self):
        print(f"{self.judul} Genre: {self.genre} | Rating: {self.__rating_usia}")

    @staticmethod
    def validasi_genre(genre):
        genre_valid = ["Action", "RPG", "Sports", "Racing", "Fighting"]
        return genre in genre_valid



class Pelanggan:
    total_pelanggan = 0
    nama_tempat = "GameZone Center"

    def __init__(self, nama, no_hp, saldo_awal=0):
        self.nama = nama
        self.no_hp = no_hp
        self.__saldo = saldo_awal

        # ===== ASOSIASI: Pelanggan cuma "menunjuk" ke Game favorit, keduanya tetap independen =====
        self.game_favorit = None

        Pelanggan.total_pelanggan += 1

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, saldo_baru):
        if saldo_baru < 0:
            print("Saldo tidak boleh negatif!")
        else:
            self.__saldo = saldo_baru

    def pilih_game_favorit(self, game):
        """Asosiasi: menghubungkan ke objek Game yang sudah ada di luar, tanpa memilikinya."""
        self.game_favorit = game
        print(f"{self.nama} menjadikan '{game.judul}' sebagai game favorit.")

    def top_up_saldo(self, jumlah):
        if jumlah <= 0:
            print("Jumlah top up harus lebih dari 0.")
        else:
            self.__saldo += jumlah
            print(f"Top up berhasil. Saldo {self.nama} sekarang: Rp {self.__saldo}")

    def tampilkan_saldo(self):
        favorit = self.game_favorit.judul if self.game_favorit else "Belum ada"
        print(f"{self.nama} ({self.no_hp}) | Saldo: Rp{self.__saldo} | Game favorit: {favorit}")

    @staticmethod
    def validasi_no_hp(no_hp):
        return no_hp.startswith("08") and len(no_hp) >= 10


class NotaPembayaran:
    """Objek ini SELALU dibuat di dalam Penyewaan, tidak pernah berdiri sendiri dari luar."""
    nomor_urut = 0

    def __init__(self, nama_pelanggan, total_bayar):
        NotaPembayaran.nomor_urut += 1
        self.nomor_nota = f"NOTA-{NotaPembayaran.nomor_urut:04d}"
        self.nama_pelanggan = nama_pelanggan
        self.total_bayar = total_bayar

    def cetak(self):
        print(f"--- {self.nomor_nota} ---")
        print(f"Atas nama : {self.nama_pelanggan}")
        print(f"Total     : Rp{self.total_bayar}")
        print("-" * 20)


class Penyewaan:
    total_transaksi = 0
    nama_toko = "GameZone Center"
    denda_telat_per_jam = 5000

    def __init__(self, pelanggan, konsol, game, durasi_jam):
        self.pelanggan = pelanggan
        self.konsol = konsol
        self.game = game
        self.durasi_jam = durasi_jam
        self.__total_bayar = 0

        # ===== KOMPOSISI: NotaPembayaran dibuat DI DALAM, eksklusif milik Penyewaan ini =====
        self.nota = None

        Penyewaan.total_transaksi += 1

    @property
    def total_bayar(self):
        return self.__total_bayar

    def hitung_total(self):
        self.__total_bayar = self.konsol.harga_sewa_per_jam * self.durasi_jam
        return self.__total_bayar

    def hitung_denda(self, durasi_telat):
        if durasi_telat <= 0:
            return 0
        return durasi_telat * Penyewaan.denda_telat_per_jam

    def bayar(self):
        self.hitung_total()
        print(f"{self.pelanggan.nama} menyewa {self.konsol.nama_konsol} "
            f"main {self.game.judul} selama {self.durasi_jam} jam. "
            f"Total bayar: Rp{self.__total_bayar}")
        if self.pelanggan.saldo < self.__total_bayar:
            print(f"Saldo {self.pelanggan.nama} tidak cukup!")
        else:
            self.pelanggan.saldo = self.pelanggan.saldo - self.__total_bayar
            # komposisi: nota baru dibuat di sini, eksklusif untuk transaksi ini
            self.nota = NotaPembayaran(self.pelanggan.nama, self.__total_bayar)
            print(f"Pembayaran berhasil. Sisa saldo: Rp{self.pelanggan.saldo}")
            self.nota.cetak()

    @staticmethod
    def cek_durasi_valid(jam):
        return jam > 0



konsol1 = KonsolPlayStation("Playstation 5", "PS5", 5, "SVC-PS5-01", 4)
konsol2 = KonsolNintendo("Nintendo Switch", "Nintendo Switch", 3, "SVC-SW-01", True)

game1 = Game("EA Sports FC26", "Sports", "E")
game2 = Game("Resident Evil Requiem", "Action", "M")

pelanggan1 = Pelanggan("Pari", "08123456789", 100000)
pelanggan2 = Pelanggan("Akbar", "082345678901", 50000)

print ("=== Data Konsol (Inheritance) ===")
konsol1.tampilkan_info()
konsol2.tampilkan_info()
konsol1.cek_kode_servis()
print("Total konsol terdaftar:", Konsol.total_konsol_terdaftar)
print("konsol1 instance dari Konsol (superclass)?", isinstance(konsol1, Konsol))

print("\n=== Data Game ===")
game1.tampilkan_info()
game2.tampilkan_info()

print("\n=== Pengujian Agregasi (Konsol <-> Game) ===")
konsol1.tambah_game(game1)
konsol2.tambah_game(game2)
konsol1.tampilkan_info()

print("\n=== Data Pelanggan ===")
pelanggan1.tampilkan_saldo()
pelanggan2.tampilkan_saldo()

print("\n=== Pengujian Asosiasi (Pelanggan <-> Game) ===")
pelanggan1.pilih_game_favorit(game1)
pelanggan1.tampilkan_saldo()

print("\n=== Pengujian Setter ===")

konsol1.stok = 7
print("Stok Konsol 1: ", konsol1.stok)

konsol1.stok = -5

pelanggan1.saldo = 150000
print("Saldo Pari: ", pelanggan1.saldo)
pelanggan1.saldo = -10000

game1.rating_usia = "T"
print("Rating Usia EA SPORTS FC26: ", game1.rating_usia)
game1.rating_usia = "X"

print("\n=== Pengujian Instance Method ===")

pelanggan1.top_up_saldo(50000)
pelanggan1.tampilkan_saldo()

print("\n=== Pengujian Subclass: Method Khusus (servis_konsol) ===")
konsol1.servis_konsol()   # subclass mengakses & mengubah _stok langsung

print("\n=== Pengujian Class Method ===")

print("\nHarga sewa awal: ", Konsol.harga_sewa_per_jam)

Konsol.ubah_harga_sewa(15000)

print("\nHarga sewa setelah diubah: ", Konsol.harga_sewa_per_jam)


print("\n=== Pengujian Static Method ===")

print("PS5: ", Konsol.validasi_tipe_konsol("PS5"))
print("Xbox: ", Konsol.validasi_tipe_konsol("Xbox"))

print("Sports: ", Game.validasi_genre("Sports"))
print("Horror: ", Game.validasi_genre("Horror"))

print("Nomor HP: ", Pelanggan.validasi_no_hp("081234567890"))
print("Nomor HP: ", Pelanggan.validasi_no_hp("12345"))

print("Durasi 2 jam: ", Penyewaan.cek_durasi_valid(2))
print("Durasi 0 jam: ", Penyewaan.cek_durasi_valid(0))

print("\n=== Data Penyewaan ===")
penyewaan1 = Penyewaan(pelanggan1,konsol1,game1,2)
penyewaan2 = Penyewaan(pelanggan2,konsol2,game2,5)

print("\nPelanggan: ", penyewaan1.pelanggan.nama,
    "| Konsol: ", penyewaan1.konsol.nama_konsol,
    "| Game: ", penyewaan1.game.judul,
    "| Durasi: ", penyewaan1.durasi_jam, " jam")

print("\nPelanggan: ", penyewaan2.pelanggan.nama,
    "| Konsol: ", penyewaan2.konsol.nama_konsol,
    "| Game: ", penyewaan2.game.judul,
    "| Durasi: ", penyewaan2.durasi_jam, " jam")
print("\n=== Transaksi Penyewaan (Komposisi: Penyewaan -> NotaPembayaran) ===")
penyewaan1.bayar()
penyewaan2.bayar()


print("\n=== Pengujian Denda ===")
print("Denda terlambat 2 jam: ", penyewaan1.hitung_denda(2))
print("Denda terlambat 0 jam: ", penyewaan2.hitung_denda(0))