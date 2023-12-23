from character import *

# buat Hero sebagai class child dari Character
class Hero(Character):
    # atribut / properti
    name = ""
    defense = 0

    # constructor adalah method yg di jalankan ketika class dipanggil
    def __init__(self, name, damage, hp, defense):
        super().__init__(hp, damage)
        self.name = name
        self.defense = defense

    # method
    def info(self):
        super().info()
        print("Name \t: ", self.name)
        print("Defense : ", self.defense)

    def attack(self, target):
        target.hp -= self.damage
        print("="*20)
        print(self.name, " menyerang ", target.name)
        print("HP dari ", target.name, " saat ini adalah ", target.hp)
        print("="*20)

# instansiasi objek
hero1 = Hero("Layla", 320, 2100, 30)

hero2 = Hero("Alucard", 270, 3000, 90)

# mengakses atribut
# print(hero2.name)

# akses method
hero1.info()
hero1.attack(hero2)