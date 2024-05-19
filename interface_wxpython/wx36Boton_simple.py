


import wx

class BotonSimple(wx.Frame):
    def __init__(self, *args, **kw):
        super(BotonSimple, self).__init__(*args, **kw)
        self.Contenedor()
        self.SetTitle("Botón simple de Cerrar")
        self.SetSize((350, 250))
        self.Centre()
        self.Show(True)
    def Contenedor(self):
        self.panel = wx.Panel(self, -1)
        self.boton_cerrar = wx.Button(self.panel, wx.ID_ANY, label = "Cerrar", pos = (20, 20))
        self.boton_cerrar.Bind(wx.EVT_BUTTON, self.OnCerrar)
    def OnCerrar(self, e):
        self.Close(True)


if __name__ == "__main__":
    app = wx.App()
    BotonSimple(None)
    app.MainLoop()