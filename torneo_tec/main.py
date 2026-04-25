from Competidor import Competidor
from Observador import Observador

# --- Competidor ---
carlos = Competidor("Carlos Méndez", "21100123", "avanzado", "Team Overflow")
print("--- Competidor ---")
carlos.mostrar_perfil()
carlos.ganar_puntos(50)
carlos.perder_puntos(20)

print()

# --- Observador ---
ana = Observador("Ana Torres", "21100456", "principiante")
ana.ver_partida()
ana.ver_partida()
print("--- Observador ---")
ana.mostrar_perfil()