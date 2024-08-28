
angka1 = int(input("angka1:"))
angka2 = int(input("angka2:"))
angka3 = int(input("angka3:"))
array = [angka1,angka2,angka3]
urutan = max(angka1,angka2,angka3)
median = sorted(array)[1]

print(f"{urutan} dan {median}")
