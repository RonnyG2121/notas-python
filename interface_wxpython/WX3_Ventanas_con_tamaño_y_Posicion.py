# Este Ejemplo es de una ventana con un tamaño y posición en la pantalla

import wx


class TamañoYPosicionV(wx.Frame):
    def __init__(self, parent, title):
        super(TamañoYPosicionV, self).__init__(parent, title = title, size = (250, 200)) # Este parámetro es una tubla y se encarga de darle el tamaño a la ventana
        self.Move((800, 200)) # Esto mueve una ventana a una posición dada


def main():
    app = wx.App()
    ventana = TamañoYPosicionV(None, "Ventana con tamaño y posición")
    ventana.Show(True)
    app.MainLoop()

if __name__ == "__main__":
    main()

