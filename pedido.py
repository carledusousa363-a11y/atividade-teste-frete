from abc import ABC, abstractmethod

class EstrategiaFrete(ABC):
    @abstractmethod
    def calcular(self, pedido) -> float:
        pass

class FreteSedex(EstrategiaFrete):
    def calcular(self, pedido) -> float:
        return 10.0 + (pedido.peso_kg * 1.5)

class FretePac(EstrategiaFrete):
    def calcular(self, pedido) -> float:
        return 5.0 + (pedido.peso_kg * 1.0)

class FreteTransportadora(EstrategiaFrete):
    def calcular(self, pedido) -> float:
        return 20.0 + (pedido.peso_kg * 3.0)

class FreteMotoboy(EstrategiaFrete):
    def calcular(self, pedido) -> float:
        return 15.0

class FreteDrone(EstrategiaFrete):
    def calcular(self, pedido) -> float:
        return 25.0

class Pedido:
    def __init__(self, peso_kg: float):
        self._peso_kg = peso_kg
        self.estrategia: EstrategiaFrete = None

    def set_estrategia(self, estrategia: EstrategiaFrete):
        self.estrategia = estrategia

    def calcular_frete(self) -> float:
        if not self.estrategia:
            raise ValueError("Estratégia não definida.")
        return self.estrategia.calcular(self)

    @property
    def peso_kg(self) -> float:
        return self._peso_kg