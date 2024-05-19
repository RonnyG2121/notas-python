


import wx
import wx.adv


id_Acerca = 1

class DialogoAcercaDe(wx.Frame):
    def __init__(self, *args, **kw):
        super(DialogoAcercaDe, self).__init__(*args, **kw)
        self.Contenedor()
        self.SetTitle("Diálogo Acerca De")
        self.Centre()
        self.SetSize((300, 250))
        self.Show(True)
    def Contenedor(self):
        barraAyuda = wx.MenuBar()
        ayudaMenu = wx.Menu()
        ayudaMenu.Append(id_Acerca, "&Acerca De")
        ayudaMenu.Bind(wx.EVT_MENU, self.OnAcercaD, id= id_Acerca)
        barraAyuda.Append(ayudaMenu, "Ayuda")
        self.SetMenuBar(barraAyuda)
    def OnAcercaD(self, evento):
        descripcion = """File Hunter is an advanced file manager for the
Unix operating
system. Features include powerful built-in editor, advanced search
capabilities,
powerful batch renaming, file comparison, extensive archive handling y more.
"""
        licencia = """File Hunter is free software; you can redistribute
it and/or modify it under the terms of the GNU General Public License as
published by the Free Software Foundation; either version 2 of the License,
or (at your option) any later version.
File Hunter is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU General Public License for more details. You should have
received a copy of the GNU General Public License along with File Hunter;
if not, write to the Free Software Foundation, Inc., 59 Temple Place,
Suite 330, Boston, MA  02111-1307  USA"""
        info = wx.adv.AboutDialogInfo()

        info.SetName('File Hunter')
        info.SetVersion('1.0')
        info.SetDescription(descripcion)
        info.SetCopyright('(C) 2007 - 2022 Jan Bodnar')
        info.SetWebSite('http://www.zetcode.com')
        info.SetLicence(licencia)
        info.AddDeveloper('Jan Bodnar')
        info.AddDocWriter('Jan Bodnar')
        info.AddArtist('The Tango crew')
        info.AddTranslator('Jan Bodnar')
        wx.adv.AboutBox(info)


if __name__ == "__main__":
    app = wx.App()
    DialogoAcercaDe(None)
    app.MainLoop()

