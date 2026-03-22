class Platillo:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrarInformacion(self):
        print(f"Platillo: {self.nombre}, Precio: ${self.precio:.2f}")


    def tipo(self):
        return "Platillo"