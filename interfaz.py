from tkinter import *
from tkinter.ttk import *

root = Tk()
root.resizable(False, False)

frame = Frame(root)
frame.grid(row = 0, column = 0)



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



#Cuadros de texto
rayas = '----------------------------------------------------------------------------------------------------------------'
lb_separacion = Label(frame, text = rayas)
lb_separacion.grid(row = 2, column = 0, columnspan = 2, pady = 9, sticky = 'w') 

pady = 3

et_idTicket = Entry(frame)
et_idTicket.grid(row = 3, column = 0, pady = pady, padx = 12, ipady = 5, ipadx = 5, sticky = 'w')
et_idTicket.insert(0, 'ID_DEL_TICKET')


et_fecha = Entry(frame)
et_fecha.grid(row = 4, column = 0, pady = pady, padx = 12, ipady = 5, ipadx = 5, sticky = 'w')
et_fecha.insert(0, 'FECHA')

et_recurrente = Entry(frame, width = 40)
et_recurrente.grid(row = 5, column = 0, pady = pady, padx = 12, ipady = 5, ipadx = 5, sticky = 'w')
et_recurrente.insert(0, 'RECURRENTE(NOMBRE_Y_APELLIDO)')

et_cIdentidad = Entry(frame)
et_cIdentidad.grid(row = 5, column = 1, pady = pady, padx = 12, ipady = 5, ipadx = 5, sticky = 'w')
et_cIdentidad.insert(0, 'CEDULA_DE_IDENTIDAD')

et_tipoReclamo = Entry(frame)
et_tipoReclamo.grid(row = 6, column = 0, pady = pady, padx = 12, ipady = 5, ipadx = 5, sticky = 'w')
et_tipoReclamo.insert(0, 'TIPO_DE_RECLAMO')


tx_reclamo = Text(frame, width = 65, height = 12)
tx_reclamo.grid(row = 7, column = 0, pady = 12, padx = 12, columnspan = 2, ipadx = 5, sticky = 'w')
tx_reclamo.insert('1.0', 'RECLAMO')




#Botones de abajo
bt_edit = Button(frame, text = 'EDITAR TICKET')
bt_edit.grid(row = 8, column = 0, pady = 12, padx = 12, ipady = 5, ipadx = 5, sticky = 'w' )
bt_edit.config(width = 15)

bt_guardar = Button(frame, text = 'GUARDAR')
bt_guardar.config(width = 15)
bt_guardar.grid(row = 8, column = 1, pady = 12, padx = 12, ipady = 5, ipadx = 5, sticky = 'e' )

root.mainloop()
