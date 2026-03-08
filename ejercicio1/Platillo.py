class Platillo:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar_info(self):
        print(f"{self.nombre} — ${self.precio}")

    def tipo(self):
        print("Tipo de platillo: desconocido")
