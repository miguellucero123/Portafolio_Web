#!/usr/bin/env python3
"""Script para actualizar FORMULARIO_CONTACTO_HTML en server_1.ipynb"""

import json
import re

# Leer el formulario correcto
with open('formulario_contacto_correcto.html', 'r', encoding='utf-8') as f:
    formulario_correcto = f.read()

# Leer el notebook
with open('server_1.ipynb', 'r', encoding='utf-8') as f:
    notebook = json.load(f)

# Encontrar la celda con FORMULARIO_CONTACTO_HTML
for i, cell in enumerate(notebook['cells']):
    if cell['cell_type'] == 'code':
        source = ''.join(cell['source'])
        if 'FORMULARIO_CONTACTO_HTML' in source:
            print(f"Encontrado FORMULARIO_CONTACTO_HTML en celda {i}")
            
            # Reemplazar el contenido entre las comillas triples
            # Buscar desde FORMULARIO_CONTACTO_HTML = """ hasta el siguiente """
            
            # Construir el nuevo contenido
            # Primero, encontrar dónde empieza la variable
            new_source = []
            in_string = False
            string_start = 0
            
            for line in cell['source']:
                if 'FORMULARIO_CONTACTO_HTML = """' in line:
                    new_source.append(line)
                    in_string = True
                    # Agregar el contenido nuevo línea por línea
                    for html_line in formulario_correcto.split('\n'):
                        new_source.append(html_line + '\n')
                elif in_string and '"""' in line and 'FORMULARIO_CONTACTO_HTML' not in line:
                    # Fin de la cadena
                    new_source.append('"""\n')
                    in_string = False
                elif not in_string:
                    new_source.append(line)
            
            # Si no encontramos el patrón, intentar otro método
            if in_string or not any('FORMULARIO_CONTACTO_HTML' in line for line in new_source):
                # Método alternativo: buscar y reemplazar
                full_text = ''.join(cell['source'])
                
                # Patrón para encontrar el FORMULARIO_CONTACTO_HTML completo
                pattern = r'(FORMULARIO_CONTACTO_HTML = """.*?""")'
                
                # Reemplazar
                replacement = f'FORMULARIO_CONTACTO_HTML = """{formulario_correcto}"""'
                
                new_text = re.sub(pattern, replacement, full_text, flags=re.DOTALL)
                cell['source'] = new_text.splitlines(keepends=True)
            else:
                cell['source'] = new_source
            
            print(f"Celda {i} actualizada")
            break

# Guardar el notebook actualizado
with open('server_1.ipynb', 'w', encoding='utf-8') as f:
    json.dump(notebook, f, ensure_ascii=False, indent=1)

print("✅ Notebook actualizado correctamente")

