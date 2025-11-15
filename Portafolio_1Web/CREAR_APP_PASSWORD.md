# 🔐 Crear App Password de Gmail - Guía Paso a Paso

## ✅ Ya tienes la Verificación en dos pasos activada

Ahora necesitas crear la App Password:

## 📋 Pasos para Crear App Password

### 1. Ir a App Passwords
Ve directamente a: **https://myaccount.google.com/apppasswords**

O sigue estos pasos:
1. Ve a: https://myaccount.google.com/
2. Haz clic en **"Seguridad"** (lado izquierdo)
3. En la sección **"Acceso a Google"**, busca **"Contraseñas de aplicaciones"**
4. Haz clic en **"Contraseñas de aplicaciones"**

### 2. Generar la App Password

1. Si te pide verificar tu identidad, ingresa tu contraseña de Google
2. En el menú desplegable **"Seleccionar app"**, elige: **"Correo"**
3. En el menú **"Seleccionar dispositivo"**, elige: **"Otro (nombre personalizado)"**
4. Escribe: **"Portfolio Web"** (o cualquier nombre que prefieras)
5. Haz clic en **"Generar"**

### 3. Copiar la Contraseña

- Verás una **contraseña de 16 caracteres** (sin espacios)
- Ejemplo: `abcd efgh ijkl mnop` (pero sin espacios: `abcdefghijklmnop`)
- **IMPORTANTE**: Esta contraseña solo se muestra UNA VEZ
- **Cópiala inmediatamente** antes de cerrar la ventana

### 4. Configurar en el Sistema

Una vez que tengas la App Password de 16 caracteres:

**En PowerShell:**
```powershell
$env:EMAIL_PASSWORD = "abcdefghijklmnop"
```
(Reemplaza con tu App Password real)

**O usa el script automático:**
```powershell
.\configurar_email.ps1
```

### 5. Probar el Envío

```bash
python test_email.py
```

## ⚠️ Notas Importantes

- La App Password es diferente a tu contraseña normal de Gmail
- Tiene 16 caracteres (a veces se muestra con espacios, pero úsala sin espacios)
- Puedes crear múltiples App Passwords para diferentes aplicaciones
- Si olvidas la contraseña, simplemente crea una nueva

## 🔍 ¿No encuentras "Contraseñas de aplicaciones"?

Si no ves la opción "Contraseñas de aplicaciones":
1. Verifica que la **Verificación en dos pasos** esté realmente activada
2. Espera unos minutos (a veces tarda en aparecer)
3. Intenta desde otro navegador
4. Asegúrate de estar en: https://myaccount.google.com/apppasswords

