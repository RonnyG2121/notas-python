# En este código crearé un simple control de texto y lo redimencionaré
# Estaré usando posicionamiento absoluto para este ejemplo

import wx

class ControlDeTextoPosicionado(wx.Frame):
    def __init__(self, parent, title):
        super(ControlDeTextoPosicionado, self).__init__(parent, title = title, size = (260, 180))
        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI(self):
        self.panel = wx.Panel(self, -1) # Esto es un panel
        barraM = wx.MenuBar()
        archivo = wx.Menu()
        editar = wx.Menu()
        ayuda = wx.Menu()
        barraM.Append(archivo, "Menú")
        barraM.Append(editar, "Editar")
        barraM.Append(ayuda, "Ayuda")
        self.SetMenuBar(barraM)
        control = wx.TextCtrl(self.panel, wx.ID_ANY, pos = (3, 3), size = (250, 150))


def main():
    app = wx.App()
    objeto = ControlDeTextoPosicionado(None, title = "Control de texto posicionado en un panel")
    app.MainLoop()

if __name__ == "__main__":
    main()

