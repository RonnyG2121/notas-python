# Creando la clase Conexion. Esta Trabajará con la base de datos postgres
import psycopg2
from logger_base import log
from psycopg2 import pool
import sys


class Conexion:
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'kitsune1234'
    _DB_PORT = '5432'
    _HOST = 'localhost'
    # Desarrollando el pool de conexiones
    _min_conexiones = 1
    _max_conexiones = 5
    _pool_conexiones = None

    # Método que configura este pool
    @classmethod
    def obtenerPool(cls):
        if cls._pool_conexiones is None:
            try:
                cls._pool_conexiones = pool.SimpleConnectionPool(cls._min_conexiones, cls._max_conexiones, host=cls._HOST, user=cls._USERNAME, password=cls._PASSWORD, port=cls._DB_PORT, database=cls._DATABASE)
                log.debug(f"El pool de conexiones se generó exitosamente\n{cls._pool_conexiones}")
                return cls._pool_conexiones

            except psycopg2.pool.PoolError() as e:
                log.error(f"A ocurrido un error:\n{e}")
                sys.exit()
        else:
            return cls._pool_conexiones

# Método para obtener la conexión
    @classmethod
    def obtenerConexion(cls):
        # Nueva forma de implementación
        conexion = cls.obtenerPool().getconn()
        log.debug(f"La conexión se obtuvo exitosamente\n{conexion}")
        return conexion

    # Método para liberar el objeto conexi'on ocupado

    @classmethod
    def liberarConexion(cls, objetoConexion):
        cls.obtenerPool().putconn(objetoConexion)
        log.debug(f"Conexión liberada exitosamente:\n{objetoConexion}")

    # Cerrando la conexión
    @classmethod
    def cerrarConexion(cls):
        cls.obtenerPool().closeall()
        log.debug(f"Conexión cerrada exitosamente")

# Zona de pruebas
if __name__ == '__main__':
    conexion1 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion1)
    conexion2 = Conexion.obtenerConexion()
    conexion3 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion3)
    conexion4 = Conexion.obtenerConexion()
    conexion5 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion5)
    conexion6 = Conexion.obtenerConexion()
