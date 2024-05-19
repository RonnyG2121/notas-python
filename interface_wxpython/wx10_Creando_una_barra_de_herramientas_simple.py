# En este código, haré una barra de herramientas simple con un único botón para cerrar la aplicación


import wx


class Barra_H(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Barra_H, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):

        barra = self.CreateToolBar()
        herramienta = barra.AddTool(wx.ID_ANY, "Salir", wx.Bitmap("salir.png"))
        barra.Realize()

        self.Bind(wx.EVT_TOOL, self.OnQuit, herramienta)

        self.SetSize((350, 250))
        self.SetTitle("Barra De Herramientas Simple")
        self.Centre()
        self.Show(True)

    def OnQuit(self, e):
        self.Close()


def main():

    app = wx.App()
    ex = Barra_H(None)
    app.MainLoop()


if __name__ == '__main__':
    main()