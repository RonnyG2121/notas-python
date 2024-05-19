


import wx


class DialogoSimple(wx.Frame):
    def __init__(self, *args, **kw):
        super(DialogoSimple, self).__init__(*args, **kw)
        self.Contenedor()
        self.SetSize((350, 250))
        self.SetTitle("cuadro de mensaje simple")
        self.Centre()
    def Contenedor(self):
        wx.CallLater(3000, self.MostrarMensaje)
    def MostrarMensaje(self):
        wx.MessageBox("Descarga Completa", "Información",
        wx.OK | wx.ICON_INFORMATION)

if __name__ == "__main__":
    app = wx.App()
    DialogoSimple(None)
    app.MainLoop()

