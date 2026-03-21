#Excepciones basicas

#Parte 1: try / except simple
print("=" * 50)
print("PARTE 1: Division con manejo de errores")
print("=" * 50)

try:
    a = int(input("Ingresa uel numerador: "))
    b = int(input("Ingresar el denominador: "))
    total = a / b

except ValueError:
    print("Ingresar un numero entero no una letra")

except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")

else:
    print(f"El resultado de {a} / {b} es: {total}")