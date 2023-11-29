motor = {"Beat", "Scoopy", "Vario", "Aerox"}
mobil = {"Lamborghini", "Ferrari", "Bemo", "Avanza"}
print(motor)

# Menambah item
motor.add("Nmax")
print(motor)

# Menghapus item
motor.remove("Beat")
print(motor)

# Menggabungkan set
kendaraan = motor.union(mobil)
print(kendaraan)

# Update set
motor.update(mobil)
print(motor)