# Creamos un programa que muestra y oculta barras de herramientas y de estado


import wx


class ItemDeComprobacion(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(ItemDeComprobacion, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):

        menuBarra = wx.MenuBar()
        VerMenu = wx.Menu()
        self.shst = VerMenu.Append(wx.ID_ANY, "Mostrar barra de estado", "Mostrar la barra de estado", kind=wx.ITEM_CHECK)
        self.shtl = VerMenu.Append(wx.ID_ANY, "Mostrar barra de herramientas", "Mostrar la barra de herramientas", kind=wx.ITEM_CHECK)

        VerMenu.Check(self.shst.GetId(), True)
        VerMenu.Check(self.shtl.GetId(), True)

        self.Bind(wx.EVT_MENU, self.ToggleStatusBar, self.shst)
        self.Bind(wx.EVT_MENU, self.ToggleToolBar, self.shtl)

        menuBarra.Append(VerMenu, "&Ver")
        self.SetMenuBar(menuBarra)

        self.toolbar = self.CreateToolBar()
        self.toolbar.AddTool(1, "", wx.Bitmap("salir.png"))
        self.toolbar.Realize()

        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetStatusText("Listo")

        self.SetSize((450, 350))
        self.SetTitle("Item de menú de comprobación")
        self.Centre()
        self.Show(True)
    def ToggleStatusBar(self, e):

        if self.shst.IsChecked():
            self.statusbar.Show()
        else:
            self.statusbar.Hide()

    def ToggleToolBar(self, e):

        if self.shtl.IsChecked():
            self.toolbar.Show()
        else:
            self.toolbar.Hide()


def main():

    app = wx.App()
    ventana = ItemDeComprobacion(None)
    app.MainLoop()


if __name__ == '__main__':
    main()

