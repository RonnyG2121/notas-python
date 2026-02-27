from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton, QDialog, QDialogButtonBox, QVBoxLayout, QLabel, \
    QMessageBox


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Dialogos')
        # Agregamos un boton
        boton = QPushButton('Mostrar dialogo')
        boton.clicked.connect(self.click_boton)

        # Publicamos el boton
        self.setCentralWidget(boton)

    def click_boton(self, s):
        print(f'Click sobre boton: {s}')
        # Creamos el dialogo
        dialogo = QMessageBox.question(self, 'Pregunta', 'Ventana con pregunta')

        if dialogo == QMessageBox.Yes:
            print('Regreso el valor Yes (Si)')
        else:
            print('Regreso el valor de No')


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()