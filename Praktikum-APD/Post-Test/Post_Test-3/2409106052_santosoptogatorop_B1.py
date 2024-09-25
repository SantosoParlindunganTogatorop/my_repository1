#buat import agar os.system yang digunakan dikenal dalam ruang
#lingkup program

import os
os.system('cls') 

# buat var nama untuk memasukkan data nama

nama = input("masukkan nama anda : ")

#buat os untuk membersihkan tampilan input nama di variabel
os.system('cls') 


#buat keterangan menu

pesan = (f" Hai, {nama}")
judul = ("Menu Program Menghitung Luas/Volume Bangun Ruang")
menu = (""" Menu yang tersedia :
        1. luas permukaan balok 
        2. volume tabung 
        3. volume kerucut
        4. volume limas segita 
        5. keluar dari program""")

#print menu dengan membatatasi menggunakan ====

print()
print(pesan)
print("=" * 60)
print(judul.center(60))
print("=" * 60)
print(menu)
print("=" * 60)

#buat var pilih untuk memilih menu

pilih = int(input("Silahkan  pilih dari salah satu menu diatas : "))
print("=" * 60)

#buat fungsi percabangannya

if pilih == 1 :
    print  ("menu yang anda pilih adalah mencari luas permukaan balok")
    panjang = float(input("panjang balok : "))
    lebar = float(input("lebar balok : "))
    tinggi = float(input("tinggi balok : "))
    hasil = (panjang * lebar * tinggi)
    print("=" * 60)
    print (f"luas permukaan balok yang anda peroleh adalah {hasil:.2f} m²")
    print("=" * 60)
elif pilih == 2 :
    print("menu yang anda pilih adalah mencari volume tabung")
    r = float(input("jari-jari : "))
    tinggi = float(input("tinggi : "))
    hasil = ( 3.14 * (r**2) * tinggi)
    print("=" * 60)
    print(f"volume tabung yang anda peroleh adalah {hasil:.2f} m³")
    print("=" * 60)
elif pilih == 3 :
    print("menu yang anda pilih adalah mencari volume kerucut")
    r = float(input("jari-jari : "))
    tinggi = float(input("tinggi : "))
    hasil = (1/3 * 3.14 * (r**2) * tinggi)
    print("=" * 60)
    print(f"volume kerucut yang anda peroleh adalah {hasil:.2f}m³")
    print("=" * 60)
elif pilih == 4 :
    print("menu yang anda pilih adalah mencari volume limas segitiga")
    panjang = float(input("panjang alas : "))
    tinggi = float(input("tinggi alas : "))
    h = float(input("tinggi limas : "))
    hasil = (1/3 * (1/2 * panjang * tinggi)*h)
    print("=" * 60)
    print(f"volume kerucut yang anda peroleh adalah {hasil:.2f}m³")
    print("=" * 60)

    #buat cls untuk membersihkan terminal keika user tidak memilih dari keempat menu

else :
    os.system('cls') 
    print("=" * 60)
    print("anda keluar dari program".center(60))
    print("=" * 60)
       
    


