<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Eksemplar</title>
</head>
<body>
    <h1>Input Sebuah Buku</h1>
    <form action="" method="post">
        <table>
            <tr>
                <td>Input Jumlah Buku</td>
                <td><input type="number" name="buku" id=""></td>
            </tr>
            <tr>    
                <td></td>
                <td><input type="submit" name="submit" value="Simpan"></td>
            </tr>
        </table>
    </form>
</body>
</html> 

<br>

<?php
if (isset($_POST['submit'])) {
    $jum_buku = $_POST['buku'];
    $harga = $jum_buku * 50000;
    if ($jum_buku <= 10) {
        echo "anda tidak mendapatkan diskon <br>harga yang harus dibayar ialah $harga";
    }
    if ($jum_buku > 10 && $jum_buku <=20) {
        $sisa_lembar = $jum_buku % 10;
        $diskon_diatas_100 = ($sisa_lembar * 50000) * 0.15;
        $buku_lembar_pertama = $jum_buku - $sisa_lembar;
        $diskon_lembar_pertama = ($buku_lembar_pertama * 50000) * 0.05;
        $harga_akhir = $harga - $diskon_diatas_100 - $diskon_lembar_pertama; 
        echo "diskon 100 eksemplar pertama: $diskon_lembar_pertama <br> 
            sisa $sisa_lembar eksemplar, diskon : $diskon_diatas_100<br>
            total harga: $harga_akhir";
    }
    if ($jum_buku > 20) {
        $sisa_lembar_diatas_200 = $jum_buku % 20;
        $diskon_diatas_200 = ($sisa_lembar_diatas_200 * 50000) * 0.27;
        $sisa_lembar_200 = $jum_buku - $sisa_lembar_diatas_200 - 10;
        $diskon_200_eksemplar = ($sisa_lembar_200 * 50000) * 0.17;
        $sisa_lembar_100 = $sisa_lembar_200;
        $diskon_100_eksemplar = ($sisa_lembar_100 * 50000) * 0.07;

        $harga_akhir = $harga - $diskon_diatas_200 - $diskon_200_eksemplar - $diskon_100_eksemplar; 
        echo "diskon 100 eksemplar pertama: $diskon_100_eksemplar<br>
        diskon 100 eksemplar kedua: $diskon_200_eksemplar <br>
        diskon sisa eksemplar: $diskon_diatas_200 <br>
        harga yang harus dibayar: $harga_akhir";
}
}
?>
