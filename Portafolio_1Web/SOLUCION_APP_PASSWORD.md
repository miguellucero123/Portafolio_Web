# 🔧 Solución: No puedo crear App Password en Gmail

## ❓ Problemas Comunes y Soluciones

### 1. La verificación en dos pasos no está completamente activada

**Síntomas:**
- No ves la opción "Contraseñas de aplicaciones" en el menú
- Te dice que primero debes activar la verificación en dos pasos

**Solución:**
1. Ve a: https://myaccount.google.com/security
2. Verifica que **"Verificación en dos pasos"** esté **ACTIVADA** (no solo configurada)
3. Si dice "Inactiva", haz clic y actívala completamente
4. Espera 5-10 minutos después de activarla
5. Intenta nuevamente crear la App Password

### 2. Necesitas esperar después de activar la verificación

A veces Google tarda unos minutos en habilitar la opción de App Passwords.

**Solución:**
- Espera 5-10 minutos
- Cierra y abre el navegador nuevamente
- Intenta acceder a: https://myaccount.google.com/apppasswords

### 3. Problema con el navegador

**Solución:**
- Intenta desde otro navegador (Chrome, Firefox, Edge)
- Limpia la caché del navegador
- Prueba en modo incógnito/privado

### 4. La cuenta tiene restricciones

Si tu cuenta de Google es de una organización (empresa/universidad), puede tener restricciones.

**Solución:**
- Contacta al administrador de tu organización
- O usa una cuenta personal de Gmail para las pruebas

## 🔄 Alternativa: Usar Contraseña de Aplicación Menos Segura (No recomendado, pero funciona)

Si no puedes crear App Password, hay una alternativa (menos segura):

1. Ve a: https://myaccount.google.com/lesssecureapps
2. Activa "Permitir el acceso de aplicaciones menos seguras" (si está disponible)
3. Usa tu contraseña normal de Gmail (pero esto es menos seguro)

**⚠️ NOTA:** Esta opción está siendo eliminada por Google, por eso la App Password es mejor.

## 📧 Alternativa: Otra cuenta de Email

Si Gmail no funciona, puedes usar otro proveedor:

### Outlook/Hotmail
- SMTP: `smtp-mail.outlook.com`
- Puerto: `587`
- Usa tu contraseña normal de Outlook

### Yahoo
- SMTP: `smtp.mail.yahoo.com`
- Puerto: `587`
- Necesita App Password también

### Otro proveedor SMTP
- Puedes usar cualquier servidor SMTP compatible

## 🛠️ Otra Opción: Configuración Manual Temporal

Si solo necesitas probar, puedo ayudarte a configurar el código para usar tu contraseña normal (temporalmente), pero **no es recomendable para producción**.

## ✅ Próximos Pasos

1. ¿Puedes acceder a: https://myaccount.google.com/apppasswords?
2. ¿Qué mensaje de error ves exactamente?
3. ¿La verificación en dos pasos está completamente activada?

Con esta información puedo ayudarte mejor.

