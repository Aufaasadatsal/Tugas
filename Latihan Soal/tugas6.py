angka = float(input("input tinggi air:"))
if angka <= 500:
    print("AMAN")
elif angka <= 600:
    print("WASPADA")
elif angka <= 650:
    print("SIAGA 2")
elif angka > 650:
    print("SIAGA 1")