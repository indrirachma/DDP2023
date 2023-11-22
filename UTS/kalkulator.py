angka1 = int(input("Masukkan angka 1: "))
angka2 = int(input("Masukkan angka 2: "))
operator = input("Pilih operator (+, -, *, /, **): ")

def bilangan(angka1, angka2, operator):
    if operator == '+':
        hasil = angka1 + angka2
        operator_str = 'tambah'
    elif operator == '-':
        hasil = angka1 - angka2
        operator_str = 'kurang'
    elif operator == '/':
        hasil = angka1 / angka2
        operator_str = 'bagi'
    elif operator == '*':
        hasil = angka1 * angka2
        operator_str = 'kali'
    elif operator == '**':
        hasil = angka1 ** angka2
        operator_str = 'pangkat'
    else:
        return "Operator tidak valid."

    return f"Angka pertama : {angka1}\nAngka kedua : {angka2}\nPilihan Operator : {operator_str}\nHasil operator {angka1} {operator} {angka2} = {hasil}"

hasil_bilangan = bilangan(angka1, angka2, operator)

print(hasil_bilangan)