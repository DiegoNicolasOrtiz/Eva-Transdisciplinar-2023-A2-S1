from tkinter import *
from tkinter import messagebox
from tkinter import font
import matplotlib 
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
import pygame
from pygame.locals import *
from PIL import Image, ImageTk

#--------------------------------------tkinter---------------------------------------------------------------------

ventana = Tk()

ventana.title("Proyecto")#El titulo modificado
ventana.config(bg="RoyalBlue4")#Color de fondo

#Tamaño de la ventana
width = ventana.winfo_screenwidth()
height = ventana.winfo_screenheight()
ventana.geometry("%dx%d" % (width, height))

#---------------------------frame1 y 1.1----------------------------------------------------
frame_1 = Frame(ventana)
frame_1.config(bg = "RoyalBlue3")
frame_1.config(width ="500", height ="400") 
frame_1.config(border = "8")
frame_1.config(relief = SUNKEN)
frame_1.pack_propagate(False)
frame_1.pack()
frame_1.place(x=0, y=0)

graphframe = Frame(ventana,
                bg ="midnight blue",
                width ="500", height ="336",
                border = "10",
                relief = SUNKEN)
graphframe.pack_propagate(False)
graphframe.pack()
graphframe.place(x=0, y=400)

labelgraph = Label(graphframe, 
                text = "GRAFICO",
                bg = "midnight blue",
                fg = "white",
                font = ("consolas 12 bold"))
labelgraph.pack()
            


#-----------------------------titulo-------------------------------------------------------
title = Label(frame_1, 
    text= "Movimiento Rectilineo \n Uniforme Acelerado.", 
    font= ("Impact", 30), bg="steel blue",
    relief = GROOVE, bd=2)
title.pack(side=TOP)
#-----------------------------------Labels Aceleracion y Velocidad Inicial----------------------------------------------------------

label_velocidad = Label(frame_1, 
            text = "Velocidad Inicial: ", 
            bg = "RoyalBlue3",
            font = ("Cascadia Code", 9))
label_velocidad.pack()
label_velocidad.place(x=90, y=200)

label_aceleracion = Label(frame_1, 
            text = "Aceleracion: ", 
            bg="RoyalBlue3",
            font = ("Cascadia Code", 9))
label_aceleracion.pack()
label_aceleracion.place(x=132, y=170)
#----------------------------Entrys--------------------------------------------------------------

entry_velocidad = Entry(frame_1)
entry_velocidad.pack()
entry_velocidad.place(x=220, y=200)

aceleracion_entry = Entry(frame_1)
aceleracion_entry.pack()
aceleracion_entry.place(x=220, y=170)

#---------------------------FRAME 2-------------------------------------------------------------------------

frame_2 = Frame(ventana, bg = "RoyalBlue4",
                width="860", height="240",
                border = "15",
                relief = SUNKEN,)
frame_2.pack()
frame_2.place(x=500, y=500)
frame_2.pack_propagate(False)


#--------------------------------Frame 3--------------------------------------------------------

frame_3 = Frame(ventana)
frame_3.pack_propagate(False)#No se altera el tamaño junto por los labels o entrys
frame_3.pack()
frame_3.config(bg = "RoyalBlue3")
frame_3.config(width = "860", height = "500")    
frame_3.config(border = "15")
frame_3.config(relief = SUNKEN)
frame_3.place(x=500, y=0)

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

    def create_graph_widgets(self): 
        graph_label = Label(self.graphframe, text="Gráfica") 
        graph_label.pack() 
         
        self.figure = Figure(figsize=(5, 4), dpi=100) 
        self.plot = self.figure.add_subplot(111) 
         
        self.canvas = FigureCanvasAgg(self.figure, master=self.graph_frame) 
        self.canvas.draw() 
        self.canvas.get_tk_widget().pack() 

#################BOTON INICIO#########################
boton_inicio = Button(frame_1, 
                text = "INICIO SIMULACIÓN", 
                command = start_simulation, 
                bg = "powder blue",
                font = ("consolas 8 bold"))#BOTON
boton_inicio.config(relief=SUNKEN)
boton_inicio.pack()
boton_inicio.place(x = 180, y= 270, width = 120, height = 60)#Pocision y tamaño del boton



ventana.mainloop()
