# En este ejemplo se muestra una ventana que te pido un mensaje de confirmacion al precionar el  botón cerrar


import wx


class EventoVetado(wx.Frame):
    def __init__(self, *args, **kw):
        super(EventoVetado, self).__init__(*args, **kw)
        self.InitUI()
    def InitUI(self):
        self.Bind(wx.EVT_CLOSE, self.OnCerrar)
        self.SetTitle("Evento Vetado")
        self.Centre()
        self.Show(True)
    def OnCerrar(self, evento):
        dialogo = wx.MessageDialog(None, "¿Confirma que quiere salir de la aplicación?",
        wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
        reto = dialogo.ShowModal()
        if reto == wx.ID_YES:
            self.Destroy()
        else:
            evento.Veto()


def main():
    app = wx.App()
    objeto = EventoVetado(None)
    app.MainLoop()

if __name__ == "__main__":
    main()

