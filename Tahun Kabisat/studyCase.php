<?php
    for ($i = 1600; $i <= 2024; $i++) { 
        if ($i % 4 == 0) {
            if ($i % 400 == 0) {
                echo "<br>$i adalah tahun kabisat<br>";
        } elseif ($i % 100 == 0 && $i % 400 != 0) {
            echo "<br>$i bukan tahun kabisat<br>";
        } else {
            echo "<br>$i adalah tahun kabisat<br>";
        }
    }
}
?>