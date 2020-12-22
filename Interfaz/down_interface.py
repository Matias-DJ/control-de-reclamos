from tkinter import Button

def createDownInterface(frame):
    #Botones de abajo
    bt_edit = Button(frame, text = 'EDITAR TICKET')
    bt_edit.grid(row = 8, column = 0, pady = 12, padx = 12, ipady = 5, ipadx = 5, sticky = 'w' )
    bt_edit.config(width = 15)

    bt_guardar = Button(frame, text = 'GUARDAR')
    bt_guardar.config(width = 15)
    bt_guardar.grid(row = 8, column = 1, pady = 12, padx = 12, ipady = 5, ipadx = 5, sticky = 'e' )
