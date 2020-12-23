import sqlite3
from tkinter import messagebox
import interface_middle as middle
import funciones_datos

conexion = sqlite3.connect('Reclamo')
cursor = conexion.cursor()

try:
    cursor.execute('''CREATE TABLE RECLAMOS
        (
        TICKET VARCHAR(20) PRIMARY KEY,
        FECHA VARCHAR(12),
        NOMBRE_APELLIDO VARCHAR(50), 
        CEDULA INTEGER,
        TIPO_RECLAMO VARCHAR(20),
        RECLAMO VARCHAR(600)
        )'''
        )
except sqlite3.OperationalError:
    pass


def guardarReclamo(tupla_datos):
    cursor.execute('''
        INSERT INTO RECLAMOS VALUES (?,?,?,?,?,?)''', 
        tupla_datos
        )
    conexion.commit()

#################################

def leerDatos(ticket):

    cursor.execute(f"SELECT * FROM RECLAMOS WHERE TICKET = '{ticket}'")
    datos_leidos = cursor.fetchall()

    if len(datos_leidos) == 0 :
        messagebox.showwarning('Ticket no encontrado', 'El ticket ingresado no existe')    
        return

    funciones_datos.limpiar_campos()

    #volver a cargar los datos
    middle.et_idTicket.insert(0, datos_leidos[0][0])
    middle.et_fecha.insert(0, datos_leidos[0][1])
    middle.et_recurrente.insert(0, datos_leidos[0][2])
    middle.et_cIdentidad.insert(0, datos_leidos[0][3])
    middle.et_tipoReclamo.insert(0, datos_leidos[0][4])
    middle.tx_reclamo.insert('1.0', datos_leidos[0][5])
    
################################

def editarTicket(tupla_datos):
    cursor.execute(f'''UPDATE RECLAMOS
        SET FECHA = "{tupla_datos[1]}",
            NOMBRE_APELLIDO = "{tupla_datos[2]}",
            CEDULA = "{tupla_datos[3]}",
            TIPO_RECLAMO = "{tupla_datos[4]}",
            RECLAMO = "{tupla_datos[5]}"
        WHERE TICKET = "{tupla_datos[0]}" ''')
    conexion.commit()
