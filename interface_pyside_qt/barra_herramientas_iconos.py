from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QMainWindow, QApplication, QLabel, QToolBar, QStatusBar


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Barra de Herramientas')
        # publicamos una etiqueta
        etiqueta = QLabel('Hola')
        # etiqueta.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setCentralWidget(etiqueta)

        # Creamos la barra de herramientas
        barra = QToolBar('Mi barra de herramientas')
        barra.setIconSize(QSize(16,16))
        self.addToolBar(barra)

        # Agregamos elementos a nuestra barra de herramientas
        boton_nuevo = QAction(QIcon('nuevo.png'), 'Nuevo', self)
        boton_guardar = QAction(QIcon('guardar.png'), 'Guardar archivo', self)
        boton_acerca = QAction(QIcon('acerca.png'), 'Acerca de', self)
        # Agregamos los botones a la barra
        barra.addAction(boton_nuevo)
        barra.addAction(boton_guardar)
        barra.addAction(boton_acerca)


        # Barra de estado
        self.setStatusBar(QStatusBar(self))

        # Mostramos mensaje del boton accion
        boton_nuevo.setStatusTip('Nuevo archivo')
        boton_guardar.setStatusTip("Guarda el archivo")
        boton_acerca.setStatusTip("Acerca del programa")

        # Asociamos el evento click
        boton_nuevo.triggered.connect(self.click_boton_nuevo)
        boton_guardar.triggered.connect(self.guardar)
        boton_acerca.triggered.connect(self.Acerca)



    def click_boton_nuevo(self, s):
        print(f'Nuevo archivo {s}')

    def guardar(self, s):
        print(f"Guardar archivo. {s}")

    def Acerca(self, s):
        print(f"Acerda de: {s}")

if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()