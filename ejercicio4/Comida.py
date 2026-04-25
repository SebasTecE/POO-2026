from Platillo import Platillo

class Comida(Platillo):
    def __init__(self, nombre, precio, categoria):
        super().__init__(nombre, precio)
        self.categoria = categoria

    def mostrarInformacion(self):
        super().mostrarInformacion()
        print(f"Categoría: {self.categoria}")