#Crear botones  y titulo de la parte superior
from tkinter import Label, Button

def createTopInterface(frame):
    #Titulo Superior
    lb_titulo = Label(frame, text = 'GESTION DE RECLAMOS', justify = 'center')
    lb_titulo.config(font = ('Dyuthi', 30))
    lb_titulo.grid(row = 0, column = 0, columnspan = 2, pady = 12, padx = 12 )


    #Botones de arriba
    bt_nuevoTicket = Button(frame, text = 'NUEVO TICKET DE \nRECLAMO')
    bt_nuevoTicket.grid(row = 1, column = 0, pady = 12, padx = 12, ipady = 5, ipadx = 5, sticky = 'w') 
    bt_nuevoTicket.config(width = 15)

    bt_buscar = Button(frame, text = 'BUSCAR TICKET DE \nRECLAMO')
    bt_buscar.grid(row = 1, column = 1, pady = 12, padx = 12, ipady = 5, ipadx = 5, sticky = 'e')
    bt_buscar.config(width = 15)

    #linea separadora
    lineas = '----------------------------------------------------------------------------------------------------------------'
    lb_separacion = Label(frame, text = lineas)
    lb_separacion.grid(row = 2, column = 0, columnspan = 2, pady = 9, sticky = 'w') 