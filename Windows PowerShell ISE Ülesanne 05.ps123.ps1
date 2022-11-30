$a=hostname
"Arvuti nimi: "+ $a

(Get-WmiObject Win32_OperatingSystem)
"***********************************"
(Get-WmiObject Win32_OperatingSystem).Caption
"***********************************"
(Get-NetIPAddress -AddressFamily IPV4 -InterfaceAlias Ethernet).IPAddress
"***********************************"
(get-wmiobject -class "win32_physicalmemory" -namespace "root\CIMV2").Capacity
"***********************************"
(Get-WMIObject win32_Processor).Name
"***********************************"
(Get-WmiObject Win32_VideoController).Name
"***********************************"
[System.Security.Principal.WindowsIdentity]::GetCurrent().Name