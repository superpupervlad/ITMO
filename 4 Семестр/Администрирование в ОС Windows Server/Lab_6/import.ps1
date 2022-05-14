Import-Csv "C:\abc.csv" | ForEach-Object {
    $_ | New-ADUser
    # New-ADUser -GivenName $_.GivenName -Title $_.Title -Department $_.Department -EmailAddress $_.EmailAddress -MobilePhone $_.MobilePhone -Name $_.Name -AccountPassword $_.AccountPassword -Path $_.Path -HomeDirectory $_.HomeDirectory
    if ((Get-ADGroup -Filter {Name -like $_.Group} | measure).Count -lt 1) {
        New-ADGroup -Name $_.Group
    }
    Add-ADGroupMember -Identity $_.Group -Members $_.Name
}
 
Import-Csv "C:\abc.csv" | ConvertTo-Html
