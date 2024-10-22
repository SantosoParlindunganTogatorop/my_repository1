#Menu
import os

#program yang digunakan pada menu_akun

#buat var kontak sebagai nested dictionary

kontak = {}

def clean():
    os.system('cls || clear')

def enter():
    input("Enter untuk melanjutkan.....")


def add_kontak():
        os.system('cls || clear')
        nama = input("Masukkan nama : ")                    # variabel local
        nomor = int(input("masukkan nomor telepon : "))     # variabel local
        kontak[nama]= nomor
        print("="*40)
        print("kontak berhasil ditambahkan")
        print("="*40) 

        return nama
        

def show_kontak(kontak):                # menggunakan parameter
    os.system('cls || clear')   
    
    if kontak:
        if kontak:
            for angka, (nama, info) in enumerate(kontak.items()):
                print("="*40)
                print(f"Kontak ke-{angka + 1}")
                print(f"Nama    : {nama}")
                print(f"Telepon : {info}")
                print("="*40)
     
    else:
        print("Kontak belum tersedia!")
        return kontak


def select_kontak(kontak):              # menggunakan parameter
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
            return nama_select
    if not ditemukan:
        print("=" * 40)
        print("Tidak ditemukan")
        print("=" * 40)
        return nama
    

def del_kontak(kontak):                 # menggunakan parameter
    os.system('cls || clear') 
    show_kontak(kontak)
    nama_del = input("Masukkan nama kontak yang ingin dihapus: ")       # variabel local
    
    if nama_del in kontak :
        del kontak[nama_del]
        print("=" * 40)
        print("Kontak berhasil dihapus")
        print("=" * 40)
        return nama_del
    else:
        print("=" * 40)
        print("Kontak tidak ditemukan")
        print("=" * 40)
        return nama_del

   

def edit_kontak(kontak):                # menggunakan parameter
    os.system('cls || clear')
    show_kontak(kontak)  
    nama_lama = input("Masukkan nama kontak yang ingin diubah: ")           # variabel local
    
    if nama_lama in kontak :
        nama_baru = input("Masukkan nama baru: ")           # variabel local
        nomor_baru = input("Masukkan nomor baru: ")         # variabel local
        kontak[nama_baru] = nomor_baru  
        if nama_baru != nama_lama:  
            del kontak[nama_lama]
        print("Kontak berhasil diubah")
        return nama_baru
    else:
        print("Kontak tidak ditemukan")
        return nama_lama


        
