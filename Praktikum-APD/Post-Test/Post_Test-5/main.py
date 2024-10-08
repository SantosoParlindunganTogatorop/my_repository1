
import akun
import os

 #Buat perulangan untuk memilih menu kembali setelah menjalankan program
 #menu ke 5, user akan keluar dari program 

while True :                                           
        os.system('cls || clear')
        print("="*40)
        print("masuk/daftar".center(40))
        print("="*40)
        print("1. Registrasi pengguna")
        print("2. Login sebagai Admin")
        print("3. Login sebagai user")
        print("4. Login sebagai tamu")
        print("5. Keluar dari program")
        print("="*40)

#menggunakan pemanggilan fungsi untuk menjalankan program tanpa_         
#_menulis code kembali 


        pilih = input("pilih opsi 1-5 : ")
        if pilih == "1":
            akun.register_user()
        elif pilih == "2":
            akun.login_admin()
        elif pilih == "3":
            akun.login_user()
        elif pilih == "4":
            akun.guest_login()
        elif pilih == "5":
            print("anda keluar dari program")
            break
        else :
            os.system('cls || clear')
            print("="*40)
            print("Opsi tidak valid silahkan coba lagi !")
            print("="*40)
        input("Enter untuk melanjutkan......")





