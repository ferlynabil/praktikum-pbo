class Pemain:
    nama_klub        = "Manchester United"
    musim_aktif      = "Premier League 2025/2026"
    total_terdaftar  = 0
    pajak_gaji_pct   = 0.05

    def __init__(self, nama: str, no_punggung: int, posisi: str, gaji_dasar: float):
        self.nama   = nama
        self.posisi = posisi

        self.__no_punggung = None
        self.__gaji_dasar  = None

        self.no_punggung = no_punggung
        self.gaji_dasar  = gaji_dasar

        Pemain.total_terdaftar += 1

    @property
    def no_punggung(self) -> int:
        return self.__no_punggung

    @no_punggung.setter
    def no_punggung(self, nilai: int):
        if not Pemain.cek_no_punggung(nilai):
            print(f"  [DITOLAK] No. punggung '{nilai}' tidak valid "
                  "(harus bilangan bulat 1-99).")
            return
        self.__no_punggung = nilai

    @property
    def gaji_dasar(self) -> float:
        return self.__gaji_dasar

    @gaji_dasar.setter
    def gaji_dasar(self, nilai: float):
        if not isinstance(nilai, (int, float)):
            print("  [DITOLAK] Gaji dasar harus berupa angka.")
            return
        if nilai < 0:
            raise ValueError("Gaji dasar tidak boleh negatif.")
        if nilai < 10_000_000:
            print("  [PERINGATAN] Gaji dasar terlalu kecil (minimum Rp10.000.000).")
            return
        self.__gaji_dasar = float(nilai)

    def hitung_gaji_bersih(self) -> float:
        if self.__gaji_dasar is None:
            return 0.0
        return self.__gaji_dasar * (1 - Pemain.pajak_gaji_pct)

    def tampil_info(self):
        print(f"  {'Nama':<20}: {self.nama}")
        print(f"  {'Posisi':<20}: {self.posisi}")
        print(f"  {'No. Punggung':<20}: {self.__no_punggung}")
        print(f"  {'Klub':<20}: {Pemain.nama_klub} ({Pemain.musim_aktif})")
        print(f"  {'Gaji Dasar':<20}: {Pemain.format_rupiah(self.__gaji_dasar)}")
        print(f"  {'Gaji Bersih':<20}: {Pemain.format_rupiah(self.hitung_gaji_bersih())}")

    @classmethod
    def ubah_pajak(cls, persen: float):
        if not (0.0 <= persen <= 0.5):
            print("  [DITOLAK] Pajak harus antara 0%% dan 50%% (masukkan desimal, mis. 0.10).")
            return
        cls.pajak_gaji_pct = persen
        print(f"  [INFO] Pajak gaji diubah menjadi {persen * 100:.0f}%%.")

    @classmethod
    def dari_dict(cls, data: dict):
        return cls(
            data["nama"],
            data["no_punggung"],
            data["posisi"],
            data["gaji_dasar"],
        )

    @staticmethod
    def cek_no_punggung(no: int) -> bool:
        return isinstance(no, int) and 1 <= no <= 99

    @staticmethod
    def format_rupiah(angka) -> str:
        if angka is None:
            return "Rp-"
        return "Rp{:,.0f}".format(angka).replace(",", ".")


class Statistik:
    nama_kompetisi    = "Premier League"
    musim             = "2025/2026"
    bonus_per_gol     = 2_000_000
    bonus_clean_sheet = 1_500_000

    def __init__(self, nama_pemain: str, posisi: str):
        self.nama_pemain = nama_pemain
        self.posisi      = posisi
        self.assist      = 0

        self.__gol         = 0
        self.__clean_sheet = 0

    @property
    def gol(self) -> int:
        return self.__gol

    @gol.setter
    def gol(self, nilai: int):
        if not isinstance(nilai, int):
            print("  [DITOLAK] Jumlah gol harus bilangan bulat.")
            return
        if nilai < 0:
            raise ValueError("Jumlah gol tidak boleh negatif.")
        self.__gol = nilai

    @property
    def clean_sheet(self) -> int:
        return self.__clean_sheet

    @clean_sheet.setter
    def clean_sheet(self, nilai: int):
        if not isinstance(nilai, int):
            print("  [DITOLAK] Clean sheet harus bilangan bulat.")
            return
        if nilai < 0:
            raise ValueError("Jumlah clean sheet tidak boleh negatif.")
        if self.posisi.lower() != "kiper":
            print(f"  [PERINGATAN] {self.nama_pemain} bukan kiper, clean sheet diabaikan.")
            return
        self.__clean_sheet = nilai

    def tambah_gol(self, jumlah: int = 1):
        if not isinstance(jumlah, int) or jumlah <= 0:
            print("  [DITOLAK] Jumlah gol yang ditambahkan harus bilangan bulat positif.")
            return
        self.__gol += jumlah
        print(f"  [INFO] {self.nama_pemain} mencetak {jumlah} gol. Total: {self.__gol}")

    def tambah_clean_sheet(self, jumlah: int = 1):
        if self.posisi.lower() != "kiper":
            print(f"  [DITOLAK] {self.nama_pemain} bukan kiper.")
            return
        if not isinstance(jumlah, int) or jumlah <= 0:
            print("  [DITOLAK] Jumlah clean sheet harus bilangan bulat positif.")
            return
        self.__clean_sheet += jumlah
        print(f"  [INFO] {self.nama_pemain} tambah {jumlah} clean sheet. Total: {self.__clean_sheet}")

    def hitung_bonus(self) -> float:
        return (self.__gol * Statistik.bonus_per_gol +
                self.__clean_sheet * Statistik.bonus_clean_sheet)

    def tampil_statistik(self):
        print(f"  {'Pemain':<20}: {self.nama_pemain} ({self.posisi})")
        print(f"  {'Kompetisi':<20}: {Statistik.nama_kompetisi} {Statistik.musim}")
        print(f"  {'Gol':<20}: {self.__gol}")
        print(f"  {'Assist':<20}: {self.assist}")
        print(f"  {'Clean Sheet':<20}: {self.__clean_sheet}")
        print(f"  {'Total Bonus':<20}: {Pemain.format_rupiah(self.hitung_bonus())}")

    @classmethod
    def ubah_bonus_gol(cls, nilai: float):
        if nilai < 0:
            print("  [DITOLAK] Bonus tidak boleh negatif.")
            return
        cls.bonus_per_gol = nilai
        print(f"  [INFO] Bonus per gol diubah menjadi {Pemain.format_rupiah(nilai)}.")

    @classmethod
    def dari_dict(cls, data: dict):
        obj = cls(data["nama_pemain"], data["posisi"])
        obj.gol         = data.get("gol", 0)
        obj.assist      = data.get("assist", 0)
        obj.clean_sheet = data.get("clean_sheet", 0)
        return obj

    @staticmethod
    def rating_performa(gol: int, assist: int) -> str:
        skor = gol + assist
        if skor >= 15:
            return "Luar Biasa ***"
        elif skor >= 8:
            return "Bagus **"
        elif skor >= 3:
            return "Cukup *"
        else:
            return "Perlu Ditingkatkan"


class ManajemenSkuad:
    nama_institusi = "Manchester United FC"
    batas_skuad    = 25
    total_skuad    = 0

    def __init__(self, nama_skuad: str, pelatih: str):
        self.nama_skuad = nama_skuad
        self.pelatih    = pelatih

        self.__daftar_pemain = []
        self.__anggaran      = 0.0

        ManajemenSkuad.total_skuad += 1

    @property
    def anggaran(self) -> float:
        return self.__anggaran

    @anggaran.setter
    def anggaran(self, nilai: float):
        if not isinstance(nilai, (int, float)):
            print("  [DITOLAK] Anggaran harus berupa angka.")
            return
        if nilai < 0:
            raise ValueError("Anggaran tidak boleh negatif.")
        self.__anggaran = float(nilai)
        print(f"  [INFO] Anggaran skuad '{self.nama_skuad}' "
              f"ditetapkan: {Pemain.format_rupiah(self.__anggaran)}")

    @property
    def daftar_pemain(self) -> list:
        return list(self.__daftar_pemain)

    def daftarkan_pemain(self, pemain):
        if not isinstance(pemain, Pemain):
            print("  [DITOLAK] Hanya objek Pemain yang dapat didaftarkan.")
            return
        if len(self.__daftar_pemain) >= ManajemenSkuad.batas_skuad:
            print(f"  [DITOLAK] Skuad sudah penuh (maks. {ManajemenSkuad.batas_skuad} pemain).")
            return
        self.__daftar_pemain.append(pemain)
        print(f"  [INFO] {pemain.nama} berhasil didaftarkan ke '{self.nama_skuad}'.")

    def cetak_skuad(self):
        print(f"\n  +-- Skuad : {self.nama_skuad}")
        print(f"  |   Pelatih: {self.pelatih}  |   Institusi: {ManajemenSkuad.nama_institusi}")
        if not self.__daftar_pemain:
            print("  |   (Belum ada pemain)")
        for i, p in enumerate(self.__daftar_pemain, start=1):
            print(f"  |   {i:>2}. #{p.no_punggung:<3} {p.nama:<22} [{p.posisi}]")
        print(f"  +-- Total: {len(self.__daftar_pemain)} pemain\n")

    def total_pengeluaran_gaji(self) -> float:
        return sum(p.hitung_gaji_bersih() for p in self.__daftar_pemain)

    def laporan_keuangan(self):
        total = self.total_pengeluaran_gaji()
        sisa  = self.__anggaran - total
        print(f"  {'Skuad':<25}: {self.nama_skuad}")
        print(f"  {'Anggaran':<25}: {Pemain.format_rupiah(self.__anggaran)}")
        print(f"  {'Total Gaji Bersih':<25}: {Pemain.format_rupiah(total)}")
        status = "SURPLUS" if sisa >= 0 else "DEFISIT"
        print(f"  {'Sisa Anggaran':<25}: {Pemain.format_rupiah(abs(sisa))} ({status})")

    @classmethod
    def ubah_batas_skuad(cls, batas_baru: int):
        if not isinstance(batas_baru, int) or batas_baru <= 0:
            print("  [DITOLAK] Batas skuad harus bilangan bulat positif.")
            return
        cls.batas_skuad = batas_baru
        print(f"  [INFO] Batas skuad diubah menjadi {batas_baru} pemain.")

    @classmethod
    def dari_dict(cls, data: dict):
        return cls(data["nama_skuad"], data["pelatih"])

    @staticmethod
    def cek_nama_skuad(nama) -> bool:
        return isinstance(nama, str) and len(nama.strip()) >= 3

    @staticmethod
    def format_persen(nilai: float) -> str:
        return f"{nilai * 100:.1f}%"


if __name__ == "__main__":

    garis = "=" * 68

    print(garis)
    print(" DEMO 1: Membuat Objek (minimal 2 per class)")
    print(garis)

    p1 = Pemain("Marcus Rashford",  10, "Penyerang", 450_000_000)
    p2 = Pemain("Bruno Fernandes",   8, "Gelandang", 500_000_000)
    p3 = Pemain("Andre Onana",       1, "Kiper",     420_000_000)
    p4 = Pemain.dari_dict({
        "nama": "Kobbie Mainoo",
        "no_punggung": 37,
        "posisi": "Gelandang",
        "gaji_dasar": 300_000_000,
    })

    s1 = Statistik("Marcus Rashford", "Penyerang")
    s2 = Statistik("Bruno Fernandes",  "Gelandang")
    s3 = Statistik.dari_dict({
        "nama_pemain": "Andre Onana",
        "posisi": "Kiper",
        "gol": 0, "assist": 0, "clean_sheet": 4,
    })

    skuad_utama = ManajemenSkuad("Skuad Utama",  "Ruben Amorim")
    skuad_u21   = ManajemenSkuad("Skuad U-21",   "Marc Skinner")

    print("\n  Semua objek berhasil dibuat.\n")

    print(garis)
    print(" DEMO 2: Instance Method")
    print(garis)

    print("\n[a] tampil_info() - Pemain")
    p1.tampil_info()
    print()
    p2.tampil_info()

    print("\n[b] tambah_gol() & tambah_clean_sheet() - Statistik")
    s1.tambah_gol(5)
    s1.tambah_gol(3)
    s1.tambah_gol(-1)
    s2.tambah_gol(7)
    s2.assist = 9
    s3.tambah_clean_sheet(4)
    s3.tambah_clean_sheet(0)

    print("\n[c] tampil_statistik() - Statistik")
    s1.tampil_statistik()
    print()
    s2.tampil_statistik()
    print()
    s3.tampil_statistik()

    print("\n[d] daftarkan_pemain() & cetak_skuad() - ManajemenSkuad")
    skuad_utama.anggaran = 2_000_000_000
    skuad_utama.daftarkan_pemain(p1)
    skuad_utama.daftarkan_pemain(p2)
    skuad_utama.daftarkan_pemain(p3)
    skuad_utama.daftarkan_pemain("bukan pemain")
    skuad_u21.anggaran = 800_000_000
    skuad_u21.daftarkan_pemain(p4)
    skuad_utama.cetak_skuad()
    skuad_u21.cetak_skuad()

    print("[e] laporan_keuangan() - ManajemenSkuad")
    skuad_utama.laporan_keuangan()
    print()
    skuad_u21.laporan_keuangan()

    print()
    print(garis)
    print(" DEMO 3: Class Method")
    print(garis)

    print("\n[a] Pemain.ubah_pajak() - mengubah atribut kelas pajak_gaji_pct")
    print(f"  Gaji bersih {p1.nama} sebelum: {Pemain.format_rupiah(p1.hitung_gaji_bersih())}")
    Pemain.ubah_pajak(0.10)
    print(f"  Gaji bersih {p1.nama} setelah: {Pemain.format_rupiah(p1.hitung_gaji_bersih())}")
    Pemain.ubah_pajak(1.5)

    print("\n[b] Statistik.ubah_bonus_gol() - mengubah atribut kelas bonus_per_gol")
    print(f"  Bonus {s1.nama_pemain} sebelum: {Pemain.format_rupiah(s1.hitung_bonus())}")
    Statistik.ubah_bonus_gol(3_000_000)
    print(f"  Bonus {s1.nama_pemain} setelah: {Pemain.format_rupiah(s1.hitung_bonus())}")
    Statistik.ubah_bonus_gol(-500_000)

    print("\n[c] ManajemenSkuad.ubah_batas_skuad() - mengubah atribut kelas batas_skuad")
    print(f"  Batas skuad saat ini: {ManajemenSkuad.batas_skuad}")
    ManajemenSkuad.ubah_batas_skuad(30)
    print(f"  Batas skuad setelah diubah: {ManajemenSkuad.batas_skuad}")
    ManajemenSkuad.ubah_batas_skuad(-5)

    print("\n[d] Factory Method dari_dict() (sudah dipakai di Demo 1)")
    data_p5 = {"nama": "Rasmus Hojlund", "no_punggung": 11,
                "posisi": "Penyerang", "gaji_dasar": 380_000_000}
    p5 = Pemain.dari_dict(data_p5)
    print(f"  Berhasil dibuat via dari_dict(): {p5.nama} | #{p5.no_punggung}")

    print()
    print(garis)
    print(" DEMO 4: Static Method")
    print(garis)

    print("\n[a] Pemain.cek_no_punggung()")
    for no in [7, 99, 0, 100, "X"]:
        print(f"  cek_no_punggung({str(no):<5}) -> {Pemain.cek_no_punggung(no)}")

    print("\n[b] Pemain.format_rupiah()")
    print(f"  format_rupiah(450_000_000) -> {Pemain.format_rupiah(450_000_000)}")
    print(f"  format_rupiah(None)        -> {Pemain.format_rupiah(None)}")

    print("\n[c] Statistik.rating_performa()")
    for g, a in [(18, 2), (6, 3), (2, 1), (0, 0)]:
        print(f"  rating_performa(gol={g}, assist={a}) -> {Statistik.rating_performa(g, a)}")

    print("\n[d] ManajemenSkuad.cek_nama_skuad()")
    for nm in ["Skuad A", "OK", "", 123]:
        print(f"  cek_nama_skuad({str(nm):<14}) -> {ManajemenSkuad.cek_nama_skuad(nm)}")

    print("\n[e] ManajemenSkuad.format_persen()")
    print(f"  format_persen(0.10) -> {ManajemenSkuad.format_persen(0.10)}")
    print(f"  format_persen(0.05) -> {ManajemenSkuad.format_persen(0.05)}")

    print()
    print(garis)
    print(" DEMO 5: Pengujian Setter - Data Valid & Tidak Valid")
    print(garis)

    print("\n[1] Setter no_punggung pada objek Pemain")
    print(f"  No punggung {p2.nama} sekarang: {p2.no_punggung}")
    p2.no_punggung = 18
    print(f"  Setelah diubah ke 18       : {p2.no_punggung}")
    p2.no_punggung = 0
    print(f"  Setelah coba diubah ke 0   : {p2.no_punggung}  (tetap 18)")
    p2.no_punggung = 200
    print(f"  Setelah coba diubah ke 200 : {p2.no_punggung}  (tetap 18)")

    print("\n[2] Setter gaji_dasar pada objek Pemain")
    print(f"  Gaji dasar {p3.nama} sekarang: {Pemain.format_rupiah(p3.gaji_dasar)}")
    p3.gaji_dasar = 480_000_000
    print(f"  Setelah diubah ke 480 jt   : {Pemain.format_rupiah(p3.gaji_dasar)}")
    p3.gaji_dasar = 5_000_000
    print(f"  Setelah coba 5 jt (kecil)  : {Pemain.format_rupiah(p3.gaji_dasar)}  (tetap)")
    try:
        p3.gaji_dasar = -50_000_000
    except ValueError as e:
        print(f"  [TERBUKTI] ValueError negatif -> {e}")

    print("\n[3] Setter gol pada objek Statistik")
    print(f"  Gol {s1.nama_pemain} sekarang: {s1.gol}")
    s1.gol = 15
    print(f"  Setelah diubah ke 15       : {s1.gol}")
    try:
        s1.gol = -3
    except ValueError as e:
        print(f"  [TERBUKTI] ValueError negatif -> {e}")
    s1.gol = "dua belas"
    print(f"  Setelah coba string        : {s1.gol}  (tetap 15)")

    print("\n[4] Setter clean_sheet pada objek Statistik (harus kiper)")
    s_bukan_kiper = Statistik("Bruno Fernandes", "Gelandang")
    s_bukan_kiper.clean_sheet = 5
    print(f"  Clean sheet Gelandang      : {s_bukan_kiper.clean_sheet}  (tetap 0)")
    print(f"  Clean sheet Kiper (s3)     : {s3.clean_sheet}")
    s3.clean_sheet = 8
    print(f"  Setelah diubah ke 8        : {s3.clean_sheet}")
    try:
        s3.clean_sheet = -2
    except ValueError as e:
        print(f"  [TERBUKTI] ValueError negatif -> {e}")

    print("\n[5] Setter anggaran pada objek ManajemenSkuad")
    print(f"  Anggaran {skuad_u21.nama_skuad} sekarang: {Pemain.format_rupiah(skuad_u21.anggaran)}")
    skuad_u21.anggaran = 1_000_000_000
    print(f"  Setelah diubah ke 1 Miliar : {Pemain.format_rupiah(skuad_u21.anggaran)}")
    skuad_u21.anggaran = "satu miliar"
    print(f"  Setelah coba string        : {Pemain.format_rupiah(skuad_u21.anggaran)}  (tetap)")
    try:
        skuad_u21.anggaran = -500_000_000
    except ValueError as e:
        print(f"  [TERBUKTI] ValueError negatif -> {e}")

    print()
    print(garis)
    print(" DEMO 6: Atribut Kelas")
    print(garis)
    print(f"\n  [Pemain]")
    print(f"    nama_klub        = {Pemain.nama_klub}")
    print(f"    musim_aktif      = {Pemain.musim_aktif}")
    print(f"    total_terdaftar  = {Pemain.total_terdaftar} objek dibuat")
    print(f"    pajak_gaji_pct   = {ManajemenSkuad.format_persen(Pemain.pajak_gaji_pct)}")
    print(f"\n  [Statistik]")
    print(f"    nama_kompetisi   = {Statistik.nama_kompetisi}")
    print(f"    musim            = {Statistik.musim}")
    print(f"    bonus_per_gol    = {Pemain.format_rupiah(Statistik.bonus_per_gol)}")
    print(f"    bonus_clean_sheet= {Pemain.format_rupiah(Statistik.bonus_clean_sheet)}")
    print(f"\n  [ManajemenSkuad]")
    print(f"    nama_institusi   = {ManajemenSkuad.nama_institusi}")
    print(f"    batas_skuad      = {ManajemenSkuad.batas_skuad} pemain")
    print(f"    total_skuad      = {ManajemenSkuad.total_skuad} skuad dibuat")

    print()
    print(garis)
    print("  Program selesai. Glory Glory Man United!")
    print(garis)