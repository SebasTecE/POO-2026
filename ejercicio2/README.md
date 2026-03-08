# Ejercicio 2 — La Taberna de los Aventureros

Práctica de herencia en Python con un sistema de registro de aventureros de fantasía.

## Archivos

| Archivo | Descripción |
|--------|-------------|
| `Aventurero.py` | Clase base con nombre y nivel |
| `Guerrero.py` | Hereda de Aventurero, usa arma |
| `Mago.py` | Hereda de Aventurero, lanza hechizos |
| `Arquero.py` | Hereda de Aventurero, tiene flechas |
| `main.py` | Programa principal con los objetos |

## Ejemplo de salida

Soy Thorin, aventurero de nivel 8
Thorin ataca con su Hacha!
---
Soy Gandalf, aventurero de nivel 15
Gandalf lanza Bola de fuego!
---
Soy Legolas, aventurero de nivel 10
Legolas dispara una flecha! Le quedan 29.

## Conceptos usados
- Clases y objetos
- Herencia
- Sobreescritura de métodos (`usar_habilidad()`)
- `self.flechas -= 1` para modificar atributos
