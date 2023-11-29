daftar_menu = {
    'makanan': {
        'nasi goreng': 15000,
        'mie goreng': 12000,
        'ayam geprek': 18000
    },
    'minuman': {
        'aneka jus': 15000,
        'soft drink': 10000,
        'sweet ice tea': 5000

    }
}

nama_pembeli = input("Masukan nama pembeli : ")
no_hp_pembeli = input("Masukan no hp pembeli : ")
pesan_menu = input("Pesan menu apa? (makanan atau minuman): ")

if pesan_menu == 'makanan' :
    print("Menu makanan: ", list(daftar_menu['makanan'].keys()))
elif pesan_menu == 'minuman' :
    print("Menu minuman: ", list(daftar_menu['minuman'].keys()))
else :
    print("Pilihan tidak valid")
menu_pesanan = input("Masukan pesanan: ").lower()
jumlah_pesanan = int(input("Masukan jumlah pesanan: "))

if menu_pesanan in daftar_menu[pesan_menu]:
    harga_total = daftar_menu[pesan_menu][menu_pesanan] * jumlah_pesanan

    print("Nama pembeli:", nama_pembeli)
    print("No hp pembeli:", no_hp_pembeli)
    print("Menu yang dipesan:", menu_pesanan)
    print("Jumlah pesanan:", jumlah_pesanan)
    print("Harga yang harus dibayarkan:", "Rp.", harga_total)
else:
    print("Menu tidak tersedia.")