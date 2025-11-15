# Configuración de Notificaciones por Email

## 📧 Envío Automático de Emails

El sistema envía automáticamente un email de notificación cada vez que se recibe una nueva consulta a través del formulario de contacto.

## 🔧 Configuración

### Paso 1: Crear App Password en Gmail

1. Ve a tu cuenta de Google: https://myaccount.google.com/
2. Ve a **Seguridad**
3. En "Acceso a Google", activa la **Verificación en dos pasos** (si no está activa)
4. Después de activar, ve a **Contraseñas de aplicaciones**
5. Selecciona **Correo** y **Otro (nombre personalizado)**
6. Escribe "Portfolio Web" y genera la contraseña
7. **Copia la contraseña de 16 caracteres** (la necesitarás en el siguiente paso)

### Paso 2: Configurar Variables de Entorno

#### Opción A: Variables de Entorno del Sistema (Recomendado)

**Windows PowerShell:**
```powershell
$env:EMAIL_SENDER = "miguellucerogatica@gmail.com"
$env:EMAIL_PASSWORD = "tu_app_password_de_16_caracteres"
$env:EMAIL_RECIPIENT = "miguellucerogatica@gmail.com"
$env:ENABLE_EMAILS = "true"
```

**Windows CMD:**
```cmd
set EMAIL_SENDER=miguellucerogatica@gmail.com
set EMAIL_PASSWORD=tu_app_password_de_16_caracteres
set EMAIL_RECIPIENT=miguellucerogatica@gmail.com
set ENABLE_EMAILS=true
```

**Linux/Mac:**
```bash
export EMAIL_SENDER="miguellucerogatica@gmail.com"
export EMAIL_PASSWORD="tu_app_password_de_16_caracteres"
export EMAIL_RECIPIENT="miguellucerogatica@gmail.com"
export ENABLE_EMAILS="true"
```

#### Opción B: Archivo de Configuración (No recomendado para producción)

1. Copia `config_email.py.example` a `config_email.py`
2. Edita `config_email.py` y completa con tus credenciales
3. Importa el archivo antes de ejecutar el servidor:
   ```python
   import config_email
   start_server()
   ```

### Paso 3: Ejecutar el Servidor

Después de configurar las variables de entorno, ejecuta:

```python
start_server()
```

## ✅ Verificación

Cuando se reciba una nueva consulta:

1. La consulta se guardará en `consultas.db`
2. Se enviará un email automáticamente a `EMAIL_RECIPIENT`
3. Verás en la consola:
   ```
   ✅ Consulta guardada en SQLite con ID: X
   ✅ Email de notificación enviado a miguellucerogatica@gmail.com
   ```

## 🔍 Solución de Problemas

### Error: "EMAIL_PASSWORD no configurado"
- Verifica que hayas configurado la variable de entorno `EMAIL_PASSWORD`
- Asegúrate de usar una **App Password** de Gmail, no tu contraseña normal

### Error: "Error de autenticación SMTP"
- Verifica que la App Password sea correcta
- Asegúrate de que la verificación en dos pasos esté activada en Gmail
- Verifica que estés usando el email correcto en `EMAIL_SENDER`

### Los emails no se envían pero las consultas se guardan
- Esto es normal si `EMAIL_PASSWORD` no está configurado
- La consulta se guarda correctamente en la base de datos
- Configura `EMAIL_PASSWORD` para habilitar las notificaciones por email

## 📝 Ejemplo de Email Recibido

```
Subject: 📧 Nueva Consulta Recibida - ID: 1

Nueva consulta recibida en tu portfolio web:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
INFORMACIÓN DE LA CONSULTA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ID de Consulta: 1
Fecha: 2025-01-14 18:10:15

Nombre: Juan Pérez
Email: juan.perez@empresa.com
Empresa: Empresa XYZ

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MENSAJE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Hola, estoy interesado en...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Puedes responder directamente a: juan.perez@empresa.com
```

## 🔒 Seguridad

- **NUNCA** subas `config_email.py` a un repositorio público
- Usa **App Passwords** en lugar de tu contraseña principal de Gmail
- Las App Passwords se pueden revocar fácilmente si se comprometen
- Considera usar variables de entorno en lugar de archivos de configuración

