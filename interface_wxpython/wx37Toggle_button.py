


import wx


class botonToggle(wx.Frame):
    def __init__(self, *args, **kw):
        super(botonToggle, self).__init__(*args, **kw)
        self.Contenedor()
    def Contenedor(self):
        self.panel = wx.Panel(self)
        self.color = wx.Colour(0, 0, 0)
        self.rojo = wx.ToggleButton(self.panel, label = "Rojo", pos = (20, 25))
        self.verde = wx.ToggleButton(self.panel, label = "Verde", pos = (20, 60))
        self.azul = wx.ToggleButton(self.panel, label = "Azul", pos = (20, 100))
        self.cpnl = wx.Panel(self.panel, pos = (150, 20), size = (110, 110))
        self.cpnl.SetBackgroundColour(self.color)
        self.rojo.Bind(wx.EVT_TOGGLEBUTTON, self.ToggleRojo)
        self.verde.Bind(wx.EVT_TOGGLEBUTTON, self.ToggleVerde)
        self.azul.Bind(wx.EVT_TOGGLEBUTTON, self.ToggleAzul)
        self.SetSize((350, 250))
        self.SetTitle("Toggle Botón")
        self.Centre()
        self.Show(True)
    def ToggleRojo(self, ev):
        objeto = ev.GetEventObject()
        precionar = objeto.GetValue()
        verde = self.color.Green()
        azul = self.color.Blue()
        if precionar:
            self.color.Set(255, verde, azul)
        else:
            self.color.Set(0, verde, azul)
        self.cpnl.SetBackgroundColour(self.color)
        self.cpnl.Refresh()
    def ToggleVerde(self, ev):
        objeto = ev.GetEventObject()
        precionar = objeto.GetValue()
        rojo = self.color.Red()
        azul = self.color.Blue()
        if precionar:
            self.color.Set(rojo, 255, azul)
        else:
            self.color.Set(rojo, 0, azul)
        self.cpnl.SetBackgroundColour(self.color)
        self.cpnl.Refresh()
    def ToggleAzul(self, ev):
        objeto = ev.GetEventObject()
        precionar = objeto.GetValue()
        rojo = self.color.Red()
        verde = self.color.Green()
        if precionar:
            self.color.Set(rojo, verde, 255)
        else:
            self.color.Set(rojo, verde, 0)
        self.cpnl.SetBackgroundColour(self.color)
        self.cpnl.Refresh()


if __name__ == "__main__":
    app = wx.App()
    botonToggle(None)
    app.MainLoop()

