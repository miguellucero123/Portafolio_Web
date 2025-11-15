# 📧 Sistema SIN Emails - Instrucciones

## ⚠️ Situación Actual

Tu cuenta de Gmail tiene verificación en dos pasos activada, por lo que necesitas una App Password para enviar emails. Mientras resuelves esto, puedes usar el sistema sin emails.

## ✅ ¿Qué Funciona SIN Emails?

- ✅ El formulario de contacto funciona normalmente
- ✅ Las consultas se guardan en la base de datos (`consultas.db`)
- ✅ Puedes ver todas las consultas recibidas
- ✅ El servidor funciona normalmente

## 🔧 Cómo Desactivar Emails Temporalmente

### OPCIÓN 1: Ejecutar script (RÁPIDO)

```bash
python desactivar_emails.py
```

Este script configura la variable de entorno `ENABLE_EMAILS=false`.

### OPCIÓN 2: En el Notebook (MANUAL)

En una celda nueva del notebook `server_1.ipynb`, ejecuta:

```python
import os
os.environ['ENABLE_EMAILS'] = 'false'
print("✅ Emails desactivados temporalmente")
```

**IMPORTANTE:** Debes ejecutar esto ANTES de iniciar el servidor.

### OPCIÓN 3: Variable de entorno en PowerShell

```powershell
$env:ENABLE_EMAILS = 'false'
```

## 📊 Ver las Consultas Guardadas

Aunque no se envíen emails, todas las consultas se guardan. Para verlas:

```bash
python ver_consultas.py
```

Esto mostrará:
- ID de consulta
- Nombre
- Email
- Empresa
- Mensaje
- Fecha de recepción

## 🔄 Reactivar Emails (Cuando Tengas App Password)

1. **Crea App Password en Gmail:**
   - Ve a: https://myaccount.google.com/apppasswords
   - Crea una nueva App Password
   - Copia la contraseña de 16 caracteres

2. **Configura la contraseña:**
   ```powershell
   $env:EMAIL_PASSWORD = 'tu_app_password_de_16_caracteres'
   ```

3. **Reactiva emails:**
   En el notebook:
   ```python
   import os
   os.environ['ENABLE_EMAILS'] = 'true'
   os.environ['EMAIL_PASSWORD'] = 'tu_app_password'
   ```

## 💡 Recomendación

Por ahora, usa el sistema sin emails. Esto te permite:
- Probar el formulario completo
- Ver que las consultas se guardan correctamente
- Desarrollar otras partes del proyecto

Cuando tengas tiempo, resuelve el tema del App Password y luego reactivas los emails.

