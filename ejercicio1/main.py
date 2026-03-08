from Comida import Comida
from Bebida import Bebida
from Postre import Postre

comida = Comida("Tacos al pastor", 85.0, "Principal")
bebida = Bebida("Limonada", 35.0, "Fría")
postre = Postre("Flan", 45.0, False)

comida.mostrar_info()
comida.tipo()
print("---")
bebida.mostrar_info()
bebida.tipo()
print("---")
postre.mostrar_info()
postre.tipo()
