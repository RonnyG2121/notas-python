# Nota importante: hay 2 tipos de eventos. básicos y de comandos
# los de comandos son los que se propagan



import wx

class MiPanel(wx.Panel):
    def __init__(self, *args, **kw):
        super(MiPanel, self).__init__(*args, **kw)
        self.Bind(wx.EVT_BUTTON, self.Boton_Click)
    def Boton_Click(self, e):
        print("El evento alcanzó la clase del panel")
        e.skip()


class MiBoton(wx.Button):
    def __init__(self, *args, **kw):
        super(MiBoton, self).__init__(*args, **kw)
        self.Bind(wx.EVT_BUTTON, self.Boton_Click)
    def Boton_Click(self, e):
        print("El evento alcanzó la clase del botón")
        e.Skip()



class EventoPropagado(wx.Frame):
    def __init__(self, *args, **kw):
        super(EventoPropagado, self).__init__(*args, **kw)
        self.InitUI()
    def InitUI(self):
        ObjetoPanel = MiPanel(self)
        MiBoton(ObjetoPanel, label = "Aceptar", pos = (15, 15))
        self.Bind(wx.EVT_BUTTON, self.Boton_Click)
        self.SetTitle("Propagación de eventos")
        self.Centre()
    def Boton_Click(self, e):
        print("El evento alcanzón la clase")
        e.Skip()



def main():
    app = wx.App()
    objeto = EventoPropagado(None)
    objeto.Show(True)
    app.MainLoop()


if __name__ == "__main__":
    main()


