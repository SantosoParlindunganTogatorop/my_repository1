
from menu_akun import admin_menu, user_menu, guest_menu
import os

#membuat users sebagai nested list pada menu register dan login

users = {}
admin_username = "santoso"              # sebagai variable global
admin_password = "052"                  # sebagai variable global


def register_user():
    os.system('cls || clear')
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    if username in users:
        os.system('cls || clear')
        print("="*40)
        print("Username sudah ada. Silakan coba lagi.")
        print("="*40)
    else:
        users[username] = password
        os.system('cls || clear')
        print("="*40)
        print("Registrasi berhasil.")
        print("="*40)


# login admin dengan username = santoso; password = 052;

def login_admin():
    os.system('cls || clear')
    username = input("Masukkan username : ")
    password = input("Masukkan password : ")

    if username == admin_username and password ==admin_password:
        os.system('cls || clear')
        print("="*40)
        print(f"selamat datang, admin {username}!")
        admin_menu()
    else :
        os.system('cls || clear')
        print("="*40)
        print("username atau password admin salah!!")
        print("="*40)

# login user untuk login menggunakan akun yang sudah di registrasi sebelumnya
# dan menggunakan parameter users        

def login_user(users):                         
    os.system('cls || clear')
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    if username in users and users[username] == password:
        os.system('cls || clear')
        print("="*40)
        print(f"Selamat datang, {username}!")
        print("="*40)
        user_menu()
        # Call to user menu function should be defined elsewhere
        # menu_akun.user_menu()
    else:
        os.system('cls || clear')
        print("="*40)
        print("Username atau password salah!")
        print("="*40)


def guest_login():
    os.system('cls || clear')
    print("="*40)
    print("anda masuk sebagai tamu")
    print("="*40)
    guest_menu()