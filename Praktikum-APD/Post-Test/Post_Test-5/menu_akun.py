#Menu_akun
import menu
import os

#program yang digunakan akun

# daftar menu admin dengan memanggil fungsi_
#_tanpa menuliskan kode kembali
#Buat perulangan untuk memilih menu kembali setelah menjalankan program
 #menu ke 6, user akan keluar dari program 
def admin_menu():
    os.system('cls || clear')
    while True:
        print("="*40)
        print("Menu admin".center(40))
        print("="*40)
        print("1. Tambah kontak")
        print("2. Lihat kontak")
        print("3. Cari kontak")
        print("4. Hapus Kontak")
        print("5. Edit kontak ")
        print("6. keluar program")
        print("="*40)

        pilih = input("pilih opsi 1-4 : ")
        if pilih == "1":
            menu.add_kontak()
        elif pilih == "2":
            menu.show_kontak()
        elif pilih == "3":
            menu.select_kontak()
        elif pilih =="4":
            menu.del_kontak()
        elif pilih == "5":
            menu.up_kontak()
        elif pilih == "6":
            os.system('cls || clear')
            print("="*40)
            print("Keluar dari program")
            print("="*40)
            break
        else :
            print("opsi tidak valid silahkan coba lagi !")
            input("Enter untuk melanjutkan......")

#daftar menu admin dengan memanggil fungsi_
#_tanpa menuliskan kode kembali
#Buat perulangan untuk memilih menu kembali setelah menjalankan program
 #menu ke 4, user akan keluar dari program 
def user_menu():
    while True :
        os.system('cls || clear')
        print("="*40)
        print("Menu pengguna".center(40))
        print("="*40)
        print("1. Lihat kontak")
        print("2. Tambah kontak")
        print("3. Cari kontak")
        print("4. Keluar")
        print("="*40)

        pilih = input("pilih opsi 1-3 : ")

        if pilih == "1":
            menu.show_kontak()
        elif pilih == "2":
            menu.add_kontak()          
        elif pilih == "3":
            menu.select_kontak()
        elif pilih == "4":
            os.system('cls || clear')
            print("="*40)
            print("Keluar dari program")
            print("="*40)
            break
        else : 
            print("Opsi tidak valid silahkan coba lagi !")
            input("Enter untuk melanjutkan......")

#daftar menu admin dengan memanggil fungsi_
#_tanpa menuliskan kode kembali
#Buat perulangan untuk memilih menu kembali setelah menjalankan program
 #menu ke 3, user akan keluar dari program 

def guest_menu():
    while True :
        os.system('cls || clear')
        print("="*40)
        print("Menu pengunjung")
        print("="*40)
        print("1. Lihat kontak")
        print("2. Cari kontak")
        print("3. Keluar")
        print("="*40)

        pilih = input("pilih opsi 1-3 : ")

        if pilih == "1":
            menu.show_kontak()
        elif pilih == "2":
            menu.select_kontak()
        elif pilih == "3":
            print("Keluar dari program")
            break
        else : 
            print("Opsi tidak valid silahkan coba lagi !")
            input("Enter untuk melanjutkan......")