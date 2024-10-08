#akun
import menu_akun
import os

#membuat users sebagai nested list pada menu register dan login

users = {}
admin_username = "santoso"
admin_password = "052"

#membuat program registrasi user

def register_user():
    os.system('cls || clear')
    username = input("Masukkan username : ")
    password = int(input("Masukkan password : "))

    if username in users:
        os.system('cls || clear')
        print("="*40)
        print("username sudah ada. silahkan coba lagii")
        print("="*40)
    else :
        users[username] = password
        os.system('cls || clear')
        print("="*40)
        print("Registrasi berhasil")
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
        menu_akun.admin_menu()
    else :
        os.system('cls || clear')
        print("="*40)
        print("username atau password admin salah!!")
        print("="*40)

# login user untuk login menggunakan akun yang sudah di registrasi sebelumnya        

def login_user():
    os.system('cls || clear')
    username = input("Masukkan username : ")
    password = input("Masukkan password : ")

    if username in users and users[username]== password:
        os.system('cls || clear')
        print("="*40)
        print(f"selamat datang, {username}!")
        print("="*40)
        menu_akun.user_menu()
    else :
        os.system('cls || clear')
        print("="*40)
        print("username atau password salah ! ")
        print("="*40)

#Login tamu untuk login tanpa username dan password

def guest_login():
    os.system('cls || clear')
    print("="*40)
    print("anda masuk sebagai tamu")
    print("="*40)
    menu_akun.guest_menu()