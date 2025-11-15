#!/usr/bin/env python3
"""Script para verificar que la base de datos SQLite funcione"""

import sqlite3
from pathlib import Path

DB_PATH = Path('consultas.db')

print("=" * 70)
print("VERIFICACION DE BASE DE DATOS SQLite")
print("=" * 70)

# 1. Verificar si existe la base de datos
if DB_PATH.exists():
    print(f"[OK] Base de datos encontrada: {DB_PATH}")
else:
    print(f"[INFO] Base de datos NO existe aun: {DB_PATH}")
    print("   Se creará automáticamente cuando ejecutes start_server()")

# 2. Intentar conectar y verificar la estructura
try:
    conn = sqlite3.connect(str(DB_PATH))
    cursor = conn.cursor()
    
    # Verificar que la tabla existe
    cursor.execute("""
        SELECT name FROM sqlite_master 
        WHERE type='table' AND name='consultas'
    """)
    
    table_exists = cursor.fetchone()
    
    if table_exists:
        print("[OK] Tabla 'consultas' existe")
        
        # Verificar estructura de la tabla
        cursor.execute("PRAGMA table_info(consultas)")
        columns = cursor.fetchall()
        print(f"\nEstructura de la tabla 'consultas':")
        print(f"   {'Column':<20} {'Type':<15} {'NotNull':<10} {'Default'}")
        print("   " + "-" * 70)
        for col in columns:
            cid, name, type_name, not_null, default, pk = col
            not_null_str = "Sí" if not_null else "No"
            default_str = str(default) if default else "None"
            print(f"   {name:<20} {type_name:<15} {not_null_str:<10} {default_str}")
        
        # Contar consultas
        cursor.execute("SELECT COUNT(*) FROM consultas")
        count = cursor.fetchone()[0]
        print(f"\nConsultas guardadas: {count}")
        
        # Mostrar últimas 5 consultas si hay
        if count > 0:
            cursor.execute("""
                SELECT id, nombre, email, empresa, fecha_creacion 
                FROM consultas 
                ORDER BY fecha_creacion DESC 
                LIMIT 5
            """)
            consultas = cursor.fetchall()
            print(f"\nUltimas {len(consultas)} consultas:")
            for cons in consultas:
                id, nombre, email, empresa, fecha = cons
                empresa_str = empresa if empresa else "N/A"
                print(f"   ID {id}: {nombre} ({email}) - {empresa_str} - {fecha}")
    
    else:
        print("[INFO] Tabla 'consultas' NO existe")
        print("   Se creará automáticamente cuando ejecutes start_server()")
    
    conn.close()
    print("\n[OK] Verificacion completada correctamente")
    
except sqlite3.Error as e:
    print(f"[ERROR] Error al verificar base de datos: {e}")

except Exception as e:
    print(f"[INFO] Base de datos no existe aun: {e}")
    print("   Esto es normal si no has ejecutado start_server() todavía")

print("=" * 70)

