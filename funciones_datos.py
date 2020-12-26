from tkinter import Entry, Text
import interface_middle as middle
import bbdd

coleccion_datos = ()

def recolectarDatos(funcion_bbdd):
    global coleccion_datos

    ticket = middle.et_idTicket.get()
    fecha = middle.et_fecha.get()
    recurrente = middle.et_recurrente.get()
    cedula = middle.et_cIdentidad.get()
    tipo_reclamo = middle.et_tipoReclamo.get()
    reclamo = middle.tx_reclamo.get('1.0', 'end')

    coleccion_datos = (
        ticket,
        fecha, 
        recurrente, 
        cedula, 
        tipo_reclamo, 
        reclamo
        )

    '''elegir la siguiente funcion a realizar
    segun el boton presionado'''

    if funcion_bbdd == 'crear':
        bbdd.guardarReclamo(coleccion_datos)

    elif funcion_bbdd == 'buscar':
        bbdd.leerDatos(coleccion_datos)

    elif funcion_bbdd == 'actualizar':
        
        bbdd.editarTicket(coleccion_datos)


def limpiar_campos():
    ticket = middle.et_idTicket.delete(0, 'end')
    fecha = middle.et_fecha.delete(0, 'end')
    recurrente = middle.et_recurrente.delete(0, 'end')
    cedula = middle.et_cIdentidad.delete(0, 'end')
    tipo_reclamo = middle.et_tipoReclamo.delete(0, 'end')
    reclamo = middle.tx_reclamo.delete('1.0', 'end')
    