$scriptpath = $MyInvocation.MyCommand.Path
$dir = Split-Path $scriptpath
 

#$csv_header = @("Nimed;Kasutajanimi;email;password")
 

#$csv_header | Set-Content $dir\emails.csv
 
$users = Get-Content -path C:\Users\It22\Desktop\xd\emails.csv
 
 $users




ForEach($user in $users){
    #$fname = $user.first_name
    #$lname = $user.last_name
    $user
    $users
    }
      
$pass += Get-Random  -minimum 100 -Maximum 999

