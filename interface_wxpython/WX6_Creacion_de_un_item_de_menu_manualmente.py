# Este código muestra la creaciónn de un item de menu de forma manual
#será un menú con la opción de salir. también se incluirá un comando de teclado y un ícono


import wx


class Item_Menu_Manual(wx.Frame):
    def __init__(self, *args, **kw):
        super(Item_Menu_Manual, self).__init__(*args, **kw)
        self.InitUI()
    def InitUI(self):
        barraM = wx.MenuBar() # La barra del menú
        archivoM = wx.Menu() # Objeto de tipo menú
        salir = wx.MenuItem(archivoM, wx.ID_ANY, "&Salir\tCtrl+q") # Este es el item de menú. En su identificador también podemos poner -1 y funcionará igual
        salir.SetBitmap(wx.Bitmap("salir.png")) # Aquí añadimos un ícono al elemento del menú
        archivoM.Append(salir) # añadimos el elemento al menú
        self.Bind(wx.EVT_MENU, self.OnQuit) # Aquí creamos el evento y conectamos el elemento salir
        barraM.Append(archivoM, "&Menú") # Añadimos el menú a la barra
        self.SetMenuBar(barraM) # fijamos la barra de menú
        self.SetSize((350, 250)) # Elegimos el tamaño
        self.SetTitle("Item de menú con íconos y atajos de teclado") # damos un título
        self.Centre()
        self.Show(True) # Le decimos a la ventana que se muestre
    def OnQuit(self, e):
        self.Close() # esto cierra la aplicación


def main():
    app = wx.App() # Creamos un objeto de tipo aplicación
    ventana = Item_Menu_Manual(None) # Instanciamos la clase
    app.MainLoop() # Creamos una especie de bucle infinito que permitirá que la aplicación se ejecute

if __name__ == "__main__":
    main()