#!/usr/bin/env python3
"""Script para desactivar temporalmente los emails en el servidor"""

import os

print("=" * 70)
print("CONFIGURACION: DESACTIVAR EMAILS TEMPORALMENTE")
print("=" * 70)
print()
print("Este script configura el sistema para trabajar SIN emails.")
print("Las consultas se guardaran en la base de datos normalmente.")
print()
print("=" * 70)
print()

# Configurar variable de entorno para desactivar emails
os.environ['ENABLE_EMAILS'] = 'false'

print("[OK] Emails desactivados temporalmente")
print()
print("CONFIGURACION ACTUAL:")
print(f"  ENABLE_EMAILS = {os.environ.get('ENABLE_EMAILS', 'true')}")
print(f"  EMAIL_PASSWORD configurado = {'Sí' if os.environ.get('EMAIL_PASSWORD') else 'No'}")
print()
print("IMPORTANTE:")
print("  - El formulario seguira funcionando normalmente")
print("  - Las consultas se guardaran en: consultas.db")
print("  - Para ver las consultas: python ver_consultas.py")
print()
print("Para volver a activar emails:")
print("  1. Configura EMAIL_PASSWORD (App Password de Gmail)")
print("  2. Ejecuta: os.environ['ENABLE_EMAILS'] = 'true'")
print()
print("=" * 70)
print()
print("Ahora puedes ejecutar el servidor. Las consultas se guardaran")
print("pero no se enviaran emails hasta que configures EMAIL_PASSWORD.")
print()

