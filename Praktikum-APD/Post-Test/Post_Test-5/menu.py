#Menu
import os

#program yang digunakan pada menu_akun

#buat var kontak sebagai nested list 

kontak = []

#program menambah kontak

def add_kontak():
        os.system('cls || clear')
        nama = input("Masukkan nama : ")
        nomor = int(input("masukkan nomor telepon : "))
        kontak.append({'nama' : nama,'nomor' : nomor})
        print("="*40)
        print("kontak berhasil ditambahkan")
        print("="*40)        
        input("Enter untuk melanjutkan.....")
        os.system('cls || clear')
def show_kontak():
        os.system('cls || clear')
        if kontak :
            for nomor in range(len(kontak)):
                print("="*40)
                print(f"kontak ke-{nomor+1}")
                print(f"""Nama    : {kontak[nomor]['nama']}
Telepon : {kontak[nomor]['nomor']}""")
                print("="*40)
            input("Enter untuk melanjutkan.....")
            os.system('cls || clear')
        else :
             print("kontak belum tersedia !")
             input("Enter untuk melanjutkan.....")
             os.system('cls || clear')

def select_kontak():
    nama_select = input("Nama yang dicari : ")
    os.system('cls || clear')  
    ditemukan = False
    for cari in kontak:
        if nama_select.lower() in cari["nama"].lower():
            print("=" * 40)
            print(f"Nama         : {cari['nama']}")
            print(f"Nomor telepon: {cari['nomor']}")
            print("=" * 40)
            ditemukan = True
    if not ditemukan:
        print("=" * 40)
        print("Tidak ditemukan")
        print("=" * 40)
    input("Enter untuk melanjutkan......")


def del_kontak():
    os.system('cls || clear')
    show_kontak()
    index = int(input("Data yang ingin di hapus kontak ke-:"))
    del_nomor = kontak.pop(index-1)
    print("="*40)
    print(f"kontak Berhasil dihapus")
    print("="*40)
    input("Enter untuk melanjutkan......")
    os.system('cls || clear')


def up_kontak():
    os.system('cls || clear')
    for edit in range(len(kontak)):
        print("="*40)
    index = int(input("Data kontak yang ingin diubah, kontak ke-:"))
    nama_baru = input("Masukkan nama yang ingin diubah:  ")
    nomor_baru = int(input("Masukkan nomor yang ingin diubah: "))
    kontak[index-1]=({'nama' : nama_baru,'nomor' : nomor_baru})
    print("kontak berhasil diubah")
    input("enter...")


        
