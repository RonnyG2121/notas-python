

import wx


class EspaciosPanel(wx.Frame):
    def __init__(self, parent, title):
        super(EspaciosPanel, self).__init__(parent, title = title, size = (260, 180))
        self.InitUI()
        self.Centre()
        self.Show()
    def InitUI(self):
        panel = wx.Panel(self)
        panel.SetBackgroundColour("#4f5049")
        caja = wx.BoxSizer(wx.VERTICAL)
        panel2 = wx.Panel(panel)
        panel2.SetBackgroundColour("#ededed")
        caja.Add(panel2, 1, wx.EXPAND | wx.ALL, 20)
        panel.SetSizer(caja)


def main():
    app = wx.App()
    objeto = EspaciosPanel(None, "Agregando Espacios a 2 paneles")
    app.MainLoop()

if __name__ == "__main__":
    main()

