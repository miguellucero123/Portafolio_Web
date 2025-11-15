#!/usr/bin/env python3
"""Script directo para probar el envío de emails"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ============================================================
# CONFIGURACIÓN - EDITA ESTOS VALORES
# ============================================================
SENDER_EMAIL = "miguellucerogatica@gmail.com"
SENDER_PASSWORD = ""  # Pega aquí tu contraseña de Gmail o App Password
RECIPIENT_EMAIL = "miguellucerogatica@gmail.com"

# ============================================================
# NO EDITES NADA DESDE AQUÍ HACIA ABAJO
# ============================================================

print("=" * 70)
print("PRUEBA DE ENVIO DE EMAIL")
print("=" * 70)
print()

if not SENDER_PASSWORD:
    print("[ERROR] SENDER_PASSWORD no configurado.")
    print()
    print("INSTRUCCIONES:")
    print("1. Abre el archivo test_email_directo.py")
    print("2. Edita la variable SENDER_PASSWORD en la linea 11")
    print("3. Pega tu contraseña de Gmail o App Password")
    print("4. Ejecuta este script nuevamente")
    print()
    print("Ejemplo:")
    print("   SENDER_PASSWORD = \"tu_contrasena_aqui\"")
    print()
    print("NOTA: Si tienes verificacion en dos pasos activada,")
    print("      necesitas usar una App Password.")
    print()
    print("Si no puedes crear App Password, intenta:")
    print("1. Desactivar temporalmente la verificacion en dos pasos")
    print("2. O usar este script solo para pruebas locales")
    print()
    print("=" * 70)
    exit(1)

try:
    print(f"Enviando email de prueba...")
    print(f"Desde: {SENDER_EMAIL}")
    print(f"Hacia: {RECIPIENT_EMAIL}")
    print()
    
    # Crear el mensaje
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECIPIENT_EMAIL
    msg['Subject'] = "Prueba de Notificacion - Portfolio Web"
    
    body = """
Esta es una prueba del sistema de notificaciones por email.

Si recibes este mensaje, significa que la configuracion es correcta.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

El sistema enviara automaticamente un email cada vez que se reciba
una nueva consulta a traves del formulario de contacto.

Puedes eliminar este mensaje de prueba.
"""
    
    msg.attach(MIMEText(body, 'plain', 'utf-8'))
    
    # Conectar y enviar
    print("Conectando al servidor SMTP de Gmail...")
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    print("Autenticando...")
    server.login(SENDER_EMAIL, SENDER_PASSWORD)
    print("Enviando email...")
    server.send_message(msg)
    server.quit()
    
    print()
    print("=" * 70)
    print("[OK] Email de prueba enviado correctamente!")
    print(f"Revisa tu bandeja de entrada: {RECIPIENT_EMAIL}")
    print("=" * 70)
    
except smtplib.SMTPAuthenticationError as e:
    print()
    print("=" * 70)
    print("[ERROR] Error de autenticacion SMTP")
    print("=" * 70)
    print()
    print("Posibles causas:")
    print("1. La contrasena es incorrecta")
    print("2. La verificacion en dos pasos esta activada")
    print("   -> Necesitas una App Password")
    print("   -> Ve a: https://myaccount.google.com/apppasswords")
    print("3. Google bloqueo el acceso desde aplicaciones menos seguras")
    print()
    print("Soluciones:")
    print("1. Si tienes verificacion en dos pasos, crea App Password:")
    print("   https://myaccount.google.com/apppasswords")
    print("2. O desactiva temporalmente la verificacion en dos pasos")
    print("   (solo para pruebas, NO recomendado para produccion)")
    print("=" * 70)
    exit(1)
    
except Exception as e:
    print()
    print("=" * 70)
    print(f"[ERROR] Error al enviar email: {e}")
    print("=" * 70)
    exit(1)

