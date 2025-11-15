@echo off
REM Script para configurar email en Windows CMD
REM Ejecuta este script antes de probar el envío de emails

echo ================================================================
echo CONFIGURACION DE EMAIL PARA NOTIFICACIONES
echo ================================================================
echo.

REM Solicitar App Password de Gmail
set /p APP_PASSWORD="Ingresa tu App Password de Gmail (16 caracteres): "

if "%APP_PASSWORD%"=="" (
    echo [ERROR] No se ingreso una contraseña
    exit /b 1
)

REM Configurar variables de entorno
set EMAIL_SENDER=miguellucerogatica@gmail.com
set EMAIL_PASSWORD=%APP_PASSWORD%
set EMAIL_RECIPIENT=miguellucerogatica@gmail.com
set ENABLE_EMAILS=true

echo.
echo [OK] Variables de entorno configuradas
echo   EMAIL_SENDER: %EMAIL_SENDER%
echo   EMAIL_RECIPIENT: %EMAIL_RECIPIENT%
echo   EMAIL_PASSWORD: ********
echo   ENABLE_EMAILS: %ENABLE_EMAILS%
echo.
echo NOTA: Estas variables solo estan activas en esta ventana de CMD.
echo Para que persistan, agregalas permanentemente al sistema.
echo.
echo Para probar el envio, ejecuta:
echo   python test_email.py
echo.
echo ================================================================

