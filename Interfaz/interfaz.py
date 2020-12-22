from tkinter import Tk, Frame
import top_buttons as top
import middle_entrys as middle
import down_interface as down 


root = Tk()
root.resizable(False, False)

frame = Frame(root)
frame.grid(row = 0, column = 0)


#Creacion de la interfaz
top.createTopInterface(frame)
middle.createMiddleInterface(frame)
down.createDownInterface(frame)


root.mainloop()
