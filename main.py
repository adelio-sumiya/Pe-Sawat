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
    garis()
    print(f"{text}".center(tw))
    garis()

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


def create_seat_map(rows=12, columns='ABCDEF'):
    seats = {}
    for row in range(1, rows + 1):
        for col in columns:
            seat_label = f"{row}{col}"
            seats[seat_label] = {
                'occupied': False,
                'passenger': None,
                'type': get_seat_type(row, col)
            }
    return seats

def get_seat_type(row, column):
    if column in 'AF':
        return 'window'
    elif column in 'BC' or column in 'DE':
        return 'middle' if column in 'CD' else 'aisle'
    return 'unknown'

def book_seat(seats, seat_label, passenger_name):
    if seat_label in seats:
        if not seats[seat_label]['occupied']:
            seats[seat_label]['occupied'] = True
            seats[seat_label]['passenger'] = passenger_name
            return True
    return False

def print_seat_map(seats, columns):
    print("   " + " ".join(columns))
    for row in range(1, 13):  # Assuming 12 rows
        seat_status = [
            'X' if seats[f"{row}{col}"]['occupied'] else 'O' 
            for col in columns
        ]
        print(f"{row:2d} {' '.join(seat_status)}")

def check_booked_seats():
    booked_seats = []
    with open('riwayat_pemesanan.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            booked_seats.append(row['Kursi'])
    return booked_seats

# ============================ admin ============================
def menu_admin():
    while True:
        print_header('MENU ADMIN') 
        menu = [
        "1. Lihat Jadwal Pesawat",
        "2. Kelola Jadwal Pesawat",
        "3. Lihat Laporan",
        "4. Tambah Menu Makanan",
        "5. Update Status",
        "6. Logout",
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
                tambah_menu_makanan()
            elif masukkan == 5:
                update_status()
            elif masukkan == 6:
                break
            else:
                print("Pilihan yang anda masukkan tidak ada.")
        except ValueError:
            print("Input tidak valid! Masukkan angka sesuai pilihan menu.")

def update_status():
    cover()
    garis()
    print("UPDATE STATUS".center(tw))
    garis()

    data = []

    with open("jadwal_pesawat.csv", mode='r') as f:
        reader = csv.DictReader(f, fieldnames=['KODE', 'AIRLINES', 'TIME', 'PRICE','STATUS'])
        for row in reader:
            data.append(row)
    tabel = tabulate(data, headers='keys', tablefmt='fancy_grid')
    for line in tabel.split('\n'):
        print(line.center(tw))
    
    kode = input("Masukkan Kode Penerbangan: ")
    status = input("Masukkan Status: ")

    indeks = 0
    for item in data:
        if (item['KODE'] == kode):
            data[indeks]['STATUS'] = status
        indeks = indeks + 1
    
    with open('jadwal_pesawat.csv', mode='w', newline='') as f:

        writer = csv.DictWriter(f, fieldnames=['KODE', 'AIRLINES', 'TIME', 'PRICE','STATUS'])
        writer.writeheader()
        for new_data in data:
            writer.writerow({'KODE': new_data['KODE'], 'AIRLINES': new_data['AIRLINES'], 'TIME': new_data['TIME'], 'PRICE': new_data['PRICE'], 'STATUS':new_data['STATUS']}) 

    with open('jadwal_pesawat.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['KODE', 'AIRLINES', 'TIME', 'PRICE','STATUS'])
        writer.writeheader()
        writer.writerows(data)
def klola_data():
    while True:
        print_header("EDIT JADWAL PENERBANGAN")
        print("1. Tambah Jadwal".center(tw))
        print("2. Edit Jadwal".center(tw))
        print("3. Update Delay".center(tw))
        print("4. Kembali".center(tw))
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
            kode = input("\nMasukkan nomor jadwal yang akan diedit: ")
            jadwal = load_jadwal()
            
            for row in jadwal:
                if row['KODE'] == kode:
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
                writer = csv.DictWriter(file, fieldnames=['KODE', 'AIRLINES', 'TIME', 'PRICE'])
                writer.writeheader()
                writer.writerows(jadwal)
            print("\nJadwal berhasil diubah!")
        
        elif pilihan == '3':
            update_delay()
        elif pilihan == '4':
            break
        
        input("\nTekan Enter untuk melanjutkan...")

def update_delay():
    clear()
    cover()
    print_header('UPDATE DELAY PENERBANGAN')

    # Membaca data riwayat pemesanan
    data = []
    with open('riwayat_pemesanan.csv', 'r') as file:
        reader = csv.DictReader(file)
        fieldnames = reader.fieldnames
        data = list(reader)

    # if "Alasan" not in fieldnames:
    #     data.append("Alasan")
    #     for row in data:
    #         row['Alasan'] = ""

    # Menampilkan data pemesanan
    if not data:
        print("Tidak ada data pemesanan.")
        input("\nTekan Enter untuk kembali...")
        return

    print("\nRiwayat Pemesanan:")
    print(tabulate(data, headers='keys', tablefmt='fancy_grid'))

    # Meminta input nomor pemesanan
    no_pemesanan = input("\nMasukkan nomor pemesanan yang ingin didelay: ").strip()
    pemesanan = next((row for row in data if row['No'] == no_pemesanan), None)

    # Validasi apakah pemesanan ditemukan
    if not pemesanan:
        print("\nNomor pemesanan tidak ditemukan!")
        input("\nTekan Enter untuk kembali...")
        return

    # Validasi status tiket
    if pemesanan['Status'] == 'Dibatalkan':
        print("\nTiket ini sudah dibatalkan sebelumnya!")
        input("\nTekan Enter untuk kembali...")
        return

    # Menampilkan detail tiket
    print("\nDetail Tiket:")
    print(tabulate([pemesanan], headers='keys', tablefmt='fancy_grid'))

    # Konfirmasi delay
    konfirmasi = input("\nDelay penerbangan? (y/n): ").strip().lower()
    if konfirmasi == 'y':

        # Update status delay
        pemesanan['Status'] = 'Delay'

        # Menulis ulang file CSV
        with open('riwayat_pemesanan.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

        print("\nDelay berhasil diperbarui!")
    else:
        print("\nDelay dibatalkan.")

    input("\nTekan Enter untuk kembali...")

def lihat_laporan():
        # Baca riwayat pemesanan
    df = pd.read_csv('riwayat_pemesanan.csv')
    
    # Ringkasan total pemesanan
    total_pemesanan = df['Total'].sum()
    total_penumpang = df['Jumlah'].sum()
    
    # Kelompokkan berdasarkan maskapai
    laporan_maskapai = df.groupby('Maskapai').agg({
        'Total': 'sum',
        'Jumlah': 'sum'
    }).reset_index()
    
    print_header('TOTAL PEMASUKAN')
    print(tabulate(laporan_maskapai, headers='keys', tablefmt='fancy_grid', showindex=range(1, len(laporan_maskapai)+1)))
    print("\nRincian pemasukan :")
    print(f"Total Pendapatan: Rp {total_pemesanan:,}")
    print(f"Total Penumpang : {total_penumpang}")

def tambah_menu_makanan():
    print_header("TAMBAH MENU MAKANAN")
    try:
        makanan = input("Masukkan Nama Makanan: ")
        harga = input("Masukkan Harga Makanan: ")
        
        with open('Menu_makanan.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([makanan, harga])
        
        print("\nMenu makanan berhasil ditambahkan!")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")


# ============================ user ============================
def menu_user():
    clear()
    while True:
        print_header('MENU')
        menu = [
        "1. Pemesanan Tiket",
        "2. Lihat Jadwal Penerbangan",
        "3. Riwayat Pemesanan",
        "4. Reschedule Jadwal",
        "5. Batalkan Tiket",
        "6. Booking Makanan",
        "7. Logout"
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
                reschedule_user()
            elif masukkan == 5:
                batalkan_tiket()
            elif masukkan == 6:
                booking_makanan()
            elif masukkan == 7:
                login()
                break
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
            no_pesawat = input("Pilih kode penerbangan: ")
            pesawat = next((p for p in jadwal if p['KODE'] == no_pesawat), None)
            if 'Aktif' not in pesawat:
                print('Pesawat tidak aktif!')
            elif pesawat:
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
    
    # Membuat peta kursi
    columns = 'ABCDEF'
    seats = create_seat_map()
    booked_seats = check_booked_seats()

    # Menandai kursi yang sudah dipesan
    for seat in booked_seats:
        if seat in seats:
            seats[seat]['occupied'] = True

    # Menampilkan peta kursi
    print_seat_map(seats, columns)

    # Memesan kursi sesuai jumlah penumpang
    pesanan = []
    for _ in range(jumlah_penumpang):
        while True:
            seat_label = input("Pilih kursi (contoh: '1A'): ").strip().upper()
            if seat_label in seats and not seats[seat_label]['occupied']:
                book_seat(seats, seat_label, nama)
                print(f"Kursi {seat_label} berhasil dipesan untuk {nama}.")
                pesanan.append(seat_label)
                break
            else:
                print("Kursi sudah dipesan atau tidak valid. Silakan pilih kursi lain.")


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
    
    # Generate nomor pemesanan
    with open('riwayat_pemesanan.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader, None)  # Skip header
        no = sum(1 for _ in reader) + 1

    # cetak struk
    print_header("STRUK PEMBAYARAN")
    print(f"Tanggal Pemesanan    : {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print(f"Nama Pemesan         : {nama}")
    print(f"Tanggal Keberangkatan: {tanggal}")
    print(f"Rute Penerbangan     : {departure} -> {arrival}")
    print(f"Maskapai             : {pesawat['AIRLINES']}")
    print(f"Waktu                : {pesawat['TIME']}")
    print(f"Jumlah Penumpang     : {jumlah_penumpang}")
    print(f"Kursi                : {pesanan}")
    print(f"Total Harga          : Rp {total_harga:,}")
    print(f"Metode Pembayaran    : {metode}")
    print("\nTerima kasih telah memesan!")
    
    # simpan ke riwayat
    with open('riwayat_pemesanan.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([no, tanggal, nama, departure, arrival, pesawat['AIRLINES'], 
                        pesawat['TIME'], jumlah_penumpang, total_harga, metode, "Aktif", pesanan])
    
    input("\nTekan Enter untuk kembali ke menu...")

def booking_makanan():
    while True:
        clear()
        cover()
        print_header('BOOKING MAKANAN')
        tengah('1. Pesan Makanan')
        tengah('2. Lihat Pesanan')
        tengah('3. Lihat Menu')
        tengah('4. Kembali')
        try:
            pilihan = int(input('masukkan pilihan : '))
            if pilihan == 1:
                pesan_makanan()
            elif pilihan == 2:
                lihat_pesanan()
            elif pilihan == 3:
                lihat_menu_makanan()
            elif pilihan == 4:
                return

        except:
            input('piihan tidak valid!')

def pesan_makanan():
    clear()
    cover()
    menu_makanan = []
    
    with open('Menu_makanan.csv', 'r') as file:
        reader = csv.DictReader(file)
        menu_makanan = list(reader)
    
    print_header("MENU MAKANAN")

    pesanan_makanan = []
    Pemesan = input('Masukkan nama anda : ')
    clear()
    cover()
    
    print_header("MENU MAKANAN")

    tabel = tabulate(menu_makanan, headers="keys", tablefmt="fancy_grid")
    for line in tabel.split('\n'):
        print(line.center(tw)) 
    
    while True:
        pilihan = input("Masukkan ID makanan: ")
        
        makanan = next((item for item in menu_makanan if item['ID'] == pilihan), None)
        if makanan:
            jumlah = int(input(f"Masukkan jumlah pesanan untuk {makanan['Nama']} : "))
            total_harga_makanan = int(makanan['Harga']) * jumlah

            pesanan_makanan.append({
                'Nama': Pemesan,
                'Makanan': makanan['Nama'],
                'Jumlah': jumlah,
                'Harga': makanan['Harga'],
                'Total Harga Makanan': total_harga_makanan,
                'Metode': ''  
            })
        else:
            print("Makanan tidak ditemukan!")

        lanjut = input("Apakah Anda ingin menambah pesanan? (ya/tidak): ").lower()
        if lanjut == 'tidak':  
            break

    total_harga = sum(item['Total Harga Makanan'] for item in pesanan_makanan)

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

    for item in pesanan_makanan:
        item['Metode'] = metode
    clear()
    cover()
    
    print_header("MENU MAKANAN")

    # Menulis ke file CSV tanpa kolom "Nomor"
    with open('pesanan_makanan_user.csv', 'a', newline='') as file:
        fieldnames = ['Nama', 'Makanan', 'Jumlah', 'Harga', 'Total Harga Makanan', 'Metode']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerows(pesanan_makanan)
    
    print("Struk Pemesanan: ".center(tw))
    print(f"Nama Pemesan            : {Pemesan}".center(tw))
    for item in pesanan_makanan:
        print(f"{item['Makanan']} x {item['Jumlah']} = Rp {item['Total Harga Makanan']:,}".center(tw))

    print(f"Total Harga          : Rp {total_harga:,}".center(tw))
    print(f"Metode Pembayaran    : {metode}".center(tw))
    print("\nTerima kasih telah memesan!")

    input("\nTekan Enter untuk kembali ke menu...")


def lihat_menu_makanan():
    data = []
    with open('Menu_makanan.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    tabel = tabulate(data, headers='keys', tablefmt='fancy_grid')
    for line in tabel.split('\n'):
        print(line.center(tw))
    input('tekan enter untuk melanjutkan...')   

def lihat_pesanan():
    clear()
    cover()
    print_header('MAKANAN DAN MINUMAN YANG ANDA PESAN')
    
    data = []
    try:
        with open('pesanan_makanan_user.csv', 'r') as file:
            reader = csv.DictReader(file)
            data = list(reader)
    except FileNotFoundError:
        print("Tidak ada data pesanan yang ditemukan!")
        input("Tekan Enter untuk kembali...")
        return
    
    if not data:
        print("Tidak ada data pesanan yang ditemukan!")
        input("Tekan Enter untuk kembali...")
        return

    tabel = tabulate(data, headers='keys', tablefmt='fancy_grid')
    for line in tabel.split('\n'):
        print(line.center(tw))

    while True:
        print("\nPilih opsi:")
        print("1. Hapus riwayat")
        print("2. Kembali")
        
        try:
            pilihan = int(input("Masukkan pilihan: "))
            if pilihan == 1:
                hapus_pesanan_nama(data)
                break
            elif pilihan == 2:
                return
            else:
                print("Pilihan tidak valid!")
        except ValueError:
            print("Input harus berupa angka!")

def hapus_pesanan_nama(data):
    clear()
    cover()
    print_header("HAPUS RIWAYAT PESANAN")
    
    tabel = tabulate(data, headers='keys', tablefmt='fancy_grid')
    for line in tabel.split('\n'):
        print(line.center(tw))
    
    nama_hapus = input("\nMasukkan nama yang ingin dihapus: ").strip()
    
    data_baru = [row for row in data if row['Nama'] != nama_hapus]

    if len(data_baru) == len(data):
        print("\nNama tidak ditemukan di daftar pesanan!")
        return

    with open('pesanan_makanan_user.csv', 'w', newline='') as file:
        fieldnames = ['Nama', 'Makanan', 'Jumlah', 'Harga', 'Total Harga Makanan', 'Metode']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data_baru)

    print("\nPesanan berhasil dihapus!")

def riwayat():
    clear()
    cover()
    print_header('RIWAYAT ANDA')
    data = []
    with open('riwayat_pemesanan.csv', 'r') as file:
        reader = csv.DictReader(file)
        data = list(reader)
        for row in reader:
            if row.get('Status', 'Aktif') == 'Aktif':
                data.append(row)
    if data:
        tabel = tabulate(data, headers='keys', tablefmt='fancy_grid')
        print(tabel)
    else:
        print("Tidak ada pemesanan yang aktif.")
            
def reschedule_user():
    print_header("RESCHEDULE JADWAL PEMESANAN")
    riwayat()

    # Input nomor pemesanan
    no_pemesanan = input("\nMasukkan nomor pemesanan yang ingin di-reschedule: ").strip()

    # Baca data pemesanan dari file
    data = []
    with open('riwayat_pemesanan.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)

    # Cari tiket berdasarkan nomor pemesanan
    pemesanan = next((row for row in data if row['No'] == no_pemesanan), None)
    if not pemesanan:
        print("\nNomor pemesanan tidak ditemukan!")
    
    if pemesanan['Status'] == 'Dibatalkan':
        print("\nReschedule tidak dapat dilakukan Karena status tiket sudah dibatalkan.")
        input("\nTekan Enter untuk kembali...")
        return

    # Tampilkan detail tiket lama
    print("\nDetail Tiket Lama:")
    print(tabulate([pemesanan], headers='keys', tablefmt='fancy_grid'))

    # Pilih jadwal baru
    print("\nJadwal Penerbangan Baru:")
    tampilkan_jadwal()
    jadwal = load_jadwal()

    while True:
        no_jadwalbaru = input("\nPilih nomor penerbangan baru: ").strip()
        penerbangan_baru = next((row for row in jadwal if row['KODE'] == no_jadwalbaru), None)
        if penerbangan_baru:
            # Cek apakah jadwal baru sama dengan jadwal lama
            if (penerbangan_baru['AIRLINES'] == pemesanan['Maskapai'] and
                penerbangan_baru['TIME'] == pemesanan['Waktu']):
                print("\nJadwal baru tidak boleh sama dengan jadwal lama. Silakan pilih jadwal yang berbeda.")
                continue
            break
        print("Nomor penerbangan tidak valid!")

    # Masukkan jumlah penumpang baru
    while True:
        try:
            jumlah_penumpangnew = int(input("\nMasukkan jumlah penumpang baru: "))
            if jumlah_penumpangnew > 0:
                break
            print("Jumlah penumpang harus lebih dari 0!")
        except ValueError:
            print("Input tidak valid!")

    # Hitung perbedaan harga
    harga_lama = int(pemesanan['Total Harga'])
    harga_barusatutiket = int(penerbangan_baru['PRICE'])
    total_hargabaru = harga_barusatutiket * jumlah_penumpangnew

    selisih = total_hargabaru - harga_lama
    if selisih > 0:
        print(f"\nBiaya tambahan yang harus dibayar: Rp {selisih:,}")
        metode_pembayaran = ['Transfer', 'Kartu Kredit', 'E-wallet']
        print("\nPilih metode pembayaran:")
        for i, metode in enumerate(metode_pembayaran, 1):
            print(f"{i}. {metode}")
        
        while True:
            try:
                pilihan = int(input("Pilih metode pembayaran: "))
                if 1 <= pilihan <= len(metode_pembayaran):
                    print(f"\nMetode pembayaran yang dipilih: {metode_pembayaran[pilihan - 1]}")
                    break
            except ValueError:
                pass
            print("Pilihan tidak valid!")
    elif selisih < 0:
        print(f"\nAnda mendapatkan pengembalian dana sebesar: Rp {-selisih:,}")
    else:
        print("\nTidak ada perubahan biaya.")

    # Update data tiket lama
    pemesanan['Tanggal'] = input("\nMasukkan tanggal keberangkatan baru (DD/MM/YYYY): ").strip()
    pemesanan['Maskapai'] = penerbangan_baru['AIRLINES']
    pemesanan['Waktu'] = penerbangan_baru['TIME']
    pemesanan['Jumlah Penumpang'] = jumlah_penumpangnew
    pemesanan['Total Harga'] = total_hargabaru

    # Simpan perubahan kembali ke file CSV
    with open('riwayat_pemesanan.csv', 'w', newline='') as file:
        fieldnames = ['No', 'Tanggal', 'Nama', 'Departure', 'Arrival', 
                      'Maskapai', 'Waktu', 'Jumlah Penumpang', 'Total Harga', 'Metode', 'Status']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    print("\nReschedule berhasil dilakukan!")
    input("\nTekan Enter untuk kembali...")

def batalkan_tiket():
    print_header("PEMBATALAN TIKET")
    riwayat()
    # Input nomor pemesanan
    no_pemesanan = input("\nMasukkan nomor pemesanan yang ingin dibatalkan: ").strip()
    clear()
    cover()
    print_header('PEMBATALAN TIKET')
    
    # Cari tiket berdasarkan nomor pemesanan
    data = []
    with open('riwayat_pemesanan.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    
    pemesanan = next((row for row in data if row['No'] == no_pemesanan), None)
    if not pemesanan:
        print("\nNomor pemesanan tidak ada!")
        input("\nTekan Enter untuk kembali...")
        return

    if pemesanan['Status'] == 'Dibatalkan':
        print("\nTiket ini sudah dibatalkan sebelumnya dan tidak bisa dibatalkan lagi.")
        input("\nTekan Enter untuk kembali...")
        return
    
    # Konfirmasi pembatalan
    print("\nDetail Tiket:")
    print(tabulate([pemesanan], headers='keys', tablefmt='fancy_grid'))
    konfirmasi = input("\nApakah Anda yakin ingin membatalkan tiket ini? (ya/tidak): ").strip().lower()
    if konfirmasi == 'ya':
        pemesanan['Status'] = 'Dibatalkan'  
        clear()
        cover()
        print_header('PEMBATALAN TIKET')
    else:
        print("\nPembatalan dibatalkan!")
        return



    # Simpan perubahan ke file
    with open('riwayat_pemesanan.csv', 'w', newline='') as file:
        fieldnames = ['No', 'Tanggal', 'Nama', 'Departure', 'Arrival', 
                      'Maskapai', 'Waktu', 'Jumlah Penumpang', 'Total', 'Metode', 'Status']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data) 
    print("\nTiket Anda berhasil di batalkan.")
    riwayat()
    input("\nTekan Enter untuk kembali...")

def info_delay():
    pass

    
def main():
    # hapus_pesanan_makana()
    login()

if __name__ == "__main__":
    main()


    
