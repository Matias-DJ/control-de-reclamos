#Crear botones  y titulo de la parte superior
from tkinter import Label, Button, StringVar
import bbdd
import interface_middle as middle
ultimo_ticket = ''
frame = None 

def actualizarUltimoTicket():
    global ultimo_ticket, frame
    bbdd.cursor.execute(f"SELECT * FROM RECLAMOS")
    lectura = bbdd.cursor.fetchall()
    
    #print(datos_leidos)

    ultimo_ticket = 'Ultimo ticket ingresado: ' + str(lectura[-1][0])
    
    mostrarUltimoTicket(frame)



def createTopInterface(raiz):
    global frame
    frame = raiz
    #guardar el frame para utilizar en otras funciones

    #Titulo Superior
    lb_titulo = Label(
        frame, 
        text = 'GESTION DE RECLAMOS', 
        justify = 'center'
        )
    lb_titulo.config(
        font = ('Dyuthi', 30)
        )
    lb_titulo.grid(
        row = 0, 
        column = 0, 
        columnspan = 2,
        pady = 12, 
        padx = 12 
        )


    #Botones de arriba
    bt_nuevoTicket = Button(
        frame, 
        text = 'NUEVO TICKET DE \nRECLAMO',
        command = actualizarUltimoTicket)
    bt_nuevoTicket.grid(
        row = 1, 
        column = 0, 
        pady = 12, 
        padx = 12, 
        ipady = 5, 
        ipadx = 5, 
        sticky = 'w'
        ) 
    bt_nuevoTicket.config(
        width = 15
        )

    bt_buscar = Button(
        frame, 
        text = 'BUSCAR TICKET DE \nRECLAMO', 
        command = lambda:recolectarDatos('buscar'))
    bt_buscar.grid(
        row = 1, 
        column = 1, 
        pady = 12, 
        padx = 12, 
        ipady = 5, 
        ipadx = 5, 
        sticky = 'e'
        )
    bt_buscar.config(
        width = 15
        )


    #linea separadora
    lineas = '    ----------------------------------------------------------------------------------------------------------'
    lb_separacion = Label(
        frame, 
        text = lineas)
    lb_separacion.grid(
        row = 2, 
        column = 0, 
        columnspan = 2, 
        pady = 9, 
        sticky = 'w'
        ) 


def mostrarUltimoTicket(raiz):
    lb_info = Label(
        raiz, 
        text = ultimo_ticket
        )
    lb_info.grid(
        row = 3,
        column = 0,
        sticky = 'w'
        )
    lb_info.config(
        font = ('Arial', 10)
        ) 