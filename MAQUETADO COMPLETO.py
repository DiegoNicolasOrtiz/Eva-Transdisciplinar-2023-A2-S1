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

frame_1.config(bg = "steel blue")

frame_1.config(width ="300", height ="600")    

frame_1.pack(side=LEFT)

frame_1.config(border = "15")

frame_1.config(relief = SUNKEN)

frame_1.pack_propagate(False)
frame_1.pack()
#-----------------------------------Labels Aceleracion y Velocidad Inicial----------------------------------------------------------

label_velocidad = Label(frame_1, text = "Velocidad Inicial: ", bg="steel blue")
label_velocidad.pack()
label_velocidad.place(x=20, y=200)

label_aceleracion = Label(frame_1, text = "Aceleracion: ", bg="steel blue")
label_aceleracion.pack()
label_aceleracion.place(x=43, y=170)
#----------------------------Entrys--------------------------------------------------------------

entry_velocidad = Entry(frame_1)
entry_velocidad.pack()
entry_velocidad.place(x=120, y=200)

aceleracion_entry = Entry(frame_1)
aceleracion_entry.pack()
aceleracion_entry.place(x=120, y=170)

#---------------------------FRAME 2-------------------------------------------------------------------------

frame_2 = Frame(ventana)

frame_2.config(bg = "SteelBlue4")

frame_2.config(width ="600", height ="150")    

frame_2.pack(side = BOTTOM)

frame_2.config(border = "15")

frame_2.config(relief = SUNKEN)

frame_2.pack_propagate(False)
frame_2.pack()

#--------------------------------Frame 3--------------------------------------------------------

frame_3 = Frame(ventana)
frame_3.pack_propagate(False)
frame_3.pack()

frame_3.config(bg = "SteelBlue4")

frame_3.config(width = "600", height = "600")    

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

    def update(self, dt):
        self.position = self.initial_velocity * self.time + 0.5 * self.acceleration * self.time**2
        self.time += dt

# Función para dibujar la tabla gráfica en pygame
def draw_graph(surface, simulation):
    pygame.draw.line(surface, (255, 255, 255), (0, HEIGHT // 2), (WIDTH, HEIGHT // 2), 2)
    pygame.draw.line(surface, (255, 255, 255), (WIDTH // 2, 0), (WIDTH // 2, HEIGHT), 2)
    pygame.draw.circle(surface, (255, 0, 0), (WIDTH // 2 + int(simulation.position), HEIGHT // 2), 5)

# Función para iniciar la simulación
def start_simulation():
    initial_velocity = float(entry_velocidad.get())
    acceleration = float(aceleracion_entry.get())
    simulation = MRUASimulation(initial_velocity, acceleration)

    # Configuración de la ventana de pygame
    pygame.init()
    clock = pygame.time.Clock()
    surface = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Simulación de Movimiento Rectilíneo Uniformemente Acelerado")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        surface.fill((0, 0, 0))

        # Actualizar y dibujar la simulación
        simulation.update(1 / FPS)
        draw_graph(surface, simulation)

        pygame_image = pygame.surfarray.array3d(surface)
        image = Image.fromarray(pygame_image)
        photo = ImageTk.PhotoImage(image)

        canvas = Label(frame_3, image=photo)
        canvas.image = photo
        canvas.pack()


        ventana.update()
        clock.tick(FPS)
        
    pygame.quit()

boton_inicio = Button(frame_1, text = "INICIO", command = start_simulation, bg = "powder blue")#BOTON
boton_inicio.config(relief=SUNKEN)
boton_inicio.pack()
boton_inicio.place(x = 80, y= 270, width = 120, height = 60)#Pocision y tamaño del boton





ventana.mainloop()
