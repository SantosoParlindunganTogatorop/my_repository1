# tanpa parameter
def hasil():
    print("hello world")

hasil()

# menggunakan parameter
def hasil(nama):
    print(f"hello world {nama}")

hasil("santoso")        # pemanggilan fungsi dapat dilakukan berkali-kali
hasil("afa")
hasil("khairul")


# Membuat fungsi dengan parameter (panjang, lebar)
def luas_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    print ("Luas persegi panjang:", luas)

luas_persegi_panjang(4,6)

# fungsi pengembalian nilai
def luas_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    return luas

Luas_Persegi = luas_persegi_panjang(4,6)
print(f"luas persegi {Luas_Persegi}")

# Variabel lokal dan global
nama = "afa"

def say_hello():
    nama = "santoso"
    print(nama, "didalam fungsi")

print( nama, "diluar fungsi")       # akan memprint variabel global
say_hello()                         # akan memprint variabel lokal


# fungsi -> mengembalikan nilai
# prosedur tidak mengembalikan nilai 


def faktorial(n):
    if n == 1:
        return 1
    else:
        return n*faktorial(n-1)
print(faktorial(5))

pilihan = input("angka 1 berhenti angka 2 lannjut :")
