# Esto es un hola mundo usando pyside6 o qt
from PySide6.QtWidgets import QApplication, QWidget
import sys

# Creamos el objerto aplicación para manejar eventos, y demás
app = QApplication()

# Creando un objeto ventana
ventana = QWidget()

# Modificando características de la ventana
ventana.setWindowTitle("Hola mundo")
ventana.setAccessibleDescription("Esto es un hola mundo")
ventana.setAccessibleName("hola mundo")
ventana.resize(600, 400)
# mostrando la ventana
ventana.show()

# Ejecutando la aplicación. Esto crea una especie de bucle para que no se cierre
sys.exit(app.exec())
