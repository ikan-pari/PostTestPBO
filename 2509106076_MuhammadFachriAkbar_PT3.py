from abc import ABC, abstractmethod

class Konsol(ABC):
    total_konsol_terdaftar = 0
    nama_game_center = "GameZone Center"
    harga_sewa_per_jam = 10000

    def __init__(self, nama_konsol, tipe_konsol, stok, kode_servis):
        self.nama_konsol = nama_konsol
        self.tipe_konsol = tipe_konsol
        self._stok = stok                     # protected -- boleh diakses/diubah langsung oleh subclass
        self.__kode_servis = kode_servis       # private -- rahasia, eksklusif untuk superclass
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


    def __len__(self):
        return len(self.daftar_game)


    @abstractmethod
    def hitung_biaya_sewa(self, durasi_jam):
        pass

    @abstractmethod
    def info_spesifik(self):
        pass

    def tambah_game(self, game):
        """Agregasi: menambahkan objek Game yang SUDAH ADA ke daftar game konsol ini."""
        self.daftar_game.append(game)
        print(f"Game '{game.judul}' ditambahkan ke {self.nama_konsol}.")

    def tampilkan_info(self):
        print(f"[{self.nama_konsol}] Tipe: {self.tipe_konsol} | "
            f"Stok: {self._stok} | Sewa dasar: Rp{Konsol.harga_sewa_per_jam}/jam | "
            f"Jumlah game: {len(self)}")
        self.info_spesifik()   # tiap subclass menentukan sendiri detail tambahannya

    def cek_kode_servis(self):
        print(f"Kode servis internal {self.nama_konsol}: {self.__kode_servis}")

    @classmethod
    def ubah_harga_sewa(cls, harga_baru):
        cls.harga_sewa_per_jam = harga_baru

    @staticmethod
    def validasi_tipe_konsol(tipe):
        tipe_valid = ["PS4", "PS5", "Nintendo Switch", "Xbox Series X"]
        return tipe in tipe_valid


class KonsolPlayStation(Konsol):
    def __init__(self, nama_konsol, tipe_konsol, stok, kode_servis, jumlah_controller):
        super().__init__(nama_konsol, tipe_konsol, stok, kode_servis)
        self.jumlah_controller = jumlah_controller   # atribut unik

    def hitung_biaya_sewa(self, durasi_jam):
        # tambahan Rp1.000/jam untuk setiap controller di atas 2
        tambahan = max(0, self.jumlah_controller - 2) * 1000
        return (Konsol.harga_sewa_per_jam + tambahan) * durasi_jam

    def info_spesifik(self):
        print(f"Jumlah controller: {self.jumlah_controller}")

    def servis_konsol(self):
        """Subclass mengakses & mengubah atribut protected milik superclass secara langsung."""
        if self._stok > 0:
            self._stok -= 1
            print(f"{self.nama_konsol} sedang diservis. Stok sementara berkurang menjadi {self._stok}.")
        else:
            print(f"{self.nama_konsol} tidak ada stok untuk diservis.")


class KonsolNintendo(Konsol):
    def __init__(self, nama_konsol, tipe_konsol, stok, kode_servis, mode_portable):
        super().__init__(nama_konsol, tipe_konsol, stok, kode_servis)
        self.mode_portable = mode_portable   # atribut unik

    def hitung_biaya_sewa(self, durasi_jam):
        # konsol portable mendapat diskon 10%
        diskon = 0.1 if self.mode_portable else 0
        return int(Konsol.harga_sewa_per_jam * durasi_jam * (1 - diskon))

    def info_spesifik(self):
        status = "Bisa dibawa jalan" if self.mode_portable else "Statis di tempat"
        print(f"Mode: {status}")


class KonsolXbox(Konsol):
    def __init__(self, nama_konsol, tipe_konsol, stok, kode_servis, punya_game_pass):
        super().__init__(nama_konsol, tipe_konsol, stok, kode_servis)
        self.punya_game_pass = punya_game_pass   # atribut unik

    def hitung_biaya_sewa(self, durasi_jam):
        # biaya tetap Rp3.000 jika konsol ini membawa langganan Game Pass
        biaya_game_pass = 3000 if self.punya_game_pass else 0
        return Konsol.harga_sewa_per_jam * durasi_jam + biaya_game_pass

    def info_spesifik(self):
        status = "Aktif" if self.punya_game_pass else "Tidak ada"
        print(f"Game Pass: {status}")


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
        if rating_baru not in rating_valid:
            print("Rating usia tidak termasuk!")
        else:
            self.__rating_usia = rating_baru

    def __str__(self):
        return f"{self.judul} ({self.genre}, rating {self.__rating_usia})"

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

        # ASOSIASI: Pelanggan cuma "menunjuk" ke Game favorit, keduanya tetap independen
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


class LaporanTransaksi:
    def __init__(self, jumlah_transaksi, total_pendapatan):
        self.jumlah_transaksi = jumlah_transaksi
        self.total_pendapatan = total_pendapatan

    def cetak(self):
        print("=== LAPORAN TRANSAKSI ===")
        print(f"Transaksi berhasil : {self.jumlah_transaksi}")
        print(f"Total pendapatan   : Rp{self.total_pendapatan}")
        print("=" * 25)


def proses_cetak(dokumen):
    """Tidak peduli kelas apa, selama punya method cetak() (duck typing)."""
    dokumen.cetak()


class Penyewaan:
    total_transaksi = 0
    nama_toko = "GameZone Center"
    denda_telat_per_jam = 5000

    def __init__(self, pelanggan, konsol, game, durasi_jam):
        self.pelanggan = pelanggan
        self.konsol = konsol      # bergantung pada abstraksi Konsol, bukan subclass tertentu (DIP)
        self.game = game
        self.durasi_jam = durasi_jam
        self.__total_bayar = 0

        # KOMPOSISI: NotaPembayaran dibuat DI DALAM, eksklusif milik Penyewaan ini
        self.nota = None

        Penyewaan.total_transaksi += 1

    @property
    def total_bayar(self):
        return self.__total_bayar

    def hitung_total(self):
        # POLIMORFISME: tiap jenis konsol menghitung biayanya sendiri, tanpa if/elif type()
        self.__total_bayar = self.konsol.hitung_biaya_sewa(self.durasi_jam)
        return self.__total_bayar

    def hitung_denda(self, durasi_telat):
        if durasi_telat <= 0:
            return 0
        return durasi_telat * Penyewaan.denda_telat_per_jam

    # ----- OPERATOR OVERLOADING: membandingkan dua penyewaan berdasarkan total biaya -----
    def __lt__(self, other):
        return self.hitung_total() < other.hitung_total()

    def bayar(self):
        self.hitung_total()
        print(f"{self.pelanggan.nama} menyewa {self.konsol.nama_konsol} "
            f"main {self.game.judul} selama {self.durasi_jam} jam. "
            f"Total bayar: Rp{self.__total_bayar}")
        if self.pelanggan.saldo < self.__total_bayar:
            print(f"Saldo {self.pelanggan.nama} tidak cukup!")
        else:
            self.pelanggan.saldo = self.pelanggan.saldo - self.__total_bayar
            self.nota = NotaPembayaran(self.pelanggan.nama, self.__total_bayar)
            print(f"Pembayaran berhasil. Sisa saldo: Rp{self.pelanggan.saldo}")
            proses_cetak(self.nota)

    @staticmethod
    def cek_durasi_valid(jam):
        return jam > 0


# ======================================================
# MAIN CODE
# ======================================================
konsol1 = KonsolPlayStation("Playstation 5", "PS5", 5, "SVC-PS5-01", 4)
konsol2 = KonsolNintendo("Nintendo Switch", "Nintendo Switch", 3, "SVC-SW-01", True)
konsol3 = KonsolXbox("Xbox Series X", "Xbox Series X", 2, "SVC-XB-01", True)

game1 = Game("EA Sports FC26", "Sports", "E")
game2 = Game("Resident Evil Requiem", "Action", "M")

pelanggan1 = Pelanggan("Pari", "08123456789", 100000)
pelanggan2 = Pelanggan("Akbar", "082345678901", 50000)

print("=== Bukti Abstraksi: Abstract Class Tidak Bisa Diinstansiasi ===")
try:
    konsol_abstrak = Konsol("Konsol Abstrak", "PS5", 1, "SVC-000")
except TypeError as error:
    print("TypeError:", error)

print("\n=== Data Konsol (Inheritance) ===")
konsol1.tampilkan_info()
konsol2.tampilkan_info()
konsol3.tampilkan_info()
konsol1.cek_kode_servis()
print("Total konsol terdaftar:", Konsol.total_konsol_terdaftar)

print("\n=== Data Game (Operator Overloading __str__) ===")
print(game1)
print(game2)

print("\n=== Pengujian Agregasi (Konsol <-> Game) ===")
konsol1.tambah_game(game1)
konsol1.tambah_game(game2)
konsol2.tambah_game(game2)
print("Jumlah game di PS5 (len):", len(konsol1))
print("Jumlah game di Switch (len):", len(konsol2))

print("\n=== Pengujian Asosiasi (Pelanggan <-> Game) ===")
pelanggan1.pilih_game_favorit(game1)
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

print("\n=== Pengujian Akses Protected di Subclass ===")
konsol1.servis_konsol()

print("\n=== Pengujian Class Method ===")
print("Harga sewa awal: ", Konsol.harga_sewa_per_jam)
Konsol.ubah_harga_sewa(15000)
print("Harga sewa setelah diubah: ", Konsol.harga_sewa_per_jam)

print("\n=== Pengujian Static Method ===")
print("PS5: ", Konsol.validasi_tipe_konsol("PS5"))
print("Sega: ", Konsol.validasi_tipe_konsol("Sega"))
print("Sports: ", Game.validasi_genre("Sports"))
print("Horror: ", Game.validasi_genre("Horror"))
print("Nomor HP: ", Pelanggan.validasi_no_hp("081234567890"))
print("Nomor HP: ", Pelanggan.validasi_no_hp("12345"))
print("Durasi 2 jam: ", Penyewaan.cek_durasi_valid(2))
print("Durasi 0 jam: ", Penyewaan.cek_durasi_valid(0))

print("\n=== Polimorfisme via Pewarisan (satu loop, tiga jenis konsol) ===")
daftar_konsol = [konsol1, konsol2, konsol3]
for konsol in daftar_konsol:
    print(f"{konsol.nama_konsol} - biaya sewa 2 jam: Rp{konsol.hitung_biaya_sewa(2)}")
    konsol.info_spesifik()

print("\n=== Data Penyewaan ===")
penyewaan1 = Penyewaan(pelanggan1, konsol1, game1, 2)
penyewaan2 = Penyewaan(pelanggan2, konsol2, game2, 5)
penyewaan3 = Penyewaan(pelanggan1, konsol3, game2, 1)

print("\n=== Transaksi Penyewaan (Komposisi: Penyewaan -> NotaPembayaran) ===")
penyewaan1.bayar()
penyewaan2.bayar()
penyewaan3.bayar()

print("\n=== Operator Overloading __lt__ (urutkan penyewaan berdasar biaya) ===")
for p in sorted([penyewaan1, penyewaan2, penyewaan3]):
    print(f"{p.pelanggan.nama} - {p.konsol.nama_konsol}: Rp{p.total_bayar}")
print("Penyewaan 1 lebih murah dari Penyewaan 2?", penyewaan1 < penyewaan2)

print("\n=== Duck Typing (NotaPembayaran & LaporanTransaksi, tanpa pewarisan) ===")
semua_penyewaan = [penyewaan1, penyewaan2, penyewaan3]
berhasil = [p for p in semua_penyewaan if p.nota is not None]
laporan = LaporanTransaksi(len(berhasil), sum(p.total_bayar for p in berhasil))
for dokumen in [penyewaan1.nota, laporan]:
    proses_cetak(dokumen)

print("\n=== Pengujian Denda ===")
print("Denda terlambat 2 jam: ", penyewaan1.hitung_denda(2))
print("Denda terlambat 0 jam: ", penyewaan2.hitung_denda(0))