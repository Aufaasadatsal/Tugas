for i in range(1600, 2025):
    if i % 4 == 0:
        if i % 400 == 0:
            print(f"{i} adalah tahun kabisat")
        elif i % 100 == 0 and i % 400 != 0:
            print(f"{i} bukan tahun kabisat")
        else:
            print(f"{i} adalah tahun kabisat")
