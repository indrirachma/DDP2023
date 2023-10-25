print("""
==============
Sistem Hitung Luas Bangun Datar

Pilih Bangun Datar:
1 = persegi
2 = lingkaran
3 = segitiga
""")

bangunDatar = int(input("Masukkan pilihan bangun datar: "))

match bangunDatar:
    case 1:
        sisi = int(input("Masukkan panjang sisi: "))
        Luas = sisi ** 2
        print("Luas persegi", sisi, "adalah", Luas)
    case 2:
        jari2 = int(input("Masukkan panjang jari2: "))
        phi = 3.14
        Luas = phi * jari2 **2
        print("Luas lingkaran", jari2, "adalah", Luas)
    case 3:
        alas = int(input("Masukkan panjang alas: "))
        tinggi = int(input("Masukkan panjang tinggi: "))
        Luas = alas * tinggi * 0.5
        print("Luas segitiga", alas * tinggi, "adalah", Luas)
    case _:
        print("Salah pilih angka")