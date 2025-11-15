# 🚀 Guía Completa para Subir tu Proyecto a GitHub

## Paso 1: Crear el Repositorio en GitHub

1. **Inicia sesión en GitHub:**
   - Ve a https://github.com
   - Inicia sesión con tu cuenta

2. **Crea un nuevo repositorio:**
   - Haz clic en el botón **"+"** en la esquina superior derecha
   - Selecciona **"New repository"** (Nuevo repositorio)

3. **Configura el repositorio:**
   - **Repository name:** `Portafolio_Web` (o el nombre que prefieras)
   - **Description:** "Portafolio web personal - MetGo3D"
   - **Visibilidad:** Selecciona **Public** (público) para usar GitHub Pages gratis
   - **NO marques** "Initialize this repository with a README" (ya tienes uno)
   - Haz clic en **"Create repository"** (Crear repositorio)

## Paso 2: Conectar tu Repositorio Local con GitHub

Abre PowerShell en la carpeta del proyecto y ejecuta:

```powershell
# Verifica que estás en la rama master
git branch

# Si no estás en master, cambia a master
git checkout master

# Agrega el repositorio remoto (reemplaza TU_USUARIO con tu usuario de GitHub)
git remote add origin https://github.com/TU_USUARIO/Portafolio_Web.git

# O si ya existe, actualiza la URL
git remote set-url origin https://github.com/TU_USUARIO/Portafolio_Web.git

# Verifica la conexión
git remote -v
```

## Paso 3: Subir los Archivos

```powershell
# Agrega todos los archivos (excepto los que están en .gitignore)
git add .

# Haz commit de los cambios
git commit -m "Subir portafolio web completo"

# Sube los archivos a GitHub
git push -u origin master
```

**Nota:** Si es la primera vez que haces push, GitHub te pedirá autenticarte. Puedes usar:
- Un **Personal Access Token** (recomendado)
- O las credenciales de GitHub

## Paso 4: Activar GitHub Pages

1. **Ve a tu repositorio en GitHub:**
   - Abre: `https://github.com/TU_USUARIO/Portafolio_Web`

2. **Configura GitHub Pages:**
   - Haz clic en **Settings** (Configuración)
   - En el menú lateral, busca **Pages**
   - En **Source**, selecciona:
     - Branch: `master`
     - Folder: `/ (root)`
   - Haz clic en **Save** (Guardar)

3. **Espera unos minutos:**
   - GitHub procesará tu sitio
   - Verás un mensaje verde con la URL de tu sitio

4. **Accede a tu sitio:**
   - Tu sitio estará en: `https://TU_USUARIO.github.io/Portafolio_Web/`

## 📋 Comandos Rápidos (Copia y Pega)

Si ya tienes el repositorio creado en GitHub:

```powershell
# Verificar estado
git status

# Agregar archivos
git add .

# Hacer commit
git commit -m "Actualizar portafolio"

# Subir a GitHub
git push origin master
```

## ✅ Verificación

Una vez configurado, deberías poder acceder a:
- `https://TU_USUARIO.github.io/Portafolio_Web/index.html`
- `https://TU_USUARIO.github.io/Portafolio_Web/cv.html`
- `https://TU_USUARIO.github.io/Portafolio_Web/dashboard_marca_personal.html`
- `https://TU_USUARIO.github.io/Portafolio_Web/formulario_contacto.html`

## 🔐 Autenticación en GitHub

Si GitHub te pide autenticación al hacer push:

1. **Crea un Personal Access Token:**
   - Ve a: https://github.com/settings/tokens
   - Haz clic en **"Generate new token"** > **"Generate new token (classic)"**
   - Dale un nombre (ej: "Portafolio_Web")
   - Selecciona el scope **"repo"**
   - Haz clic en **"Generate token"**
   - **Copia el token** (solo se muestra una vez)

2. **Usa el token como contraseña:**
   - Cuando Git te pida usuario: tu nombre de usuario de GitHub
   - Cuando te pida contraseña: pega el token que copiaste

## 🆘 Solución de Problemas

**Error: "Repository not found"**
- Verifica que el repositorio exista en GitHub
- Verifica que tengas permisos de escritura
- Verifica que la URL del remoto sea correcta

**Error: "Authentication failed"**
- Usa un Personal Access Token en lugar de tu contraseña
- Verifica que el token tenga permisos de "repo"

**El sitio no aparece después de activar Pages**
- Espera 5-10 minutos
- Verifica que la rama `master` esté seleccionada
- Revisa la pestaña **Actions** en GitHub para ver errores

