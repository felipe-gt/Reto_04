class MenuItem:
    def __init__(self, nombre, precio):
        self._nombre = nombre
        self._precio = precio

    def obtener_nombre(self):
        return self._nombre

    def obtener_precio(self):
        return self._precio

    def establecer_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    def establecer_precio(self, nuevo_precio):
        self._precio = nuevo_precio

    def calcular_total(self, cantidad=1):
        return self.obtener_precio() * cantidad


class Bebida(MenuItem):
    def __init__(self, nombre, precio, volumen_ml, recipiente):
        super().__init__(nombre, precio)
        self._volumen_ml = volumen_ml
        self._recipiente = recipiente

    def obtener_volumen(self):
        return self._volumen_ml

    def obtener_recipiente(self):
        return self._recipiente

    def establecer_volumen(self, nuevo_volumen):
        self._volumen_ml = nuevo_volumen

    def establecer_recipiente(self, nuevo_recipiente):
        self._recipiente = nuevo_recipiente

    def __str__(self):
        return f"{self.obtener_nombre()} ({self.obtener_volumen()}ml, {self.obtener_recipiente()}): ${self.obtener_precio():.2f}"


class Entrada(MenuItem):
    def __init__(self, nombre, precio, tamaño_porcion, con_salsas):
        super().__init__(nombre, precio)
        self._tamaño_porcion = tamaño_porcion
        self._con_salsas = con_salsas

    def obtener_tamaño_porcion(self):
        return self._tamaño_porcion

    def tiene_salsas(self):
        return self._con_salsas

    def establecer_tamaño_porcion(self, nuevo_tamaño):
        self._tamaño_porcion = nuevo_tamaño

    def establecer_salsas(self, tiene_salsas):
        self._con_salsas = tiene_salsas

    def __str__(self):
        return f"{self.obtener_nombre()} ({self.obtener_tamaño_porcion()}): ${self.obtener_precio():.2f}"


class PlatoFuerte(MenuItem):
    def __init__(self, nombre, precio, tamaño, es_picante, incluye_salsas):
        super().__init__(nombre, precio)
        self._tamaño = tamaño
        self._es_picante = es_picante
        self._incluye_salsas = incluye_salsas

    def obtener_tamaño(self):
        return self._tamaño

    def es_picante(self):
        return self._es_picante

    def tiene_salsas(self):
        return self._incluye_salsas

    def establecer_tamaño(self, nuevo_tamaño):
        self._tamaño = nuevo_tamaño

    def establecer_picante(self, es_picante):
        self._es_picante = es_picante

    def establecer_salsas(self, tiene_salsas):
        self._incluye_salsas = tiene_salsas

    def __str__(self):
        return f"{self.obtener_nombre()} ({self.obtener_tamaño()}): ${self.obtener_precio():.2f}"


class Pedido:
    def __init__(self):
        self._items = []
        self.total = 0

    def agregar_item(self, item, cantidad=1):
        self._items.append((item, cantidad))

    def calcular_total(self):
        self.total += sum(item.calcular_total(cantidad) for item, cantidad in self._items)
        return self.total

    def aplicar_descuento_bebidas(self):
        descuento = 0
        total_bebidas = 0
        for item, _ in self._items:
            if isinstance(item, Bebida):
                total_bebidas += item.obtener_precio()
        if any(isinstance(item, PlatoFuerte) for item, _ in self._items):
            descuento = total_bebidas * 0.20
        return descuento

    def __str__(self):
        descuento = self.aplicar_descuento_bebidas()
        total_final = self.total - descuento
        return (f"Total del pedido: ${self.total:.2f}\n"
                f"Descuento en bebidas: ${descuento:.2f}\n"
                f"Total final: ${total_final:.2f}")


class Pago:
    def pagar(self, pedido):
        raise NotImplementedError("Este método debe ser implementado por las subclases.")


class PagoTarjeta(Pago):
    def __init__(self, numero_tarjeta, cvv):
        self.numero_tarjeta = numero_tarjeta
        self.cvv = cvv

    def pagar(self, pedido):
        print(f"Procesando pago de ${pedido.total:.2f} con tarjeta {self.numero_tarjeta[-4:]}")


class PagoEfectivo(Pago):
    def __init__(self, monto_entregado):
        self.monto_entregado = monto_entregado

    def pagar(self, pedido):
        cambio = self.monto_entregado - pedido.total
        if cambio >= 0:
            print(f"Pago en efectivo completado. Cambio: ${cambio:.2f}")
        else:
            print(f"Fondos insuficientes. Faltan: ${-cambio:.2f}")


# Ejemplo de uso
bebida = Bebida("Jugo de Naranja", 3.5, 300, "Vaso")
entrada = Entrada("Tacos", 5.0, "Mediano", True)
plato_fuerte = PlatoFuerte("Hamburguesa", 12.0, "Grande", False, True)

pedido = Pedido()
pedido.agregar_item(bebida, 2)
pedido.agregar_item(entrada)
pedido.agregar_item(plato_fuerte)
pedido.calcular_total()

print(pedido)

pago = PagoEfectivo(25.0)
pago.pagar(pedido)