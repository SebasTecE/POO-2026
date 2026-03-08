from Aventurero import Aventurero

class Mago(Aventurero):
    def __init__(self, nombre, nivel, hechizo):
        super().__init__(nombre, nivel)
        self.hechizo = hechizo

    def usar_habilidad(self):
        print(f"{self.nombre} lanza {self.hechizo}! 🔮")
