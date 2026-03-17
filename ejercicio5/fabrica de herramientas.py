from abc import ABC, abstractmethod

DAÑO_MATERIAL = {
    "madera"    : 2,
    "piedra"    : 3,
    "hierro"    : 4,
    "oro"       : 3,
    "diamante"  : 6,
    "netherita" : 8,
}


class Herramienta(ABC):

    def __init__(self, material: str, durabilidad: int):
        self._material       = material.lower()
        self._durabilidad    = durabilidad
        self._usos_restantes = durabilidad

    @property
    @abstractmethod
    def nombre(self) -> str:
        """Nombre de la herramienta (ej. 'Pico')."""
        pass

    @abstractmethod
    def usar(self, objetivo: str) -> str:
        """Describe la acción sobre el objetivo."""
        pass

    def calcular_daño(self) -> int:
        return DAÑO_MATERIAL.get(self._material, 1)

    def desgastar(self):
        if self._usos_restantes > 0:
            self._usos_restantes -= 1

    @property
    def rota(self) -> bool:
        return self._usos_restantes == 0

    def estado(self):
        txt = "💔 ROTA" if self.rota else f"✅ {self._usos_restantes} usos"
        print(f"[{self.nombre} de {self._material}] {txt}")


class Pico(Herramienta):

    @property
    def nombre(self) -> str:
        return "Pico"

    def usar(self, objetivo: str) -> str:
        daño = self.calcular_daño()
        self.desgastar()
        return f"Pico de {self._material} mina {objetivo} (daño: {daño})"


class Espada(Herramienta):

    @property
    def nombre(self) -> str:
        return "Espada"

    def usar(self, objetivo: str) -> str:
        daño = self.calcular_daño()
        self.desgastar()
        return f"Espada de {self._material} ataca a {objetivo} (daño: {daño})"


class Pala(Herramienta):

    @property
    def nombre(self) -> str:
        return "Pala"

    def usar(self, objetivo: str) -> str:
        daño = self.calcular_daño()
        self.desgastar()
        return f"Pala de {self._material} excava {objetivo} (daño: {daño})"


class Arco(Herramienta):

    def __init__(self, material: str, durabilidad: int, flechas: int):
        super().__init__(material, durabilidad)
        self._flechas = flechas

    @property
    def nombre(self) -> str:
        return "Arco"

    def usar(self, objetivo: str) -> str:
        if self._flechas == 0:
            return "Sin flechas"
        daño = self.calcular_daño()
        self.desgastar()
        self._flechas -= 1
        return (f"Arco de {self._material} dispara a {objetivo} "
                f"(daño: {daño}) | Flechas restantes: {self._flechas}")


if __name__ == "__main__":
    herramientas = [
        Pico("diamante", 5),
        Espada("hierro", 3),
        Pala("madera", 2),
    ]
    objetivos = ["mena de diamante", "Creeper", "arena"]

    # Uso básico
    for h, obj in zip(herramientas, objetivos):
        print(h.usar(obj))
        h.estado()
        print()

    print("--- Desgaste completo del Pico de piedra ---")
    pico_test = Pico("piedra", 4)
    while not pico_test.rota:
        print(pico_test.usar("bloque de roca"))
        pico_test.estado()
    print("¡El pico se ha roto!\n")

    # Bonus: Arco con flechas
    print("--- Prueba del Arco ---")
    arco = Arco("madera", 10, 2)
    for _ in range(3):  # intenta disparar 3 veces con solo 2 flechas
        print(arco.usar("Esqueleto"))
        arco.estado()