# Demostración de una barra de herramienta con un botón de rehacer y uno de deshacer. también mostraré una línea separadora


import wx

class Deshacer_Rehacer(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Deshacer_Rehacer, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):

        self.count = 5

        self.BarraH = self.CreateToolBar()
        deshacer = self.BarraH.AddTool(wx.ID_UNDO, "", wx.Bitmap("deshacer.png"))
        rehacer = self.BarraH.AddTool(wx.ID_REDO, "", wx.Bitmap("rehacer.png"))
        self.BarraH.EnableTool(wx.ID_REDO, False)
        self.BarraH.AddSeparator()
        salir = self.BarraH.AddTool(wx.ID_EXIT, "", wx.Bitmap("salir.png"))
        self.BarraH.Realize()

        self.Bind(wx.EVT_TOOL, self.OnQuit, salir)
        self.Bind(wx.EVT_TOOL, self.OnDeshacer, deshacer)
        self.Bind(wx.EVT_TOOL, self.OnRehacer, rehacer)

        self.SetSize((350, 250))
        self.SetTitle("Deshacer y Rehacer")
        self.Centre()
        self.Show(True)

    def OnDeshacer(self, e):
        if self.count > 1 and self.count <= 5:
            self.count = self.count - 1

        if self.count == 1:
            self.BarraH.EnableTool(wx.ID_UNDO, False)

        if self.count == 4:
            self.BarraH.EnableTool(wx.ID_REDO, True)

    def OnRehacer(self, e):
        if self.count < 5 and self.count >= 1:
            self.count = self.count + 1

        if self.count == 5:
            self.BarraH.EnableTool(wx.ID_REDO, False)

        if self.count == 2:
            self.BarraH.EnableTool(wx.ID_UNDO, True)


    def OnQuit(self, e):
        self.Close()


def main():

    app = wx.App()
    ex = Deshacer_Rehacer(None)
    app.MainLoop()


if __name__ == '__main__':
    main()

