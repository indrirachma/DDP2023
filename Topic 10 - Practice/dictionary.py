data_diri = {"nama":"Reza","mapel":"DDP"}

# mengakses dictionary
print(data_diri["nama"])

# menambah item
data_diri["jurusan"]  = "Teknik Informatika"
print(data_diri)

# update item
data_diri["nama"] = "Aldi Mahardiansyah"
print(data_diri)

# mengahapus item
data_diri.pop("mapel")
print(data_diri)

# cek keberadaan key
if "nama" in data_diri:
    print("Terdapat nama")
else:
    print("Tidak ada nama")