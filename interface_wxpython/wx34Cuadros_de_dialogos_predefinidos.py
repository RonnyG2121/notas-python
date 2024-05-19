


import wx

class DialogosPredefinidos(wx.Frame):
    def __init__(self, *args, **kw):
        super(DialogosPredefinidos, self).__init__(*args, **kw)
        self.Contenedor()
        self.SetTitle("Cuadros De Diálogos Predefinidos")
        self.SetSize((350, 250))
        self.Show(True)
    def Contenedor(self):
        self.Mipanel = wx.Panel(self, -1)
        self.caja = wx.BoxSizer(wx.HORIZONTAL)
        self.tabla = wx.GridSizer(2, 2, 2, 2)
        self.btn1 = wx.Button(self.Mipanel, wx.ID_ANY, label = "Información")
        self.btn2 = wx.Button(self.Mipanel, wx.ID_ANY, label = "Error")
        self.btn3 = wx.Button(self.Mipanel, wx.ID_ANY, label = "Pregunta")
        self.btn4 = wx.Button(self.Mipanel, wx.ID_ANY, label = "Alerta")
        self.tabla.AddMany([self.btn1, self.btn2, self.btn3, self.btn4])
        self.caja.Add(self.tabla, 0, wx.ALL, 15)
        self.Mipanel.SetSizer(self.caja)
        self.Mipanel.Layout()
        self.Mipanel.SetFocus()
        self.btn1.Bind(wx.EVT_BUTTON, self.MostrarMensaje1)
        self.btn2.Bind(wx.EVT_BUTTON, self.MostrarMensaje2)
        self.btn3.Bind(wx.EVT_BUTTON, self.MostrarMensaje3)
        self.btn4.Bind(wx.EVT_BUTTON, self.MostrarMensaje4)
    def MostrarMensaje1(self, event):
        dialogo = wx.MessageDialog(None, "Descarga Finalizada", "Información", wx.OK)
        dialogo.ShowModal()
    def MostrarMensaje2(self, event):
        dialogo = wx.MessageDialog(None, "A ocurrido un problema al cargar el archivo", "Error",
        wx.OK | wx.ICON_ERROR)
        dialogo.ShowModal()
    def MostrarMensaje3(self, event):
        dialogo = wx.MessageDialog(None, "¿Desea salir?", "Pregunta",
        wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
        dialogo.ShowModal()
    def MostrarMensaje4(self, event):
        dialogo = wx.MessageDialog(None, "¡Cudado! ¡Está Intentando borrar System32!", "Alerta",
        wx.OK | wx.ICON_EXCLAMATION)
        dialogo.ShowModal()


if __name__ == "__main__":
    app = wx.App()
    DialogosPredefinidos(None)
    app.MainLoop()
