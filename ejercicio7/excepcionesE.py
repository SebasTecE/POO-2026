###
## Excepciones personalizadas
# Parte 5: raise + clases de excepción propias

print("=" * 50)
print("PARTE 5: Excepciones personalizadas")
print("=" * 50)

# --- Definición de excepciones personalizadas ---

class EdadInvalidaError(Exception):
    def __init__(self, edad):
        super().__init__(f"Edad inválida: {edad}. Debe estar entre 0 y 120.")
        self.edad = edad

class SaldoInsuficienteError(Exception):
    def __init__(self, saldo, monto):
        super().__init__(f"Saldo insuficiente. Tienes ${saldo}, necesitas ${monto}.")
        self.saldo = saldo
        self.monto = monto

# --- Funciones que usan raise ---

def registrar_edad(edad):
    if not (0 <= edad <= 120):
        raise EdadInvalidaError(edad)
    return f"Edad {edad} registrada correctamente."

def retirar(saldo, monto):
    if monto > saldo:
        raise SaldoInsuficienteError(saldo, monto)
    return saldo - monto

# --- Programa principal ---

# Prueba 1: edad
try:
    edad = int(input("Ingresa tu edad: "))
    print(registrar_edad(edad))
except ValueError:
    print("❌ ValueError: La edad debe ser un número entero.")
except EdadInvalidaError as e:
    print(f"❌ {e}")

print("-" * 50)

# Prueba 2: retiro bancario
try:
    saldo = float(input("Saldo disponible: $"))
    monto = float(input("Monto a retirar:  $"))
    nuevo_saldo = retirar(saldo, monto)
    print(f"✅ Retiro exitoso. Nuevo saldo: ${nuevo_saldo:.2f}")
except ValueError:
    print("❌ ValueError: Ingresa solo números.")
except SaldoInsuficienteError as e:
    print(f"❌ {e}")
    print(f"   Faltan ${e.monto - e.saldo:.2f} para completar el retiro.")