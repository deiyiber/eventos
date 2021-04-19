#!/usr/bin/env python
# coding: utf-8

# In[50]:


#IMPORTAMOS LIBRERÍAS NECESARIAS.
from tkinter import *
import tkinter as tk
import pymysql
import pandas as pd
from pandastable import Table, TableModel
#CREAMOS VENTANA PRINCIPAL.
def ventana_inicio():
    global ventana_principal
    pestas_color="DarkGrey"
    ventana_principal=tk.Tk()
    ventana_principal.geometry("300x250")
    ventana_principal.title("Eventos & Reuniones")
    Label(text="Elige tu opción", bg="LightGreen", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Acceder", height="2", width="30", bg=pestas_color, command=login).pack()
    Label(text="").pack()
    Button(text="Registrarse", height="2", width="30", bg=pestas_color, command=registro).pack()
    Label(text="").pack()
    ventana_principal.mainloop()
    
#CREAMOS VENTANA PARA REGISTRO.
def registro():
    global ventana_registro
    ventana_registro = Toplevel(ventana_principal)
    ventana_registro.title("Registro")
    ventana_registro.geometry("350x350")
    #---------
    global nombre_usuario1
    nombre_usuario1 = StringVar()
    global apellidos_usuario
    apellidos_usuario =StringVar()
    global email_usuario
    email_usuario=StringVar()
    global cargo_usuario
    cargo_usuario =StringVar()
    #------- 
    global nombre_usuario
    global clave
    global entrada_nombre
    global entrada_clave
    nombre_usuario = IntVar() 
    clave = StringVar()
 
    Label(ventana_registro, text="Introduzca datos", bg="LightGreen").pack()
    Label(ventana_registro, text="").pack()
    #------------------------------------
    etiqueta_nombre1 = Label(ventana_registro, text="Nombre de usuario * ")
    etiqueta_nombre1.pack()
    entrada_nombre1 = Entry(ventana_registro, textvariable=nombre_usuario1)
    entrada_nombre1.pack()
    etiqueta_apellido = Label(ventana_registro, text="Apellido de usuario * ")
    etiqueta_apellido.pack()
    etiqueta_apellido = Entry(ventana_registro, textvariable=apellidos_usuario)
    etiqueta_apellido.pack()
    etiqueta_email = Label(ventana_registro, text="Email de usuario * ")
    etiqueta_email.pack()
    etiqueta_email = Entry(ventana_registro, textvariable=email_usuario)
    etiqueta_email.pack()
    etiqueta_cargo = Label(ventana_registro, text="Cargo de usuario * ")
    etiqueta_cargo.pack()
    etiqueta_cargo = Entry(ventana_registro, textvariable=cargo_usuario)
    etiqueta_cargo.pack()
    #-------------------------------------------------
    etiqueta_nombre = Label(ventana_registro, text="Id Usuario Ingreso * ")
    etiqueta_nombre.pack()
    entrada_nombre = Entry(ventana_registro, textvariable=nombre_usuario)
    entrada_nombre.pack()
    etiqueta_clave = Label(ventana_registro, text="Contraseña * ")
    etiqueta_clave.pack()
    entrada_clave = Entry(ventana_registro, textvariable=clave, show='*') 
    entrada_clave.pack()
    Label(ventana_registro, text="").pack()
    Button(ventana_registro, text="Registrarse", width=10, height=1, bg="LightGreen", command = ingreso_usuario_clave).pack()
    

#CREAMOS VENTANA PARA LOGIN.

def login():
    global ventana_login
    ventana_login = Toplevel(ventana_principal)
    ventana_login.title("Acceso a la cuenta")
    ventana_login.geometry("300x280")
    Label(ventana_login, text="Introduzca nombre de usuario y contraseña").pack()
    Label(ventana_login, text="").pack()
    global verifica_usuario
    global verifica_clave
    verifica_usuario = IntVar()
    verifica_clave = StringVar()
    global entrada_login_usuario
    global entrada_login_clave
    Label(ventana_login, text="ID usuario * ").pack()
    entrada_login_usuario = Entry(ventana_login, textvariable=verifica_usuario)
    entrada_login_usuario.pack()
    Label(ventana_login, text="").pack()
    Label(ventana_login, text="Contraseña * ").pack()
    entrada_login_clave = Entry(ventana_login, textvariable=verifica_clave, show= '*')
    entrada_login_clave.pack()
    Label(ventana_login, text="").pack()
    Button(ventana_login, text="Acceder", width=10, height=1, command = verifica_login).pack()

#VENTANA "VERIFICACION DE LOGIN".

def verifica_login():
    usuario1 = verifica_usuario.get()
    clave1 = verifica_clave.get()
    try:
        conexion = pymysql.connect(host='localhost',
                                   user='root',
                                   password='deiyiber',
                                   db='Eventos')
        print("Conexión correcta")
        try:
            with conexion.cursor() as cursor:
                consulta = "SELECT  Us_Id, Us_Password FROM Credenciales_Usuario where Us_Id = %s;"
                cursor.execute(consulta, (usuario1))
                peliculas =cursor.fetchall()
                cons= pd.DataFrame(peliculas)  
        finally:
            conexion.close()
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrió un error ya que usuario no existe en la DB: ", e)
    idus=cons.iloc[0][0]
    passw=cons.iloc[0][1]
    if idus == usuario1:
        if passw ==clave1:
            print("ok ingreso")
            exito_login()
        else:
            print("passwor incorrecto",passw,"--",clave1 )
            no_clave()
    else:
        print("id de usuario incorrecto",idus,"--",usuario1)
        no_usuario()


# VENTANA "Login finalizado con exito".______________--------------------------------------------------------------------
 
def exito_login():
    ventana_login.destroy()
    global ventana_exito
    ventana_exito = Toplevel(ventana_principal)
    ventana_exito.title("Asistencia")
    ventana_exito.geometry("300x520")
    Label(ventana_exito, text="Introduzca datos", bg="LightGreen").pack()
    Label(ventana_exito, text="").pack()
    global id_usu_Asistencia
    id_usu_Asistencia = IntVar()
    global id_even_Asistencia
    id_even_Asistencia = IntVar()
    global fch_even_Asistencia
    fch_even_Asistencia = StringVar()
    #-------------------------
    global ev_nombre
    ev_nombre=StringVar()
    global ev_aplicat
    ev_aplicat=StringVar()
    global ev_fec_ini
    ev_fec_ini=StringVar()
    global ev_fec_fin
    ev_fec_fin=StringVar()
    etiqueta_id_usu = Label(ventana_exito, text="Identificacion de usuario * ")
    etiqueta_id_usu.pack()
    etiqueta_id_usu = Entry(ventana_exito, textvariable=id_usu_Asistencia)
    etiqueta_id_usu.pack()
    etiqueta_id_even = Label(ventana_exito, text="Identificacion de Evento * ")
    etiqueta_id_even.pack()
    etiqueta_id_even = Entry(ventana_exito, textvariable=id_even_Asistencia) 
    etiqueta_id_even.pack()
    etiqueta_fch_even = Label(ventana_exito, text="Fecha de Evento *Ejm 2020-03-31 ")
    etiqueta_fch_even.pack()
    etiqueta_fch_even = Entry(ventana_exito, textvariable=fch_even_Asistencia)
    etiqueta_fch_even.pack()
    #----------------------------------------
    etiqueta_ev_nom = Label(ventana_exito, text="Nombre del Evento * ")
    etiqueta_ev_nom.pack()
    etiqueta_ev_nom = Entry(ventana_exito, textvariable=ev_nombre)
    etiqueta_ev_nom.pack()
    etiqueta_ev_apl = Label(ventana_exito, text="Nombre de la Aplicacion * ")
    etiqueta_ev_apl.pack()
    etiqueta_ev_apl = Entry(ventana_exito, textvariable=ev_aplicat)
    etiqueta_ev_apl.pack()
    etiqueta_ev_fech_ini = Label(ventana_exito, text="Fecha de Inicio *Ejm 2020-03-31 ")
    etiqueta_ev_fech_ini.pack()
    etiqueta_ev_fech_ini = Entry(ventana_exito, textvariable=ev_fec_ini)
    etiqueta_ev_fech_ini.pack()
    etiqueta_ev_fech_fin = Label(ventana_exito, text="Fecha Final Evento *Ejm 2020-03-31 ")
    etiqueta_ev_fech_fin.pack()
    etiqueta_ev_fech_fin = Entry(ventana_exito, textvariable=ev_fec_fin)
    etiqueta_ev_fech_fin.pack()
    Button(ventana_exito, text="INGRESAR", command=ingreso_asistencia1).pack()
    etiqueta_id_usu = Label(ventana_exito, text="-------------")
    etiqueta_id_usu.pack()
    Button(ventana_exito, text="Consultar Credenciales", command=Consultas_creden).pack(padx=10, pady=10)
    Button(ventana_exito, text="Consultar Datos Usuario", command=Consultas_datos_usuario).pack()
    Button(ventana_exito, text="Consultar Asistencias", command=Consultas_datos_asistencia).pack(padx=10, pady=10)
    Button(ventana_exito, text="Consultar Eventos", command=Consultas_datos_eventos).pack()
 
#VENTANA DE "Contraseña incorrecta".
 
def no_clave():
    global ventana_no_clave
    ventana_no_clave = Toplevel(ventana_login)
    ventana_no_clave.title("ERROR")
    ventana_no_clave.geometry("150x100")
    Label(ventana_no_clave, text="Contraseña incorrecta ").pack()
    Button(ventana_no_clave, text="OK", command=borrar_no_clave).pack() #EJECUTA "borrar_no_clave()".
 
#VENTANA DE "Usuario no encontrado".
 
def no_usuario():
    global ventana_no_usuario
    ventana_no_usuario = Toplevel(ventana_login)
    ventana_no_usuario.title("ERROR")
    ventana_no_usuario.geometry("150x100")
    Label(ventana_no_usuario, text="Usuario no encontrado").pack()
    Button(ventana_no_usuario, text="OK", command=borrar_no_usuario).pack() #EJECUTA "borrar_no_usuario()"

#CERRADO DE VENTANAS

#def borrar_exito_login():
    #ventana_exito.destroy()
 
 
def borrar_no_clave():
    ventana_no_clave.destroy()
 
 
def borrar_no_usuario():
    ventana_no_usuario.destroy()


#registro a base de datos 
def ingreso_usuario_clave():
    ingreso_usuario1()
    nombre_usuario1=nombre_usuario.get()
    clave1=clave.get()
    try:
        conexion = pymysql.connect(host='localhost',
                                   user='root',
                                   password='deiyiber',
                                   db='Eventos')
        print("ingreso_usuario_clave OK")
        try:
            with conexion.cursor()as cursor:
                sql = "INSERT INTO Credenciales_Usuario (Us_Id , Us_Password ) VALUES (%s, %s)"
                val = (nombre_usuario1, clave1)
                cursor.execute(sql, val)
                conexion.commit()
        finally:
            conexion.close()
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrió un error al conectar: ", e)
    Label(ventana_registro, text="Registro completado con éxito", fg="green", font=("calibri", 11)).pack()
#ingreso a la table de usuario informacion
def ingreso_usuario1():
    nombre_usuario11=nombre_usuario1.get()
    apellidos_usuario1=apellidos_usuario.get()
    email_usuario1=email_usuario.get()
    cargo_usuario1=cargo_usuario.get()
    try:
        conexion = pymysql.connect(host='localhost',
                                   user='root',
                                   password='deiyiber',
                                   db='Eventos')
        print("ingreso_usuario OK")
        try:
            with conexion.cursor()as cursor:
                sql = "INSERT INTO Datos_Usuario (Us_Nombres, Us_Apellido, Us_Email, Us_Cargo ) VALUES (%s, %s, %s, %s)"
                val = (nombre_usuario11, apellidos_usuario1,email_usuario1,cargo_usuario1)
                cursor.execute(sql, val)
                conexion.commit()
        finally:
            conexion.close()
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrió un error al conectar: ", e)
#ingreso a base de datos tabla asistencia 3 campos
def ingreso_asistencia1():
    id_usu_Asistencia1=id_usu_Asistencia.get()
    id_even_Asistencia1=id_even_Asistencia.get()
    fch_even_Asistencia1=fch_even_Asistencia.get()
    
    try:
        conexion = pymysql.connect(host='localhost',
                                   user='root',
                                   password='deiyiber',
                                   db='Eventos')
        print("ingreso_asistencia OK")
        try:
            with conexion.cursor()as cursor:
                sql = "INSERT INTO Asistencia (Us_Id, Ev_Id, As_Fecha_Registro ) VALUES (%s, %s, %s)"
                val = (id_usu_Asistencia1,id_even_Asistencia1,fch_even_Asistencia1)
                cursor.execute(sql, val)
                conexion.commit()
        finally:
            conexion.close()
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrió un error al conectar: ", e)
    ingreso_Eventos()
#ingreso a base  de datos eventos 4 campos
def ingreso_Eventos():
    ev_nombre1=ev_nombre.get()
    ev_aplicat1=ev_aplicat.get()
    ev_fec_ini1=ev_fec_ini.get()
    ev_fec_fin1=ev_fec_fin.get()
    
    try:
        conexion = pymysql.connect(host='localhost',
                                   user='root',
                                   password='deiyiber',
                                   db='Eventos')
        print("Conexión correcta")
        try:
            with conexion.cursor()as cursor:
                sql = "INSERT INTO Eventos (Ev_Nombre, Ev_Aplicacion, Ev_Fecha_Inicio, Ev_Fecha_Fin) VALUES (%s, %s, %s, %s)"
                val = (ev_nombre1,ev_aplicat1,ev_fec_ini1,ev_fec_fin1)
                cursor.execute(sql, val)
                conexion.commit()
        finally:
            conexion.close()
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrió un error : ", e)
    Label(ventana_exito, text="Igreso de informacion con éxito", fg="green", font=("calibri", 11)).pack()

def Consultas_creden():
    try:
        conexion = pymysql.connect(host='localhost',
                                   user='root',
                                   password='deiyiber',
                                   db='Eventos')
        print("Consultas_creden ok")
        try:
            with conexion.cursor() as cursor:
                cons_credenciales= pd.read_sql("SELECT  *FROM Credenciales_Usuario;", conexion)
        finally:
            conexion.close()
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrió un error al conectar: ", e)
    global ventana_consulta
    ventana_consulta = Toplevel(ventana_principal)
    ventana_consulta.title("Consulta de Credenciales")
    #ventana_registro.geometry("350x350")
    table = tk.Text(ventana_consulta)
    table.insert(tk.INSERT, cons_credenciales.to_string())
    table.pack()
#consulta datos de uduario 
def Consultas_datos_usuario():
    try:
        conexion = pymysql.connect(host='localhost',
                                   user='root',
                                   password='deiyiber',
                                   db='Eventos')
        print("Consultas_datos_usuario ok")
        try:
            with conexion.cursor() as cursor:
                cons_dato_usuarios= pd.read_sql("SELECT  *FROM Datos_Usuario;", conexion)
        finally:
            conexion.close()
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrió un error al conectar: ", e)
    global ventana_dat_usuario
    ventana_dat_usuario = Toplevel(ventana_principal)
    ventana_dat_usuario.title("Consulta Datos Usuarios")
    table = tk.Text(ventana_dat_usuario)
    table.insert(tk.INSERT, cons_dato_usuarios.to_string())
    table.pack()

def Consultas_datos_asistencia():
    try:
        conexion = pymysql.connect(host='localhost',
                                   user='root',
                                   password='deiyiber',
                                   db='Eventos')
        print("Consultas_datos_asistencia ok")
        try:
            with conexion.cursor() as cursor:
                cons_asistencia= pd.read_sql("SELECT  *FROM Asistencia;", conexion)
        finally:
            conexion.close()
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrió un error al conectar: ", e)
    global ventana_data_asistencia
    ventana_data_asistencia = Toplevel(ventana_principal)
    ventana_data_asistencia.title("Consulta Datos Usuarios")
    #ventana_registro.geometry("350x350")
    table = tk.Text(ventana_data_asistencia)
    table.insert(tk.INSERT, cons_asistencia.to_string())
    table.pack()

def Consultas_datos_eventos():
    try:
        conexion = pymysql.connect(host='localhost',
                                   user='root',
                                   password='deiyiber',
                                   db='Eventos')
        print("Consultas_datos_eventos ok")
        try:
            with conexion.cursor() as cursor:
                cons_eventos= pd.read_sql("SELECT  *FROM Eventos;", conexion)
        finally:
            conexion.close()
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
        print("Ocurrió un error al conectar: ", e)
    global ventana_data_evento
    ventana_data_evento = Toplevel(ventana_principal)
    ventana_data_evento.title("Consulta Datos Usuarios")
    #ventana_registro.geometry("350x350")
    table = tk.Text(ventana_data_evento)
    table.insert(tk.INSERT, cons_eventos.to_string())
    table.pack()
if __name__ == "__main__":
    ventana_inicio()  #EJECUCIÓN DE LA VENTANA DE INICIO.


# In[ ]:




