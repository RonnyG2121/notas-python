# Trabajando con el diseño de clases
from diseño_de_clases1 import Producto

class Orden:
    contador_orden = 0
    def __init__(self, productos):
        Orden.contador_orden+=1
        self._id_orden = Orden.contador_orden
        self._productos = list(productos)

    # Método para agregar un producto
    def agregar_productos(self, add_producto):
        self._productos.append(add_producto)

    # Método que calcula el total de la orden
    def calcula_total_orden(self):
        total = 0
        for p in self._productos:
            total += p.get_precio()
        return total

    # Método str
    def __str__(self):
        producto_str = ""
        for p in self._productos:
            producto_str += p.__str__() + '|'
        return f"Orden: {self._id_orden}. Producto: {producto_str}"

if __name__ == "__main__":
    producto1 = Producto('Camisa', 100.00)
    producto2 = Producto('Pantalón', 150.00)
    productos1 = [producto1, producto2]
    orden1 = Orden(productos1)
    print(orden1)
    orden2 = Orden(productos1)
    print(orden2)
