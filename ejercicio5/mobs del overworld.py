from abc import ABC, abstractmethod

class Mob(ABC):


    def __init__(self, nombre: str, vida: int):
        self.nombre = nombre
        self.vida   = vida


    @abstractmethod
    def hacer_sonido(self) -> str:
        pass

    @abstractmethod
    def comportamiento(self) -> str:
        pass

    @abstractmethod
    def moverse(self) -> str:
        pass


    def presentarse(self):
        print(f"=== {self.nombre} ===")
        print(f"  Vida       : {self.vida} HP")
        print(f"  Sonido     : {self.hacer_sonido()}")
        print(f"  Tipo       : {self.comportamiento()}")
        print(f"  Movimiento : {self.moverse()}")
        print()

