###
## Excepciones básicas | Función con bucle de validación
# Parte 3: pedir_entero() + calculadora simple

print("=" * 50)
print("PARTE 3: Calculadora con validación de entrada")
print("=" * 50)

def pedir_entero(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("  ⚠️  Solo se aceptan números enteros. Intenta de nuevo.\n")

# Uso de la función
a = pedir_entero("Primer número: ")
b = pedir_entero("Segundo número: ")

print(f"\nSuma:           {a + b}")
print(f"Resta:          {a - b}")
print(f"Multiplicación: {a * b}")

if b != 0:
    print(f"División:       {a / b:.2f}")
else:
    print("División:       no definida (b = 0)")

print("=" * 50)