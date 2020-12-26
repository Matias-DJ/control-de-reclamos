from tkinter import Entry, Text, Scrollbar

et_idTicket = 0
et_fecha = 0
et_recurrente = 0
et_cIdentidad = 0
et_tipoReclamo = 0
tx_reclamo = 0


def createMiddleInterface(frame):
    global et_idTicket, et_fecha, et_recurrente
    global et_cIdentidad, et_tipoReclamo, tx_reclamo
    pady = 3

    et_idTicket = Entry(
        frame
        )
    et_idTicket.grid(
    row = 4, 
    column = 0, 
    pady = pady, 
    padx = 12, 
    ipady = 5, 
    ipadx = 5, 
    sticky = 'w'
    )
    et_idTicket.configure(state = 'disabled')
    #et_idTicket.insert(0, 'ID_DEL_TICKET')


    et_fecha = Entry(
        frame
        )
    et_fecha.grid(
        row = 5, 
        column = 0, 
        pady = pady, 
        padx = 12, 
        ipady = 5, 
        ipadx = 5, 
        sticky = 'w'
        )
    et_fecha.insert(0, 'FECHA')


    et_recurrente = Entry(
        frame, 
        width = 40
        )
    et_recurrente.grid(
        row = 6, 
        column = 0, 
        pady = pady, 
        padx = 12, 
        ipady = 5, 
        ipadx = 5, 
        sticky = 'w'
        )
    et_recurrente.insert(0, 'RECURRENTE(NOMBRE_Y_APELLIDO)')


    et_cIdentidad = Entry(
        frame
        )
    et_cIdentidad.grid(
        row = 6, 
        column = 1, 
        pady = pady, 
        padx = 12, 
        ipady = 5, 
        ipadx = 5, 
        sticky = 'w'
        )
    et_cIdentidad.insert(0, 'CEDULA_DE_IDENTIDAD')


    et_tipoReclamo = Entry(
        frame, 
        width = 40
        )
    et_tipoReclamo.grid(
        row = 7, 
        column = 0, 
        pady = pady, 
        padx = 12, 
        ipady = 5, 
        ipadx = 5, 
        sticky = 'w'
        )
    et_tipoReclamo.insert(0, 'TIPO_DE_RECLAMO')


    tx_reclamo = Text(
        frame, 
        width = 65, 
        height = 12
        )
    tx_reclamo.grid(
        row = 8,
        column = 0, 
        pady = 12, 
        padx = 12, 
        columnspan = 2, 
        ipadx = 5, 
        sticky = 'w')
    tx_reclamo.insert('1.0', 'RECLAMO')
    
    scroll = Scrollbar(
        frame, 
        command = tx_reclamo.yview
        )
    scroll.grid(
        row = 8, 
        column = 2, 
        sticky = 'nsew', 
        ipadx = 3,
        padx = 0
        )
    tx_reclamo.config(yscrollcommand = scroll.set)