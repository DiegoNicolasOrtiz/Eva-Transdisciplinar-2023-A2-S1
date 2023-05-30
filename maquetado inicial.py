from tkinter import *
from tkinter import messagebox

ventana = Tk()

frame = Frame(ventana)
frame.pack()
ventana.title("Proyecto")#El titulo modificado

ventana.geometry("900x600")#Dimension 

ventana.config(bg="RoyalBlue4")#Color de fondo


#---------------------------frame1----------------------------------------------------
frame_1 = Frame(ventana)
frame_1.pack()

frame_1.config(bg = "steel blue")

frame_1.config(width ="300", height ="600")    

frame_1.pack(side=LEFT)

frame_1.config(border = "15")

frame_1.config(relief = SUNKEN)


#------------------boton con mensaje----------------------------------------------------------------------------------

def boton_inicio():
    msg = messagebox.showinfo("HOLA", "LO SIENTO EL PROGRAMA AUN NO ESTA LISTO")#cuadrado de texto para mostrar

boton = Button(ventana, text = "INICIO", command = boton_inicio, bg = "powder blue")#BOTON
boton.config(relief="sunken")
boton.pack()
boton.place(x = 90, y = 50, width = 120, height = 60)#Pocision del boton

#-------------------botones sin mensaje--------------------------------------------------------------
botonrojo = Button(ventana, text = "ROJO", fg = "red")
botonrojo.place(x = 100, y = 400, width = 90, height = 50)

botonazul = Button(ventana, text = "AZUL", fg = "blue")
botonazul.place(x = 100, y = 350, width = 90, height = 50)

botonnegro = Button(ventana, text = "NEGRO", fg = "black")
botonnegro.place(x = 100, y = 300, width = 90, height = 50)

#---------------------------FRAME 2--------------------------------------------------------

frame_2 = Frame(ventana)
frame_2.pack()

frame_2.config(bg = "SteelBlue4")

frame_2.config(width ="600", height ="150")    

frame_2.pack(side = BOTTOM)

frame_2.config(border = "15")

frame_2.config(relief = SUNKEN)

#--------------------------------Frame 3--------------------------------------------------------

frame_3 = Frame(ventana)
frame_3.pack()

frame_3.config(bg = "SteelBlue4")

frame_3.config(width ="600", height ="450")    

frame_3.pack(side = TOP)

frame_3.config(border = "15")

frame_3.config(relief = SUNKEN)












ventana.mainloop()
