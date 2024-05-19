# Este Código muestra un dimencionador que no está visible
# usaré el mismo control de texto para mostrarlo


import wx

class DimencionadorNoVisible(wx.Frame):
    def __init__(self, parent, title):
        super(DimencionadorNoVisible, self).__init__(parent, title = title, size = (250, 180))
        self.InitUI()
        self.Centre()
        self.Show()
    def InitUI(self):
        barramenu = wx.MenuBar()
        archivo = wx.Menu()
        ver = wx.Menu()
        editar = wx.Menu()
        barramenu.Append(archivo, "&Archivo")
        barramenu.Append(ver, "&Ver")
        barramenu.Append(editar, "&Editar")
        self.SetMenuBar(barramenu)
        controlT = wx.TextCtrl(self) # Esto añade un control de Texto con su dimencionador, lo que sucede aquí es que este no está visible en el código


def main():
    app = wx.App()
    objeto = DimencionadorNoVisible(None, title= "Uso De Dimencionadores")
    app.MainLoop()

if __name__ == "__main__":
    main()