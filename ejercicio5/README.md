# Ejercicio 5 — Abstracción en POO con Python

Práctica 3 sobre clases abstractas en Python usando el universo Minecraft.

## Archivos

| Archivo | Descripción |
|--------|-------------|
| `mobs del overworld.py` | Clase abstracta `Mob` y subclases `Vaca`, `Creeper`, `Enderman`, `Zombie` |
| `fabrica de herramientas.py` | Clase abstracta `Herramienta` y subclases `Pico`, `Espada`, `Pala`, `Arco` |

## Ejemplo de salida
```
=== Bessie ===
❤️  Vida       : 10 HP
🔊  Sonido     : Muuuu
⚔️  Tipo       : pasivo
🏃  Movimiento : Camina lentamente por el prado

Pico de diamante mina mena de diamante (daño: 6)
[Pico de diamante] ✅ 4 usos
```

## Conceptos usados

- Clases abstractas (`ABC`, `abstractmethod`)
- Herencia y polimorfismo
- Propiedades abstractas (`@property`)
- Métodos concretos reutilizables