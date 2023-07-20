# Aplikasi Data Mahasiswa
# Latar belakang untuk mendata nama dan nim mahasiswa 

# KHolis Iqbal       (A710220039)
# Rendito Abimanyu   (A710220035)
# Satria Fais        (A710220042)

import os
os.system('cls')
from collections import deque

class Data:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama

class Daftar:
    def __init__(self, max_size):
        self.undo_stack = deque(maxlen=max_size)
        self.redo_stack = deque(maxlen=max_size)
        self.Mahasiswa = deque(maxlen=max_size)

    def tambah_Mahasiswa(self, nim, nama):
        item = Data(nim, nama)
        self.Mahasiswa.append(item)
        self.undo_stack.append(('tambah-mahasiswa', item))
        self.redo_stack.clear()

    def hapus_Mahasiswa(self, index):
        item = self.Mahasiswa[index]
        self.Mahasiswa.remove(item)
        self.undo_stack.append(('hapus-mahasiswa', item))
        self.redo_stack.clear()

    def undo(self):
        if not self.undo_stack:
            print("Tidak ada aksi undo yang tersedia.")
            return

        action, item = self.undo_stack.pop()
        if action == 'tambah-mahasiswa':
            self.Mahasiswa.remove(item)
        elif action == 'hapus-mahasiswa':
            self.Mahasiswa.append(item)

        self.redo_stack.append((action, item))
        self.tampil_Mahasiswa()

    def redo(self):
        if not self.redo_stack:
            print("Tidak ada aksi redo yang tersedia.")
            return

        action, item = self.redo_stack.pop()
        if action == 'tambah-mahasiswa':
            self.Mahasiswa.append(item)
        elif action == 'hapus-mahasiswa':
            self.Mahasiswa.remove(item)

        self.undo_stack.append((action, item))
        self.tampil_Mahasiswa()

    def check_empty(self):
        return len(self.Mahasiswa) == 0

    def tampil_pencarian(self, hasil_pencarian):
        print('Menampilkan Data'.center(50))
        print('+----+-------------+-------------------------+')
        print("| No |     nama     |           Nim          |")
        print('+----+-------------+-------------------------+')
        for i, data in enumerate(hasil_pencarian, start=1):
            print(f"| {i:<2} | {data.nim:<12}| {data.nama:<23} |")
            print('+----+-------------+-------------------------+')

    def tampil_Mahasiswa(self):
        print('Menampilkan Data'.center(50))
        print('+----+-------------+-------------------------+')
        print("| No |     NIM     |           Nama          |")
        print('+----+-------------+-------------------------+')
        for i, data in enumerate(self.Mahasiswa, start=1):
            print(f"| {i:<2} | {data.nim:<12}| {data.nama:<23} |")
            print('+----+-------------+-------------------------+')

    def urutkan_Mahasiswa(self, berdasarkan): #selection sort
        if berdasarkan == "nim":
            for i in range(len(self.Mahasiswa)):
                min_idx = i
                for j in range(i+1, len(self.Mahasiswa)):
                    if self.Mahasiswa[j].nim < self.Mahasiswa[min_idx].nim:
                        min_idx = j
                self.Mahasiswa[i], self.Mahasiswa[min_idx] = self.Mahasiswa[min_idx], self.Mahasiswa[i]
                
        elif berdasarkan == "nama":
            for i in range(len(self.Mahasiswa)):
                min_idx = i
                for j in range(i+1, len(self.Mahasiswa)):
                    if self.Mahasiswa[j].nama < self.Mahasiswa[min_idx].nama:
                        min_idx = j
                self.Mahasiswa[i], self.Mahasiswa[min_idx] = self.Mahasiswa[min_idx], self.Mahasiswa[i]

    def searc(self, masukan): #sequential search
        if masukan == "nim":
            ketemu = False
            masukan = input("Masukkan nim yang akan dicari: ")
            hasil_pencarian = []
            for data in self.Mahasiswa:
                if masukan == data.nim:
                    ketemu = True
                    hasil_pencarian.append(data)
                    break
            if ketemu:
                print("Data dari:", masukan, "berhasil ditemukan")
                self.tampil_pencarian(hasil_pencarian)
            else:
                print("Pencarian anda", masukan, "tidak ditemukan")

        elif masukan == "nama":
            ketemu = False
            masukan = input("Masukkan nama yang akan dicari: ")
            hasil_pencarian = []
            for data in self.Mahasiswa:
                if masukan == data.nama:
                    ketemu = True
                    hasil_pencarian.append(data)
                    break
            if ketemu:
                print("Data dari:", masukan, "berhasil ditemukan")
                self.tampil_pencarian(hasil_pencarian)
            else:
                print("Pencarian anda", masukan, "tidak ditemukan")

    def undo_redo(self):
        print("Pilih Opsi")
        print("1. Undo")
        print("2. Redo")
        print("3. Lanjutkan")
        aksi = input("Masukkan tindakan: ")
        if aksi == "1":
            self.undo()
            self.undo_redo()
        elif aksi == "2":
            self.redo()
            self.undo_redo()
        elif aksi == "3":
            return
        else:
            print('Masukkan opsi tindakan yang benar')
            self.undo_redo()
            
    def alert(self):
        print("Data sudah penuh, jika dilanjutkan maka data pertama akan terhapus (Konsep QUEUE FIFO)")
        print("1. Lanjutkan")
        print("2. Kembali")
        pilihan = input("Masukkan Pilihan Anda: ")
        if pilihan == "1":
            nim = input("Masukkan NIM  : ")
            nama = input("Masukkan Nama : ")
            self.hapus_Mahasiswa(0)
            self.tambah_Mahasiswa(nim, nama)
            print('Data berhasil diinput')
            print('======================')
            self.tampil_Mahasiswa()
            self.undo_redo()
        else:
            return

max_size = 5  # Jumlah maksimum elemen dalam antrian
daftar_Mahasiswa = Daftar(max_size)

while True:
    print("Aplikasi Data Mahasiswa")
    print("Menu:")
    print("1. Tambah Data")
    print("2. Hapus Data")
    print("3. Tampilkan Data")
    print("4. Urutkan Data")
    print('5. Cari Data')
    print("6. Keluar")
    pilihan = input("Masukkan pilihan: ")
    print('======================')
    if pilihan == "1":
        if len(daftar_Mahasiswa.Mahasiswa) == max_size:
            daftar_Mahasiswa.alert()
        else:
            nim = input("Masukkan NIM  : ")
            nama = input("Masukkan Nama : ")
            daftar_Mahasiswa.tambah_Mahasiswa(nim.upper(), nama.upper())
            print('Data berhasil diinput')
            print('======================')
            daftar_Mahasiswa.tampil_Mahasiswa()
            daftar_Mahasiswa.undo_redo()
            

    elif pilihan == "2":
        if daftar_Mahasiswa.check_empty():
            print('Data masih kosong')
            print('=======================')
        else:
            daftar_Mahasiswa.tampil_Mahasiswa()
            index = int(input("Masukkan nomor data yang akan dihapus: "))
            daftar_Mahasiswa.hapus_Mahasiswa(index - 1)
            print('Data berhasil dihapus')
            print('======================')
            daftar_Mahasiswa.tampil_Mahasiswa()
            daftar_Mahasiswa.undo_redo()

    elif pilihan == "3":
        if daftar_Mahasiswa.check_empty():
            print('Data masih kosong')
            print('=======================')
        else:
            daftar_Mahasiswa.tampil_Mahasiswa()

    elif pilihan == "4":
        if daftar_Mahasiswa.check_empty():
            print('Data masih kosong')
            print('=======================')
        else:
            daftar_Mahasiswa.tampil_Mahasiswa()
            print("Menu Urutkan Data:")
            print("1. Berdasarkan NIM")
            print("2. Berdasarkan Nama")
            berdasarkan = input("Masukkan pilihan: ")
            if berdasarkan == "1":
                daftar_Mahasiswa.urutkan_Mahasiswa("nim")
                print('Data berhasil diurutkan berdasarkan NIM')
                daftar_Mahasiswa.tampil_Mahasiswa()
            elif berdasarkan == "2":
                daftar_Mahasiswa.urutkan_Mahasiswa("nama")
                print('Data berhasil diurutkan berdasarkan Nama')
                daftar_Mahasiswa.tampil_Mahasiswa()
            else:
                print('Input tidak valid!')

    elif pilihan == "5":
        if daftar_Mahasiswa.check_empty():
            print('Data masih kosong')
            print('=======================')
        else:
            print("Cari data berdasarkan:")
            print("1. Berdasarkan NIM")
            print("2. Berdasarkan Nama")
            cari = input("Masukkan nilai yang dicari: ")
            if cari == "1":
                daftar_Mahasiswa.searc("nim")
            elif cari == "2":
                daftar_Mahasiswa.searc("nama")
            else:
                print("Pilihan tidak valid")

    elif pilihan == "6":
        print('Program telah selesai')
        break

    else:
        print('Input tidak valid, silahkan masukkan input yang sesuai')