###
## Excepciones básicas | Manejo de archivos
# Parte 4: Lectura de archivo .txt con manejo de errores

print("=" * 50)
print("PARTE 4: Lectura de archivo .txt")
print("=" * 50)

nombre = input("Nombre del archivo (.txt): ")

try:
    with open(nombre, "r", encoding="utf-8") as f:
        contenido = f.read()
    print("\n--- Contenido ---")
    print(contenido)

except FileNotFoundError:
    print(f"❌ FileNotFoundError: El archivo '{nombre}' no existe.")

except PermissionError:
    print(f"❌ PermissionError: No tienes permisos para leer '{nombre}'.")

except Exception as e:
    print(f"❌ Error inesperado: {e}")

finally:
    print("\n✅ Intento de lectura concluido.")