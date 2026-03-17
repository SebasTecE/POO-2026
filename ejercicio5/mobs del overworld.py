from abc import ABC, abstractmethod

class Mob(ABC):

    def __init__(self, nombre: str, vida: int):
        self.nombre = nombre
        self.vida   = vida

    @abstractmethod
    def hacer_sonido(self) -> str:
        """Retorna el sonido característico del mob."""
        pass

    @abstractmethod
    def comportamiento(self) -> str:
        """Retorna 'pasivo' o 'agresivo'."""
        pass

    @abstractmethod
    def moverse(self) -> str:
        """Describe cómo se mueve el mob."""
        pass

    def presentarse(self):
        print(f"=== {self.nombre} ===")
        print(f"  Vida       : {self.vida} HP")
        print(f"  Sonido     : {self.hacer_sonido()}")
        print(f"  Tipo       : {self.comportamiento()}")
        print(f"  Movimiento : {self.moverse()}")
        print()


class Vaca(Mob):

    def hacer_sonido(self) -> str:
        return "Muuuu"

    def comportamiento(self) -> str:
        return "pasivo"

    def moverse(self) -> str:
        return "Camina lentamente por el prado"


class Creeper(Mob):

    def hacer_sonido(self) -> str:
        return "...Ssssss"

    def comportamiento(self) -> str:
        return "agresivo"

    def moverse(self) -> str:
        return "Corre directamente hacia el jugador"


class Enderman(Mob):

    def hacer_sonido(self) -> str:
        return "~sonido distorsionado~"

    def comportamiento(self) -> str:
        return "neutral"

    def moverse(self) -> str:
        return "Se teletransporta de bloque en bloque"


class Zombie(Mob):

    def hacer_sonido(self) -> str:
        return "Uuuurrgh..."

    def comportamiento(self) -> str:
        return "agresivo"

    def moverse(self) -> str:
        return "Arrastra los pies lentamente hacia el jugador"


# OBSERVACIÓN TAREA 2:
# Al intentar instanciar Mob("test", 10) directamente, Python lanza:
# TypeError: Can't instantiate abstract class Mob with abstract methods
# hacer_sonido, comportamiento, moverse
# Esto ocurre porque Mob hereda de ABC y tiene métodos con @abstractmethod,
# lo que le indica a Python que no puede existir un objeto de esa clase base,
# solo de sus subclases que implementen todos los métodos abstractos.

if __name__ == "__main__":
    mobs = [
        Vaca("Bessie", 10),
        Creeper("Explosi", 20),
        Enderman("Tall Boi", 40),
        Zombie("Braaaains", 20),
    ]
    for mob in mobs:
        mob.presentarse()