# Creando una aplicación que muestra una ventana centrada en la pantalla


import wx

class VentanaCentrada(wx.Frame):
    def __init__(self, parent, title):
        super(VentanaCentrada, self).__init__(parent, title = title, size = (250, 200))
        self.Centre() # Este método permite centrar la ventana en el centro de la pantalla


def main():
    app = wx.App()
    ex = VentanaCentrada(None, "Ventana centrada")
    ex.Show(True)
    app.MainLoop()

if __name__ == "__main__":
    main()