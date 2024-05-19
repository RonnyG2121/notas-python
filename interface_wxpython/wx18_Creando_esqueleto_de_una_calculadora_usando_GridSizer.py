# Creando un ejemplo de un esqueleto de una calculadora usando wx.GridSizer
# Este Dimencionador organiza los elementos de la interface como en una tabla con varias dimenciones


import wx


class EsqueletoCalculadora(wx.Frame):
    def __init__(self, parent, title):
        super(EsqueletoCalculadora, self).__init__(parent, title = title, size = (300, 250))
        self.InitUI()
        self.Centre()
        self.Show(True)
    def InitUI(self):
        # self.apsalir = 1
        barraM = wx.MenuBar()
        archivo = wx.Menu()
        barraM.Append(archivo, "&Menú Archivo")
        salir = wx.MenuItem(archivo, -1, "&Salir")
        archivo.Append(salir)
        self.Bind(wx.EVT_MENU, self.OnSalir)
        self.SetMenuBar(barraM)
        caja = wx.BoxSizer(wx.VERTICAL)
        self.pantalla = wx.TextCtrl(self, style = wx.TE_RIGHT)
        caja.Add(self.pantalla, flag = wx.EXPAND | wx.Top | wx.Bottom, border = 4)
        tabla = wx.GridSizer(5, 5, 5, 5)
        tabla.AddMany([(wx.Button(self, label = "Cls"), 0, wx.EXPAND),
            (wx.Button(self, label = "Pck"), 0, wx.EXPAND),
            (wx.StaticText(self), wx.EXPAND),
            (wx.Button(self, label = "Close"), 0, wx.EXPAND),
            (wx.Button(self, label = "7"), 0, wx.EXPAND),
            (wx.Button(self, label = "8"), 0, wx.EXPAND),
            (wx.Button(self, label = "9"), 0, wx.EXPAND),
            (wx.Button(self, label = "/Dividir"), 0, wx.EXPAND),
            (wx.Button(self, label = "4"), 0, wx.EXPAND),
            (wx.Button(self, label = "5"), 0, wx.EXPAND),
            (wx.Button(self, label = "6"), 0, wx.EXPAND),
            (wx.Button(self, label = "*Multiplicar"), 0, wx.EXPAND),
            (wx.Button(self, label = "1"), 0, wx.EXPAND),
            (wx.Button(self, label = "2"), 0, wx.EXPAND),
            (wx.Button(self, label = "3"), 0, wx.EXPAND),
            (wx.Button(self, label = "-Menos"), 0, wx.EXPAND),
            (wx.Button(self, label = "0"), 0, wx.EXPAND),
            (wx.Button(self, label = ".Punto Decimal"), 0, wx.EXPAND),
            (wx.Button(self, label = "=Igual Que"), 0, wx.EXPAND),
            (wx.Button(self, label = "+Mas"), 0, wx.EXPAND)])
        caja.Add(tabla, proportion=1, flag=wx.EXPAND)
        self.SetSizer(caja)
    def OnSalir(self, e):
        self.Close(True)


def main():
    ap = wx.App()
    objeto = EsqueletoCalculadora(None, "Esqueleto de una calculadora")
    ap.MainLoop()


if __name__ == "__main__":
    main()

