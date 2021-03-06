from tkinter import Button
from funciones_datos import *

def createDownInterface(frame):

    bt_edit = Button(
        frame, 
        text = 'GUARDAR CAMBIOS', 
        command = lambda:recolectarDatos('actualizar')
        )
    bt_edit.grid(
        row = 9, 
        column = 0, 
        pady = 12, 
        padx = 12, 
        ipady = 5, 
        ipadx = 5, 
        sticky = 'w'
        )
    bt_edit.config(width = 15)


    bt_guardar = Button(
        frame, 
        text = 'GUARDAR', 
        command = lambda:recolectarDatos('crear')
        )
    bt_guardar.grid(
        row = 9, 
        column = 1, 
        pady = 12, 
        padx = 12, 
        ipady = 5, 
        ipadx = 5, 
        sticky = 'e' 
        )
    bt_guardar.config(width = 15)
