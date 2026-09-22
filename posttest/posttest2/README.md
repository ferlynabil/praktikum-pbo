# Sistem Manajemen Skuad & Gaji Pemain Manchester United


**Tema:** Manajemen Pemain Manchester United  
**Nama:** [Ferly Ahmad Nabil]  
**NIM:** [2509106024]  
**Kelas:** [A'25]

Program Python berbasis *Object-Oriented Programming* (OOP) yang mengelola data pemain, kalkulasi gaji bersih setelah pajak dan bonus performa, serta struktur skuad tim Manchester United. 


---

## 📌 Fitur & Pemenuhan Modul

| Modul | Topik Utama | Implementasi dalam Kode |
| :--- | :--- | :--- |
| **Modul 1** | *Class & Object* | Implementasi 4 class utama (`Pemain`, `PemainDepan`, `Kiper`, dan `ManajemenMU`) serta instansiasi minimal 2 objek untuk tiap class. |
| **Modul 2** | *Atribut & Method* | Atribut kelas (`nama_klub`, `musim_liga`, `pajak_gaji`, `total_pemain`), atribut private (`__no_punggung`, `__gaji_dasar`, `__daftar_pemain`), serta penerapan *Instance Method*, *Class Method*, dan *Static Method*. |
| **Modul 3** | *Encapsulation & Property* | Enkapsulasi atribut private menggunakan decorator `@property` (getter) dan `@<property>.setter` (setter) yang dilengkapi fungsi validasi data. |

---

## 🏗️ Struktur Class

```text
                   +------------------------+
                   |         Pemain         |  (Abstract Base Class)
                   +------------------------+
                               |
            +------------------+------------------+
            |                                     |
+------------------------+               +------------------------+
|      PemainDepan       |               |         Kiper          |
+------------------------+               +------------------------+
            \                                     /
             +-----------------+-----------------+
                               |  (Digunakan oleh)
                     +-------------------+
                     |    ManajemenMU    |
                     +-------------------+

```

### 1. `Pemain` (Base Class)

* **Atribut Kelas:** `nama_klub`, `musim_liga`, `pajak_gaji`, `total_pemain`.
* **Atribut Instance:** `nama` (Public), `__no_punggung` (Private), `__gaji_dasar` (Private).
* **Property (Getter/Setter):**
* `no_punggung`: Memvalidasi agar nomor berada pada rentang 1–99.
* `gaji_dasar`: Memvalidasi agar nilai gaji tidak negatif (akan me-raise `ValueError`).


* **Method:**
* `ubah_pajak_gaji(cls, pajak_baru)` (`@classmethod`): Mengubah persentase pajak gaji seluruh klub.
* `validasi_no_punggung(no_punggung)` (`@staticmethod`): Memeriksa tipe data dan rentang nomor.
* `format_rupiah(angka)` (`@staticmethod`): Mengubah format angka menjadi mata uang Rupiah.



### 2. `PemainDepan` (Subclass)

* **Atribut Kelas:** `bonus_per_gol` (Rp2.000.000 / gol).
* **Atribut Instance:** `jumlah_gol` (Public).
* **Method Utama:**
* `tambah_gol(jumlah)`: *Instance method* untuk menambah statistik gol.
* `hitungGaji()`: Override hitung gaji (Gaji Dasar + Bonus Gol - Pajak).
* `dari_dict(cls, data)` (`@classmethod`): *Factory method* pembuatan objek dari data dictionary.



### 3. `Kiper` (Subclass)

* **Atribut Kelas:** `bonus_per_clean_sheet` (Rp1.500.000 / clean sheet).
* **Atribut Instance:** `jumlah_clean_sheet` (Public).
* **Method Utama:**
* `tambah_clean_sheet(jumlah)`: *Instance method* untuk menambah catatan clean sheet.
* `hitungGaji()`: Override hitung gaji (Gaji Dasar + Bonus Clean Sheet - Pajak).
* `dari_dict(cls, data)` (`@classmethod`): *Factory method* pembuatan objek dari data dictionary.



### 4. `ManajemenMU` (Class Pengelola Skuad)

* **Atribut Kelas:** `nama_lembaga`.
* **Atribut Instance:** `nama_tim`, `__daftar_pemain` (Private list).
* **Method Utama:**
* `tambah_pemain(pemain)`: Menambahkan objek pemain ke daftar internal.
* `cetak_total_gaji()`: Menghitung total pengeluaran gaji bersih seluruh pemain dalam sebuah skuad.

---

## 🧪 Panduan Pengujian (Skenario Demo)

Pengujian program terdapat pada blok `if __name__ == "__main__":` yang berada di bagian bawah kode program, mencakup 8 skenario pengujian (Demo):

1. **Demo 1 (Abstract Behavior):** Pengujian pemanggilan method `tampilKontrak()` langsung dari instance class dasar `Pemain` untuk membuktikan method wajib di-*override* (memunculkan `NotImplementedError`).
2. **Demo 2 (Inisialisasi Objek):** Pembuatan minimal 2 objek untuk tiap class (`depan1`, `depan2`, `depan3`, `kiper1`, dll.), baik melalui konstruktor biasa (`__init__`) maupun *factory method* berupa class method (`dari_dict`).
3. **Demo 3 & 4 (Instance Methods):** Memanggil rincian kontrak pemain dan menguji penambahan statistik (gol/clean sheet) dengan data input positif maupun negatif (ditolak).
4. **Demo 5 (Encapsulation & Validation):**
* Menguji setter dengan data valid (gaji berhasil diubah).
* Menguji setter dengan data invalid (angka negatif memicu `ValueError` dan nomor punggung > 99 ditolak).
5. **Demo 6 (Class Method):** Mengubah atribut kelas `pajak_gaji` via `ubah_pajak_gaji()` secara global dan melihat dampaknya pada kalkulasi *take-home pay* pemain yang bersifat dinamis.
6. **Demo 7 (Static Method):** Pengujian dua fungsi utilitas (bantuan) `validasi_no_punggung()` dan `format_rupiah()` secara independen melalui class pemanggilnya.
7. **Demo 8 (Interaksi Objek & Manajemen):** Menggabungkan objek-objek pemain ke dalam instance pengelola `ManajemenMU` (Skuad Utama & Skuad U21) untuk memproses kalkulasi dan mencetak total pengeluaran gaji seluruh pemain dalam skuad.

```

```