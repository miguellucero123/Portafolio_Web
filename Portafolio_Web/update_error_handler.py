#!/usr/bin/env python3
"""Actualiza el manejo de errores para cierre automático"""

import json
import re

# Leer notebook
with open('server_1.ipynb', 'r', encoding='utf-8') as f:
    notebook = json.load(f)

# Celda 9 tiene start_server
cell = notebook['cells'][9]
lines = cell['source']

# Buscar el bloque except OSError
new_lines = []
i = 0
found_except = False

while i < len(lines):
    line = lines[i]
    
    # Detectar inicio del except OSError
    if 'except OSError as e:' in line:
        found_except = True
        new_lines.append(line)
        i += 1
        
        # Buscar y reemplazar el if
        if i < len(lines) and 'if e.errno == 48' in lines[i]:
            # Reemplazar todo el bloque hasta return None
            new_lines.append('        if e.errno == 48 or e.errno == 98 or e.errno == 10048:  # Puerto en uso (WinError 10048)\n')
            i += 1
            
            # Saltar líneas antiguas hasta encontrar return None
            while i < len(lines) and 'return None' not in lines[i]:
                i += 1
            
            # Agregar nuevo código
            new_code = '''            print(f"\\n{'='*70}")
            print(f"⚠️  ADVERTENCIA: El puerto {PORT} ya está en uso")
            print(f"{'='*70}")
            print(f"\\n🔄 Cerrando proceso automáticamente...")
            
            # Intentar cerrar el proceso automáticamente
            if kill_port_process(PORT):
                print(f"\\n✅ Proceso cerrado. Reintentando iniciar servidor...")
                # Esperar un momento para que el puerto se libere
                import time
                time.sleep(1.5)
                
                # Intentar iniciar el servidor nuevamente
                try:
                    _httpd = socketserver.TCPServer(("", PORT), MetGoHandler)
                    _httpd.allow_reuse_address = True
                    
                    def run_server():
                        try:
                            _httpd.serve_forever()
                        except Exception as e:
                            print(f"❌ Error en el servidor: {e}")
                    
                    _server_thread = threading.Thread(target=run_server, daemon=True)
                    _server_thread.start()
                    
                    print(f"\\n{'='*70}")
                    print(f"✅ SERVIDOR PROFESIONAL ACTIVO")
                    print(f"{'='*70}")
                    print(f"\\n🌐 Accede a tu portfolio profesional en:")
                    print(f"   📍 http://localhost:{PORT}")
                    print(f"   📍 http://127.0.0.1:{PORT}")
                    print(f"\\n📄 Páginas disponibles:")
                    print(f"   🏢 Inicio:     http://localhost:{PORT}/index.html")
                    print(f"   📋 CV:         http://localhost:{PORT}/cv.html")
                    print(f"   📊 Dashboard:  http://localhost:{PORT}/dashboard_marca_personal.html")
                    print(f"\\n⏹️  El servidor está corriendo en segundo plano")
                    print(f"   Para detenerlo, ejecuta: stop_server()")
                    print(f"{'='*70}\\n")
                    
                    return _httpd
                except OSError as retry_error:
                    print(f"\\n❌ Error al reintentar iniciar servidor: {retry_error}")
                    print(f"   Por favor, espera unos segundos y ejecuta start_server() nuevamente")
                    return None
            else:
                print(f"\\n⚠️  No se pudo cerrar el proceso automáticamente.")
                print(f"   Por favor, ejecuta manualmente: stop_server()")
                print(f"   O cierra el proceso manualmente desde el Administrador de tareas")
                return None
'''
            new_lines.extend(new_code.splitlines(keepends=True))
            i += 1  # Saltar el return None antiguo
            continue
    elif found_except and 'return None' in line and 'if e.errno' not in ''.join(new_lines[-10:]):
        # Ya agregamos nuestro código, saltar este return None
        i += 1
        continue
    else:
        new_lines.append(line)
        i += 1

# Actualizar celda
cell['source'] = new_lines

# También agregar allow_reuse_address
cell_source = ''.join(new_lines)
if '_httpd = socketserver.TCPServer' in cell_source and 'allow_reuse_address' not in cell_source:
    cell_source = cell_source.replace(
        '_httpd = socketserver.TCPServer(("", PORT), MetGoHandler)',
        '_httpd = socketserver.TCPServer(("", PORT), MetGoHandler)\n        _httpd.allow_reuse_address = True  # Permitir reutilizar el puerto'
    )
    cell['source'] = cell_source.splitlines(keepends=True)

# Guardar
with open('server_1.ipynb', 'w', encoding='utf-8') as f:
    json.dump(notebook, f, ensure_ascii=False, indent=1)

print("OK: Código actualizado correctamente")

