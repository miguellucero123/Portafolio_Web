#!/usr/bin/env python3
"""
Portfolio Profesional - Server Simplificado v4.0
"""

import http.server
import socketserver
import os
from pathlib import Path

# Configuración
PORT = 8081
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

print("=" * 60)
print("🚀 INICIANDO SERVIDOR...")
print(f"📂 Directorio: {DIRECTORY}")
print(f"🐍 Python: {os.sys.version}")
print("=" * 60)

# Crear archivos HTML básicos para prueba
def create_test_files():
    """Crea archivos HTML de prueba"""
    
    # index.html
    index_content = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Portfolio - Miguel Lucero</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 20px; }
        nav { background: #1a365d; color: white; padding: 15px; margin: -20px -20px 20px -20px; }
        nav a { color: white; margin: 0 15px; text-decoration: none; }
        h1 { color: #1a365d; }
        .btn { background: #2c5282; color: white; padding: 10px 20px; text-decoration: none; display: inline-block; margin: 10px 5px; }
    </style>
</head>
<body>
    <nav>
        <a href="index.html">Inicio</a>
        <a href="cv.html">CV</a>
        <a href="dashboard_marca_personal.html">Dashboard</a>
    </nav>
    <h1>Miguel Ignacio Lucero Gatica</h1>
    <h2>Consultor en Análisis de Datos</h2>
    <p>Transformando datos en decisiones estratégicas</p>
    <a href="dashboard_marca_personal.html" class="btn">Ver Dashboard</a>
    <a href="cv.html" class="btn">Ver CV</a>
</body>
</html>"""
    
    # cv.html
    cv_content = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>CV - Miguel Lucero</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 20px; }
        nav { background: #1a365d; color: white; padding: 15px; margin: -20px -20px 20px -20px; }
        nav a { color: white; margin: 0 15px; text-decoration: none; }
        h1 { color: #1a365d; }
    </style>
</head>
<body>
    <nav>
        <a href="index.html">Inicio</a>
        <a href="cv.html">CV</a>
        <a href="dashboard_marca_personal.html">Dashboard</a>
    </nav>
    <h1>Currículum Vitae</h1>
    <h2>Miguel Ignacio Lucero Gatica</h2>
    <h3>Experiencia</h3>
    <p>8+ años en análisis de datos</p>
    <h3>Educación</h3>
    <p>Técnico en Análisis de Datos - AIEP</p>
</body>
</html>"""
    
    # dashboard_marca_personal.html
    dashboard_content = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Dashboard - Marca Personal</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 20px; }
        nav { background: #1a365d; color: white; padding: 15px; margin: -20px -20px 20px -20px; }
        nav a { color: white; margin: 0 15px; text-decoration: none; }
        h1 { color: #1a365d; }
        .metric { background: #f0f0f0; padding: 20px; margin: 10px; display: inline-block; }
    </style>
</head>
<body>
    <nav>
        <a href="index.html">Inicio</a>
        <a href="cv.html">CV</a>
        <a href="dashboard_marca_personal.html">Dashboard</a>
    </nav>
    <h1>Dashboard de Marca Personal</h1>
    <div class="metric">
        <h3>8</h3>
        <p>Casos de Estudio</p>
    </div>
    <div class="metric">
        <h3>20%</h3>
        <p>Engagement Objetivo</p>
    </div>
    <div class="metric">
        <h3>+30%</h3>
        <p>Crecimiento de Red</p>
    </div>
</body>
</html>"""
    
    # Crear archivos
    files = {
        'index.html': index_content,
        'cv.html': cv_content,
        'dashboard_marca_personal.html': dashboard_content
    }
    
    for filename, content in files.items():
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Creado: {filename}")
        except Exception as e:
            print(f"❌ Error creando {filename}: {e}")

# Crear archivos de prueba
print("\n📝 Creando archivos HTML...")
create_test_files()

# Servidor simple
class SimpleHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

# Iniciar servidor
try:
    print(f"\n🌐 Iniciando servidor en puerto {PORT}...")
    with socketserver.TCPServer(("", PORT), SimpleHandler) as httpd:
        print("\n" + "="*60)
        print("✅ SERVIDOR ACTIVO")
        print("="*60)
        print(f"\n🌐 Abre tu navegador en:")
        print(f"   http://localhost:{PORT}")
        print(f"\n⏹️  Presiona Ctrl+C para detener")
        print("="*60 + "\n")
        
        httpd.serve_forever()
        
except Exception as e:
    print(f"\n❌ ERROR: {e}")
    print("\nPosibles soluciones:")
    print("1. Verifica que el puerto 8080 no esté en uso")
    print("2. Ejecuta como administrador")
    print("3. Prueba con otro puerto cambiando PORT = 8081")