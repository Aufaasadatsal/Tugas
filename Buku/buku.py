def hitung_harga_total(jum_buku):
    harga_per_buku = 50000
    harga = jum_buku * harga_per_buku

    if jum_buku <= 10:
        print(f"Anda tidak mendapatkan diskon\nHarga yang harus dibayar ialah Rp {harga:,.0f}")
    elif 10 < jum_buku <= 20:
        sisa_lembar = jum_buku % 10
        diskon_diatas_100 = sisa_lembar * harga_per_buku * 0.15
        buku_lembar_pertama = jum_buku - sisa_lembar
        diskon_lembar_pertama = buku_lembar_pertama * harga_per_buku * 0.05
        harga_akhir = harga - diskon_diatas_100 - diskon_lembar_pertama
        print(f"Diskon 100 eksemplar pertama: Rp {diskon_lembar_pertama:,.0f}\n"
              f"Sisa {sisa_lembar} eksemplar, diskon: Rp {diskon_diatas_100:,.0f}\n"
              f"Total harga: Rp {harga_akhir:,.0f}")
    elif jum_buku > 20:
        sisa_lembar_diatas_200 = jum_buku % 20
        diskon_diatas_200 = sisa_lembar_diatas_200 * harga_per_buku * 0.27
        sisa_lembar_200 = jum_buku - sisa_lembar_diatas_200 - 10
        diskon_200_eksemplar = sisa_lembar_200 * harga_per_buku * 0.17
        sisa_lembar_100 = sisa_lembar_200
        diskon_100_eksemplar = sisa_lembar_100 * harga_per_buku * 0.07

        harga_akhir = harga - diskon_diatas_200 - diskon_200_eksemplar - diskon_100_eksemplar
        print(f"Diskon 100 eksemplar pertama: Rp {diskon_100_eksemplar:,.0f}\n"
              f"Diskon 100 eksemplar kedua: Rp {diskon_200_eksemplar:,.0f}\n"
              f"Diskon sisa eksemplar: Rp {diskon_diatas_200:,.0f}\n"
              f"Harga yang harus dibayar: Rp {harga_akhir:,.0f}")  

# Input dari pengguna
jum_buku = int(input("Masukkan jumlah buku yang dibeli: "))
hitung_harga_total(jum_buku)
