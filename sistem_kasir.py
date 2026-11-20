
class Produk:
    jumlah_produk = 0

    # Constructor
    def __init__(self, nama, harga, stok):
        self._nama = nama
        self._harga = harga
        self._stok = stok
        Produk.jumlah_produk += 1

    # Property nama
    @property
    def nama(self):
        return self._nama

    @nama.setter
    def nama(self, nilai):
        if nilai.strip():
            self._nama = nilai
        else:
            raise ValueError("Nama tidak boleh kosong!")

    # Property harga
    @property
    def harga(self):
        return self._harga

    @harga.setter
    def harga(self, nilai):
        if nilai > 0:
            self._harga = nilai
        else:
            raise ValueError("Harga harus lebih dari 0!")

    # Property stok
    @property
    def stok(self):
        return self._stok

    @stok.setter
    def stok(self, nilai):
        if nilai >= 0:
            self._stok = nilai
        else:
            raise ValueError("Stok tidak boleh negatif!")

    # Class Method
    @classmethod
    def total_produk(cls):
        return cls.jumlah_produk

    # Static Method
    @staticmethod
    def format_rupiah(nilai):
        return "Rp" + format(nilai, ",").replace(",", ".")


# Class kedua
class Kasir:

    def __init__(self, nama_kasir):
        self.nama_kasir = nama_kasir
        self.keranjang = []

    # Method menambahkan produk
    def tambah_produk(self, produk, jumlah):
        if jumlah <= 0:
            print("Jumlah harus lebih dari 0!")
        elif jumlah > produk.stok:
            print("Stok produk tidak mencukupi!")
        else:
            produk.stok -= jumlah
            self.keranjang.append((produk, jumlah))
            print("Produk berhasil ditambahkan!")

    # Method menampilkan keranjang
    def tampilkan_keranjang(self):
        print("\n===== KERANJANG BELANJA =====")

        if not self.keranjang:
            print("Keranjang masih kosong.")
            return

        for produk, jumlah in self.keranjang:
            subtotal = produk.harga * jumlah
            print(
                f"{produk.nama} x{jumlah} = "
                f"{Produk.format_rupiah(subtotal)}"
            )

    # Method menghitung total
    def hitung_total(self):
        total = 0
        for produk, jumlah in self.keranjang:
            total += produk.harga * jumlah
        return total

    # Method pembayaran
    def pembayaran(self):
        if not self.keranjang:
            print("Keranjang masih kosong!")
            return

        total = self.hitung_total()

        print("\n===== PEMBAYARAN =====")
        print("Total:", Produk.format_rupiah(total))

        try:
            bayar = int(input("Masukkan uang pembayaran: Rp"))

            if bayar < total:
                print("Uang pembayaran tidak mencukupi!")
                return

            kembalian = bayar - total

            print("\n===== STRUK PEMBELIAN =====")
            print("Kasir:", self.nama_kasir)
            self.tampilkan_keranjang()
            print("Total:", Produk.format_rupiah(total))
            print("Bayar:", Produk.format_rupiah(bayar))
            print("Kembalian:",
                  Produk.format_rupiah(kembalian))
            print("===========================")
            print("Terima kasih sudah berbelanja!")

            self.keranjang.clear()

        except ValueError:
            print("Masukkan nominal berupa angka!")


# Membuat object dari class Produk
produk1 = Produk("Indomie", 3500, 20)
produk2 = Produk("Aqua", 4000, 15)
produk3 = Produk("Roti", 5000, 10)

# Membuat object dari class Kasir
kasir = Kasir("Nurul Falah")

# Program utama
while True:
    print("\n===== SISTEM KASIR SEDERHANA =====")
    print("1. Lihat Daftar Produk")
    print("2. Tambah Produk ke Keranjang")
    print("3. Lihat Keranjang")
    print("4. Pembayaran")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        print("\n===== DAFTAR PRODUK =====")

        daftar = [produk1, produk2, produk3]

        for i, produk in enumerate(daftar, 1):
            print(
                f"{i}. {produk.nama} | "
                f"Harga: {Produk.format_rupiah(produk.harga)} | "
                f"Stok: {produk.stok}"
            )

    elif pilihan == "2":
        print("\nPilih Produk:")
        print("1. Indomie")
        print("2. Aqua")
        print("3. Roti")

        try:
            nomor = int(input("Nomor produk: "))
            jumlah = int(input("Jumlah beli: "))

            daftar = [produk1, produk2, produk3]

            if 1 <= nomor <= len(daftar):
                kasir.tambah_produk(daftar[nomor - 1], jumlah)
            else:
                print("Pilihan produk tidak tersedia!")

        except ValueError:
            print("Masukkan angka yang benar!")

    elif pilihan == "3":
        kasir.tampilkan_keranjang()

    elif pilihan == "4":
        kasir.pembayaran()

    elif pilihan == "5":
        print("Terima kasih telah menggunakan program!")
        break

    else:
        print("Pilihan tidak valid!")
