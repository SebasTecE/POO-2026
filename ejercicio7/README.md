# ejercicio7 — Excepciones en Python

Práctica progresiva de manejo de errores en Python: desde `try / except` básico hasta excepciones personalizadas con `raise`.

---

## Archivos

### `excepciones.py` — División con manejo de errores
Divide dos números ingresados por el usuario. Captura `ValueError` si se escribe texto y `ZeroDivisionError` si el denominador es cero. Usa los cuatro bloques: `try / except / else / finally`.

### `excepcionesB.py` — Acceso a lista
Muestra una lista de colores y deja elegir uno por índice. Captura `ValueError` e `IndexError` por separado usando `as e` para mostrar el mensaje original del error.

### `excepcionesC.py` — Función `pedir_entero()` + calculadora
Define una función reutilizable que repite la solicitud hasta recibir un entero válido (bucle `while True` + `try/except` interno). La usa para una calculadora de cuatro operaciones.

### `excepcionesD.py` — Lectura de archivo `.txt`
Pide el nombre de un archivo y lo abre con `with open(...)`. Captura `FileNotFoundError`, `PermissionError` y cualquier otro error con `Exception` genérico.

### `excepcionesE.py` — Excepciones personalizadas
Define `EdadInvalidaError` y `SaldoInsuficienteError` heredando de `Exception`, con atributos propios. Las lanza con `raise` dentro de funciones de validación y las captura en el programa principal.

### `excepcionesReto.py` — Reto integrador
Registro de calificaciones en bucle. Combina `pedir_entero()`, la excepción personalizada `CalificacionFueraDeRangoError`, escritura en archivo `.txt` y un contador que muestra al final cuántos estudiantes se registraron en la sesión.

---

## Conceptos vistos

| Concepto | Para qué sirve |
|---|---|
| `try / except / else / finally` | Estructura base del manejo de errores |
| `as e` | Accede al mensaje y atributos de la excepción |
| `raise` | Lanza una excepción manualmente |
| Excepción personalizada | Clase que hereda de `Exception` para errores propios |
| `with open(...)` | Abre y cierra archivos de forma segura |
