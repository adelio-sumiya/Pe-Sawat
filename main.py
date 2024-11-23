import os

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
    print('''
          1. melihat jadwal pesawat
          2. kelola data jadwal pesawat
          3. lihat laporan
          4. logout
          ''')

def menu_user():
    print('''
          1. pemesanan tiket
          2. lihat jadwal pesawat
          3. riwayat pemesanan
          4. logout
          ''')


def pemesanan_tiket():
    nama = input('masukkan nama :')
    tanggalberangkat = input('')
    print ('''
    1. Jakarta
    2. Surabaya
    3. Makassar
    4. Denpasar
    ''')
    arrival = input('masukkan lokasi arrival :')
    print ('''
    1. Jakarta
    2. Surabaya
    3. Makassar
    4. Denpasar
    ''')
    departure = input('masukkan lokasi departure')


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
