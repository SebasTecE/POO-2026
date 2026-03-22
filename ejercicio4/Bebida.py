#Este ejercicio es una continuación del ejercicio anterior, donde se creó la clase Platillo. En este caso, se creará una clase Bebida que herede de Platillo y tenga un atributo adicional llamado temperatura. Además, se implementará un método tipo() que determine si la bebida es fría o caliente según el valor de temperatura, y un método mostrarInformacion() que muestre toda la información de la bebida, incluyendo su tipo.
from Platillo import Platillo

class Bebida(Platillo):
    def __init__(self, nombre, precio, temperatura):
        super().__init__(nombre, precio)
        self.temperatura = temperatura

    def tipo(self):
        if self.temperatura.lower() == "fría":
            return "Bebida fría"
        elif self.temperatura.lower() == "caliente":
            return "Bebida caliente"
        else:
            return "Tipo desconocido"

    def mostrarInformacion(self):
        super().mostrarInformacion()
        print(f"Tipo: {self.tipo}")