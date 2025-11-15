#!/usr/bin/env python3
"""Script SIMPLIFICADO para probar el envío de emails sin App Password"""

import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

print("=" * 70)
print("PRUEBA SIMPLE DE ENVIO DE EMAIL")
print("=" * 70)
print()
print("Este script te permite probar el envio usando tu contrasena normal")
print("(NO recomendado para produccion, solo para pruebas)")
print()
print("=" * 70)
print()

# Solicitar credenciales
print("Configuracion de email:")
sender_email = input("miguellucerogatica@gmail.com: ").strip()
sender_password = input("Marzo2026: ").strip()
recipient_email = input("Email destinatario (ej: miguellucerogatica@gmail.com): ").strip()

if not sender_email or not sender_password or not recipient_email:
    print("[ERROR] Debes completar todos los campos")
    exit(1)

try:
    print()
    print("Enviando email de prueba...")
    print(f"Desde: {sender_email}")
    print(f"Hacia: {recipient_email}")
    print()
    
    # Crear el mensaje
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = "Prueba de Notificacion - Portfolio Web"
    
    body = """
Esta es una prueba del sistema de notificaciones por email.

Si recibes este mensaje, significa que la configuracion es correcta.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

IMPORTANTE: Este script usa la contrasena normal de Gmail.
Para produccion, usa una App Password que es mas segura.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

El sistema enviara automaticamente un email cada vez que se reciba
una nueva consulta a traves del formulario de contacto.

Puedes eliminar este mensaje de prueba.
"""
    
    msg.attach(MIMEText(body, 'plain', 'utf-8'))
    
    # Conectar y enviar
    print("Conectando al servidor SMTP...")
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    print("Autenticando...")
    server.login(sender_email, sender_password)
    print("Enviando email...")
    server.send_message(msg)
    server.quit()
    
    print()
    print("=" * 70)
    print("[OK] Email de prueba enviado correctamente!")
    print(f"Revisa tu bandeja de entrada: {recipient_email}")
    print("=" * 70)
    print()
    print("NOTA: Si recibes este email, puedes usar estas credenciales")
    print("en el servidor, pero recuerda usar App Password para produccion.")
    
except smtplib.SMTPAuthenticationError as e:
    print()
    print("=" * 70)
    print("[ERROR] Error de autenticacion")
    print("=" * 70)
    print()
    print("Posibles causas:")
    print("1. La contrasena es incorrecta")
    print("2. La verificacion en dos pasos esta activada (necesitas App Password)")
    print("3. Google bloqueo el acceso desde aplicaciones menos seguras")
    print()
    print("Soluciones:")
    print("1. Crea una App Password en: https://myaccount.google.com/apppasswords")
    print("2. O activa 'Permitir el acceso de aplicaciones menos seguras':")
    print("   https://myaccount.google.com/lesssecureapps")
    print("=" * 70)
    exit(1)
    
except Exception as e:
    print()
    print("=" * 70)
    print(f"[ERROR] Error al enviar email: {e}")
    print("=" * 70)
    exit(1)

