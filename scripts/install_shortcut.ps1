# scripts/install_shortcut.ps1: an Epoch shortcut on the Desktop and in the Start Menu.
# The shortcut runs the windowless Python on space/app.py: the hub starts when needed and the dashboard
# opens in its own app window. Run once:  powershell -ExecutionPolicy Bypass -File scripts\install_shortcut.ps1
$repo = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$pyw = "D:\AGI-lab\.venv\Scripts\pythonw.exe"
if (-not (Test-Path $pyw)) { $pyw = (Get-Command pythonw -ErrorAction SilentlyContinue).Source }
if (-not $pyw) { Write-Error "pythonw.exe not found"; exit 1 }
$icon = Join-Path $repo "space\web\epoch.ico"
$shell = New-Object -ComObject WScript.Shell
foreach ($dir in @([Environment]::GetFolderPath("Desktop"), (Join-Path $env:APPDATA "Microsoft\Windows\Start Menu\Programs"))) {
  $lnk = $shell.CreateShortcut((Join-Path $dir "Epoch.lnk"))
  $lnk.TargetPath = $pyw
  $lnk.Arguments = '"' + (Join-Path $repo "space\app.py") + '"'
  $lnk.WorkingDirectory = $repo
  $lnk.Description = "Epoch: a team of AI researchers"
  if (Test-Path $icon) { $lnk.IconLocation = $icon }
  $lnk.Save()
  Write-Output ("shortcut: " + (Join-Path $dir "Epoch.lnk"))
}
