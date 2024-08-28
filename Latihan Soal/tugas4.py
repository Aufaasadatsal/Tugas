barang1 = int(input("barang1:"))
barang2 = int(input("barang2:"))
barang3 = int(input("barang3:"))
listBarang = [barang1,barang2,barang3]
hargaAwal = sum(listBarang)

if hargaAwal > 1000000:
    diskon = hargaAwal * 0.1
    hargaAkhir = hargaAwal - diskon
    print(f"diskon:{diskon} harga awal:{hargaAwal} harga akhir:{hargaAkhir}")
else:
    print(f"harga:{hargaAwal}")