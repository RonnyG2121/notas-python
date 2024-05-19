# este código, muestra algunos identificadores estándares en los eventos en wxPytho

import wx

class IdentificadoresEstandares(wx.Frame):
    def __init__(self, *args, **kw):
        super(IdentificadoresEstandares, self).__init__(*args, **kw)
        self.Centre()
        self.SetTitle("Identificadores Estándares en Eventos")
        self.Show(True)
        self.InitUI()
    def InitUI(self):
        pnl = wx.Panel(self, -1)

        tabla = wx.GridSizer(3, 2)
        tabla.AddMany([
            (wx.Button(pnl, wx.ID_CANCEL), 0, wx.TOP | wx.LEFT, 9),
            (wx.Button(pnl, wx.ID_DELETE), 0, wx.TOP, 9),
            (wx.Button(pnl, wx.ID_SAVE), 0, wx.LEFT, 9),
            (wx.Button(pnl, wx.ID_EXIT)),
            (wx.Button(pnl, wx.ID_STOP), 0, wx.LEFT, 9),
            (wx.Button(pnl, wx.ID_NEW))
            ])
        self.Bind(wx.EVT_BUTTON, self.OnSalir, id= wx.ID_EXIT)
        pnl.SetSizer(tabla)
    def OnSalir(self, event):
        self.Close(True)



def main():
    aplicacion = wx.App()
    objeto = IdentificadoresEstandares(None)
    aplicacion.MainLoop()

if __name__ == "__main__":
    main()

