# GET AD USER DN PATH
$ADUser=Get-ADUser -Identity %AD_USERNAME%

#REMOVE EXTRA SPACES AND NEW LINES
$ADUser=($ADUser.DistinguishedName | Out-String).Trim()

Write-Host $ADUser

#MOVE AD USER TO DISABLED OU FOR USERS
Move-ADObject -Identity $ADUser -TargetPath "%DISABLED_USERS_OU_PATH%"


