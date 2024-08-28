angka = int(input("masukkan angka yang akan dicek:"))
if angka == 0:
    print(f"{angka} merupakan nol")
else:
    print(f"{angka} tidak nol")

if angka < 0:
    print(f"{angka} negatif")
else:
    print(f"{angka} positif")

if angka % 2 == 0:
    print(f"{angka} genap")
else:
    print(f"{angka} ganjil")