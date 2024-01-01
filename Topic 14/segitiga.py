# import package tkinter
from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# buat objek root dari class tk
root = ttk.Window(themename="morph")

# atur lebar dan tinggi aplikasi
root.geometry("500x500")

# atur judul aplikasi
root.title("Aplikasi Penghitung Luas Segitiga")

# buat teks
ttk.Label(root, text="Aplikasi Penghitung Luas Segitiga", font =("calibri", 15, "bold")).pack(pady=9)

ttk.Label(root, text="Masukan Alas:").pack(pady=10)

# buat input alas
alas = Entry()
alas.insert(END, 0)
alas.pack()

ttk.Label(root, text="Masukan Tinggi:").pack(pady=10)

# buat input tinggi
tinggi = Entry()
tinggi.insert(END, 0)
tinggi.pack()

# buat function menghitung 
def hitung():
    Halas = int(alas.get())
    Htinggi = int(tinggi.get())
    luas = 0.5 * Halas * Htinggi
    hasil = f"Hasil perhitungan luas adalah : {luas}"
    ttk.Label(root, text=hasil).pack()

# buat tombol hitung
ttk.Button(root, text="Hitung", command=hitung, bootstyle=WARNING).pack(pady=10)

# Jalankan Aplikasi
root.mainloop()