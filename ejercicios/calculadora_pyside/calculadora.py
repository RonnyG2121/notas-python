from functools import partial
from sys import exception
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QWidget, QVBoxLayout, QGridLayout


class Calculadora(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculadora By Pyside_Qt6')
        self.setFixedSize(235, 235)
        self._contenedor = QWidget()
        self.setCentralWidget(self._contenedor)
        self._layout_principal = QVBoxLayout()
        self._contenedor.setLayout(self._layout_principal)
        self.__initUI()
        self.__botones()
        self.__conectarBotones()


    def __initUI(self):
        self._lb_text = QLabel('Pantalla', self._contenedor)
        # self._lb_text.setText('Pantalla')
        self._textbox = QLineEdit(self._contenedor)
        self._textbox.setAccessibleName('Pantalla')
        self._textbox.setFixedHeight(35)
        self._textbox.setAlignment(Qt.AlignmentFlag.AlignRight)
        self._textbox.setReadOnly(True)
        self._layout_principal.addWidget(self._lb_text)
        self._layout_principal.addWidget(self._textbox)

    def __botones(self):
        self._dic_btn = {}
        self._layout_botones = QGridLayout(self._contenedor)
        botones = {
            '7':(0,0),
            '8':(0,1),
            '9':(0,2),
            '/':(0,3),
            '4':(1,0),
            '5':(1,1),
            '6':(1,2),
            '*':(1,3),
            '1':(2,0),
            '2':(2,1),
            '3':(2,2),
            '-':(2,3),
            '0':(3,0),
            '.':(3,1),
            'C':(3,2),
            '+':(3,3),
            '=':(3,4)}
        
        for text_boton,  posicion in botones.items():
            self._dic_btn[text_boton] = QPushButton(text_boton)
            self._dic_btn[text_boton].setFixedSize(40,40)
            self._layout_botones.addWidget(self._dic_btn[text_boton], posicion[0],posicion[1])
            self._layout_principal.addLayout(self._layout_botones)

    def __conectarBotones(self):
        for texto_bton, boton in self._dic_btn.items():
            if texto_bton not in {'=','C'}:
                boton.clicked.connect(partial(self.__construirExpresion, texto_bton))
            elif texto_bton in {'C'}:
                boton.clicked.connect(self.limpiar)

            elif texto_bton in {'='}:
                boton.clicked.connect(self.__igual)

    def __construirExpresion(self, texto_boton):
        expresion = self.obtenerTexto() + texto_boton
        self.actualizarTexto(expresion)

    def obtenerTexto(self):
        return self._textbox.text()

    def actualizarTexto(self, texto):
        self._textbox.setText(texto)
        # self._textbox.setFocus()

    def limpiar(self):
        self.actualizarTexto('')

    def __igual(self):
        resultado = self.__evaluarExpresion(self.obtenerTexto())
        self.actualizarTexto(resultado)

    def __evaluarExpresion(self, expresion):
        try:
            resultado = str(eval(expresion))
        except Exception as e:
            resultado = 'Operación inválida'
        return resultado


if __name__ == "__main__":
    app = QApplication()
    calculadora = Calculadora()
    calculadora.show()
    app.exec()

