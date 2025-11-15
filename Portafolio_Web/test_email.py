#!/usr/bin/env python3
"""Script para probar el envío de emails"""

import os
import sys

# Importar configuración del servidor
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Simular importación de configuración
EMAIL_CONFIG = {
    'smtp_server': 'smtp.gmail.com',
    'smtp_port': 587,
    'sender_email': os.environ.get('EMAIL_SENDER', 'miguellucerogatica@gmail.com'),
    'sender_password': os.environ.get('EMAIL_PASSWORD', ''),
    'recipient_email': os.environ.get('EMAIL_RECIPIENT', 'miguellucerogatica@gmail.com'),
    'enable_emails': os.environ.get('ENABLE_EMAILS', 'true').lower() == 'true'
}

def test_email():
    """Prueba el envío de un email de notificación"""
    
    print("=" * 70)
    print("PRUEBA DE ENVIO DE EMAIL")
    print("=" * 70)
    print()
    
    if not EMAIL_CONFIG['sender_password']:
        print("[ERROR] EMAIL_PASSWORD no configurado.")
        print()
        print("OPCION 1: Usar script de configuracion (Windows)")
        print("   PowerShell: .\\configurar_email.ps1")
        print("   CMD: configurar_email.bat")
        print()
        print("OPCION 2: Configurar manualmente:")
        print("1. Crea una App Password en Gmail:")
        print("   https://myaccount.google.com/apppasswords")
        print("2. Configura la variable de entorno:")
        print()
        print("   Windows PowerShell:")
        print("   $env:EMAIL_PASSWORD = 'tu_app_password'")
        print()
        print("   Windows CMD:")
        print("   set EMAIL_PASSWORD=tu_app_password")
        print()
        print("   Linux/Mac:")
        print("   export EMAIL_PASSWORD='tu_app_password'")
        print()
        print("3. Ejecuta este script nuevamente")
        print("=" * 70)
        return False
    
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    
    try:
        print(f"Enviando email de prueba...")
        print(f"Desde: {EMAIL_CONFIG['sender_email']}")
        print(f"Hacia: {EMAIL_CONFIG['recipient_email']}")
        print()
        
        # Crear el mensaje
        msg = MIMEMultipart()
        msg['From'] = EMAIL_CONFIG['sender_email']
        msg['To'] = EMAIL_CONFIG['recipient_email']
        msg['Subject'] = "Prueba de Notificación - Portfolio Web"
        
        body = """
Esta es una prueba del sistema de notificaciones por email.

Si recibes este mensaje, significa que la configuración es correcta.

El sistema enviará automáticamente un email cada vez que se reciba
una nueva consulta a través del formulario de contacto.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Puedes eliminar este mensaje de prueba.
"""
        
        msg.attach(MIMEText(body, 'plain', 'utf-8'))
        
        # Conectar y enviar
        print("Conectando al servidor SMTP...")
        server = smtplib.SMTP(EMAIL_CONFIG['smtp_server'], EMAIL_CONFIG['smtp_port'])
        server.starttls()
        print("Autenticando...")
        server.login(EMAIL_CONFIG['sender_email'], EMAIL_CONFIG['sender_password'])
        print("Enviando email...")
        server.send_message(msg)
        server.quit()
        
        print()
        print("[OK] Email de prueba enviado correctamente!")
        print(f"Revisa tu bandeja de entrada: {EMAIL_CONFIG['recipient_email']}")
        print("=" * 70)
        return True
        
    except smtplib.SMTPAuthenticationError:
        print()
        print("[ERROR] Error de autenticación")
        print("Verifica que:")
        print("1. EMAIL_PASSWORD sea una App Password válida")
        print("2. La verificación en dos pasos esté activada en Gmail")
        print("3. El email EMAIL_SENDER sea correcto")
        print("=" * 70)
        return False
    except Exception as e:
        print()
        print(f"[ERROR] Error al enviar email: {e}")
        print("=" * 70)
        return False

if __name__ == "__main__":
    test_email()

