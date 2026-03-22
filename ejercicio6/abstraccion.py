from abc import ABC, abstractmethod

# Clase abstracta (plantilla)
class Animal(ABC):

  @abstractmethod
  def hablar(self):
    pass # No se implementa el método

# Clase en específico
class Perro(Animal):

  def hablar(self):
    return "Guau!"

# Clase en específico
class Gato(Animal):

  def hablar(self):
    return "Miau!"

# usar las clases
perro = Perro()
gato = Gato()
print(perro.hablar()) # Guau!
print(gato.hablar()) # Miau!