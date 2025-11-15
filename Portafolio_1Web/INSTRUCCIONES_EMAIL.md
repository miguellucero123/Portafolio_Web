# 📧 Instrucciones para Configurar Email de Notificaciones

## ⚡ Configuración Rápida (Windows)

### Paso 1: Crear App Password de Gmail

1. **Ve a**: https://myaccount.google.com/apppasswords
   - Si no aparece el enlace, primero activa la **Verificación en dos pasos**: https://myaccount.google.com/security

2. **Genera una App Password**:
   - Selecciona **"Correo"**
   - Selecciona **"Otro (nombre personalizado)"**
   - Escribe: `Portfolio Web`
   - Haz clic en **"Generar"**

3. **Copia la contraseña de 16 caracteres** (la verás solo una vez)

### Paso 2: Configurar Variables de Entorno

#### Opción A: Script Automático (RECOMENDADO)

**PowerShell:**
```powershell
.\configurar_email.ps1
```

**CMD:**
```cmd
configurar_email.bat
```

El script te pedirá que ingreses tu App Password.

#### Opción B: Configuración Manual

**PowerShell:**
```powershell
$env:EMAIL_PASSWORD = "tu_app_password_de_16_caracteres"
```

**CMD:**
```cmd
set EMAIL_PASSWORD=tu_app_password_de_16_caracteres
```

### Paso 3: Probar el Envío

```bash
python test_email.py
```

Si todo está bien, verás:
```
[OK] Email de prueba enviado correctamente!
Revisa tu bandeja de entrada: miguellucerogatica@gmail.com
```

## ✅ Verificación

1. Revisa tu bandeja de entrada de Gmail
2. Deberías recibir un email con el asunto: **"Prueba de Notificación - Portfolio Web"**
3. Si lo recibes, ¡la configuración es correcta! ✅

## 🔄 Ejecutar el Servidor con Email

Una vez configurado el email:

1. **Configura la variable** (en la misma sesión de terminal):
   ```powershell
   $env:EMAIL_PASSWORD = "tu_app_password"
   ```

2. **Ejecuta el servidor** en el notebook:
   ```python
   start_server()
   ```

3. **Cuando alguien envíe el formulario**:
   - Se guardará en la base de datos ✅
   - Se enviará email automáticamente ✅
   - Verás en la consola:
     ```
     ✅ Consulta guardada en SQLite con ID: X
     ✅ Email de notificación enviado a miguellucerogatica@gmail.com
     ```

## ⚠️ Notas Importantes

- **Las variables de entorno solo duran mientras la sesión de terminal esté abierta**
- Si cierras PowerShell/CMD, tendrás que configurar `EMAIL_PASSWORD` nuevamente
- **NUNCA** compartas tu App Password
- Puedes crear múltiples App Passwords en Gmail (una para cada aplicación)

## 🔧 Configuración Permanente (Opcional)

Si quieres que `EMAIL_PASSWORD` esté siempre disponible:

### Windows (Permanente)

1. Abre **Configuración del Sistema** → **Variables de Entorno**
2. Haz clic en **"Nuevo"** en Variables de Usuario
3. Nombre: `EMAIL_PASSWORD`
4. Valor: `tu_app_password`
5. Haz clic en **"Aceptar"**

Ahora la variable estará disponible en todas las sesiones.

## ❓ Solución de Problemas

### Error: "EMAIL_PASSWORD no configurado"
- Verifica que hayas ejecutado el script de configuración o configurado la variable manualmente
- Asegúrate de estar en la misma sesión de terminal

### Error: "Error de autenticación SMTP"
- Verifica que la App Password sea correcta (16 caracteres, sin espacios)
- Asegúrate de que la verificación en dos pasos esté activada en Gmail
- Verifica que el email `EMAIL_SENDER` sea correcto

### El email no se envía pero la consulta se guarda
- Esto es normal si `EMAIL_PASSWORD` no está configurado
- La consulta se guarda correctamente en la base de datos
- Configura `EMAIL_PASSWORD` para habilitar las notificaciones

