import wx

class EventoKey(wx.Frame):
    def __init__(self, *args, **kw):
        super(EventoKey, self).__init__(*args, **kw)
        self.InitUI()
    def InitUI(self):
        mipanel = wx.Panel(self, -1)
        mipanel.Bind(wx.EVT_KEY_DOWN, self.OnComando)
        mipanel.SetFocus()
        self.Centre()
        self.Show(True)
    def OnComando(self, event):
        codigoKey = event.GetKeyCode()
        if codigoKey == wx.WXK_ESCAPE:
            reto = wx.MessageBox("¿Desea salir?", "Salir", wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION, self)
            if reto == wx.YES:
                self.Close(True)
        else:
            event.Skyp()


def main():
    app = wx.App()
    objeto = EventoKey(None)
    app.MainLoop()

if __name__ == "__main__":
    main()

