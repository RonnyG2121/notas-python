import wx


class EventoTamaño(wx.Frame):
    def __init__(self, parent, id, title):
        super(EventoTamaño, self).__init__(parent, id, title)
        self.InitUI()
        self.Centre()
        self.Show(True)
    def InitUI(self):
        self.Bind(wx.EVT_SIZE, self.OnTamaño)
    def OnTamaño(self, ev):
        self.SetTitle(str(ev.GetSize()))


def main():
    app = wx.App()
    objeto = EventoTamaño(None, 1, "Evento De Tamaño")
    app.MainLoop()

if __name__ == "__main__":
    main()

