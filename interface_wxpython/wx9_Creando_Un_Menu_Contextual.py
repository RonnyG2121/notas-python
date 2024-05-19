# Este código muestra como se crea un menú contextual


import wx

class MenuContextual(wx.Menu):

    def __init__(self, parent):
        super(MenuContextual, self).__init__()

        self.parent = parent

        minimiza = wx.MenuItem(self, wx.NewId(), "Minimizar")
        self.Append(minimiza)
        self.Bind(wx.EVT_MENU, self.OnMinimize, minimiza)

        cierra = wx.MenuItem(self, wx.NewId(), "Cerrar")
        self.Append(cierra)
        self.Bind(wx.EVT_MENU, self.OnClose, cierra)


    def OnMinimize(self, e):
        self.parent.Iconize()

    def OnClose(self, e):
        self.parent.Close()


class VentanaContext(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(VentanaContext, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):

        self.Bind(wx.EVT_RIGHT_DOWN, self.OnRightDown)

        self.SetSize((350, 250))
        self.SetTitle("Menú Contextual")
        self.Centre()
        self.Show(True)
    def OnRightDown(self, e):
        self.PopupMenu(MenuContextual(self), e.GetPosition())


def main():

    app = wx.App()
    ex = VentanaContext(None)
    app.MainLoop()

if __name__ == '__main__':
    main()