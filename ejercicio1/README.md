# Ejercicio 1 — El Menú del Restaurante

Práctica de herencia en Python usando un sistema de menú para un restaurante.

## Archivos

| Archivo | Descripción |
|--------|-------------|
| `Platillo.py` | Clase base con nombre y precio |
| `Comida.py` | Hereda de Platillo, agrega categoría |
| `Bebida.py` | Hereda de Platillo, agrega temperatura |
| `Postre.py` | Hereda de Platillo, indica si es sin gluten |
| `main.py` | Programa principal con los objetos |

## Ejemplo de salida

Tacos al pastor — $85.0
Tipo: Comida — Principal
---
Limonada — $35.0
Tipo: Bebida — Fría
---
Flan — $45.0
Tipo: Postre — Sin gluten: No

## Conceptos usados
- Clases y objetos
- Herencia
- Sobreescritura de métodos (`tipo()`)
- `super().__init__()`
