import os
import csv
pengguna = {
        "admin": {"username": "admin", "password": "admin123", "role": "admin"},
        "user1": {"username": "user1", "password": "user123", "role": "user"}
}
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

def pemesanan_tiket():
    nama = input('masukkan nama : ')
    tanggalberangkat = input('')
    print ('''
    1. Jakarta
    2. Surabaya
    3. Makassar
    4. Denpasar
    ''')
    arrival = input('masukkan lokasi arrival : ')
    print ('''
    1. Jakarta
    2. Surabaya
    3. Makassar
    4. Denpasar
    ''')
    departure = input('masukkan lokasi departure : ')

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
