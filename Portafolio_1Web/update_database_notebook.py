#!/usr/bin/env python3
"""Script para agregar inicialización de BD en server_1.ipynb"""

import json

# Leer el notebook
with open('server_1.ipynb', 'r', encoding='utf-8') as f:
    notebook = json.load(f)

# Buscar la celda con start_server (celda 9, índice 9)
if len(notebook['cells']) > 9:
    cell = notebook['cells'][9]
    source = ''.join(cell['source'])
    
    # Buscar dónde insertar init_database()
    # Buscar después de create_assets_structure()
    if 'create_assets_structure()' in source and 'init_database()' not in source:
        # Reemplazar PASO 3 con PASO 3 (init BD) y PASO 4 (validar)
        old_pattern = '    print("\\n📋 PASO 3: Validando archivos...")\n    \n    # Validar archivos'
        new_pattern = '    print("\\n📋 PASO 3: Inicializando base de datos...")\n    \n    # Inicializar base de datos SQLite\n    init_database()\n    \n    print("\\n📋 PASO 4: Validando archivos...")\n    \n    # Validar archivos'
        
        if old_pattern in source:
            source = source.replace(old_pattern, new_pattern)
            cell['source'] = source.splitlines(keepends=True)
            print("OK: Actualizado PASO 3 y PASO 4")
        
        # Actualizar PASO 4 a PASO 5
        if 'print("\\n📋 PASO 4: Iniciando servidor web...")' in source:
            source = source.replace(
                'print("\\n📋 PASO 4: Iniciando servidor web...")',
                'print("\\n📋 PASO 5: Iniciando servidor web...")'
            )
            cell['source'] = source.splitlines(keepends=True)
            print("OK: Actualizado PASO 4 a PASO 5")

# Guardar el notebook actualizado
with open('server_1.ipynb', 'w', encoding='utf-8') as f:
    json.dump(notebook, f, ensure_ascii=False, indent=1)

print("OK: Notebook actualizado correctamente")

