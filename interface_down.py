from tkinter import Button
from funciones_datos import *

def createDownInterface(frame):
    #Botones de abajo
    bt_edit = Button(frame, text = 'EDITAR TICKET', command = lambda:recolectarDatos('actualizar'))
    bt_edit.grid(row = 8, column = 0, pady = 12, padx = 12, ipady = 5, ipadx = 5, sticky = 'w' )
    bt_edit.config(width = 15)

    bt_guardar = Button(frame, text = 'GUARDAR', command = lambda:recolectarDatos('crear'))
    bt_guardar.config(width = 15)
    bt_guardar.grid(row = 8, column = 1, pady = 12, padx = 12, ipady = 5, ipadx = 5, sticky = 'e' )
