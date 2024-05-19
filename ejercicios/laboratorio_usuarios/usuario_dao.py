# Creando y trabajando con la clase UsuarioDAO. Esta hará las consultas a la database
from conexion import Conexion
from cursor_del_pool import CursorDelPool
from usuario import Usuarios
from logger_base import log


class UsuarioDAO:
    """
    DAO significa Data Acces Object
    Con esto se puede acceder a la base de datos y realizarle consultas usando objetos de clase
    """

    _SELECCIONAR = 'SELECT * FROM usuarios ORDER BY id_usuario'
    _INSERTAR = 'INSERT INTO usuarios(username, password) VALUES(%s, %s)'
    _ACTUALIZAR = 'UPDATE usuarios SET username=%s, password=%s WHERE id_usuario=%s'
    _ELIMINAR = 'DELETE FROM usuarios WHERE id_usuario=%s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            lista_usuarioss = []
            for i in registros:
                objeto_usuarios = Usuarios(i[0], i[1], i[2])
                lista_usuarioss.append(objeto_usuarios)
            return lista_usuarioss

    @classmethod
    def insertar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.setusername, usuario.setpassword)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f"usuarios a inseertar:\n{usuario}")
            return cursor.rowcount

    @classmethod
    def actualizar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.setusername, usuario.setpassword, usuario.getid_usuarios)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f"usuarios actualizada:\n{usuario}")
            return cursor.rowcount

    @classmethod
    def eliminar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.getid_usuarios,)
            cursor.execute(cls._ELIMINAR, valores)
            log.debug(f'Objeto eliminado: {usuario}')
            return cursor.rowcount


# Zona de pruebas

if __name__ == '__main__':
    # Insertar un registro
    usuarios1 = Usuarios(username="florimon", password="f1234")
    usuarioss_insertadas = UsuarioDAO.insertar(usuarios1)
    log.debug(f'usuarioss insertadas: {usuarioss_insertadas}')

    # Actualizar un registro
    usuarios1 = Usuarios(4, 'Alex07', 'axx1234')
    usuarioss_actualizadas = UsuarioDAO.actualizar(usuarios1)
    log.debug(f'usuarioss actualizadas: {usuarioss_actualizadas}')

    # Eliminar un registro
    usuarios1 = Usuarios(id_usuario=1)
    usuarios_eliminados = UsuarioDAO.eliminar(usuarios1)
    log.debug(f'usuarioss eliminadas: {usuarios_eliminados}')

    # Seleccionar objetos
    usuarios_seleccionados = UsuarioDAO.seleccionar()
    for i in usuarios_seleccionados:
        log.debug(i)