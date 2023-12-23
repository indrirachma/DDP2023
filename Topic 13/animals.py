class Animals:
    def __init__(self, nama, makanan, hidup, berkembangbiak):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembangbiak = berkembangbiak

    def info(self):
        print("-"*30)
        print("Nama \t\t:", self.nama)
        print("Makanan \t:", self.makanan)
        print("Hidup \t\t:", self.hidup)
        print("Berkembang Biak :", self.berkembangbiak)