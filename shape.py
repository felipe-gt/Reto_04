class Punto:
    def __init__(self, coord_x=0, coord_y=0):
        self._coord_x = coord_x
        self._coord_y = coord_y

    def definir_x(self, x):
        self._coord_x = x

    def definir_y(self, y):
        self._coord_y = y

    def obtener_x(self):
        return self._coord_x

    def obtener_y(self):
        return self._coord_y

    def calcular_distancia(self, otro_punto: "Punto"):
        return ((otro_punto._coord_x - self._coord_x) ** 2 + (otro_punto._coord_y - self._coord_y) ** 2) ** 0.5

    def __repr__(self):
        return f"Punto(x={self.obtener_x()}, y={self.obtener_y()})"


class Segmento:
    def __init__(self, inicio: Punto, fin: Punto):
        self._inicio = inicio
        self._fin = fin
        self._longitud = self._inicio.calcular_distancia(self._fin)

    def obtener_inicio(self):
        return self._inicio

    def obtener_fin(self):
        return self._fin

    def obtener_longitud(self):
        return self._longitud

    def definir_inicio(self, nuevo_inicio):
        self._inicio = nuevo_inicio

    def definir_fin(self, nuevo_fin):
        self._fin = nuevo_fin

    def __repr__(self):
        return f"Segmento(inicio={self.obtener_inicio()}, fin={self.obtener_fin()})"


class Figura:
    def __init__(self, puntos: list):
        self._puntos = puntos
        self._bordes = self.calcular_bordes()
        self._longitudes_bordes = [borde.obtener_longitud() for borde in self._bordes]
        self._regularidad = self.verificar_regularidad()

    def calcular_bordes(self):
        bordes = []
        for i in range(len(self._puntos)):
            bordes.append(Segmento(self._puntos[i], self._puntos[(i + 1) % len(self._puntos)]))
        return bordes

    def verificar_regularidad(self):
        return all(longitud == self._longitudes_bordes[0] for longitud in self._longitudes_bordes)

    def calcular_area(self):
        pass

    def calcular_perimetro(self):
        return sum(self._longitudes_bordes)

    def __repr__(self):
        return f"Figura(puntos={self._puntos})"


class Rectangulo(Figura):
    def __init__(self, esquina: Punto, ancho, alto):
        puntos = [
            esquina,
            Punto(esquina.obtener_x() + ancho, esquina.obtener_y()),
            Punto(esquina.obtener_x() + ancho, esquina.obtener_y() + alto),
            Punto(esquina.obtener_x(), esquina.obtener_y() + alto),
        ]
        super().__init__(puntos)

    def calcular_area(self):
        return self._longitudes_bordes[0] * self._longitudes_bordes[1]


class Triangulo(Figura):
    def __init__(self, vertice1: Punto, vertice2: Punto, vertice3: Punto):
        super().__init__([vertice1, vertice2, vertice3])

    def calcular_area(self):
        a, b, c = self._longitudes_bordes
        s = sum(self._longitudes_bordes) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5


class Cuadrado(Rectangulo):
    def __init__(self, esquina: Punto, lado):
        super().__init__(esquina, lado, lado)

    def calcular_area(self):
        return self._longitudes_bordes[0] ** 2


# Pruebas
print("PRUEBA DE FIGURAS")
punto_a = Punto(1, 1)
punto_b = Punto(6, 1)
punto_c = Punto(6, 4)
punto_d = Punto(1, 4)

rectangulo = Rectangulo(punto_a, 5, 3)
print(f"Área del rectángulo: {rectangulo.calcular_area()}")
print(f"Perímetro del rectángulo: {rectangulo.calcular_perimetro()}")

triangulo = Triangulo(punto_a, punto_b, Punto(3.5, 6))
print(f"Área del triángulo: {triangulo.calcular_area()}")
print(f"Perímetro del triángulo: {triangulo.calcular_perimetro()}")

cuadrado = Cuadrado(Punto(0, 0), 4)
print(f"Área del cuadrado: {cuadrado.calcular_area()}")
print(f"Perímetro del cuadrado: {cuadrado.calcular_perimetro()}")