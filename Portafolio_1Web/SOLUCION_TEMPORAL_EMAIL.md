# 🔧 Solución Temporal: Email con Verificación en Dos Pasos

## Problema Actual
- ✅ Tienes verificación en dos pasos activada
- ❌ No puedes crear App Password
- ❌ La contraseña normal no funciona para SMTP

## Opciones Disponibles

### OPCIÓN 1: Desactivar temporalmente la verificación en dos pasos (SOLO PARA PRUEBAS)

**⚠️ IMPORTANTE: Solo haz esto para probar. Luego vuelve a activarla.**

1. Ve a: https://myaccount.google.com/security
2. En "Verificación en dos pasos", haz clic en "Desactivar"
3. Confirma la desactivación
4. Prueba enviar el email con tu contraseña normal
5. **VUELVE A ACTIVAR** la verificación en dos pasos después

### OPCIÓN 2: Usar el sistema SIN emails (solo guarda en BD)

Mientras resuelves el problema de email, puedes hacer que el sistema funcione normalmente pero sin enviar emails. Las consultas se guardarán en la base de datos y podrás verlas con `ver_consultas.py`.

Para desactivar emails temporalmente:
```python
# En el notebook, en una celda ejecuta:
import os
os.environ['ENABLE_EMAILS'] = 'false'
```

### OPCIÓN 3: Configurar la contraseña directamente en el notebook

Si logras desactivar temporalmente la verificación en dos pasos, puedes configurar la contraseña directamente:

```python
import os
os.environ['EMAIL_PASSWORD'] = 'Marzo2026'
```

Luego reinicia el servidor.

### OPCIÓN 4: Contactar al administrador (si es cuenta empresarial)

Si tu cuenta de Gmail es gestionada por una organización:
- Contacta al administrador de tu organización
- Solicita que habilite la creación de App Passwords
- O solicita una cuenta personal para las pruebas

## Recomendación

**Para probar AHORA mismo:**
1. Usa la OPCIÓN 2 (desactivar emails temporalmente)
2. El formulario seguirá funcionando
3. Las consultas se guardarán en `consultas.db`
4. Puedes verlas con: `python ver_consultas.py`
5. Luego resuelves el problema de email cuando tengas tiempo

## ¿Cómo ver las consultas guardadas?

```bash
python ver_consultas.py
```

Esto mostrará todas las consultas recibidas, incluso sin emails.

