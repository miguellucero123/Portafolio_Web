# Configuración de Base de Datos PostgreSQL

## Instalación de PostgreSQL

### Windows:
1. Descarga PostgreSQL desde: https://www.postgresql.org/download/windows/
2. Instala PostgreSQL (por defecto usa puerto 5432)
3. Recuerda la contraseña del usuario `postgres` que configures durante la instalación

### Linux/Mac:
```bash
# Ubuntu/Debian
sudo apt-get install postgresql postgresql-contrib

# macOS (con Homebrew)
brew install postgresql
brew services start postgresql
```

## Configuración de la Base de Datos

### 1. Crear la base de datos:

```sql
-- Conectar como usuario postgres
psql -U postgres

-- Crear base de datos
CREATE DATABASE portfolio_consultas;

-- Conectar a la base de datos
\c portfolio_consultas;

-- Ejecutar el script de creación de tablas
\i setup_database.sql
```

O ejecutar directamente:
```bash
psql -U postgres -f setup_database.sql
```

### 2. Configurar Variables de Entorno

Puedes configurar la conexión a PostgreSQL de dos formas:

#### Opción A: Variables de Entorno (Recomendado)

Antes de ejecutar el notebook, configura las variables de entorno:

```bash
# Windows PowerShell
$env:DB_HOST="localhost"
$env:DB_PORT="5432"
$env:DB_NAME="portfolio_consultas"
$env:DB_USER="postgres"
$env:DB_PASSWORD="tu_contraseña_aqui"
```

```bash
# Windows CMD
set DB_HOST=localhost
set DB_PORT=5432
set DB_NAME=portfolio_consultas
set DB_USER=postgres
set DB_PASSWORD=tu_contraseña_aqui
```

```bash
# Linux/Mac
export DB_HOST=localhost
export DB_PORT=5432
export DB_NAME=portfolio_consultas
export DB_USER=postgres
export DB_PASSWORD=tu_contraseña_aqui
```

#### Opción B: Modificar directamente en el notebook

Edita la celda de CONFIGURACIÓN en `server_1.ipynb`:

```python
DB_CONFIG = {
    'host': 'localhost',
    'port': '5432',
    'database': 'portfolio_consultas',
    'user': 'postgres',
    'password': 'tu_contraseña_aqui'
}
```

### 3. Instalar dependencias

```bash
pip install psycopg2-binary
```

O usar el archivo requirements.txt:

```bash
pip install -r requirements.txt
```

## Verificar la Conexión

Después de configurar, ejecuta `start_server()` en el notebook. Deberías ver:

```
✅ Base de datos PostgreSQL inicializada correctamente
   Host: localhost:5432
   Database: portfolio_consultas
```

## Consultar las Consultas Guardadas

Puedes consultar las consultas directamente desde psql:

```sql
-- Conectar a la base de datos
psql -U postgres -d portfolio_consultas

-- Ver todas las consultas
SELECT * FROM consultas ORDER BY fecha_creacion DESC;

-- Contar consultas
SELECT COUNT(*) FROM consultas;

-- Ver consultas del último día
SELECT * FROM consultas WHERE fecha_creacion >= CURRENT_DATE;
```

## Solución de Problemas

### Error: "No module named 'psycopg2'"
```bash
pip install psycopg2-binary
```

### Error: "Connection refused"
- Verifica que PostgreSQL esté corriendo
- En Windows: Servicios > PostgreSQL
- En Linux: `sudo systemctl status postgresql`

### Error: "database does not exist"
```sql
CREATE DATABASE portfolio_consultas;
```

### Error: "password authentication failed"
- Verifica la contraseña en DB_CONFIG
- Puedes cambiar la contraseña: `ALTER USER postgres PASSWORD 'nueva_contraseña';`

