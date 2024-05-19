

import wx


class IdentificaVentanas(wx.Frame):
    def __init__(self, *args, **kw):
        super(IdentificaVentanas, self).__init__(*args, **kw)
        self.Centre()
        self.SetTitle("Identificadores de ventanas")
        self.Show(True)
        self.InitUI()
    def InitUI(self):
        mipanel = wx.Panel(self, -1)
        salirBoton = wx.Button(mipanel, -1, "Salir", (10, 10))
        self.Bind(wx.EVT_BUTTON, self.OnSalir, id= salirBoton.GetId())
        mipanel.Layout()
    def OnSalir(self, e):
        self.Close(True)


def main():
    app = wx.App()
    objeto = IdentificaVentanas(None, -1)
    app.MainLoop()

if __name__ == "__main__":
    main()

