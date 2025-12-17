import sqlite3
import os
import time

db_path = 'gestion_productividad.db'  # Ajusta si es diferente

print("=== DIAGNÓSTICO BASE DE DATOS ===")
print(f"Archivo: {db_path}")
print(f"Existe: {os.path.exists(db_path)}")

if os.path.exists(db_path):
    print(f"Tamaño: {os.path.getsize(db_path)} bytes")
    print(f"Permisos: {oct(os.stat(db_path).st_mode)[-3:]}")
    print(f"Dueño: {os.stat(db_path).st_uid}")
    
    # Intentar con diferentes timeouts
    for timeout in [5, 10, 30]:
        print(f"\nIntentando conexión con timeout={timeout}s...")
        try:
            conn = sqlite3.connect(db_path, timeout=timeout)
            cursor = conn.cursor()
            
            # Ver tablas
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()
            print(f"Tablas: {[t[0] for t in tables] if tables else 'No hay tablas'}")
            
            # Ver transacciones pendientes
            cursor.execute("SELECT * FROM sqlite_master;")
            conn.commit()
            conn.close()
            print("✓ Conexión exitosa y cerrada")
            break
        except sqlite3.OperationalError as e:
            print(f"✗ Error: {e}")
            time.sleep(2)
else:
    print("El archivo de base de datos no existe en esta ubicación")