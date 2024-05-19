

import wx

class DimencionadoresImportantes(wx.Frame):
    def __init__(self, parent, title):
        super(DimencionadoresImportantes, self).__init__(parent, title = title, size = (350, 260))
        self.InitUI()
        self.Centre()
        self.Show()
    def InitUI(self):
        self.panel = wx.Panel(self)
        # optener la fuente del sistema
        fuente = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
        fuente.SetPointSize(9)
        caja1 = wx.BoxSizer(wx.VERTICAL)
        caja2 = wx.BoxSizer(wx.HORIZONTAL)
        textoEstatico1 = wx.StaticText(self.panel, label = "Clase de Nombre")
        textoEstatico1.SetFont(fuente)
        caja1.Add(textoEstatico1, flag = wx.Right, border = 8)
        controlTexto = wx.TextCtrl(self.panel)
        caja1.Add(controlTexto, proportion = 1)
        caja2.Add(caja1, flag = wx.EXPAND | wx.Left | wx.Right | wx.Top, border = 10)
        caja2.Add((-1, 10))
        caja3 = wx.BoxSizer(wx.HORIZONTAL)
        textoEstatico2 = wx.StaticText(self.panel, label = "Clases de máquinas")
        textoEstatico2.SetFont(fuente)
        caja3.Add(textoEstatico2)
        caja1.Add(caja3, flag = wx.LEFT | wx.TOP, border = 10)
        caja1.Add((-1, 10))
        caja4 = wx.BoxSizer(wx.HORIZONTAL)
        controlTexto2 = wx.TextCtrl(self.panel, style = wx.TE_MULTILINE,)
        caja4.Add(controlTexto2, proportion = 1, flag = wx.EXPAND)
        caja1.Add(caja4, proportion = 1, flag = wx.LEFT | wx.RIGHT | wx.EXPAND, border=10)
        caja1.Add((-1, 25))
        caja5 = wx.BoxSizer(wx.HORIZONTAL)
        cb1 = wx.CheckBox(self.panel, -1, "distingue entre mayúsculas y minúsculas")
        cb1.SetFont(fuente)
        caja5.Add(cb1)
        cb2 = wx.CheckBox(self.panel, label = "clase anidada")
        cb2.SetFont(fuente)
        caja5.Add(cb2, flag = wx.LEFT, border = 10)
        cb3 = wx.CheckBox(self.panel, label = "Clases y proyectos")
        cb3.SetFont(fuente)
        caja5.Add(cb3, flag = wx.LEFT, border = 10)
        caja1.Add(caja5, flag = wx.Left, border = 10)
        caja1.Add((-1, 25))
        caja6 = wx.BoxSizer(wx.HORIZONTAL)
        bonton_Aceptar = wx.Button(self.panel, label = "Aceptar", size = (70, 30))
        caja6.Add(bonton_Aceptar)
        boton_Cerrar = wx.Button(self.panel, label = "Cerrar", size = (90, 30))
        caja6.Add(boton_Cerrar, flag = wx.LEFT | wx.BOTTOM, border = 5)
        caja1.Add(caja6, flag = wx.ALIGN_RIGHT | wx.RIGHT, border = 10)
        self.panel.SetSizer(caja1)
        self.panel.Layout()
        self.Show(True)


def main():
    app = wx.App()
    objeto = DimencionadoresImportantes(None, "Dimencionadores importantes")
    app.MainLoop()

if __name__ == "__main__":
    main()
