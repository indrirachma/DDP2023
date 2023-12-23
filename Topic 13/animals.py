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
        print(self.nama, "adalah hewan langka.")

    def attack(self):
        print(self.nama, "menyerang dengan tanduk.")

class Ikan(Animals):
    def two(self):
        print(self.nama, "Hiu merupakan hewan purba.")

    def swim(self):
        print(self.nama, "sedang berenang.")

class Ular(Animals):
    def three(self):
        print(self.nama, "adalah hewan yang berbisa.")

    def slither(self):
        print(self.nama, "sedang merayap.")

# akses method
a = Badak("Badak", "Herbivora", "Darat", "Vivipar",)
a.info()
a.one()
a.attack()

b = Ikan("Ikan", "Omnivora", "Air", "Ovovivipar")
b.info()
b.two()
b.swim()

c = Ular("Ular", "Karnivora", "Amfibi", "Ovovivipar")
c.info()
c.three()
c.slither()