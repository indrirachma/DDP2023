class Gempa:
    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala

    def dampak(self):
        dampak = "Gempa di " + self.lokasi + " "
        if self.skala < 2:
            dampak += "tidak berasa."
        elif 2 <= self.skala < 4:
            dampak += "menyebabkan bangunan retak-retak."
        elif 4 <= self.skala < 6:
            dampak += "menyebabkan bangunan roboh."
        elif self.skala >= 6:
            dampak += "menyebabkan bangunan roboh dan berpotensi tsunami."
        return dampak
