from tkinter import Entry, Text

def imprimir():
    print('Funciona!')

def createMiddleInterface(frame):
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