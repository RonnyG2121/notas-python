# Creando un evento de movimiento


import wx

class EventoMovido(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size = (250, 180))
        self.InitUI()
    def InitUI(self):
        wx.StaticText(self, -1, "X", pos = (10,10))
        wx.StaticText(self, -1, "Y", pos = (10,30))
        self.st1 = wx.StaticText(self, label = "X", pos = (30,10))
        self.st2 = wx.StaticText(self, label = "Y", pos = (30,30))
        self.Bind(wx.EVT_MOVE, self.OnMovida)
        self.Centre()
        self.Show(True)
    def OnMovida(self, event):
        x, y = event.GetPosition()
        self.st1.SetLabel(str(x))
        self.st2.SetLabel(str(y))

def main():
    app = wx.App()
    objeto = EventoMovido(None, -1, "Evento Simple")
    app.MainLoop()

if __name__ == "__main__":
    main()

