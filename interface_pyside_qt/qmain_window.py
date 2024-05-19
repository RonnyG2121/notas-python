import sys
from PySide6.QtWidgets import QApplication, QPushButton, QMainWindow

# Clase base de Qt (PySide)
# Se encarga de procesar los eventos (event loop)
app = QApplication()
# Crear un objeto ventana
# Cualquier componente puede ser una ventana en PySide
ventana2 = QMainWindow()
# Cambiar el título
ventana2.setWindowTitle('Hola Mundo con PySide')
# Modificamos el tamaño de la ventana
ventana2.resize(600, 400)
# Crear un botón
ventana_btn = QPushButton('Botón con pyside')
# Mostrar la ventana
ventana2.show()
# Se ejecuta la aplicación
sys.exit(app.exec())

