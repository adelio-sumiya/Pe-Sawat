import os
import csv
from datetime import datetime
import time
import pandas as pd
from tabulate import tabulate



# ============================ fungsi tambahan ============================
tw = os.get_terminal_size().columns
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

tw = os.get_terminal_size().columns

def tengah(text, b=tw):
    print(f'{text}'.center(b))

def cover():
    tengah("8 888888888o   8 8888888888     d888888o.           .8. `8.`888b                 ,8' .8.    8888888 8888888888") 
    tengah("8 8888    `88. 8 8888         .`8888:' `88.        .888. `8.`888b               ,8' .888.         8 8888      ")
    tengah("8 8888     `88 8 8888         8.`8888.   Y8       :88888. `8.`888b             ,8' :88888.        8 8888      ") 
    tengah("8 8888     ,88 8 8888         `8.`8888.          . `88888. `8.`888b     .b    ,8' . `88888.       8 8888      ") 
    tengah("8 8888.   ,88' 8 888888888888  `8.`8888.        .8. `88888. `8.`888b    88b  ,8' .8. `88888.      8 8888      ") 
    tengah("8 888888888P'  8 8888           `8.`8888.      .8`8. `88888. `8.`888b .`888b,8' .8`8. `88888.     8 8888      ") 
    tengah("8 8888         8 8888            `8.`8888.    .8' `8. `88888. `8.`888b8.`8888' .8' `8. `88888.    8 8888      ") 
    tengah("8 8888         8 8888        8b   `8.`8888.  .8'   `8. `88888. `8.`888`8.`88' .8'   `8. `88888.   8 8888      ") 
    tengah("8 8888         8 8888        `8b.  ;8.`8888 .888888888. `88888. `8.`8' `8,`' .888888888. `88888.  8 8888      ") 
    tengah("8 8888         8 888888888888 `Y8888P ,88P'.8'       `8. `88888. `8.`   `8' .8'       `8. `88888. 8 8888      ") 


def garis():
    print('='*tw)

def print_header(text):
    clear()
    cover()
    print("="*tw)
    print(f"{text}".center(tw))
    print("="*tw)


def login():
    while True:
        garis()
        cover()
        garis()
        print("1. Login")
        print("2. Keluar")
        
        pilihan = input("\nPilih menu: ")
        
        if pilihan == '1':
            clear()
            cover()
            garis()
            tengah(".##........#######...######...####.##....##")
            tengah(".##.......##.....##.##....##...##..###...##")
            tengah(".##.......##.....##.##.........##..####..##")
            tengah(".##.......##.....##.##...####..##..##.##.##")
            tengah(".##.......##.....##.##....##...##..##..####")
            tengah(".##.......##.....##.##....##...##..##...###")
            tengah(".########..#######...######...####.##....##")           
            garis()
            username = input("Username: ")
            password = input("Password: ")
            pengguna = {'user' : 'user123', 'admin' : 'admin123'}
            if username in pengguna and pengguna[username] == password:
                print("\nLogin berhasil!")
                time.sleep(1)
                if username == 'admin':
                    menu_admin()
                else:
                    menu_user()
            else:
                print("\nUsername atau password salah!")
                time.sleep(1)
        
        elif pilihan == '2':
            print("\nTerima kasih telah menggunakan layanan kami!")
            break
        else:
            print("Menu tidak valid!")


# ============================ admin ============================
def menu_admin():
    while True:
        print_header('MENU ADMIN') 
        menu = [
        "1. Lihat Jadwal Pesawat",
        "2. Kelola Jadwal Pesawat",
        "3. Lihat Laporan",
        "4. Logout",
        ]
        for item in menu:
            print(item.center(tw))       
        try:
            masukkan = int(input("Masukkan pilihan: "))
            if masukkan == 1:
                tampilkan_jadwal()
                input("\nTekan Enter untuk kembali ke menu...")    
            elif masukkan == 2:
                klola_data()
            elif masukkan == 3:
                lihat_laporan()
                input("\nTekan Enter untuk melanjutkan...")
            elif masukkan == 4:
                login()
            else:
                print("Pilihan yang anda masukkan tidak ada.")
        except ValueError:
            print("Input tidak valid! Masukkan angka sesuai pilihan menu.")

def klola_data():
    while True:
        print_header("EDIT JADWAL PENERBANGAN")
        print("1. Tambah Jadwal".center(tw))
        print("2. Edit Jadwal".center(tw))
        print("3. Kembali".center(tw))
        garis()
        pilihan = input("\nPilih menu: ")
        
        if pilihan == '1':
            jadwal = load_jadwal()
            new_no = str(len(jadwal) + 1)
            airlines = input("Masukkan nama maskapai: ")
            waktu = input("Masukkan waktu (HH.MM - HH.MM): ")
            while True:
                try:
                    harga = int(input("Masukkan harga: "))
                    break
                except ValueError:
                    print("Harga harus berupa angka!")
            
            with open('jadwal_pesawat.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([new_no, airlines, waktu, harga])
            print("\nJadwal berhasil ditambahkan!")
            
        elif pilihan == '2':
            tampilkan_jadwal()
            no = input("\nMasukkan nomor jadwal yang akan diedit: ")
            jadwal = load_jadwal()
            
            for row in jadwal:
                if row['NO'] == no:
                    row['AIRLINES'] = input("Masukkan nama maskapai baru: ")
                    row['TIME'] = input("Masukkan waktu baru (HH.MM - HH.MM): ")
                    while True:
                        try:
                            row['PRICE'] = input("Masukkan harga baru: ")
                            break
                        except ValueError:
                            print("Harga harus berupa angka!")
                    break
            
            with open('jadwal_pesawat.csv', 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=['NO', 'AIRLINES', 'TIME', 'PRICE'])
                writer.writeheader()
                writer.writerows(jadwal)
            print("\nJadwal berhasil diubah!")
            
        elif pilihan == '3':
            break
        
        input("\nTekan Enter untuk melanjutkan...")

def lihat_laporan():
    return riwayat()

# ============================ user ============================
def menu_user():
    clear()
    while True:
        print_header('MENU')
        menu = [
        "1. Pemesanan Tiket",
        "2. Lihat Jadwal Penerbangan",
        "3. Riwayat Pemesanan",
        "4. Logout",
        ]
        for item in menu:
            print(item.center(tw))
        try:
            garis()
            masukkan = int(input("Masukkan pilihan: "))
            if masukkan == 1:
                pemesanan_tiket()
            elif masukkan == 2:
                tampilkan_jadwal()
                input("\nTekan Enter untuk kembali ke menu...")       
            elif masukkan == 3:
                riwayat()
                input("\nTekan Enter untuk kembali ke menu...")       
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
        for row in reader:
            jadwal.append(row)
    return jadwal

    
def tampilkan_jadwal():
    clear()
    cover()
    print_header('JADWAL PENERBANGAN')
    data = []
    with open('jadwal_pesawat.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    tabel = tabulate(data, headers='keys', tablefmt='fancy_grid')
    for line in tabel.split('\n'):
        print(line.center(tw))
 
    
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
    print(f"Tanggal Pemesanan    : {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}".center(tw))
    print(f"Nama Pemesan         : {nama}".center(tw))
    print(f"Tanggal Keberangkatan: {tanggal}".center(tw))
    print(f"Rute Penerbangan    : {departure} -> {arrival}".center(tw))
    print(f"Maskapai            : {pesawat['AIRLINES']}".center(tw))
    print(f"Waktu               : {pesawat['TIME']}".center(tw))
    print(f"Jumlah Penumpang    : {jumlah_penumpang}".center(tw))
    print(f"Total Harga         : Rp {total_harga:,}".center(tw))
    print(f"Metode Pembayaran   : {metode}".center(tw))
    print("\nTerima kasih telah memesan!")
    
    # simpan ke riwayat
    with open('riwayat_pemesanan.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([tanggal, nama, departure, arrival, pesawat['AIRLINES'], 
                        pesawat['TIME'], jumlah_penumpang, total_harga, metode])
    
    input("\nTekan Enter untuk kembali ke menu...")

def riwayat():
    data = []
    with open('riwayat_pemesanan.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    tabel = tabulate(data, headers='keys', tablefmt='fancy_grid')
    print(tabel)
            

    
def main():
    login()


if __name__ == "__main__":
    main()