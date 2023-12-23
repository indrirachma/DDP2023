class Character:
    hp = 0
    damage = 0

    # constructor
    def __init__(self, hp, damage):
        self.hp = hp
        self.damage = damage

    def info(self):
        print("="*20)
        print("Character information")
        print("-"*10)
        print("HP \t:", self.hp)
        print("Damage \t:", self.damage)