# Script PowerShell para configurar email
# Ejecuta este script antes de probar el envío de emails

Write-Host "================================================================"
Write-Host "CONFIGURACION DE EMAIL PARA NOTIFICACIONES"
Write-Host "================================================================"
Write-Host ""

# Solicitar App Password de Gmail
$appPassword = Read-Host "Ingresa tu App Password de Gmail (16 caracteres)"

if ([string]::IsNullOrWhiteSpace($appPassword)) {
    Write-Host "[ERROR] No se ingresó una contraseña" -ForegroundColor Red
    exit 1
}

# Configurar variables de entorno
$env:EMAIL_SENDER = "miguellucerogatica@gmail.com"
$env:EMAIL_PASSWORD = $appPassword
$env:EMAIL_RECIPIENT = "miguellucerogatica@gmail.com"
$env:ENABLE_EMAILS = "true"

Write-Host ""
Write-Host "[OK] Variables de entorno configuradas:" -ForegroundColor Green
Write-Host "  EMAIL_SENDER: $env:EMAIL_SENDER"
Write-Host "  EMAIL_RECIPIENT: $env:EMAIL_RECIPIENT"
Write-Host "  EMAIL_PASSWORD: ********"
Write-Host "  ENABLE_EMAILS: $env:ENABLE_EMAILS"
Write-Host ""
Write-Host "NOTA: Estas variables solo están activas en esta sesión de PowerShell." -ForegroundColor Yellow
Write-Host "Para que persistan, agrégalas permanentemente al sistema."
Write-Host ""
Write-Host "Para probar el envío, ejecuta:" -ForegroundColor Cyan
Write-Host "  python test_email.py"
Write-Host ""
Write-Host "================================================================"

