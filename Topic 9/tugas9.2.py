nilai = int(input("masukan nilai :"))

def kelulusan(nilai):
    if nilai < 0:
        return "Nilai tidak valid!"
    elif nilai <= 60:
        return "Gagal"
    elif nilai <= 70:
        return "Baik"
    elif nilai <= 80:
        return "Sangat Baik"
    elif nilai <= 100:
        return "Istimewa"
    else:
        return "Nilai tidak valid!"


print(kelulusan(nilai))