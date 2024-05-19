# Demostración de una aplicación con 2 barras de herramientas en una caja vertical

import wx


class Barra_H2_CV(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Barra_H2_CV, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):

        vcaja = wx.BoxSizer(wx.VERTICAL)

        barra_Herramientas1 = wx.ToolBar(self)
        barra_Herramientas1.AddTool(wx.ID_ANY, "Nuevo", wx.Bitmap("nuevo.png"))
        barra_Herramientas1.AddTool(wx.ID_ANY, "Abrir", wx.Bitmap("abrir.png"))
        barra_Herramientas1.AddTool(wx.ID_ANY, "Guardar", wx.Bitmap("guardar.png"))
        barra_Herramientas1.Realize()

        barra_Herramientas2 = wx.ToolBar(self)
        qherramienta = barra_Herramientas2.AddTool(wx.ID_EXIT, "Salir", wx.Bitmap("salir.png"))
        barra_Herramientas2.Realize()

        vcaja.Add(barra_Herramientas1, 0, wx.EXPAND)
        vcaja.Add(barra_Herramientas2, 0, wx.EXPAND)

        self.Bind(wx.EVT_TOOL, self.OnQuit, qherramienta)

        self.SetSizer(vcaja)

        self.SetSize((350, 250))
        self.SetTitle("Barras de herramientas en Caja vertical")
        self.Centre()
        self.Show(True)

    def OnQuit(self, e):
        self.Close()


def main():

    app = wx.App()
    ex = Barra_H2_CV(None)
    app.MainLoop()


if __name__ == '__main__':
    main()
