# 🚀 Instrucciones para Subir el Proyecto Limpio a GitHub

Tu repositorio local está limpio y listo. Solo contiene los archivos necesarios para la web.

## ✅ Archivos que se subirán (solo estos):

- ✅ `index.html` - Página principal
- ✅ `cv.html` - Currículum
- ✅ `dashboard_marca_personal.html` - Dashboard
- ✅ `formulario_contacto.html` - Formulario
- ✅ `assets/` - CSS y JavaScript
- ✅ `METGO_3D.JPG` - Imagen
- ✅ `README.md` - Documentación
- ✅ `GITHUB_PAGES_SETUP.md` - Instrucciones
- ✅ `.gitignore` - Configuración

## 📋 Pasos para Subir a GitHub

### Paso 1: Crear el Repositorio en GitHub

1. Ve a https://github.com
2. Haz clic en el botón **"+"** (esquina superior derecha) > **"New repository"**
3. Configura:
   - **Repository name:** `Portafolio_Web` (o el nombre que prefieras)
   - **Description:** "Portafolio web personal - MetGo3D"
   - **Visibilidad:** Selecciona **Public** (necesario para GitHub Pages gratis)
   - ⚠️ **NO marques** "Initialize this repository with a README"
   - ⚠️ **NO agregues** .gitignore ni license
4. Haz clic en **"Create repository"**

### Paso 2: Conectar y Subir

Abre PowerShell en esta carpeta y ejecuta estos comandos:

```powershell
# Si el repositorio tiene un nombre diferente, actualiza la URL:
git remote set-url origin https://github.com/miguellucero123/Portafolio_Web.git

# O si necesitas agregar el remoto de nuevo:
# git remote add origin https://github.com/miguellucero123/Portafolio_Web.git

# Verifica la conexión
git remote -v

# Sube todos los archivos
git push -u origin master
```

**Nota:** Si GitHub te pide autenticación:
- **Usuario:** tu nombre de usuario de GitHub
- **Contraseña:** usa un **Personal Access Token** (no tu contraseña normal)
  - Crea uno en: https://github.com/settings/tokens
  - Selecciona el scope **"repo"**

### Paso 3: Activar GitHub Pages

1. Ve a tu repositorio en GitHub
2. Haz clic en **Settings** (Configuración)
3. En el menú lateral, busca **Pages**
4. En **Source**:
   - Branch: `master`
   - Folder: `/ (root)`
5. Haz clic en **Save**

### Paso 4: Acceder a tu Sitio

Después de 1-2 minutos, tu sitio estará disponible en:
```
https://miguellucero123.github.io/Portafolio_Web/
```

## ✅ Verificación

Una vez configurado, deberías poder acceder a:
- `https://miguellucero123.github.io/Portafolio_Web/index.html`
- `https://miguellucero123.github.io/Portafolio_Web/cv.html`
- `https://miguellucero123.github.io/Portafolio_Web/dashboard_marca_personal.html`
- `https://miguellucero123.github.io/Portafolio_Web/formulario_contacto.html`

## 🔍 Verificar Archivos en el Repositorio

Para verificar que solo están los archivos correctos, ejecuta:
```powershell
git ls-files
```

Deberías ver solo los archivos listados arriba.

