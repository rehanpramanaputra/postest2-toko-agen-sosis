````
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
````
![WhatsApp Image 2023-09-08 at 07 14 41-fotor-bg-remover-2023091313018](https://github.com/rehanpramanaputra/postest2-toko-agen-sosis/assets/144860056/4258b0c5-e11e-4480-b906-708f3bed4c8a)
![Screenshot (57)](https://github.com/rehanpramanaputra/postest2-toko-agen-sosis/assets/144860056/8673bebb-0046-45ee-a21f-aaba5b2555d1)
/![Screenshot (54)](https://github.com/rehanpramanaputra/postest2-toko-agen-sosis/assets/144860056/90a95d6c-12de-47c9-9f9b-99806862d9e0)
![Screenshot (55)](https://github.com/rehanpramanaputra/postest2-toko-agen-sosis/assets/144860056/a9b8cb03-31ff-4155-b58e-efdb4f7932a6)
![Screenshot (56)](https://github.com/rehanpramanaputra/postest2-toko-agen-sosis/assets/144860056/400edb9f-6a41-419c-aeee-1bfe9f1b6977)
![flowchart postest 2 drawio](https://github.com/rehanpramanaputra/postest2-toko-agen-sosis/assets/144860056/7ae62576-55d5-44f9-ae1e-11ee00e8a947)
![Screenshot (62)](https://github.com/rehanpramanaputra/postest2-toko-agen-sosis/assets/144860056/9763e814-7389-49b5-acaa-b8ceb4f34a02)
![Screenshot (58)](https://github.com/rehanpramanaputra/postest2-toko-agen-sosis/assets/144860056/82c746ca-2d01-45c2-bcf7-5dc69b691bc8)
![Screenshot (61)](https://github.com/rehanpramanaputra/postest2-toko-agen-sosis/assets/144860056/f769b5c8-70de-4d0a-8690-903a0be85d15)
![Screenshot (60)](https://github.com/rehanpramanaputra/postest2-toko-agen-sosis/assets/144860056/af6b82f5-607b-44e2-a17a-5e3af0736fab)
![Screenshot (59)](https://github.com/rehanpramanaputra/postest2-toko-agen-sosis/assets/144860056/12c198eb-b80f-4ce7-8c0a-ba5fa08d9e84)
![Screenshot (63)](https://github.com/rehanpramanaputra/postest2-toko-agen-sosis/assets/144860056/5017ebbe-9c0b-4466-99b9-2d6a1787558d)

