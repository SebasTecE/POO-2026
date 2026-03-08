class Aventurero:
    def __init__(self, nombre, nivel):
        self.nombre = nombre
        self.nivel = nivel

    def presentarse(self):
        print(f"Soy {self.nombre}, aventurero de nivel {self.nivel}")

    def usar_habilidad(self):
        print("Habilidad desconocida...")
