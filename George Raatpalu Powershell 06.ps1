$nimi = "Georgeraatpalu"
$email = "georgeraatpalu10@gmail.com"
$kuupaev = get-date -Format "dd.mm.yy"


$nimi
$email
$kuupaev

$skriptiAsukoht = $MyInvocation.MyCommand.Path
$dir = Split-Path $skriptiAsukoht
$emailid = Get-Content -path $dir\emailid.txt
$file_data | Select-Object -Last 1


$kasutajad=$emailid.split(",")
$kasutajad+=$email
"esimene kasutaja on "+$kasutajad[0]
"viimane kasutaja on "+$kasutajad[-1]
"kasutajaid kokku " +$emailid.Length


