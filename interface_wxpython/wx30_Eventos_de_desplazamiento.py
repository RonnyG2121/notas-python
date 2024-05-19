import wx


class EventoDesplazado(wx.Frame):
    def __init__(self, parent, id, title):
        super(EventoDesplazado, self).__init__(parent, id, title)
        mipanel = wx.Panel(self, -1)
        self.st = wx.StaticText(mipanel, -1, "0", (30,0))
        mipanel.Bind(wx.EVT_SCROLLWIN, self.OnScroll)
        mipanel.SetScrollbar(wx.VERTICAL,0 , 6, 50)
        self.Centre()
        self.Show()
    def OnScroll(self, e):
        y = e.GetPosition()
        self.st.SetLabel(str(y))


def main():
    app = wx.App()
    objeto = EventoDesplazado(None, -1, "Eventos de Desplazamiento")
    app.MainLoop()


if __name__ == "__main__":
    main()

