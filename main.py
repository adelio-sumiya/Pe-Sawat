import os
import csv
from datetime import datetime
import time

def print_header(text):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("="*50)
    print(f"{text:^50}")
    print("="*50)

pengguna = {
        "admin": {"username": "admin", "password": "admin123", "role": "admin"},
        "user1": {"username": "user1", "password": "user123", "role": "user"}
}

print('''                                                                                                             
8 888888888o   8 8888888888     d888888o.           .8. `8.`888b                 ,8' .8.    8888888 8888888888 
8 8888    `88. 8 8888         .`8888:' `88.        .888. `8.`888b               ,8' .888.         8 8888       
8 8888     `88 8 8888         8.`8888.   Y8       :88888. `8.`888b             ,8' :88888.        8 8888       
8 8888     ,88 8 8888         `8.`8888.          . `88888. `8.`888b     .b    ,8' . `88888.       8 8888       
8 8888.   ,88' 8 888888888888  `8.`8888.        .8. `88888. `8.`888b    88b  ,8' .8. `88888.      8 8888       
8 888888888P'  8 8888           `8.`8888.      .8`8. `88888. `8.`888b .`888b,8' .8`8. `88888.     8 8888       
8 8888         8 8888            `8.`8888.    .8' `8. `88888. `8.`888b8.`8888' .8' `8. `88888.    8 8888       
8 8888         8 8888        8b   `8.`8888.  .8'   `8. `88888. `8.`888`8.`88' .8'   `8. `88888.   8 8888       
8 8888         8 8888        `8b.  ;8.`8888 .888888888. `88888. `8.`8' `8,`' .888888888. `88888.  8 8888       
8 8888         8 888888888888 `Y8888P ,88P'.8'       `8. `88888. `8.`   `8' .8'       `8. `88888. 8 8888       
''')
current_user = []
def login():
    while True:
        print("=== SISTEM PEMESANAN TIKET PESAWAT ===")
        username = input("Username: ")
        password = input("Password: ")

        if username in pengguna and pengguna[username]["password"] == password:
            current_user = pengguna[username]
            print(f"Login berhasil sebagai {current_user['role']}")
            return True
        else:
            print("Username atau password salah!")
            if input("Coba lagi? (y/n): ").lower() != 'y':
                return False



def menu_admin():
    while True:
        print('''
        ===== Menu Admin =====
          1. lihat jadwal pesawat
          2. kelola data jadwal pesawat
          3. lihat laporan
          4. logout
          ''')
        try:
            masukkan = int(input("Masukkan pilihan: "))
            if masukkan == 1:
                jadwal_pesawat()
            elif masukkan == 2:
                klola_data()
            elif masukkan == 3:
                lihat_laporan()
            elif masukkan == 4:
                login()
            else:
                print("Pilihan yang anda masukkan tidak ada.")
        except ValueError:
            print("Input tidak valid! Masukkan angka sesuai pilihan menu.")

def klola_data():
    pass

def lihat_laporan():
    pass


def menu_user():
    while True:
        print('''
         ===== Menu User =====
          1. pemesanan tiket
          2. lihat jadwal pesawat
          3. riwayat pemesanan
          4. logout
          ''')
        try:
            masukkan = int(input("Masukkan pilihan: "))
            if masukkan == 1:
                pemesanan_tiket()
            elif masukkan == 2:
               jadwal_pesawat()
            elif masukkan == 3:
                riwayat()
            elif masukkan == 4:
                login()
            else:
                print("Pilihan yang anda masukkan tidak ada.")
        except ValueError:
            print("Input tidak valid! Masukkan angka sesuai pilihan menu.")

def load_jadwal():
    jadwal = []
    with open('jadwal_pesawat.csv', 'r') as file:
        reader = csv.DictReader(file)
    return jadwal
    
def tampilkan_jadwal():
    jadwal = load_jadwal()
    print("\nJadwal Penerbangan:")
    print("-"*80)
    print(f"{'NO':<4}{'AIRLINES':<15}{'WAKTU':<20}{'HARGA':<15}")
    print("-"*80)
    for row in jadwal:
        print(f"{row['NO']:<4}{row['AIRLINES']:<15}{row['TIME']:<20}Rp {int(row['PRICE']):,}")
    print("-"*80)
    
def pemesanan_tiket():
    print_header("PEMESANAN TIKET")
    
    # input nama
    nama = input("Masukkan nama pemesan: ")
    
    # input tanggal
    while True:
        try:
            tanggal = input("Masukkan tanggal keberangkatan (DD/MM/YYYY): ")
            datetime.strptime(tanggal, '%d/%m/%Y')
            break
        except ValueError:
            print("Format tanggal salah! Gunakan format DD/MM/YYYY")
    
    # pilih kota
    kota = ['Jakarta', 'Surabaya', 'Makassar', 'Denpasar']
    print("\nPilih kota keberangkatan:")
    for i, city in enumerate(kota, 1):
        print(f"{i}. {city}")
    
    while True:
        try:
            departure = int(input("Pilih nomor kota keberangkatan: "))
            if 1 <= departure <= 4:
                departure = kota[departure-1]
                break
        except ValueError:
            pass
        print("Pilihan tidak valid!")
    
    print("\nPilih kota tujuan:")
    for i, city in enumerate(kota, 1):
        print(f"{i}. {city}")
    
    while True:
        try:
            arrival = int(input("Pilih nomor kota tujuan: "))
            if 1 <= arrival <= 4 and kota[arrival-1] != departure:
                arrival = kota[arrival-1]
                break
        except ValueError:
            pass
        print("Pilihan tidak valid!")
    
    # tampilkan dan pilih jadwal
    print("\nJadwal Penerbangan yang Tersedia:")
    tampilkan_jadwal()
    
    jadwal = load_jadwal()
    while True:
        try:
            no_pesawat = input("Pilih nomor penerbangan: ")
            pesawat = next((p for p in jadwal if p['NO'] == no_pesawat), None)
            if pesawat:
                break
            print("Nomor penerbangan tidak valid!")
        except ValueError:
            print("Input tidak valid!")
    
    # input jumlah penumpang
    while True:
        try:
            jumlah_penumpang = int(input("\nMasukkan jumlah penumpang: "))
            if jumlah_penumpang > 0:
                break
            print("Jumlah penumpang harus lebih dari 0!")
        except ValueError:
            print("Input tidak valid!")
    
    # hitung total harga
    total_harga = int(pesawat['PRICE']) * jumlah_penumpang
    print(f"\nTotal harga: Rp {total_harga:,}")
    
    # pilih metode pembayaran
    metode_pembayaran = ['Transfer', 'Kartu Kredit', 'E-wallet']
    print("\nPilih metode pembayaran:")
    for i, metode in enumerate(metode_pembayaran, 1):
        print(f"{i}. {metode}")
    
    while True:
        try:
            pilihan = int(input("Pilih metode pembayaran: "))
            if 1 <= pilihan <= 3:
                metode = metode_pembayaran[pilihan-1]
                break
        except ValueError:
            pass
        print("Pilihan tidak valid!")
    
    # cetak struk
    print_header("STRUK PEMBAYARAN")
    print(f"Tanggal Pemesanan    : {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print(f"Nama Pemesan         : {nama}")
    print(f"Tanggal Keberangkatan: {tanggal}")
    print(f"Rute Penerbangan    : {departure} -> {arrival}")
    print(f"Maskapai            : {pesawat['AIRLINES']}")
    print(f"Waktu               : {pesawat['TIME']}")
    print(f"Jumlah Penumpang    : {jumlah_penumpang}")
    print(f"Total Harga         : Rp {total_harga:,}")
    print(f"Metode Pembayaran   : {metode}")
    print("\nTerima kasih telah memesan!")
    
    # simpan ke riwayat
    with open('riwayat_pemesanan.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([tanggal, nama, departure, arrival, pesawat['AIRLINES'], 
                        pesawat['TIME'], jumlah_penumpang, total_harga, metode])
    
    input("\nTekan Enter untuk kembali ke menu...")


def jadwal_pesawat():
    try:
        with open('jadwal_pesawat.csv', mode='r', newline='') as file:
            reader = csv.reader(file)
            header = next(reader)
            print(f"{header[0]:<20} {header[1]:<20} {header[2]:<20} {header[3]:<20}")
            print("-" * 80)
            for row in reader:
                print(f"{row[0]:<20} {row[1]:<20} {row[2]:<20} {row[3]:<20}")
    except FileNotFoundError:
        print("File jadwal_pesawat.csv tidak ditemukan.")

def riwayat():
    pass

def main():
    login()
    while True:
        if current_user == 'admin':
            menu_admin()
            break
        else:
            menu_user()
            break

if __name__ == "__main__":
    main()