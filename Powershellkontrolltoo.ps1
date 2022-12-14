#George Raatpalu
#13.12.2022

$scriptpath = $MyInvocation.MyCommand.Path
$dir = Split-Path $scriptpath
 

#$csv_header = @("Nimed;Kasutajanimi;email;password")
 

#$csv_header | Set-Content $dir\emails.csv
#massiivid
$users = Get-Content -path C:\Users\It22\Desktop\xd\emails.csv
 
$users




ForEach($user in $users){
    $fname = $user.first_name
    $lname = $user.last_name
    $user
    $users
    $fullname = $fname+$lname
}      
$pass = 0 | ForEach-Object { Get-Random -Maximum $lname.Length }
$pass = -join $lname[$pass]
$pass += Get-Random  -minimum 100 -Maximum 999
$items = Get-ChildItem -Path "c:\temp"

$fullname >> C:\Users\It22\Desktop\xd/emails.txt

