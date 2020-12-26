import sqlite3
from tkinter import messagebox
import interface_middle as middle
import funciones_datos

conexion = sqlite3.connect('Reclamo')
cursor = conexion.cursor()

try:
    cursor.execute('''
        CREATE TABLE RECLAMOS(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        TICKET VARCHAR(20) UNIQUE,
        FECHA VARCHAR(12),
        NOMBRE_APELLIDO VARCHAR(50), 
        CEDULA INTEGER,
        TIPO_RECLAMO VARCHAR(20),
        RECLAMO VARCHAR(600))
        ''')
except sqlite3.OperationalError:
    pass

################################
def guardarReclamo(tupla_datos):
    cursor.execute('''
        INSERT INTO RECLAMOS VALUES (NULL,?,?,?,?,?,?)''', 
        tupla_datos
        )
    conexion.commit()

#################################
identificador = None
def obtenerID(tupla_datos):
    global identificador

    try:
        cursor.execute(f'SELECT * FROM RECLAMOS WHERE TICKET = "{tupla_datos[0]}"')
        lectura = cursor.fetchall()
        identificador = lectura[0][0]
    except IndexError:
        pass

###################################

def leerDatos(tupla_datos):
    obtenerID(tupla_datos)

    cursor.execute(f"SELECT * FROM RECLAMOS WHERE TICKET = '{tupla_datos[0]}'")
    datos_leidos = cursor.fetchall()

    if len(datos_leidos) == 0 :
        messagebox.showwarning('Ticket no encontrado', 'El ticket ingresado no existe')    
        return

    funciones_datos.limpiar_campos()

    #volver a cargar los datos
    middle.et_idTicket.insert(0, datos_leidos[0][1])
    middle.et_fecha.insert(0, datos_leidos[0][2])
    middle.et_recurrente.insert(0, datos_leidos[0][3])
    middle.et_cIdentidad.insert(0, datos_leidos[0][4])
    middle.et_tipoReclamo.insert(0, datos_leidos[0][5])
    middle.tx_reclamo.insert('1.0', datos_leidos[0][6])
    
################################

def editarTicket(tupla_datos):
    obtenerID(tupla_datos)

    cursor.execute(f'''UPDATE RECLAMOS
        SET TICKET = "{tupla_datos[0]}",
            FECHA = "{tupla_datos[1]}",
            NOMBRE_APELLIDO = "{tupla_datos[2]}",
            CEDULA = "{tupla_datos[3]}",
            TIPO_RECLAMO = "{tupla_datos[4]}",
            RECLAMO = "{tupla_datos[5]}"
        WHERE ID = {identificador}''')
    coneccion.commit()
