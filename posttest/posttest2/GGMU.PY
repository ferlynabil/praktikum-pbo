class SlipGaji:
    def __init__(self, id_slip, musim, gaji_kotor, gaji_bersih):
        self.id_slip = id_slip
        self.musim = musim
        self.gaji_kotor = gaji_kotor
        self.gaji_bersih = gaji_bersih

    def __str__(self):
        return (f"[{self.id_slip}] Musim {self.musim} | "
                f"Kotor: Rp{self.gaji_kotor:,.0f} -> Bersih: Rp{self.gaji_bersih:,.0f}")


class BankPembayaran:
    def __init__(self, nama_bank, kode_bank):
        self.nama_bank = nama_bank
        self.kode_bank = kode_bank

    def proses_transfer(self, nama_penerima, jumlah):
        jumlah_format = f"Rp{jumlah:,.0f}".replace(",", ".")
        print(f"  [{self.kode_bank}] {self.nama_bank} berhasil mentransfer "
              f"{jumlah_format} ke {nama_penerima}.")


class Pemain:
    nama_klub = "Manchester United"
    musim_liga = "Premier League 2025/2026"
    pajak_gaji = 0.05
    total_pemain = 0

    def __init__(self, nama, no_punggung, gaji_dasar):
        self.nama = nama
        self._no_punggung = None
        self._gaji_dasar = None

        self.no_punggung = no_punggung
        self.gaji_dasar = gaji_dasar

        self.__kode_registrasi = f"MU-{Pemain.total_pemain + 1:04d}"
        self._riwayat_slip = []

        Pemain.total_pemain += 1

    @property
    def no_punggung(self):
        return self._no_punggung

    @no_punggung.setter
    def no_punggung(self, nilai):
        if not Pemain.validasi_no_punggung(nilai):
            print(f"[DITOLAK] No. punggung {nilai} tidak valid (harus angka 1-99).")
            return
        self._no_punggung = nilai

    @property
    def gaji_dasar(self):
        return self._gaji_dasar

    @gaji_dasar.setter
    def gaji_dasar(self, nilai):
        if nilai < 0:
            raise ValueError("Gaji dasar tidak boleh negatif.")
        self._gaji_dasar = nilai

    @property
    def kode_registrasi(self):
        return self.__kode_registrasi

    def hitungGaji(self):
        return self._gaji_dasar * (1 - Pemain.pajak_gaji)

    def tampilKontrak(self):
        print(f"--- Kontrak {type(self).__name__} ---")
        print(f"Nama            : {self.nama}")
        print(f"No. Punggung    : {self._no_punggung}")
        print(f"Kode Registrasi : {self.kode_registrasi}")
        print(f"Klub            : {Pemain.nama_klub} ({Pemain.musim_liga})")
        print(f"Gaji Take Home  : {Pemain.format_rupiah(self.hitungGaji())}")

    def proses_gaji_bulanan(self):
        gaji_kotor = self._gaji_dasar
        gaji_bersih = self.hitungGaji()
        id_slip = f"SLIP-{len(self._riwayat_slip) + 1:03d}"
        slip = SlipGaji(id_slip, Pemain.musim_liga, gaji_kotor, gaji_bersih)
        self._riwayat_slip.append(slip)
        print(f"[INFO] Slip gaji {id_slip} untuk {self.nama} berhasil dibuat.")
        return slip

    def tampilkan_riwayat_slip(self):
        print(f"\nRiwayat Slip Gaji - {self.nama}")
        if not self._riwayat_slip:
            print("  (Belum ada slip gaji)")
            return
        for slip in self._riwayat_slip:
            print(f"  {slip}")

    def terima_gaji(self, bank):
        gaji = self.hitungGaji()
        print(f"  {self.nama} meminta {bank.nama_bank} memproses gaji bulan ini...")
        bank.proses_transfer(self.nama, gaji)

    @classmethod
    def ubah_pajak_gaji(cls, pajak_baru):
        if 0 <= pajak_baru < 1:
            Pemain.pajak_gaji = pajak_baru
            print(f"[INFO] Pajak gaji klub diubah menjadi {pajak_baru * 100:.0f}%.")
        else:
            print("[DITOLAK] Pajak harus berupa desimal antara 0 dan 1 (contoh 0.1 = 10%).")

    @staticmethod
    def validasi_no_punggung(no_punggung):
        return isinstance(no_punggung, int) and 1 <= no_punggung <= 99

    @staticmethod
    def format_rupiah(angka):
        return f"Rp{angka:,.0f}".replace(",", ".")


class PemainDepan(Pemain):
    bonus_per_gol = 2_000_000

    def __init__(self, nama, no_punggung, gaji_dasar, jumlah_gol=0):
        super().__init__(nama, no_punggung, gaji_dasar)
        self.jumlah_gol = jumlah_gol

    def tambah_gol(self, jumlah=1):
        if jumlah > 0:
            self.jumlah_gol += jumlah
            print(f"[INFO] {self.nama} mencetak {jumlah} gol. Total gol: {self.jumlah_gol}")
        else:
            print("[DITOLAK] Jumlah gol yang ditambahkan harus lebih dari 0.")

    def hitungGaji(self):
        bonus = self.jumlah_gol * PemainDepan.bonus_per_gol
        gaji_kotor = self._gaji_dasar + bonus
        return gaji_kotor * (1 - Pemain.pajak_gaji)

    def tampilKontrak(self):
        super().tampilKontrak()
        print(f"Jumlah Gol      : {self.jumlah_gol}")
        print()

    @classmethod
    def dari_dict(cls, data):
        return cls(
            data["nama"],
            data["no_punggung"],
            data["gaji_dasar"],
            data.get("jumlah_gol", 0),
        )


class Kiper(Pemain):
    bonus_per_clean_sheet = 1_500_000

    def __init__(self, nama, no_punggung, gaji_dasar, jumlah_clean_sheet=0):
        super().__init__(nama, no_punggung, gaji_dasar)
        self.jumlah_clean_sheet = jumlah_clean_sheet

    def tambah_clean_sheet(self, jumlah=1):
        if jumlah > 0:
            self.jumlah_clean_sheet += jumlah
            print(f"[INFO] {self.nama} menambah {jumlah} clean sheet. "
                  f"Total: {self.jumlah_clean_sheet}")
        else:
            print("[DITOLAK] Jumlah clean sheet yang ditambahkan harus lebih dari 0.")

    def hitungGaji(self):
        bonus = self.jumlah_clean_sheet * Kiper.bonus_per_clean_sheet
        gaji_kotor = self._gaji_dasar + bonus
        return gaji_kotor * (1 - Pemain.pajak_gaji)

    def tampilKontrak(self):
        super().tampilKontrak()
        print(f"Clean Sheet     : {self.jumlah_clean_sheet}")
        print()

    @classmethod
    def dari_dict(cls, data):
        return cls(
            data["nama"],
            data["no_punggung"],
            data["gaji_dasar"],
            data.get("jumlah_clean_sheet", 0),
        )


class ManajemenMU:
    nama_lembaga = "MU Governance Board"

    def __init__(self, nama_tim):
        self.nama_tim = nama_tim
        self._daftar_pemain = []

    def tambah_pemain(self, pemain):
        if isinstance(pemain, Pemain):
            self._daftar_pemain.append(pemain)
            print(f"[INFO] {pemain.nama} berhasil ditambahkan ke skuad {self.nama_tim}.")
        else:
            print("[DITOLAK] Objek yang ditambahkan bukan instance dari Pemain.")

    def keluarkan_pemain(self, nama):
        awal = len(self._daftar_pemain)
        self._daftar_pemain = [p for p in self._daftar_pemain if p.nama != nama]
        if len(self._daftar_pemain) < awal:
            print(f"[INFO] {nama} telah dikeluarkan dari skuad {self.nama_tim}.")

    @property
    def total_pemain_skuad(self):
        return len(self._daftar_pemain)

    def cetak_total_gaji(self):
        total = 0
        print(f"\n=== Total Gaji Skuad: {self.nama_tim} ===")
        if not self._daftar_pemain:
            print("(Belum ada pemain di skuad ini)")
            return 0
        for pemain in self._daftar_pemain:
            gaji = pemain.hitungGaji()
            total += gaji
            print(f"{pemain.nama:<20}: {Pemain.format_rupiah(gaji)}")
        print(f"{'TOTAL GAJI':<20}: {Pemain.format_rupiah(total)}")
        return total

    @property
    def daftar_pemain(self):
        return self._daftar_pemain


if __name__ == "__main__":

    print("=" * 70)
    print(" DEMO 1: Inheritance -> super().__init__() & objek tiap class")
    print("=" * 70)
    pemain_umum = Pemain("Pemain Trial", 0, 100_000_000)

    depan1 = PemainDepan("Diego Marlow", 9, 450_000_000, jumlah_gol=5)
    depan2 = PemainDepan("Elian Voss", 11, 400_000_000, jumlah_gol=3)

    kiper1 = Kiper("Malik Osei", 1, 300_000_000, jumlah_clean_sheet=4)
    kiper2 = Kiper("Tomas Reyner", 13, 250_000_000, jumlah_clean_sheet=2)

    data_striker_baru = {"nama": "Farid Kanu", "no_punggung": 21, "gaji_dasar": 350_000_000, "jumlah_gol": 1}
    depan3 = PemainDepan.dari_dict(data_striker_baru)

    data_kiper_baru = {"nama": "Ivo Santer", "no_punggung": 22, "gaji_dasar": 200_000_000}
    kiper3 = Kiper.dari_dict(data_kiper_baru)
    print("Semua objek berhasil dibuat lewat constructor masing-masing (subclass memanggil super().__init__()).\n")

    print("=" * 70)
    print(" DEMO 2: Method Overriding -> tampilKontrak() & hitungGaji() beda tiap class")
    print("=" * 70)
    pemain_umum.tampilKontrak()
    print()
    depan1.tampilKontrak()
    kiper1.tampilKontrak()

    print("=" * 70)
    print(" DEMO 3: Cek relasi pewarisan -> isinstance() & issubclass()")
    print("=" * 70)
    print("isinstance(depan1, Pemain)        :", isinstance(depan1, Pemain))
    print("isinstance(depan1, Kiper)         :", isinstance(depan1, Kiper))
    print("issubclass(PemainDepan, Pemain)   :", issubclass(PemainDepan, Pemain))
    print("issubclass(Kiper, Pemain)         :", issubclass(Kiper, Pemain))
    print()

    print("=" * 70)
    print(" DEMO 4: Protected vs Private pada Pewarisan")
    print("=" * 70)
    print(f"Akses protected langsung (dipakai di hitungGaji() subclass): depan1._gaji_dasar = "
          f"{Pemain.format_rupiah(depan1._gaji_dasar)}")
    print(f"Akses private lewat getter read-only                      : depan1.kode_registrasi = "
          f"{depan1.kode_registrasi}")
    print()

    print("=" * 70)
    print(" DEMO 5: Instance Method lain -> tambah_gol() / tambah_clean_sheet()")
    print("=" * 70)
    depan2.tambah_gol(2)
    depan2.tambah_gol(-1)
    kiper2.tambah_clean_sheet(1)
    kiper2.tambah_clean_sheet(0)
    print()

    print("=" * 70)
    print(" DEMO 6: Setter & Validasi Data")
    print("=" * 70)
    print(f"Gaji dasar {depan1.nama} sebelum diubah : {Pemain.format_rupiah(depan1.gaji_dasar)}")
    depan1.gaji_dasar = 500_000_000
    print(f"Gaji dasar {depan1.nama} setelah diubah : {Pemain.format_rupiah(depan1.gaji_dasar)}")
    try:
        depan1.gaji_dasar = -100_000_000
    except ValueError as e:
        print(f"[TERBUKTI] Setter menolak nilai negatif -> {e}")
    kiper1.no_punggung = 150
    print(f"No. punggung {kiper1.nama} tetap        : {kiper1.no_punggung}\n")

    print("=" * 70)
    print(" DEMO 7: Class Method & Static Method")
    print("=" * 70)
    print(f"Gaji {kiper1.nama} sebelum pajak diubah : {Pemain.format_rupiah(kiper1.hitungGaji())}")
    Pemain.ubah_pajak_gaji(0.10)
    print(f"Gaji {kiper1.nama} setelah pajak diubah : {Pemain.format_rupiah(kiper1.hitungGaji())}")
    print("Validasi no. punggung 7  :", Pemain.validasi_no_punggung(7))
    print("Validasi no. punggung 150:", Pemain.validasi_no_punggung(150))
    print()

    print("=" * 70)
    print(" DEMO 8 (Relasi UML - ASOSIASI): Pemain 'menggunakan' BankPembayaran")
    print("=" * 70)
    bank_mu = BankPembayaran("Santander UK", "SAN-01")
    depan1.terima_gaji(bank_mu)        # objek bank hanya dipakai sesaat, tidak disimpan di Pemain
    kiper1.terima_gaji(bank_mu)
    print()

    print("=" * 70)
    print(" DEMO 9 (Relasi UML - AGREGASI): ManajemenMU 'memiliki' banyak Pemain")
    print("=" * 70)
    skuad_utama = ManajemenMU("Manchester United - Skuad Utama")
    skuad_u21 = ManajemenMU("Manchester United - Skuad U21")

    skuad_utama.tambah_pemain(depan1)
    skuad_utama.tambah_pemain(depan2)
    skuad_utama.tambah_pemain(kiper1)

    skuad_u21.tambah_pemain(depan3)
    skuad_u21.tambah_pemain(kiper3)

    skuad_utama.cetak_total_gaji()
    skuad_u21.cetak_total_gaji()

    print(f"\n[INFO] Membubarkan entitas skuad_u21 (del skuad_u21)...")
    del skuad_u21
    print("[BUKTI AGREGASI] Objek Pemain yang sebelumnya ada di skuad_u21 tetap hidup mandiri:")
    depan3.tampilKontrak()

    print("=" * 70)
    print(" DEMO 10 (Relasi UML - KOMPOSISI): Pemain 'terdiri dari' SlipGaji")
    print("=" * 70)
    kiper2.proses_gaji_bulanan()
    kiper2.tambah_clean_sheet(1)
    kiper2.proses_gaji_bulanan()
    kiper2.tampilkan_riwayat_slip()

    print(f"\n[INFO] Pemain kiper2 ({kiper2.nama}) dihapus dari memori (del kiper2)...")
    del kiper2
    print("[BUKTI KOMPOSISI] Seluruh SlipGaji milik kiper2 ikut musnah karena hanya "
          "ada di dalam instance tersebut (tidak direferensikan di tempat lain).")

    print("\n" + "=" * 70)
    print(f" Total objek Pemain yang pernah dibuat (atribut kelas): {Pemain.total_pemain}")
    print(f" Nama klub  : {Pemain.nama_klub}")
    print(f" Musim liga : {Pemain.musim_liga}")
    print(f" Pajak gaji berlaku saat ini: {Pemain.pajak_gaji * 100:.0f}%")
    print("=" * 70)