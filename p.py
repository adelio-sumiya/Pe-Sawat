import os
import csv
from datetime import datetime
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(text):
    clear_screen()
    print("="*50)
    print(f"{text:^50}")
    print("="*50)

def load_jadwal():
    jadwal = []
    with open('jadwal_pesawat.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            jadwal.append(row)
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

def pesan_tiket():
    print_header("PEMESANAN TIKET")
    
    # Input nama
    nama = input("Masukkan nama pemesan: ")
    
    # Input tanggal
    while True:
        try:
            tanggal = input("Masukkan tanggal keberangkatan (DD/MM/YYYY): ")
            datetime.strptime(tanggal, '%d/%m/%Y')
            break
        except ValueError:
            print("Format tanggal salah! Gunakan format DD/MM/YYYY")
    
    # Pilih kota
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
    
    # Tampilkan dan pilih jadwal
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
    
    # Input jumlah penumpang
    while True:
        try:
            jumlah_penumpang = int(input("\nMasukkan jumlah penumpang: "))
            if jumlah_penumpang > 0:
                break
            print("Jumlah penumpang harus lebih dari 0!")
        except ValueError:
            print("Input tidak valid!")
    
    # Hitung total harga
    total_harga = int(pesawat['PRICE']) * jumlah_penumpang
    print(f"\nTotal harga: Rp {total_harga:,}")
    
    # Pilih metode pembayaran
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
    
    # Cetak struk
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
    
    # Simpan ke riwayat
    with open('riwayat_pemesanan.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([tanggal, nama, departure, arrival, pesawat['AIRLINES'], 
                        pesawat['TIME'], jumlah_penumpang, total_harga, metode])
    
    input("\nTekan Enter untuk kembali ke menu...")

def load_riwayat():
    try:
        with open('riwayat_pemesanan.csv', 'r') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        with open('riwayat_pemesanan.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Tanggal', 'Nama', 'Departure', 'Arrival', 'Airlines', 'Waktu', 'Jumlah_Penumpang', 'Total_Harga', 'Metode_Pembayaran'])
        return []

def tampilkan_riwayat():
    riwayat = load_riwayat()
    print("\nRiwayat Pemesanan:")
    print("-"*100)
    print(f"{'Tanggal':<12}{'Nama':<15}{'Departure':<15}{'Arrival':<15}{'Airlines':<15}{'Waktu':<20}{'Penumpang':<10}{'Total':<15}{'Pembayaran':<15}")
    print("-"*100)
    for row in riwayat:
        print(f"{row['Tanggal']:<12}{row['Nama']:<15}{row['Departure']:<15}{row['Arrival']:<15}{row['Airlines']:<15}{row['Waktu']:<20}{row['Jumlah_Penumpang']:<10}Rp {int(row['Total_Harga']):,}<15}}{row['Metode_Pembayaran']:<15}")
    print("-" * 100)
    input("\nTekan Enter untuk kembali ke menu...")

def edit_jadwal():
    while True:
        print_header("EDIT JADWAL PENERBANGAN")
        print("1. Tambah Jadwal")
        print("2. Edit Jadwal")
        print("3. Kembali")
        
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
    riwayat = load_riwayat()
    total_pemasukan = sum(int(row['Total_Harga']) for row in riwayat)
    total_penumpang = sum(int(row['Jumlah_Penumpang']) for row in riwayat)
    
    print_header("LAPORAN PEMESANAN")
    print(f"Total Pemesanan   : {len(riwayat)}")
    print(f"Total Penumpang   : {total_penumpang}")
    print(f"Total Pemasukan   : Rp {total_pemasukan:,}")
    
    tampilkan_riwayat()

def menu_admin():
    while True:
        print_header("MENU ADMIN")
        print("1. Lihat Jadwal")
        print("2. Edit Jadwal")
        print("3. Lihat Laporan")
        print("4. Logout")
        
        pilihan = input("\nPilih menu: ")
        
        if pilihan == '1':
            print_header("JADWAL PENERBANGAN")
            tampilkan_jadwal()
            input("\nTekan Enter untuk kembali ke menu...")
        elif pilihan == '2':
            edit_jadwal()
        elif pilihan == '3':
            lihat_laporan()
        elif pilihan == '4':
            break
        else:
            print("Menu tidak valid!")

def menu_user():
    while True:
        print_header("MENU USER")
        print("1. Pesan Tiket")
        print("2. Lihat Jadwal")
        print("3. Riwayat Pemesanan")
        print("4. Logout")
        
        pilihan = input("\nPilih menu: ")
        
        if pilihan == '1':
            pesan_tiket()
        elif pilihan == '2':
            print_header("JADWAL PENERBANGAN")
            tampilkan_jadwal()
            input("\nTekan Enter untuk kembali ke menu...")
        elif pilihan == '3':
            print_header("RIWAYAT PEMESANAN")
            tampilkan_riwayat()
        elif pilihan == '4':
            break
        else:
            print("Menu tidak valid!")

def main():
    # Data login sederhana
    users = {'user': 'user123', 'admin': 'admin123'}
    
    while True:
        print_header("SISTEM PEMESANAN TIKET PESAWAT")
        print("1. Login")
        print("2. Keluar")
        
        pilihan = input("\nPilih menu: ")
        
        if pilihan == '1':
            print("\nLogin")
            username = input("Username: ")
            password = input("Password: ")
            
            if username in users and users[username] == password:
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

if __name__ == '__main__':
    main()