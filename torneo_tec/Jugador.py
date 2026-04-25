class Jugador:
    def __init__(self, nombre, num_control, nivel):
        self.nombre = nombre
        self.num_control = num_control
        self.nivel = nivel
        self.puntos = 0

    def ganar_puntos(self, cantidad):
        self.puntos += cantidad
        print(f"{self.nombre} ganó {cantidad} puntos. Total: {self.puntos}")

    def perder_puntos(self, cantidad):
        if self.puntos - cantidad < 0:
            self.puntos = 0
        else:
            self.puntos -= cantidad
        print(f"{self.nombre} perdió {cantidad} puntos. Total: {self.puntos}")

    def mostrar_perfil(self):
        print(f"Nombre: {self.nombre}")
        print(f"No. Control: {self.num_control}")
        print(f"Nivel: {self.nivel}")
        print(f"Puntos: {self.puntos}")