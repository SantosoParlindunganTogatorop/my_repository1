#Menu
import os

#program yang digunakan pada menu_akun

#buat var kontak sebagai nested dictionary

kontak = {}

#program menambah kontak

def add_kontak():
        os.system('cls || clear')
        nama = input("Masukkan nama : ")
        nomor = int(input("masukkan nomor telepon : "))
        kontak[nama]=nomor
        print("="*40)
        print("kontak berhasil ditambahkan")
        print("="*40)        
        input("Enter untuk melanjutkan.....")
        os.system('cls || clear')

def show_kontak():
    os.system('cls || clear')
    
    if kontak:
        if kontak:
            for angka, (nama, info) in enumerate(kontak.items()):
                print("="*40)
                print(f"Kontak ke-{angka + 1}")
                print(f"Nama    : {nama}")
                print(f"Telepon : {info}")
                print("="*40)
        
        input("Tekan Enter untuk melanjutkan.....")
        os.system('cls || clear')
    else:
        print("Kontak belum tersedia!")
        input("Tekan Enter untuk melanjutkan.....")
        os.system('cls || clear')


def select_kontak():
    nama_select = input("Nama yang dicari : ")
    os.system('cls || clear')  
    ditemukan = False
    for nama,nomor in kontak.items():
        if nama_select.lower() in nama.lower():
            print("=" * 40)
            print(f"Nama         : {nama}")
            print(f"Nomor telepon: {nomor}")
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
    show_kontak()

    nama_del = input("Masukkan nama kontak yang ingin dihapus: ")
    
    if nama_del in kontak:
        del kontak[nama_del]
        print("=" * 40)
        print("Kontak berhasil dihapus")
        print("=" * 40)
    else:
        print("=" * 40)
        print("Kontak tidak ditemukan")
        print("=" * 40)

    input("Tekan Enter untuk melanjutkan...")
   

def up_kontak():
    os.system('cls || clear')
    show_kontak()  
    nama_lama = input("Masukkan nama kontak yang ingin diubah: ")
    
    if nama_lama in kontak:
        nama_baru = input("Masukkan nama baru: ")
        nomor_baru = input("Masukkan nomor baru: ") 
        kontak[nama_baru] = nomor_baru  
        if nama_baru != nama_lama:  
            del kontak[nama_lama]
        print("Kontak berhasil diubah")
    else:
        print("Kontak tidak ditemukan")

    input("Enter...")

        
