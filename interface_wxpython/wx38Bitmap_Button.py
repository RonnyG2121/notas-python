import wx


class ReproductorVideo(wx.Frame):
    def __init__(self, *args, **kw):
        super(ReproductorVideo, self).__init__(*args, **kw):
        self.Contenedor()
        self.SetTitle("Reproductor de video")
        self.SetSize((300, 200))
        self.Show(True)
    def Contenedor(self):
        self.panel1 = wx.Panel(self, -1)
        self.panel2 = wx.Panel(self, -1)
        self.panel2.SetBackgroundColour(wx.BLUE)
        self.panel3 = wx.Panel(self, -1)
        self.barra_menu = wx.MenuBar()
        self.archivo = wx.Menu()
        self.reproducir = wx.Menu()
        self.ver = wx.Menu()
        self.herramientas = wx.Menu()
        self.favoritos = wx.Menu()
        self.ayuda = wx.Menu()
        self.archivo.Append(101, "&Salir", "Cierra la aplicación")
        self.barra_menu.Append(self.archivo, "&Menú")
        self.barra_menu.Append(self.reproducir, "&Reproducir")
        self.barra_menu.Append(self.ver, "&Ver")
        self.barra_menu.Append(self.herramientas, "&Herramientas")
        self.barra_menu.Append(self.favoritos, "&Favoritos")
        self.barra_menu.Append(self.ayuda, "&Ayuda")
        self.SetMenuBar(self.barra_menu)
        self.slider1 = wx.Slider(self.panel2, -1, 0, 0, 1000)
        self.BTN_pausar = wx.BitmapButton(self.panel2, -1, wx.Bitmap("icons/stock_media_pause.png"))
        self.BTN_play = wx.BitmapButton(self.panel2, -1, wx.Bitmap("iconsstock_media_play.png"))
        self.BTN_siguente = wx.BitmapButton(self.panel2, -1, wx.Bitmap("iconsstock_media_next.png"))
        self.BTN_anterior = wx.BitmapButton(self.panel2, -1, wx.Bitmap("anterior.png"))
        