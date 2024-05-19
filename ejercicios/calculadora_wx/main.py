import wx


index = 0


class CalculadoraWX(wx.Frame):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        self.SetTitle("Calculadora WX")
        self.Centre()
        self.SetSize((600, 400))
        self.Show(True)
        self._InitUI()

    def _InitUI(self):
        self.panel = wx.Panel(self, wx.ID_ANY)
        self.grid = wx.GridSizer(7, 5, 5, 5)  # 7 filas, 5 columnas, 5px de espacio

        self.lb_text = wx.StaticText(self.panel, wx.ID_ANY, "Ingrese valores")
        self.tb_valores = wx.TextCtrl(self.panel, wx.ID_EDIT)
        self.btn_open_paren = wx.Button(self.panel, wx.ID_ANY, "(")
        self.btn_close_paren = wx.Button(self.panel, wx.ID_ANY, ")")

        self.btn_1 = wx.Button(self.panel, wx.ID_ANY, "1")
        self.btn_2 = wx.Button(self.panel, wx.ID_ANY, "2")
        self.btn_3 = wx.Button(self.panel, wx.ID_ANY, "3")
        self.btn_add = wx.Button(self.panel, wx.ID_ANY, "+")
        self.btn_4 = wx.Button(self.panel, wx.ID_ANY, "4")
        self.btn_5 = wx.Button(self.panel, wx.ID_ANY, "5")
        self.btn_6 = wx.Button(self.panel, wx.ID_ANY, "6")
        self.btn_sub = wx.Button(self.panel, wx.ID_ANY, "-")
        self.btn_7 = wx.Button(self.panel, wx.ID_ANY, "7")
        self.btn_8 = wx.Button(self.panel, wx.ID_ANY, "8")
        self.btn_9 = wx.Button(self.panel, wx.ID_ANY, "9")
        self.btn_mul = wx.Button(self.panel, wx.ID_ANY, "*")
        self.btn_clear = wx.Button(self.panel, wx.ID_ANY, "C")
        self.btn_0 = wx.Button(self.panel, wx.ID_ANY, "0")
        self.btn_point = wx.Button(self.panel, wx.ID_ANY, ".")
        self.btn_eq = wx.Button(self.panel, wx.ID_ANY, "=")
        self.btn_div = wx.Button(self.panel, wx.ID_ANY, "/")

        # añadiendo eventos a los botones
        self.Bind(wx.EVT_BUTTON, lambda event: self.get_numbers("1"), self.btn_1)
        self.Bind(wx.EVT_BUTTON, lambda event: self.get_numbers("2"), self.btn_2)
        self.Bind(wx.EVT_BUTTON, lambda event: self.get_numbers("3"), self.btn_3)
        self.Bind(wx.EVT_BUTTON, lambda event: self.get_numbers("4"), self.btn_4)
        self.Bind(wx.EVT_BUTTON, lambda event: self.get_numbers("5"), self.btn_5)
        self.Bind(wx.EVT_BUTTON, lambda event: self.get_numbers("6"), self.btn_6)
        self.Bind(wx.EVT_BUTTON, lambda event: self.get_numbers("7"), self.btn_7)
        self.Bind(wx.EVT_BUTTON, lambda event: self.get_numbers("8"), self.btn_8)
        self.Bind(wx.EVT_BUTTON, lambda event: self.get_numbers("9"), self.btn_9)
        self.Bind(wx.EVT_BUTTON, lambda event: self.get_numbers("0"), self.btn_0)

        self.Bind(wx.EVT_BUTTON, lambda event: self.getOperator("+"), self.btn_add)
        self.Bind(wx.EVT_BUTTON, lambda event: self.getOperator("+"), self.btn_add)
        self.Bind(wx.EVT_BUTTON, lambda event: self.getOperator("-"), self.btn_sub)
        self.Bind(wx.EVT_BUTTON, lambda event: self.getOperator("*"), self.btn_mul)
        self.Bind(wx.EVT_BUTTON, lambda event: self.getOperator("/"), self.btn_div)

        self.Bind(wx.EVT_BUTTON, self.limpiar, self.btn_clear)

        self.Bind(wx.EVT_BUTTON, self.igual, self.btn_eq)
        # Añadiendo componentes al grid
        self.grid.AddMany(
            [
                (self.lb_text, 0, wx.EXPAND),
                (self.tb_valores, 0, wx.EXPAND),
                (
                    wx.StaticText(self.panel),
                    0,
                    wx.EXPAND,
                ),  # Espacio vacío para alineación
                (self.btn_open_paren, 0, wx.EXPAND),
                (self.btn_close_paren, 0, wx.EXPAND),
                (
                    wx.StaticText(self.panel),
                    0,
                    wx.EXPAND,
                ),  # Espacio vacío para alineación
                (self.btn_7, 0, wx.EXPAND),
                (self.btn_8, 0, wx.EXPAND),
                (self.btn_9, 0, wx.EXPAND),
                (self.btn_div, 0, wx.EXPAND),
                (self.btn_4, 0, wx.EXPAND),
                (self.btn_5, 0, wx.EXPAND),
                (self.btn_6, 0, wx.EXPAND),
                (self.btn_mul, 0, wx.EXPAND),
                (self.btn_1, 0, wx.EXPAND),
                (self.btn_2, 0, wx.EXPAND),
                (self.btn_3, 0, wx.EXPAND),
                (self.btn_sub, 0, wx.EXPAND),
                (self.btn_clear, 0, wx.EXPAND),
                (self.btn_0, 0, wx.EXPAND),
                (self.btn_point, 0, wx.EXPAND),
                (self.btn_eq, 0, wx.EXPAND),
                (self.btn_add, 0, wx.EXPAND),
            ]
        )

        self.panel.SetSizer(self.grid)
        self.panel.Layout()
        self.panel.Fit()
        self.panel.SetFocus()

    # Eventos
    def get_numbers(self, n):
        global index
        self.tb_valores.SetInsertionPoint(index)
        self.tb_valores.WriteText(n)
        index += 1

    def getOperator(self, operator):
        global index
        longitudoperator = len(operator)
        self.tb_valores.SetInsertionPoint(index)
        self.tb_valores.WriteText(operator)
        index += longitudoperator

    def igual(self, event):
        operacion = self.tb_valores.GetValue()
        try:
            resultado = eval(operacion)
            self.tb_valores.setValue("")
            self.tb_valores.SetValue(resultado)

        except Exception as e:
            self.tb_valores.SetValue("Error de la operación")

    def limpiar(self, event):
        self.tb_valores.SetValue("")

    def igual(self, event):
        operacion = self.tb_valores.GetValue()
        try:
            resultado = eval(operacion)
            self.tb_valores.setValue("")
            self.tb_valores.SetValue(resultado)

        except Exception as e:
            self.tb_valores.SetValue("Error de la operación")


if __name__ == "__main__":
    app = wx.App()
    frame = CalculadoraWX(None)
    app.MainLoop()
