function Calculate-Circle {
    param(
        [float]$radius
    )

    $surface = $radius*$radius*[Math]::PI

     $surface
}
Calculate-Circle(15)




function puhasta_nimi {

param($nimi)
$nimi=$nimi.Trim()
$nimi=$nimi.Replace("ü","u").Replace("õ","o").Replace("ä","a").Replace("ö","o")
$nimi
}


puhasta_nimi("  Jüõäöri  ")