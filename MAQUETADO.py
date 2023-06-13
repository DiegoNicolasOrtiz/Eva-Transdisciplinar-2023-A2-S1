from tkinter import *
from tkinter import messagebox
import matplotlib 
import pygame
from pygame.locals import *
from PIL import Image, ImageTk

#--------------------------------------tkinter---------------------------------------------------------------------

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

#-----------------------------------Labels Aceleracion y Velocidad Inicial----------------------------------------------------------

label_texto = Label(ventana, text = """Movimiento Rectilíneo Uniformemente Acelerado
(MRUA)""")
label_texto.pack()
label_texto.place(x=20, y=55)

label_velocidad = Label(ventana, text = "Velocidad Inicial: ", bg="steel blue")
label_velocidad.pack()
label_velocidad.place(x=35, y=200)

label_aceleracion = Label(ventana, text = "Aceleración: ", bg="steel blue")
label_aceleracion.pack()
label_aceleracion.place(x=57, y=160)

#----------------------------Entrys--------------------------------------------------------------

entry_velocidad = Entry(ventana)
entry_velocidad.pack()
entry_velocidad.place(x=130, y=200)

aceleracion_entry = Entry(ventana)
aceleracion_entry.pack()
aceleracion_entry.place(x=130, y=160)

#---------------------------FRAME 2-------------------------------------------------------------------------

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

#--------------------------------------------pygame--------------------------------------------------

# Configuración de la ventana de pygame
WIDTH, HEIGHT = 800, 600
FPS = 60

# Clase para la simulación del movimiento
class MRUASimulation:
    def __init__(self, initial_velocity, acceleration):
        self.initial_velocity = initial_velocity
        self.acceleration = acceleration
        self.time = 0
        self.position = 0
        self.positiony = 0

    def update(self, dt):
        self.position = self.initial_velocity * self.time + 0.5 * self.acceleration * self.time**2
        self.positiony = -1*(self.initial_velocity * self.time + 0.5 * self.acceleration * self.time**3)
        self.time += dt

# Función para dibujar la tabla gráfica en pygame
def draw_graph(ventana, simulation):
    pygame.draw.line(ventana, (0, 0, 0), (0, 450), (WIDTH, 450), 2)
    pygame.draw.line(ventana, (0, 0, 0), (WIDTH // 4, 0), (WIDTH // 4, HEIGHT), 2)
    pygame.draw.circle(ventana, (255, 0, 0), (WIDTH // 4 + int(simulation.time*100), 450 + int(simulation.positiony)), 5)

# Función para iniciar la simulación
def start_simulation():
    initial_velocity = float(entry_velocidad.get())
    acceleration = float(aceleracion_entry.get())
    simulation = MRUASimulation(initial_velocity, acceleration)
    
    # Configuración de la ventana de pygame
    pygame.init()
    clock = pygame.time.Clock()
    ventana = pygame.display.get_surface()
    pygame.display.set_caption("Simulación de Movimiento Rectilíneo Uniformemente Acelerado")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False


        # Actualizar y dibujar la simulación
        simulation.update(1 / FPS)
        draw_graph(ventana, simulation)

        pygame.display.flip()
        clock.tick(FPS)
        
    pygame.quit()

boton_inicio = Button(ventana, text = "Iniciar Simulación", command = start_simulation, bg = "powder blue")#BOTON
boton_inicio.config(relief=SUNKEN)
boton_inicio.pack()
boton_inicio.place(x = 90, y = 270, width = 120, height = 60)#Pocision del boton









ventana.mainloop()
