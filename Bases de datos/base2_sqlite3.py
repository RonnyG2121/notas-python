import sqlite3

conexion = sqlite3.connect("Gestión_productos.db")

mi_cursor = conexion.cursor()
mi_cursor.execute("""CREATE TABLE producto(
    ID_producto INTEGER PRIMARY KEY AUTOINCREMENT, 

    codigo_producto TEXT(4) UNIQUE, 
    nombre VARCHAR(100), 
    precio INTEGER,
    seccion VARCHAR(20))""")

listaDproductos = [("ar01", "Computadora", "1500", "Tecnología"), ("ar02", "balón", "30", "Deporte")]

mi_cursor.executemany("INSERT INTO producto VALUES (?, ?, ?, ?)", listaDproductos)

conexion.commit()

conexion.close()

