import os


def login():
    username = input('')
    password = input('')


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
