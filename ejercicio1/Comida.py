from Platillo import Platillo

class Comida(Platillo):
    def __init__(self, nombre, precio, categoria):
        super().__init__(nombre, precio)
        self.categoria = categoria

    def tipo(self):
        print(f"Tipo: Comida — {self.categoria}")
