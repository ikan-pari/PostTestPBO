class Konsol:
    total_konsol_terdaftar = 0
    nama_game_center = "GameZone Center"
    harga_sewa_per_jam = 10000

    def __init__(self, nama_konsol, tipe_konsol, stok):
        self.nama_konsol = nama_konsol
        self.tipe_konsol = tipe_konsol
        self.__stok = stok
        Konsol.total_konsol_terdaftar += 1

    @property
    def stok(self):
        return self.__stok

    @stok.setter
    def stok(self, stok_baru):
        if stok_baru < 0:
            print("Peringatan : stok tidak boleh negatif!")
        else:
            self.__stok = stok_baru

    def tampilkan_info(self):
        print(f"[{self.nama_konsol}] Tipe: {self.tipe_konsol} | "
            f"Stok: {self.__stok} | Sewa: Rp{Konsol.harga_sewa_per_jam}/jam")

    @classmethod
    def ubah_harga_sewa(cls, harga_baru):
        cls.harga_sewa_per_jam = harga_baru


    @staticmethod
    def validasi_tipe_konsol(tipe):
        tipe_valid = ["PS4", "PS5","Nintendo Switch"]
        return tipe in tipe_valid

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

    def top_up_saldo(self, jumlah):
        if jumlah <= 0:
            print("Jumlah top up harus lebih dari 0.")
        else:
            self.__saldo += jumlah
            print(f"Top up berhasil. Saldo {self.nama} sekarang: Rp {self.__saldo}")

    def tampilkan_saldo(self):
        print(f"{self.nama} ({self.no_hp}) | Saldo: Rp{self.__saldo}")


    @staticmethod
    def validasi_no_hp(no_hp):
        return no_hp.startswith("08") and len(no_hp) >= 10

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
            print(f"Pembayaran berhasil. Sisa saldo: Rp{self.pelanggan.saldo}")

    @staticmethod
    def cek_durasi_valid(jam):
        return jam > 0

konsol1 = Konsol("Playstation 5", "PS5", 5)
konsol2 = Konsol("Playstation 4", "PS4", 3)

game1 = Game("EA Sports FC26", "Sports", "E")
game2 = Game("Resident Evil Requiem", "Action", "M")

pelanggan1 = Pelanggan("Pari", "08123456789", 100000)
pelanggan2 = Pelanggan("Akbar", "082345678901", 50000)

print ("=== Data Konsol ===")
konsol1.tampilkan_info()
konsol2.tampilkan_info()

print("\n=== Data Game ===")
game1.tampilkan_info()
game2.tampilkan_info()

print("\n=== Data Pelanggan ===")
pelanggan1.tampilkan_saldo()
pelanggan2.tampilkan_saldo()

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
print("\n=== Transaksi Penyewaan ===")
penyewaan1.bayar()
penyewaan2.bayar()


print("\n=== Pengujian Denda ===")
print("Denda terlambat 2 jam: ", penyewaan1.hitung_denda(2))
print("Denda terlambat 0 jam: ", penyewaan2.hitung_denda(0))