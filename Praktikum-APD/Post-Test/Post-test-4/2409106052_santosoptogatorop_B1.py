#buat import agar os.system yang digunakan dikenal dalam ruang
#lingkup program

import os
os.system('cls') 

#buat variabel kesempatan untuk membatasi banyaknya user dalam menginput username

kesempatan = 3

#fungsi "while kesempatan > 0" untuk menjalankan program selama kesempatan lebih besar dari 0
#username untuk menginput nama dari user

while kesempatan > 0:
    username = input("masukkan nama anda     : ")
    if username == "santoso":
         
        #fungsi while untuk mengulang program apabila user salah memasukkan password

         kesempatan = 3
         while kesempatan > 0:
            password = input("masukkan password anda : ")

            #fungsi if apabila user benar memasukkan password maka lanjut ke pemilihan menu

            if password == "052":

                #data menu pilihan user

                pesan = (f" Hai, {username}")
                judul = ("Menu Program Menghitung Luas/Volume Bangun Ruang")
                menu = (""" Menu yang tersedia :
        1. luas permukaan balok 
        2. volume tabung 
        3. volume kerucut
        4. volume limas segita 
        5. keluar dari program""")

                #os untuk mengclear inputan data yang sebelumnya agar lebih rapi
                #print var pesan, judul, dan menu agar tertampilkan di layar user

                os.system('cls') 
                print()
                print(pesan)
                print("=" * 80)
                print(judul.center(80))
                print("=" * 80)
                print(menu)
                print("=" * 80)
                pilih = (input("Silahkan  pilih dari salah satu menu diatas : "))
                print("=" * 80)

                #fungsi if : apabila user memilih menu 1 ; fungsi break untuk memberhentikan program.

                if pilih == "1" :
                    os.system('cls') 
                    print("=" * 80)
                    print  ("menu yang anda pilih adalah mencari luas permukaan balok")
                    panjang = float(input("panjang balok : "))
                    lebar =   float(input("lebar balok   : "))
                    tinggi =  float(input("tinggi balok  : "))
                    hasil = (panjang * lebar * tinggi)
                    print("=" * 80)
                    print (f"luas permukaan balok yang anda peroleh adalah {hasil:.2f} m²".center(80))
                    print("=" * 80)
                    break

                #fungsi if : apabila user memilih menu 2 ; fungsi break untuk memberhentikan program.

                elif pilih == "2" :
                    os.system('cls') 
                    print("=" * 80)
                    print("menu yang anda pilih adalah mencari volume tabung")
                    r =      float(input("jari-jari : "))
                    tinggi = float(input("tinggi    : "))
                    hasil = ( 3.14 * (r**2) * tinggi)
                    print("=" * 80)
                    print(f"volume tabung yang anda peroleh adalah {hasil:.2f} m³".center(80))
                    print("=" * 80)
                    break

                #fungsi if : apabila user memilih menu 3 ; fungsi break untuk memberhentikan program.

                elif pilih == "3" :
                    os.system('cls') 
                    print("=" * 80)
                    print("menu yang anda pilih adalah mencari volume kerucut")
                    r =      float(input("jari-jari : "))
                    tinggi = float(input("tinggi    : "))
                    hasil = (1/3 * 3.14 * (r**2) * tinggi)
                    print("=" * 80)
                    print(f"volume kerucut yang anda peroleh adalah {hasil:.2f}m³".center(80))
                    print("=" * 80)
                    break

                #fungsi if : apabila user memilih menu 4 ; fungsi break untuk memberhentikan program.

                elif pilih == "4" :
                    os.system('cls') 
                    print("=" * 80)
                    print("menu yang anda pilih adalah mencari volume limas segitiga")
                    panjang = float(input("panjang alas : "))
                    tinggi =  float(input("tinggi alas  : "))
                    h = float(input("tinggi limas : "))
                    hasil = (1/3 * (1/2 * panjang * tinggi)*h)
                    print("=" * 80)
                    print(f"volume kerucut yang anda peroleh adalah {hasil:.2f}m³".center(80))
                    print("=" * 80)
                    break

                #fungsi else : apabila user memilih menu diluar 1-4 ; fungsi break untuk memberhentikan program.

                else :
                    os.system('cls') 
                    print("=" * 80)
                    print("anda keluar dari program".center(80))
                    print("=" * 80)
                    break
       
            #fungsi else : apabila user salah memasukkan password
            # maka akan melakukan perulangan dengan mengurangi nilai kesemptan dengan 1                            

            else:  
                os.system('cls') 
                print("password anda salah !")
                kesempatan -= 1
                print(f"kesempatan login tersisa {kesempatan} kali")

                #fungsi if : apabila kesempatan 0 atau habis maka user akan diarahkan keluar program
                
                if kesempatan == 0:
                    os.system('cls')
                    print("="*80)
                    print("Anda salah memasukkan password sebanyak 3 kali. anda akan keluar dari  program".center(80))
                    print("="*80)
                    break
                
        #fungsi break : agar setelah program menu selesai program akan berhenti, tidak looping ke username lagi

         print("")
         break
              
        #fungsi else : apabila user name salah mengisi username
        #maka akan melakukan perulangan dengan mengurangi nilai kesemptan dengan 1 

    else :
        os.system('cls') 
        print("username anda salah !")
        kesempatan -= 1

        #fungsi if : apabila kesempatan 0 atau habis maka user akan diarahkan keluar program

        print(f"kesempatan login tersisa {kesempatan} kali")
        if kesempatan == 0 :
            os.system('cls') 
            print("=" * 80)
            print("Anda salah memasukkan username sebanyak 3 kali. anda akan  keluar dari program".center(80))
            print("=" * 80)
          
 
