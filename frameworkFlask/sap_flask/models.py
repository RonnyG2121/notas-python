from database import db
from sqlalchemy import Column, String, Integer


class Persona(db.Model):
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250))
    apellido = Column(String(250))
    email = Column(String(250))

    def __str__(self):
        return (
            f'Id: {self.id}, '
            f'Nombre: {self.nombre}, '
            f'Apellido: {self.apellido}, '
            f'Email: {self.email}'
        )
