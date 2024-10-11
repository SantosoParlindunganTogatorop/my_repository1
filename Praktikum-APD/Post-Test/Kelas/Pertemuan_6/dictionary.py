# data_mhs = {
#     "nama" : "ucup",
#     "nim"  : 1 ,
#     "matkul" : ["apd", "kalkulus","agama"],
#     "dosen" :{
#         "nama" : "awang",
#         "matkul" : "apd"
#     }
# }

# print(data_mhs["dosen"]["nama"])
# print(data_mhs['nama'])
# print(data_mhs['nim'])

# print(data_mhs.get('mapel',"tidak ada"))        ##untuk menampilkan key dan apabila tidak ada akan menampilkan "tidak ada"

# for data in data_mhs:                              ##cuma menampilkan key
#     print(data)

# for key_data, value in data_mhs.items():            ##untuk menampilkan key dan value secara terurut
#     print(f"key: {key_data}\nvalue: {value}")

# data_mhs['alamat'] = "samarinda"                  ##untuk menambah dictionary menggunakan list 

# data_mhs.update({"alamat" : "samarinda"})           ##untuk menambah dictionary menggunakan .update

# data_mhs["nama"] = "michael"                        ##untuk menambah dictionary

# del data_mhs['nim']                                   ## menghapus data tanpa menyimpan data yang dihapus

# cache = data_mhs.pop('nim')                         ##untuk menhapus namu data yang terhapus tetap tersimpan
# print(data_mhs,"dictionary")
# print(cache,"cache")
# data_mhs['id'] = cache
# print(data_mhs)

# print(len(data_mhs))                                ##menghitung jumlah dictionary

# key = "apel","jeruk","mangga","semangka"
# value = 1
# buah = dict.fromkey(key, value)
# print(buah)

# for value in data_mhs.values():
#     print(value)

# Nilai = {
#     "Matematika" : 80,
#     "Bahasa inggris" : 100
# }

# ##menggunakan setdefault
# print("nilai:"), Nilai.setdefault("kimia",70)
# print("")
# print(Nilai)

# data_mhs = [                                ##untuk mengakses data lebih muda menggunakan "nama"
#     {"nama" : "ucup",
#      "role" : "admin"},

#      {"nama" : "ucup",
#      "role" : "user"}
# ]

# print(data_mhs[0]['nama'])
# print(data_mhs[1]['nama'])