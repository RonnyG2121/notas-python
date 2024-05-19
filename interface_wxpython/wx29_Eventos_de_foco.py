import wx

class Miventana(wx.Panel):
    def __init__(self, parent):
        super(Miventana, self).__init__(parent)
        self.color = "#b3b3b3"
        self.Bind(wx.EVT_PAINT, self.OnPintura)
        self.Bind(wx.EVT_SIZE, self.OnTamaño)
        self.Bind(wx.EVT_SET_FOCUS, self.OnObtenerFoco)
        self.Bind(wx.EVT_KILL_FOCUS, self.OnEliminarFoco)
    def OnPintura(self, e):
        dc = wx.PaintDC(self)
        dc.SetPen(wx.Pen(self.color))
        x, y = self.GetSize()
        dc.DrawRectangle(0, 0, x, y)
    def OnTamaño(self, e):
        self.Refresh()
    def OnObtenerFoco(self, e):
        self.color = "#ff0000"
        self.Refresh()
    def OnEliminarFoco(self, e):
        self.color = "#b3b3b3"
        self.Refresh()

class EventoFoco(wx.Frame):
    def __init__(self, *args, **kw):
        super(EventoFoco, self).__init__(*args, **kw)
        self.InitUI()
        self.Centre()
        self.SetTitle("Evento Foco")
        self.Show(True)
    def InitUI(self):
        grid = wx.GridSizer(2, 2, 10, 10)
        grid.AddMany([(Miventana(self), 0, wx.EXPAND|wx.TOP|wx.LEFT, 9),
            (Miventana(self), 0, wx.EXPAND|wx.TOP|wx.RIGHT, 9),
            (Miventana(self), 0, wx.EXPAND|wx.BOTTOM|wx.LEFT, 9),
            (Miventana(self), 0, wx.EXPAND|wx.BOTTOM|wx.RIGHT, 9)])


        self.SetSizer(grid)
    def OnMover(self, e):
        print(e.GetEventObject())
        x, y = e.GetPosition()
        self.st1.SetLabel(str(x))
        self.st2.SetLabel(str(y))


def main():
    app = wx.App()
    objeto = EventoFoco(None)
    app.MainLoop()

if __name__ == "__main__":
    main()

