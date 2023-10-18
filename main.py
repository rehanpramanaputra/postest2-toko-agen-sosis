import sys
def check_login(username, password):
    if username == "rehan" and password == "2309116082":
        return True
    else:
        return False

username_input = input("Masukkan username: ")
password_input = input("Masukkan password: ")

if not check_login(username_input, password_input):
    print("salah login woi!")
    sys.exit()

print("login anda benar!")

from prettytable import PrettyTable

class Sosis:
    def __init__(self, jenis, harga, stok):
        self.jenis = jenis
        self.harga = harga
        self.stok = stok

class TokoSosis:
    def __init__(self):
        # Inisiasi jenis-jenis sosis dengan harga dan stok awal
        self.sosis = [
            Sosis("sapi", 30000, 10),
            Sosis("ayam", 10000, 15),
            Sosis("kambing", 20000, 5)
        ]

    def tampilkan_sosis(self):
        tabel = PrettyTable()
        tabel.field_names = ["Jenis Sosis", "Harga", "Stok"]
        for sosis in self.sosis:
            tabel.add_row([sosis.jenis, "Rp" + str(sosis.harga), sosis.stok])
        print(tabel)

    def tambah_stok(self, jenis_sosis, jumlah):
        for sosis in self.sosis:
            if sosis.jenis == jenis_sosis:
                sosis.stok += jumlah
                print(f"Stok {jenis_sosis} bertambah {jumlah}, sekarang {sosis.stok}")
                return
        print(f"Jenis sosis {jenis_sosis} tidak ditemukan.")

    def jual_sosis(self, jenis_sosis, jumlah):
        for sosis in self.sosis:
            if sosis.jenis == jenis_sosis:
                if sosis.stok >= jumlah:
                    sosis.stok -= jumlah
                    print(f"Terjual {jumlah} sosis {jenis_sosis}")
                    return sosis.harga * jumlah
                else:
                    print(f"Maaf, stok sosis {jenis_sosis} tidak cukup")
                    return None
        print(f"Maaf, kami tidak memiliki sosis {jenis_sosis}")
        return None

def main():
    toko = TokoSosis()

    while True:
        print("\n--- Menu Utama Toko Sosis ---")
        role = input(" penjual (p) atau pembeli (b)? Keluar (k): ")

        if role == "p":
            while True:
                print("\n--- Antarmuka Penjual ---")
                aksi = input("Tambah stok (t), Lihat stock sosis (l), Kembali (k): ")
                if aksi == "k":
                    break
                elif aksi == "t":
                    jenis = input("Masukkan jenis sosis (sapi/ayam/kambing): ")
                    jumlah = int(input("Masukkan jumlah yang ditambahkan: "))
                    toko.tambah_stok(jenis, jumlah)
                elif aksi == "l":
                    toko.tampilkan_sosis()
                else:
                    print("Pilihan tidak dikenal.")

        elif role == "b":
            while True:
                print("\n--- Antarmuka Pembeli ---")
                toko.tampilkan_sosis()
                aksi = input("Beli sosis (b), Kembali (k): ")
                if aksi == "k":
                    break
                elif aksi == "b":
                    jenis = input("Jenis sosis apa yang ingin di beli? (sapi/ayam/kambing) ")
                    jumlah = int(input("Berapa banyak yang ingin di beli? "))
                    total = toko.jual_sosis(jenis, jumlah)
                    if total:
                        print(f"Total yang harus dibayar Rp{total}")
                else:
                    print("Pilihan tidak dikenal.")

        elif role == "k":
            break

        else:
            print("Pilihan tidak dikenal.")

if __name__ == "__main__":
    main()
