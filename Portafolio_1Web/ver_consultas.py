#!/usr/bin/env python3
"""Script para ver todas las consultas guardadas en SQLite"""

import sqlite3
from pathlib import Path
from datetime import datetime

DB_PATH = Path('consultas.db')

print("=" * 70)
print("CONSULTAS GUARDADAS EN BASE DE DATOS")
print("=" * 70)
print(f"\nUbicacion de la base de datos: {DB_PATH.absolute()}")
print()

if not DB_PATH.exists():
    print("[ERROR] La base de datos no existe aun.")
    print("   Esto puede significar que:")
    print("   1. El servidor no se ha ejecutado aun")
    print("   2. No se ha enviado ninguna consulta")
    print("   3. La base de datos se creo en otra ubicacion")
    print("\n   Por favor:")
    print("   1. Ejecuta start_server() en el notebook")
    print("   2. Envia una consulta desde el formulario")
    print("   3. Ejecuta este script nuevamente")
    print("=" * 70)
    exit(1)

try:
    conn = sqlite3.connect(str(DB_PATH))
    cursor = conn.cursor()
    
    # Verificar que la tabla existe
    cursor.execute("""
        SELECT name FROM sqlite_master 
        WHERE type='table' AND name='consultas'
    """)
    
    if not cursor.fetchone():
        print("[ERROR] La tabla 'consultas' no existe.")
        print("   La base de datos existe pero no tiene la estructura correcta.")
        print("   Por favor, ejecuta start_server() para inicializar la base de datos.")
        conn.close()
        print("=" * 70)
        exit(1)
    
    # Contar consultas
    cursor.execute("SELECT COUNT(*) FROM consultas")
    count = cursor.fetchone()[0]
    
    print(f"Total de consultas guardadas: {count}")
    print()
    
    if count == 0:
        print("[INFO] No hay consultas guardadas aun.")
        print("   Por favor:")
        print("   1. Asegurate de que el servidor este corriendo")
        print("   2. Accede a: http://localhost:8081/formulario_contacto.html")
        print("   3. Completa y envia el formulario")
        print("   4. Ejecuta este script nuevamente")
    else:
        # Obtener todas las consultas
        cursor.execute("""
            SELECT id, nombre, email, empresa, mensaje, fecha_creacion 
            FROM consultas 
            ORDER BY fecha_creacion DESC
        """)
        
        consultas = cursor.fetchall()
        
        print("=" * 70)
        print("TODAS LAS CONSULTAS:")
        print("=" * 70)
        
        for i, consulta in enumerate(consultas, 1):
            id_consulta, nombre, email, empresa, mensaje, fecha = consulta
            empresa_str = empresa if empresa and empresa.strip() else "N/A"
            
            print(f"\n[Consulta #{i}]")
            print(f"ID: {id_consulta}")
            print(f"Nombre: {nombre}")
            print(f"Email: {email}")
            print(f"Empresa: {empresa_str}")
            print(f"Mensaje: {mensaje[:100]}{'...' if len(mensaje) > 100 else ''}")
            print(f"Fecha: {fecha}")
            print("-" * 70)
    
    conn.close()
    print("\n[OK] Consulta completada correctamente")
    
except sqlite3.Error as e:
    print(f"[ERROR] Error al acceder a la base de datos: {e}")

except Exception as e:
    print(f"[ERROR] Error inesperado: {e}")

print("=" * 70)

