# En Este código creo un menú simple con un solo elemento de menú

import wx


class MenuSimple(wx.Frame):
    def __init__(self, *args, **kw):
        super(MenuSimple, self).__init__(*args, **kw)
        self.InitUI()
    def InitUI(self):
        barramenu = wx.MenuBar() # Esto crea una barra de menú
        archivomenu = wx.Menu() # Este es el menú que aparecerá en la barra
        elementomenu = archivomenu.Append(wx.ID_EXIT, "Salir", "Cierra la aplicación") # Este es el elemento de menú
        barramenu.Append(archivomenu, "&Barra De Menú") # Aquí añadimos el menú a la barra correspondiente
        self.SetMenuBar(barramenu) # Aquí se fija la barra de menú
        self.Bind(wx.EVT_MENU, self.OnQuit, elementomenu) # Aquí Creamos el evento que ará el elemento de menú, llamamos al método que ejecutará la opción deseada y llamamos también al elemento del menú que se ejecutará
        self.SetSize((350, 250)) # Elegimos el tamaño de la barra de menú
        self.SetTitle("Menú Simple") # Damos un título a la barra de menú
        self.Centre() # Centramos la barra de menú en pantalla
    def OnQuit(self, e): # Este es el método llamado en el evento del elemento del menú
        self.Close() # Este método permite cerrar el menú


def main():
    aplicacion = wx.App()
    ventana = MenuSimple(None)
    ventana.Show(True)
    aplicacion.MainLoop()

if __name__ == "__main__":
    main()