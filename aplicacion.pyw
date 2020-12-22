from tkinter import Tk, Frame
import interface_top as top
import interface_middle as middle
import interface_down as down 


root = Tk()
root.resizable(False, False)

frame = Frame(root)
frame.grid(row = 0, column = 0)


#Creacion de la interfaz
top.createTopInterface(frame)
middle.createMiddleInterface(frame)
down.createDownInterface(frame)


root.mainloop()