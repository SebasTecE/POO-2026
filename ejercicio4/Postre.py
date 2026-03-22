from Platillo import Platillo

class Postre(Platillo):
    def __init__(self, nombre, precio, es_con_gluten):
        super().__init__(nombre, precio)
        self.es_con_gluten = es_con_gluten

    def mostrarInformacion(self):
        super().mostrarInformacion()
        print(f"Contiene gluten: {self.es_con_gluten}")

    def tipo(self):
        if self.es_con_gluten:
            return "Postre con gluten"
        else:
            return "Postre sin gluten"