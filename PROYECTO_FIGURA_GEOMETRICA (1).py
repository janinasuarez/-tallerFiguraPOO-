
class FiguraGeometrica:

    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, valor):
        if valor <= 0:
            raise ValueError("El ancho debe ser mayor que 0")
        self._ancho = valor

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, valor):
        if valor <= 0:
            raise ValueError("El alto debe ser mayor que 0")
        self._alto = valor

    def area(self):
        return self._ancho * self._alto

    def perimetro(self):
        pass

    def __str__(self):
        return f"Ancho: {self._ancho}, Alto: {self._alto}"


# ── Clase Cuadrado ───────────────────────────
class Cuadrado(FiguraGeometrica):

    def __init__(self, lado):
        super().__init__(lado, lado)

    def area(self):
        return self._ancho ** 2

    def perimetro(self):
        return 4 * self._ancho

    def __str__(self):
        return f"Cuadrado | Lado: {self._ancho}"


# ── Clase Rectangulo ─────────────────────────
class Rectangulo(FiguraGeometrica):

    def __init__(self, ancho, alto):
        super().__init__(ancho, alto)

    def area(self):
        return self._ancho * self._alto

    def perimetro(self):
        return 2 * (self._ancho + self._alto)

    def __str__(self):
        return f"Rectangulo | Ancho: {self._ancho}, Alto: {self._alto}"


# ── Funciones ────────────────────────────────
def sumar_areas(figuras):
    total = 0
    for figura in figuras:
        total += figura.area()
    return total


def sumar_perimetros(figuras):
    total = 0
    for figura in figuras:
        total += figura.perimetro()
    return total


# ── Main ─────────────────────────────────────
cuadrado1 = Cuadrado(5)
cuadrado2 = Cuadrado(3)
rectangulo1 = Rectangulo(4, 7)
rectangulo2 = Rectangulo(6, 2)

figuras = [cuadrado1, cuadrado2, rectangulo1, rectangulo2]

print("=" * 40)
print("       FIGURAS GEOMETRICAS")
print("=" * 40)

for figura in figuras:
    print(figura)
    print("  Area:      ", figura.area())
    print("  Perimetro: ", figura.perimetro())
    print()

print("Suma de areas:     ", sumar_areas(figuras))
print("Suma de perimetros:", sumar_perimetros(figuras))

print("\n-- Modificando cuadrado1: lado 5 -> 10 --")
cuadrado1.ancho = 10
cuadrado1.alto = 10
print(cuadrado1)
print("  Nueva area:", cuadrado1.area())

print("\n-- Probando valores invalidos --")
try:
    c_malo = Cuadrado(-5)
except ValueError as e:
    print("Error:", e)

try:
    rectangulo1.ancho = 0
except ValueError as e:
    print("Error:", e)
