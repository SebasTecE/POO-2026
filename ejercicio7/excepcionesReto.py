###
## Reto integrador | Excepciones
# Registro de calificaciones con validación, excepción personalizada y archivo

print("=" * 50)
print("RETO: Registro de calificaciones")
print("=" * 50)

# --- Excepción personalizada ---

class CalificacionFueraDeRangoError(Exception):
    def __init__(self, calificacion):
        super().__init__(f"Calificación fuera de rango: {calificacion}. Debe estar entre 0 y 100.")
        self.calificacion = calificacion

# --- Funciones auxiliares ---

def pedir_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("  ⚠️  Solo se aceptan números enteros. Intenta de nuevo.\n")

def validar_calificacion(cal):
    if not (0 <= cal <= 100):
        raise CalificacionFueraDeRangoError(cal)

# --- Programa principal ---

estudiantes_registrados = 0

nombre_archivo = "calificaciones.txt"

continuar = True
while continuar:
    print()
    nombre = input("Nombre del estudiante (o 'salir' para terminar): ").strip()

    if nombre.lower() == "salir":
        break

    calificacion = pedir_entero("Calificación (0-100): ")

    try:
        validar_calificacion(calificacion)

        try:
            with open(nombre_archivo, "a", encoding="utf-8") as f:
                f.write(f"{nombre}: {calificacion}\n")
            estudiantes_registrados += 1
            print(f"✅ {nombre} registrado con calificación {calificacion}.")

        except FileNotFoundError:
            print(f"❌ FileNotFoundError: No se encontró el archivo '{nombre_archivo}'.")

        except PermissionError:
            print(f"❌ PermissionError: Sin permisos para escribir en '{nombre_archivo}'.")

    except CalificacionFueraDeRangoError as e:
        print(f"❌ {e}")

finally_msg = True  # el finally equivalente al final del programa
print()
print("=" * 50)
print(f"✅ Sesión finalizada. Estudiantes registrados: {estudiantes_registrados}")
print("=" * 50)