import os

def tampilkan_mahasiswa():
    for i in range(len(data_mahasiswa)):
                print(f"data ke {i+1}")
                print(f"Nama : {data_mahasiswa[i]}")
                print("="*10)
def tambah_data():
     inputUser = input("Data yang mau ditambahkan : ")
     data_mahasiswa.append(inputUser)
     return inputUser
def ubah_data():
     index= int(input("masukkan index yang mau diedit : "))
     data_baru = input("masukkan nama anda :")
     data_mahasiswa[index-1]=data_baru
     return data_baru
def hapus():
    index_user = int(input("masukkan index yang ingin dihapus: "))
    data_mahasiswa.pop(index_user-1)
    return index_user


data_mahasiswa =["Ifnu","Adi","ucup","michael"]
os.system('cls || clear')
while True:
    print("""
    Menu
Lihat Data  >> 1
Tambah Data >> 2
Edit Data   >> 3
Hapus Data  >> 4
Keluar      >> 5
""")
    pilih = input("Masukan Pilihan menu >> ")
    os.system('cls || clear')
    match(pilih):
        case "1":
            print("===Lihat Data===")
            tampilkan_mahasiswa()
            input("Enter....")
            os.system('cls || clear')
        case "2":
            print("MENU TAMBAH DATA")
            print("=" * 10)
            print(f"berhasil menambahkan {tambah_data()}")
            input("Enter....")
            os.system('cls || clear')
        case "3":
            print("Menu ubah data")
            tampilkan_mahasiswa()
            print(f"data{ubah_data()} berhasil diubah")
            input("Enter.....")
            os.system('cls || clear')
        case "4":
            print("Menu Hapus Data")
            tampilkan_mahasiswa()
            print(f"{hapus()} telah dihapus")
            input("Enter.....")
            os.system('cls || clear')
        case "5":
            print("Anda memilih menu 5")
            exit()
        case _:
            print(f"Menu {pilih} tidak tersedia")
            input("Enter.....")
            os.system('cls || clear')