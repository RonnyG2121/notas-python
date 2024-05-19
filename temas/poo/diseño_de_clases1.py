# Creando el diseño de clases. 2 clases se relacionarán entre sí


class Producto:
    contador_producto = 0
    def __init__(self, nombre_producto, precio_producto):
        Producto.contador_producto +=1
        self._id_producto = Producto.contador_producto
        self._nombre = nombre_producto
        self._precio = precio_producto

    # Área de geters y setters
    # Obteniendo  el id del producto, este no se modifica por lo que no tendrá un setter
    def get_id_producto(self):
        return self._id_producto

    # Obteniendo y estableciendo el nombre del producto
    def get_nombre_producto(self):
        return self._nombre

    def set_nombre_producto(self, nombre):
        self._nombre = nombre

    # Obteniendo y estableciendo el precio del producto
    def get_precio(self):
        return self._precio

    def set_precio(self, precio):
        self._precio = precio

    # El método str
    def __str__(self):
        return f" ID del producto: {self._id_producto}. Nombre del producto: {self._nombre}. precio: {self._precio}"


# Probando desde el módulo principal
if __name__ == "__main__":
    procuto1 = Producto("Camisa", 125.00)
    producto2 = Producto("Pantalón", 250.00)
    print(procuto1, producto2)

