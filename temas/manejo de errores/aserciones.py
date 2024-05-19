"""
Ñas aserciones nos ayudan a derpurar nuestros programas.
son muy útiles sobre todo para depurar errores irrecuperables o que hacen que el programa caiga
"""


def Dibidir(a, b):
    assert b != 0, "Dibisión entre 0"
    print(f"División {a /b}")


#Dibidir(10,0)
#Dibidir(10, 2)

#Ejemplo 2
def getPromedio(calificaciones=[]):
    assert len(calificaciones) != 0, "La lista está vacía"
    print(f"El promedio final es: {sum(calificaciones) / len(calificaciones)}")

#getPromedio([10, 12, 8, 15])
#getPromedio([])


#Ejemplo 3
def descuento(productos, descuento):
    precioConDescuento = productos["precio"] * (1.0 - descuento)
    print(f"El nuevo precio del producto {productos['nombre']} es : {precioConDescuento:0.2f}")
    assert 0<= precioConDescuento <= productos["precio"], f"Precio inválido {precioConDescuento:0.2f}"
    print("Descuento válido...")

productos = {
    "nombre": "pantalón",
    "precio": 1500}
descuento(productos, 0.11)