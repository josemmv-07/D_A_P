
"""
Diseña una clase Producto con:

Constructor (método __init__), con los atributos: nombre, precio.

Método de instancia aplicar_descuento(porcentaje) que modifique el precio (comprobar que los valores estén comprendidos entre 0 y 100).

Método de clase desde_texto(cls, texto) que cree un producto a partir de una cadena, como por ejemplo: "Camiseta,19.99".

Método estático es_precio_valido(precio) que devuelva True si el precio es mayor que 0.
"""


class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def aplicar_descuento(self, porcentaje):
        if 0 <= porcentaje <= 100:
            descuento = self.precio * (porcentaje / 100)
            self.precio -= descuento
        else:
            print("Error: el porcentaje debe estar entre 0 y 100.")

    @classmethod
    def desde_texto(cls, texto):
        nombre, precio = texto.split(",")
        return cls(nombre.strip(), float(precio.strip()))

    @staticmethod
    def es_precio_valido(precio):
        return precio > 0


if __name__ == "__main__":
    pro = Producto.desde_texto("Camiseta, 19.99")

    print(f"Producto: {pro.nombre}, precio inicial: {pro.precio:.2f}€")

    pro.aplicar_descuento(20)
    print(f"Precio tras descuento: {pro.precio:.2f}€")

    print("¿Precio válido?", Producto.es_precio_valido(pro.precio))


