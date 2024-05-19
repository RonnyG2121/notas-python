#Creando una ventana que no se puede minimizar

import wx

app = wx.App()
ventana = wx.Frame(None, style = wx.MAXIMIZE_BOX | wx.RESIZE_BORDER | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)
ventana.Show()
app.MainLoop()
