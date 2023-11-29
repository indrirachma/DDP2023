jumlah_baris = int(input("Masukkan jumlah baris: "))

for i in range(1, jumlah_baris + 1):
    for j in range(i):
        print("*", end="")
    print()