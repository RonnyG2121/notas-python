# Programa en wxpython que muestra una lista de texto
import wx

class MuestraTexto(wx.Frame):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        # Estableciendo propieddades
        self.SetTitle("Muestra Textos")
        self.SetSize((600, 600))
        self.Show(True)
        self.InitUI()
    # Método principal de la ventana
    def InitUI(self):
        # Creando un panel
        self.panel = wx.Panel(self, -1)
        # Creando contenedor
        self.caja = wx.BoxSizer(wx.HORIZONTAL)
        # Cuadro de texto y su label
        self.lb_Text = wx.StaticText(self.panel, wx.ID_ANY, label="Ingrese Texto aquí")
        self.texto = wx.TextCtrl(self.panel, wx.ID_EDIT,style=wx.TE_CENTRE | wx.TE_PROCESS_ENTER)
        # Estableciendo el foco en el cuadro de texto
        self.texto.SetFocus()
        # Evento del cuadro de texto al pulsar enter
        self.Bind(wx.EVT_TEXT_ENTER, self.OnEnviar, self.texto)
        # Botón que envía la información a la lista
        self.btnEnviar = wx.Button(self.panel, wx.ID_ADD, label="Agregar texto a la lista")
        # Evento para el botón
        self.Bind(wx.EVT_BUTTON, self.OnEnviar, self.btnEnviar)
        # Botón para salir de la aplicación
        self.btn_Salir = wx.Button(self.panel, wx.ID_CLOSE,  label="Cerrar")
        # Conectando evento salir
        self.Bind(wx.EVT_BUTTON, self.OnSalir, self.btn_Salir)
        # Lista que mostrará los elementos y su label
        self.lb_Lista = wx.StaticText(self.panel, wx.ID_ANY, label="Lista de Textos agregados")
        self.lista = wx.ListBox(self.panel, wx.ID_ANY, style=wx.CB_READONLY)

        # Agregando todos los elementos a el contenedor
        self.caja.Add(self.lb_Text)
        self.caja.Add(self.texto)
        self.caja.Add(self.btnEnviar)
        # Creando un contenedor a parte para la lista
        self.caja_Lista = wx.BoxSizer(wx.VERTICAL)
        self.caja_Lista.Add(self.lb_Lista)
        self.caja_Lista.Add(self.lista)
        self.caja.Add(self.btn_Salir)
        self.caja.Add(self.caja_Lista)
        
        # Estableciendo el contenedor principal en el panel
        self.panel.SetSizer(self.caja)
        self.panel.SetFocus()
        self.panel.Fit()
        self.panel.Layout()

    # Eventos del programa
    def OnEnviar(self, event):
        self.lista.Append(self.texto.GetValue())
        # Limpiando el cuadro de texto
        self.texto.Clear()
    # Evento salir
    def OnSalir(self, event):
        self.Close(True)


# Esto permitirá que se ejecute en consola el programa
if __name__ == "__main__":
    # Creando objeto aplicación
    app = wx.App()
    MuestraTexto(None)
    app.MainLoop()