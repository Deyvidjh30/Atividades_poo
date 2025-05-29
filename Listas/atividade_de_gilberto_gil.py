
import math

class Retangulo:
    def __init__(self, b: float, h: float):
        self.b = b if b > 0 else 1
        self.h = h if h > 0 else 1

    def SetBase(self, b: float):
        if b > 0:
            self.b = b

    def SetAltura(self, h: float):
        if h > 0:
            self.h = h

    def GetBase(self) -> float:
        return self.b

    def GetAltura(self) -> float:
        return self.h

    def CalcArea(self) -> float:
        return self.b * self.h

    def CalcDiagonal(self) -> float:
        return math.sqrt(self.b ** 2 + self.h ** 2)

    def ToString(self) -> str:
        return f'Retângulo(Base: {self.b}, Altura: {self.h})'

class Frete:
    def __init__(self, distancia: float, peso: float):
        self.distancia = distancia if distancia > 0 else 1
        self.peso = peso if peso > 0 else 1

    def SetDistancia(self, d: float):
        if d > 0:
            self.distancia = d

    def SetPeso(self, p: float):
        if p > 0:
            self.peso = p

    def GetDistancia(self) -> float:
        return self.distancia

    def GetPeso(self) -> float:
        return self.peso

    def CalcFrete(self) -> float:
        return self.peso * self.distancia * 0.01  # 1 centavo por kg/km

    def ToString(self) -> str:
        return f'Frete(Distância: {self.distancia} km, Peso: {self.peso} kg)'

import math

class EquacaoSegundoGrau:
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

    def SetA(self, a: float):
        self.a = a

    def SetB(self, b: float):
        self.b = b

    def SetC(self, c: float):
        self.c = c

    def GetA(self) -> float:
        return self.a

    def GetB(self) -> float:
        return self.b

    def GetC(self) -> float:
        return self.c

    def Delta(self) -> float:
        return self.b ** 2 - 4 * self.a * self.c

    def TemRaizesReais(self) -> bool:
        return self.Delta() >= 0

    def Raiz1(self) -> float:
        if self.TemRaizesReais():
            return (-self.b + math.sqrt(self.Delta())) / (2 * self.a)
        else:
            return None

    def Raiz2(self) -> float:
        if self.TemRaizesReais():
            return (-self.b - math.sqrt(self.Delta())) / (2 * self.a)
        else:
            return None
