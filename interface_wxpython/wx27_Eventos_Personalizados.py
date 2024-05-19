import wx


id_Menu_Nuevo = wx.NewId()
id_Menu_Abrir = wx.NewId()
id_Menu_Guardar = wx.NewId()


class Eventos_Personalizados(wx.Frame):
    def __init__(self, *args, **kw):
        super(Eventos_Personalizados, self).__init__(*args, **kw)
        self.InitUI()
    def InitUI(self):
        self.CrearBarraH()
        self.CreateStatusBar()
        self.SetSize((350, 250))
        self.SetTitle("Identificadores personalizados")
        self.Centre()
    def CrearBarraH(self):
        barramenu = wx.MenuBar()
        archivoMenu = wx.Menu()
        salir = wx.MenuItem(archivoMenu, wx.ID_ANY, "&Salir\tCtrl+S")
        archivoMenu.Append(id_Menu_Nuevo, "&Nuevo")
        archivoMenu.Append(id_Menu_Abrir, "&Abrir")
        archivoMenu.Append(id_Menu_Guardar, "&Guardar")
        archivoMenu.Append(salir)
        barramenu.Append(archivoMenu, "&Menú Archivo")
        self.SetMenuBar(barramenu)
        self.Bind(wx.EVT_MENU, self.MensajeEnPantalla, id= id_Menu_Nuevo)
        self.Bind(wx.EVT_MENU, self.MensajeEnPantalla, id= id_Menu_Abrir)
        self.Bind(wx.EVT_MENU, self.MensajeEnPantalla, id= id_Menu_Guardar)
        self.Bind(wx.EVT_MENU, self.OnSalir)
    def OnSalir(self, ev):
        self.Close(True)
    def MensajeEnPantalla(self, e):
        barraS = self.GetCreateStatusBar()
        eid = e.GetId()
        if eid == id_Menu_Nuevo:
            mensaje = "A seleccionado el menú Nuevo"
        elif eid == id_Menu_Abrir:
            mensaje = "A seleccionado el menú Abrir"
        elif eid == id_Menu_Guardar:
            mensaje = "A seleccionado el menú Guardar"
        barraS.SetStatusText(mensaje)


def main():
    app = wx.App()
    objeto = Eventos_Personalizados(None)
    objeto.Show(True)
    app.MainLoop()


if __name__ == "__main__":
    main()