
# input  tipe data String

Nama = str(input("Massukkan Nama Lengkap : "))
Tanggal_Lahir = str(input("Masukkan Tanggal Lahir(DD-MM-YYYY) : "))
Alamat = str(input("Masukkan Alamat : "))

# input tipe data integer

Nim = int(input("Masukkan Nomor Induk Mahasiswa : "))
Nomor_Telp = int(input("Masukkan Nomor Telepon : (+62)"))

# input tipe data float

Tinggi_Badan = float(input("Masukkan Tinggi Badan (cm) : "))
Berat_Badan = float(input("Masukkan Berat Badan (Kg) : "))

# input tipe data boolean

Kuliah_Bekerja =bool(input("Apakah Anda Kuliah sambil Bekerja? (ya/tidak): ").strip().lower()) == 'ya'

# Membuat variabel numerik untuk menjumlahkan tipe data integer dan float 

Numerik = Nim + Tinggi_Badan + Berat_Badan + Nomor_Telp

# Membuat F-String untuk memformat string pada variabel Biodata
 
Biodata = (
    f"Nama                      : {Nama}\n"
    f"Tanggal Lahir             : {Tanggal_Lahir}\n"
    f"Alamat                    : {Alamat}\n"
    f"Nim                       : {Nim}\n"
    f"Nomor telepon             : +62{Nomor_Telp} \n"
    f"Tinggi Badan              : {Tinggi_Badan:.2f} cm \n"
    f"Berat Badan               : {Berat_Badan:.2f} kg \n"
    f"Kuliah sambil bekeja?     : {'ya' if Kuliah_Bekerja else 'Tidak'} \n"
    f"Total integer dan float   : {Numerik}"
)

# Print Output Berdasarkan data input 

print("=" * 80)
print("Biodata Diri".center(80))
print("=" * 80)
print(Biodata)
print("=" * 80)