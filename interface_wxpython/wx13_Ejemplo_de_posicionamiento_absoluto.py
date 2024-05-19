# En este código se mostrará el posicionamiento absoluto de un widget
# 3 Imágenes serán posicionadas dentro de un panel

import wx

class Posicionamiento_Absoluto(wx.Frame):
    def __init__(self, parent, title):
        super(Posicionamiento_Absoluto, self).__init__(parent, title = title, size = (350, 300))
        self.InitUI()
        self.Centre()
    def InitUI(self):
        self.panel = wx.Panel(self) # Esto crea un panel
        self.panel.SetBackgroundColour("blue") # añadimos un color al panel
        self.CargarImagen()
        self.mincol.SetPosition((20, 20))
        self.bardejov.SetPosition((40, 160))
        self.rotunda.SetPosition((170, 50))
    def CargarImagen(self):
        self.mincol = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.Bitmap("mincol.png", wx.BITMAP_TYPE_ANI))
        self.bardejov = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.Bitmap("bardejov.png", wx.BITMAP_TYPE_ANI))
        self.rotunda = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.Bitmap("rotundal.png", wx.BITMAP_TYPE_ANI))


def main():
    app = wx.App()
    ex = Posicionamiento_Absoluto(None, title = "Posicionamiento Absoluto")
    ex.Show()
    app.MainLoop()

if __name__ == "__main__":
    main()

