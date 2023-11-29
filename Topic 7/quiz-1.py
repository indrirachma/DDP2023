kendaraan = input("Masukkan nama kendaraan: ")
bensin = input("Masukkan jenis bensin (Pertalite/Pertamax/Pertamax Turbo): ")
kota = input("Masukkan kota yg dituju (Jabodetabek): ")

jarak = 0
harga = 0
jarak_tempuh = 0

match kota.lower():
    case "jakarta":
        jarak = 20
    case "bekasi":
        jarak = 35.7
    case "depok":
        jarak = 5
    case "tangerang":
        jarak = 99
    case "bogor":
        jarak = 120.6
    case _:
        print("Kota yang Anda masukkan tidak valid!")

if bensin.lower() == "pertalite":
    harga = 10000
    jarak_tempuh = 12
elif bensin.lower() == "pertamax":
    harga = 14000
    jarak_tempuh = 13
elif bensin.lower() == "pertamax turbo":
    harga = 17000
    jarak_tempuh = 13.5
else:
    print("Jenis Bensin yang Anda masukkan tidak valid!")

pemakaian_bensin = jarak / jarak_tempuh
total_harga = pemakaian_bensin * harga

print("=====================================")
print("Nama Kendaraan\t: ", kendaraan)
print("Jenis Bensin\t: ", bensin)
print("Kota yg dituju\t: ", kota)
print("Pemakaian Bensin\t: ", round(pemakaian_bensin, 2), " Liter")
print("Total Harga Bensin\t:  Rp. ", round(total_harga, 2))
print("=====================================")