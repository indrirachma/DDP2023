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

class Badak(Animals):
    def one(self):
        print("Badak adalah hewan langka.")

class Ikan(Animals):
    def two(self):
        print("Hiu merupakan hewan purba.")

class Ular(Animals):
    def three(self):
        print("Ular adalah hewan yang berbisa.")

# akses method
a = Badak("Badak", "Herbivora", "Darat", "Vivipar",)
a.info()
a.one()

b = Ikan("Ikan", "Omnivora", "Air", "Ovovivipar")
b.info()
b.two()

c = Ular("Ular", "Karnivora", "Amfibi", "Ovovivipar")
c.info()
c.three()