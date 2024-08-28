angka = int(input("jam lembur:"))
if angka < 6 and angka > 0:
    print("dapet duit Rp 100.000")
elif angka == 6:
    print("dapet duit Rp 200.000")
elif angka > 6:
    print("dapet duit Rp 300.000")
else:
    print("gaje lu")