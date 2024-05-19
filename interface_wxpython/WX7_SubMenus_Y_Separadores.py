# Creando un subMenú y un separador de menú

import wx

class SubMenu_S(wx.Frame):
    def __init__(self, *args, **kw):
        super(SubMenu_S, self).__init__(*args, **kw)
        self.InitUI()
    def InitUI(self):
        barraMenu = wx.MenuBar()
        archivo = wx.Menu()
        archivo.Append(wx.ID_NEW, "Nuevo")
        archivo.Append(wx.ID_OPEN, "Abrir")
        archivo.Append(wx.ID_SAVE, "Guardar")
        archivo.AppendSeparator()
        importar = wx.Menu()
        importar.Append(wx.ID_ANY, "Importar listas")
        importar.Append(wx.ID_ANY, "Importar marcadores")
        importar.Append(wx.ID_ANY, "Importar correos")
        archivo.AppendMenu(wx.ID_ANY, "i&mportar", importar)
        salir = wx.MenuItem(archivo, wx.ID_EXIT, "&Salir\tCtrl+q")
        archivo.AppendItem(salir)
        self.Bind(wx.EVT_MENU, self.OnQuit, salir)
        barraMenu.Append(archivo, "&Menú")
        self.SetMenuBar(barraMenu)
        self.SetSize((350, 250))
        self.SetTitle("SubMenú")
        self.Centre()
        self.Show(True)
    def OnQuit(self, e):
        self.Close(True)


def main():
    aplicacion = wx.App()
    SubMenu_S(None)
    aplicacion.MainLoop()


if __name__ == "__main__":
    main()