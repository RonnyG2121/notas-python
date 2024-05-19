# Importamos el módulo
import sqlite3

# Nos conectamos a la base de datos ejemplo.db (la crea si no existe)
conexion = sqlite3.connect('Base_productos.db')


# Creamos el puntero
puntero = conexion.cursor()

# Ahora crearemos una tabla de usuarios con productos, precios y sección
# puntero.execute("CREATE TABLE productos" "(nombre VARCHAR(50), precio INTEGER, seccion VARCHAR(20))")

# Cuando se crea la tabla es conveniente comentar o eliminar esta línea. ya que da error
# Insertamos un registro en la tabla de usuarios
# puntero.execute("INSERT INTO productos VALUES " "('Balón', 27, 'Deporte')")

# Insertaré más registros a la tabla por medio de una lista que contenga tublas
Lista_tabla = [("Camiseta", 20, "ropa"), ("Jarrón", 100, "Electrodomésticos"), ("Computadora", 1000, "Tecnología")]
# Esta manera es mucho más cómoda, ya que podemos insertar un mayor lote de registros en la base de datos

# ahora insertaemos este nuevo registro y lo comentaré luego de ejecutarlo para que no de error
# puntero.executemany("INSERT INTO productos VALUES(?,?,?)", Lista_tabla)
# recuperando los registros para verlos
puntero.execute("select* from productos")

# leeremos esto con una lista
Lista_tabla = puntero.fetchall()
# print(Lista_tabla)

# Ahora, leemos esto con un bucle for es otra manera de recorrer la lista
for producto in Lista_tabla:
    print(producto)

# Guardamos los cambios haciendo un commit
conexion.commit()


# Cerramos la conexión, si no la cerramos quedará abierta
# y no podremos gestionar el fichero
conexion.close()

