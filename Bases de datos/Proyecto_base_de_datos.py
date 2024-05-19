
import wx

import re

import sqlite3


class BaseDDato(wx.Frame):
    def __init__(self, *args, **kw):
        super(BaseDDato, self).__init__(*args, **kw)
        self.Menu_Principal()
        self.Botones()      
        self.Centre()
        self.SetTitle("Administrador De Base De Datos")
        self.SetSize((600, 400))
        self.Show(True)
    def Menu_Principal(self):
        # creando unos menús 

        self.barramenu = wx.MenuBar()

        self.menu_base = wx.Menu()
        self.crear_base = wx.MenuItem(self.menu_base, wx.ID_ANY, "&Crear nueva base de datos\tCtrl+n")
        self.Bind(wx.EVT_MENU, self.ConectaBaseDDatos, self.crear_base)
        self.menu_base.Append(self.crear_base)

        self.CRUD = wx.Menu()
        self.insertar = wx.MenuItem(self.CRUD, wx.ID_ANY, "&Insertar registros en la Base de datos\tCtrl+i")
        self.Bind(wx.EVT_MENU, self.OnCrear, self.insertar)
        self.leer = wx.MenuItem(self.CRUD, wx.ID_ANY, "&Leer Base de datos\tCtrl+l")
        self.Bind(wx.EVT_MENU, self.AceptaNumero, self.leer)
        self.actualizar = wx.MenuItem(self.CRUD, wx.ID_ANY, "&Actualizar registros\tCtrl+a")
        self.Bind(wx.EVT_MENU, self.PideYActualiza, self.actualizar)
        self.borrar = wx.MenuItem(self.CRUD, wx.ID_ANY, "&Borrar registros\tCtrl+b")
        self.Bind(wx.EVT_MENU, self.PideYBorra, self.borrar)
        self.CRUD.Append(self.insertar)
        self.CRUD.Append(self.leer)
        self.CRUD.Append(self.borrar)
        self.CRUD.Append(self.actualizar)
        self.menu_base.Append(wx.ID_ANY, "&CRUD", self.CRUD)
        self.ayuda_menu = wx.Menu()
        self.acerca = wx.MenuItem(self.ayuda_menu, wx.ID_ANY, "&Acerca del programa\tAtl+a")
        self.licencia = wx.MenuItem(self.ayuda_menu, wx.ID_ANY, "&Licencia\tAlt+Ctrl+l")
        self.ayuda_menu.Append(self.acerca)
        self.ayuda_menu.Append(self.licencia)
        self.menu_base.Append(wx.ID_ANY, "&Ayuda", self.ayuda_menu)

        self.salir = wx.MenuItem(self.menu_base, wx.ID_ANY, "&salir\tAlt+s")
        self.Bind(wx.EVT_MENU, self.OnSalir, self.salir)
        self.menu_base.Append(self.salir)

        self.barramenu.Append(self.menu_base, "&Menú De Opciones")
        self.SetMenuBar(self.barramenu)

# Función para conectar la base de datos
    def ConectaBaseDDatos(self, evento):
        self.miConexion = sqlite3.connect("base.db")
        self.puntero = self.miConexion.cursor()
        try:
            self.puntero.execute("""CREATE TABLE usuarios(
                CampoID INTEGER PRIMARY KEY AUTOINCREMENT, 
                CampoNombre TEXT(50), 
                CampoContraseña VARCHAR(15), 
                CampoApellido TEXT(50),
                CampoDireccion VARCHAR(100), 
                CampoComentario VARCHAR(500) )""")
            self.mensaje = wx.MessageBox("Base de datos creada exitosamente", "Información: ", wx.ICON_INFORMATION)
        except:
            self.mensaje2 = wx.MessageBox("La base de datos ya existe.", "¡Atención!", style= wx.ICON_EXCLAMATION)


# Función salir

    def OnSalir(self, evento):
        self.pregunta = wx.MessageBox("¿Desea salir?", "Pregunta: ", style= wx.ICON_QUESTION | wx.YES_NO | wx.NO_DEFAULT)
        if self.pregunta == wx.YES:
            self.Close(True)
        else:
            evento.Skyp()



# función botones principales



    def Botones(self):
        self.Mi_panel = wx.Panel(self, -1)
        self.caja = wx.BoxSizer(wx.HORIZONTAL)
        self.Boton_Crear = wx.Button(self.Mi_panel, wx.ID_ANY, label = "Insertar registros en la  Base De Datos")
        self.Boton_Crear.SetFocus()
        self.Boton_Crear.Bind(wx.EVT_BUTTON, self.OnCrear)
        self.caja.Add(self.Boton_Crear)
        self.Boton_Leer = wx.Button(self.Mi_panel, wx.ID_ANY, label = "Leer Base De datos")
        self.Boton_Leer.Bind(wx.EVT_BUTTON, self.AceptaNumero)
        self.caja.Add(self.Boton_Leer)
        self.BTN_Actualizar = wx.Button(self.Mi_panel, wx.ID_ANY, label = "Actualizar")
        self.BTN_Actualizar.Bind(wx.EVT_BUTTON, self.PideYActualiza)
        self.caja.Add(self.BTN_Actualizar)
        self.Boton_Eliminar= wx.Button(self.Mi_panel, wx.ID_ANY, label = "Borrar Los Campos")
        self.Boton_Eliminar.Bind(wx.EVT_BUTTON, self.PideYBorra)
        self.caja.Add(self.Boton_Eliminar)
        self.Mi_panel.SetSizer(self.caja)
        self.Mi_panel.Layout()
        self.Mi_panel.Fit()


# Función crear

    def OnCrear(self, event):
        self.Ventana_Dialogo = wx.Dialog(self, -1, "Ingrese los datos para la base de datos")
        self.cajaDialogo = wx.BoxSizer(wx.HORIZONTAL)
        self.label_Id = wx.StaticText(self.Ventana_Dialogo, wx.ID_ANY, label = "Introduzca el ID")
        self.cajaDialogo.Add(self.label_Id)
        self.Campo_id = wx.TextCtrl(self.Ventana_Dialogo, wx.ID_ANY)
        self.cajaDialogo.Add(self.Campo_id)
        self.label_Nombre = wx.StaticText(self.Ventana_Dialogo, wx.ID_ANY, label = "Introduzca el Nombre")
        self.cajaDialogo.Add(self.label_Nombre)
        self.Campo_Nombre = wx.TextCtrl(self.Ventana_Dialogo, wx.ID_ANY, style = wx.TE_CENTRE)
        self.cajaDialogo.Add(self.Campo_Nombre)
        self.label_Contraseña = wx.StaticText(self.Ventana_Dialogo, wx.ID_ANY, label = "Introduzca la contraseña")
        self.cajaDialogo.Add(self.label_Contraseña)
        self.Campo_Contraseña = wx.TextCtrl(self.Ventana_Dialogo, wx.ID_ANY, style = wx.TE_PASSWORD | wx.TE_CENTRE)
        self.cajaDialogo.Add(self.Campo_Contraseña)
        self.label_Apellido = wx.StaticText(self.Ventana_Dialogo, wx.ID_ANY, label = "Introduzca el apellido")
        self.cajaDialogo.Add(self.label_Apellido)
        self.Campo_Apellido = wx.TextCtrl(self.Ventana_Dialogo, wx.ID_ANY, style = wx.TE_CENTRE)
        self.cajaDialogo.Add(self.Campo_Apellido)
        self.label_Direccion = wx.StaticText(self.Ventana_Dialogo, wx.ID_ANY, label = "Introduzca la dirección")
        self.cajaDialogo.Add(self.label_Direccion)
        self.Campo_Direccion = wx.TextCtrl(self.Ventana_Dialogo, wx.ID_ANY, style = wx.TE_CENTRE)
        self.cajaDialogo.Add(self.Campo_Direccion)
        self.label_Comentario = wx.StaticText(self.Ventana_Dialogo, wx.ID_ANY, label = "Introduzca un comentario")
        self.cajaDialogo.Add(self.label_Comentario)
        self.Campo_Comentario = wx.TextCtrl(self.Ventana_Dialogo, wx.ID_ANY, style = wx.TE_MULTILINE)
        self.cajaDialogo.Add(self.Campo_Comentario)
        self.Boton_Guardar = wx.Button(self.Ventana_Dialogo, wx.ID_SAVE, label = "&   Guardar Cambios \tAlt+g")
        self.Boton_Guardar.Bind(wx.EVT_BUTTON, self.OnGuardaDatos)
        self.cajaDialogo.Add(self.Boton_Guardar)
        self.Boton_Cancelar = wx.Button(self.Ventana_Dialogo, wx.ID_CANCEL, label = "&Cancelar\tAlt+c")
        self.cajaDialogo.Add(self.Boton_Cancelar)
        self.Ventana_Dialogo.SetSizer(self.cajaDialogo)
        self.Ventana_Dialogo.Layout()
        self.Ventana_Dialogo.Fit()
        self.Ventana_Dialogo.ShowModal()

# Función que guarda los datos en la tabla
    def OnGuardaDatos(self, evento):
        self.Guardar = sqlite3.connect("base.db")
        self.puntero2 = self.Guardar.cursor()
        self.listaTabla = [self.Campo_id.GetValue(), self.Campo_Nombre.GetValue(), self.Campo_Contraseña.GetValue(), self.Campo_Apellido.GetValue(), self.Campo_Direccion.GetValue(), self.Campo_Comentario.GetValue()]
        self.puntero2.execute("""
        INSERT INTO usuarios(
            CampoID,
            CampoNombre,
            CampoContraseña,
            CampoApellido,
            CampoDireccion,
            CampoComentario)
            VALUES(?, ?, ?, ?, ?, ?)""", self.listaTabla)
        self.Guardar.commit()
        self.Guardar.close()
        self.mensaje3 = wx.MessageBox("Los registros han sido insertados exitosamente", "Información", style= wx.ICON_INFORMATION)
        self.Ventana_Dialogo.Destroy()



# Función para el método aceptar de la función leer
    def AceptaNumero(self, evento):
        self.dlg_aseptarnum = wx.Dialog(self, wx.ID_ANY, "Escriba su id para ver sus datos")
        self.caja3 = wx.BoxSizer(wx.VERTICAL)
        self.lb1 = wx.StaticText(self.dlg_aseptarnum, wx.ID_ANY, "Escriba su id")
        self.text1 = wx.TextCtrl(self.dlg_aseptarnum, wx.ID_ANY, style = wx.TE_CENTRE)
        self.btn_Aceptar = wx.Button(self.dlg_aseptarnum, wx.ID_ANY, "Aceptar")
        self.btn_Aceptar.Bind(wx.EVT_BUTTON, self.OnLeer)
        self.btn_Cancelar = wx.Button(self.dlg_aseptarnum, wx.ID_CANCEL, "Cancelar")
        self.caja3.Add(self.lb1)
        self.caja3.Add(self.text1)
        self.caja3.Add(self.btn_Aceptar)
        self.caja3.Add(self.btn_Cancelar)
        self.dlg_aseptarnum.SetSizer(self.caja3)
        self.dlg_aseptarnum.Layout()
        self.dlg_aseptarnum.Fit()
        self.dlg_aseptarnum.ShowModal()
        self.dlg_aseptarnum.Destroy()


# función que muestra los datos según el id en campos de texto de solo lectura, y cuando no se encuentra el id mostrar un mensaje de error
    def OnLeer(self, evento):
        self.Leer = sqlite3.connect("base.db")
        self.puntero3 = self.Leer.cursor()
        self.id = [self.text1.GetValue()]
        self.puntero3.execute("SELECT * FROM usuarios WHERE CampoID = ?", self.id)
        self.resultado = self.puntero3.fetchone()
        if self.resultado == None:
            self.mensaje4 = wx.MessageBox("No se encontró el id", "Error", style = wx.ICON_ERROR)
            self.text1.SetValue("")
            self.text1.SetFocus()
        else:
            self.dlg_aseptarnum.Destroy()
            self.dlg_aseptarnum = wx.Dialog(self, wx.ID_ANY, "Los datos del id " + str(self.id) + " son:")
            self.caja4 = wx.BoxSizer(wx.HORIZONTAL)
            self.lb2 = wx.StaticText(self.dlg_aseptarnum, wx.ID_ANY, "Nombre")
            self.text2 = wx.TextCtrl(self.dlg_aseptarnum, wx.ID_ANY, self.resultado[1], style = wx.TE_READONLY | wx.TE_MULTILINE)
            self.lb3 = wx.StaticText(self.dlg_aseptarnum, wx.ID_ANY, "Contraseña")
            self.text3 = wx.TextCtrl(self.dlg_aseptarnum, wx.ID_ANY, self.resultado[2], style = wx.TE_READONLY | wx.TE_MULTILINE)
            self.lb4 = wx.StaticText(self.dlg_aseptarnum, wx.ID_ANY, "Apellido")
            self.text4 = wx.TextCtrl(self.dlg_aseptarnum, wx.ID_ANY, self.resultado[3], style = wx.TE_READONLY | wx.TE_MULTILINE)
            self.lb5 = wx.StaticText(self.dlg_aseptarnum, wx.ID_ANY, "Dirección")
            self.text5 = wx.TextCtrl(self.dlg_aseptarnum, wx.ID_ANY, self.resultado[4], style = wx.TE_READONLY | wx.TE_MULTILINE)
            self.lb6 = wx.StaticText(self.dlg_aseptarnum, wx.ID_ANY, "Comentario")
            self.text6 = wx.TextCtrl(self.dlg_aseptarnum, wx.ID_ANY, self.resultado[5], style = wx.TE_READONLY | wx.TE_MULTILINE)
            self.btn_Cerrar = wx.Button(self.dlg_aseptarnum, wx.ID_CANCEL, "Cerrar")
            self.caja4.Add(self.lb2)
            self.caja4.Add(self.text2)
            self.caja4.Add(self.lb3)
            self.caja4.Add(self.text3)
            self.caja4.Add(self.lb4)
            self.caja4.Add(self.text4)
            self.caja4.Add(self.lb5)
            self.caja4.Add(self.text5)
            self.caja4.Add(self.lb6)
            self.caja4.Add(self.text6)
            self.caja4.Add(self.btn_Cerrar)
            self.dlg_aseptarnum.SetSizer(self.caja4)
            self.dlg_aseptarnum.Layout()
            self.dlg_aseptarnum.Fit()
            self.dlg_aseptarnum.ShowModal()
            self.dlg_aseptarnum.Destroy()

# Función que pide los datos para actualizarlos

    def PideYActualiza(self, evento):
        self.Ventana_Dialogo = wx.Dialog(self.Mi_panel, wx.ID_ANY, "Escriba aquí los datos para actualizar")
        self.cajaDialogo = wx.BoxSizer(wx.HORIZONTAL)
        self.label_Id = wx.StaticText(self.Ventana_Dialogo, wx.ID_ANY, label = "Introduzca el ID")
        self.cajaDialogo.Add(self.label_Id)
        self.Campo_id = wx.TextCtrl(self.Ventana_Dialogo, wx.ID_ANY)
        self.cajaDialogo.Add(self.Campo_id)
        self.label_Nombre = wx.StaticText(self.Ventana_Dialogo, wx.ID_ANY, label = "Introduzca el Nombre")
        self.cajaDialogo.Add(self.label_Nombre)
        self.Campo_Nombre = wx.TextCtrl(self.Ventana_Dialogo, wx.ID_ANY, style = wx.TE_CENTRE)
        self.cajaDialogo.Add(self.Campo_Nombre)
        self.label_Contraseña = wx.StaticText(self.Ventana_Dialogo, wx.ID_ANY, label = "Introduzca la contraseña")
        self.cajaDialogo.Add(self.label_Contraseña)
        self.Campo_Contraseña = wx.TextCtrl(self.Ventana_Dialogo, wx.ID_ANY, style = wx.TE_PASSWORD | wx.TE_CENTRE)
        self.cajaDialogo.Add(self.Campo_Contraseña)
        self.label_Apellido = wx.StaticText(self.Ventana_Dialogo, wx.ID_ANY, label = "Introduzca el apellido")
        self.cajaDialogo.Add(self.label_Apellido)
        self.Campo_Apellido = wx.TextCtrl(self.Ventana_Dialogo, wx.ID_ANY, style = wx.TE_CENTRE)
        self.cajaDialogo.Add(self.Campo_Apellido)
        self.label_Direccion = wx.StaticText(self.Ventana_Dialogo, wx.ID_ANY, label = "Introduzca la dirección")
        self.cajaDialogo.Add(self.label_Direccion)
        self.Campo_Direccion = wx.TextCtrl(self.Ventana_Dialogo, wx.ID_ANY, style = wx.TE_CENTRE)
        self.cajaDialogo.Add(self.Campo_Direccion)
        self.label_Comentario = wx.StaticText(self.Ventana_Dialogo, wx.ID_ANY, label = "Introduzca un comentario")
        self.cajaDialogo.Add(self.label_Comentario)
        self.Campo_Comentario = wx.TextCtrl(self.Ventana_Dialogo, wx.ID_ANY, style = wx.TE_MULTILINE)
        self.cajaDialogo.Add(self.Campo_Comentario)
        self.Boton_Actualizar = wx.Button(self.Ventana_Dialogo, wx.ID_SAVE, label = "&Actualizar Cambios y guardar\tAlt+a")
        self.Boton_Actualizar.Bind(wx.EVT_BUTTON, self.ActualizaDatos)
        self.cajaDialogo.Add(self.Boton_Actualizar)
        self.Boton_Cancelar = wx.Button(self.Ventana_Dialogo, wx.ID_CANCEL, label = "&Cancelar\tAlt+c")
        self.cajaDialogo.Add(self.Boton_Cancelar)
        self.Ventana_Dialogo.SetSizer(self.cajaDialogo)
        self.Ventana_Dialogo.Layout()
        self.Ventana_Dialogo.Fit()
        self.Ventana_Dialogo.ShowModal()

# Función para actualizar los datos
    def ActualizaDatos(self, evento):
        self.update_Datos = sqlite3.connect("base.db")
        self.puntero4 = self.update_Datos.cursor()
        self.listaTabla = (self.Campo_Nombre.GetValue(), self.Campo_Contraseña.GetValue(), self.Campo_Apellido.GetValue(), self.Campo_Direccion.GetValue(), self.Campo_Comentario.GetValue(), self.Campo_id.GetValue())
        self.puntero4.execute("UPDATE usuarios SET CampoNombre = ?, CampoContraseña =?, CampoApellido = ?, CampoDireccion = ?, CampoComentario = ? WHERE CampoID = ?", self.listaTabla)
        self.update_Datos.commit()
        self.update_Datos.close()
        self.mensaje4 = wx.MessageBox("Los registros han sido actualizados exitosamente", "Información", style= wx.ICON_INFORMATION)
        self.Ventana_Dialogo.Destroy()


# Función que pide el ID para eliminarlo de la base de datos
    def PideYBorra(self, event):
        self.dialBorrar = wx.Dialog(self, -1, "Escriba el ID de la persona a eliminar")
        self.cajaBorra = wx.BoxSizer(wx.VERTICAL)
        self.lbBorrar = wx.StaticText(self.dialBorrar, wx.ID_ANY, "Escriba el ID a borrar")
        self.cajaBorra.Add(self.lbBorrar)
        self.textBorrar = wx.TextCtrl(self.dialBorrar, wx.ID_ANY)
        self.cajaBorra.Add(self.textBorrar)
        self.Elimina = wx.Button(self.dialBorrar, wx.ID_DELETE, "Borrar ID seleccionado")
        self.Elimina.Bind(wx.EVT_BUTTON, self.BorraDatos)
        self.cajaBorra.Add(self.Elimina)
        self.Cancelar = wx.Button(self.dialBorrar, wx.ID_CANCEL, "&Calcelar\tAlt+c")
        self.cajaBorra.Add(self.Cancelar)
        self.dialBorrar.SetSizer(self.cajaBorra)
        self.dialBorrar.Layout()
        self.dialBorrar.Fit()
        self.dialBorrar.ShowModal()

#Función que borra los datos de la tabla

    def BorraDatos(self, evento):
        self.borra_Datos = sqlite3.connect("base.db")
        self.puntero3 = self.borra_Datos.cursor()
        self.listaBorrar = (self.textBorrar.GetValue(),)
        # comprovar si se ingresan letras mosrar un mensaje de error
        expresion = re.compile("^[0-9]+$")
        if self.textBorrar.GetValue() == "":
            self.mensaje2 = wx.MessageBox("No se ha escrito ningún ID", "Error", style = wx.ICON_ERROR)
            self.textBorrar.SetFocus()
        else:
            # comprovar si se ingresan letras borrar un mensaje de error
            if expresion.match(self.textBorrar.GetValue()):
                # comprobar si existe el ID
                if self.puntero3.execute("SELECT * FROM usuarios WHERE CampoID = ?", self.listaBorrar).fetchone() == None:
                    self.mensaje3 = wx.MessageBox("El ID no existe", "Error", style = wx.ICON_ERROR)
                    self.textBorrar.SetFocus()
                    self.textBorrar.SetValue("")
                else:
                    self.puntero3.execute("DELETE FROM usuarios WHERE CampoID = ?", self.listaBorrar)
                    self.borra_Datos.commit()
                    self.borra_Datos.close()
                    self.mensaje4 = wx.MessageBox("El ID ha sido borrado", "Información", style = wx.ICON_INFORMATION)
                    self.dialBorrar.Destroy()
            else:
                self.mensaje2 = wx.MessageBox("El ID debe ser un número", "Error", style = wx.ICON_ERROR)
                self.textBorrar.SetFocus()
                self.textBorrar.SetValue("")

# Creamos una condicional para que el programa se abra desde la consola y creamos el frame que va a manejar la ventana

if __name__ == "__main__":
    app = wx.App()
    BaseDDato(None)
app.MainLoop()  