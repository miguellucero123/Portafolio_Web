# Solución: Puerto 8081 ya está en uso

## 🚨 Error
```
[WinError 10048] Solo se permite un uso de cada dirección de socket (protocolo/dirección de red/puerto)
```

## ✅ Soluciones Rápidas

### **Opción 1: Detener servidor anterior (Más fácil)**
En una celda nueva del notebook, ejecuta:
```python
stop_server()
```

Luego ejecuta nuevamente:
```python
start_server()
```

### **Opción 2: Cerrar proceso manualmente (Windows)**

1. **Abrir PowerShell como Administrador**

2. **Encontrar el proceso que usa el puerto 8081:**
```powershell
netstat -ano | findstr :8081
```

Esto mostrará algo como:
```
TCP    0.0.0.0:8081           0.0.0.0:0              LISTENING       15260
```

El último número (15260) es el **PID** del proceso.

3. **Cerrar el proceso:**
```powershell
taskkill /PID 15260 /F
```
(Reemplaza 15260 con el PID que obtuviste)

### **Opción 3: Cambiar el puerto**

En la celda de configuración, cambia:
```python
PORT = int(os.environ.get('PORT', 8081))  # Cambia 8081 a otro número
```

Por ejemplo:
```python
PORT = int(os.environ.get('PORT', 8082))  # Usa puerto 8082
```

Luego ejecuta nuevamente `start_server()`

## 🔍 Verificar qué proceso está usando el puerto

### Windows PowerShell:
```powershell
Get-NetTCPConnection -LocalPort 8081 | Select-Object -Property LocalAddress, LocalPort, State, OwningProcess
```

### Windows CMD:
```cmd
netstat -ano | findstr :8081
```

## 💡 Prevención Futura

El código ahora incluye `allow_reuse_address = True` para permitir reutilizar el puerto. Sin embargo, si el proceso anterior no se cerró correctamente, aún puede dar este error.

**Siempre ejecuta `stop_server()` antes de iniciar un nuevo servidor.**

