# Display basic Windows system information.
$os = Get-CimInstance Win32_OperatingSystem
$cpu = Get-CimInstance Win32_Processor | Select-Object -First 1
Write-Host "Script Toolkit - System Info"
Write-Host "==========================="
Write-Host "Computer: $env:COMPUTERNAME"
Write-Host "OS: $($os.Caption) $($os.Version)"
Write-Host "CPU: $($cpu.Name)"
Write-Host ("RAM: {0:N1} GB" -f ($os.TotalVisibleMemorySize / 1MB))
