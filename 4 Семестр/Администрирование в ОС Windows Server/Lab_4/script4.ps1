$i = 0
while (1) {
$i = $i + 1
Copy-Item -Path "C:\1.jpg" -Destination "E:\$i"
Start-Sleep -Milliseconds 100
}

Remove-Item -Path "E:\*"
