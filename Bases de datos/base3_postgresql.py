import psycopg2

conexion = psycopg2.connect(
    user='postgres',
    password='kitsune1234',
    host='localhost',
    port='5432',
    database='test_db'
)

cursor = conexion.cursor()
sentencia = 'SELECT * FROM persona'
cursor.execute(sentencia)
registros = cursor.fetchall()
print(registros)

cursor.close()
conexion.close()