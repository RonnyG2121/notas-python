# En Este Ejemplo creo una ventana simple
# Importando librería

import wx # Esta librería también es un NameSpace o espacio de nombre

# Estructura de la ventana


app = wx.App() # Esto es un Objeto de tipo aplicación
# la ventana
ventana = wx.Frame(None, -1, "Ventana simple") # Esta es la base principal de la ventana
ventana.Show() # Esto ppermite mostrar u ocultar la ventana. dentro de los paréntesis se pueden poner True o False dependiendo

app.MainLoop() # Esto Crea una especie de bucle infinito para que se ejecute la ventana
