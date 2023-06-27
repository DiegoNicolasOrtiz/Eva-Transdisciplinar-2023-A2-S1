from tkinter import *
from tkinter import font
import matplotlib.pyplot as plt
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

#---------------------------frame1 y frame graph----------------------------------------------------
frame_1 = Frame(ventana)
frame_1.config(bg = "RoyalBlue3")
frame_1.config(width ="500", height ="737") 
frame_1.config(border = "8")
frame_1.config(relief = SUNKEN)
frame_1.pack_propagate(False)
frame_1.pack()
frame_1.place(x=0, y=0)

'''
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
'''

#-----------------------------titulo-------------------------------------------------------
title = Label(frame_1, 
    text= "Movimiento Rectilineo \n Uniforme Acelerado.", 
    font= ("Eras Bold ITC", 30), bg="steel blue",
    relief = GROOVE, bd=2)
title.pack(side=TOP)

#----------------------------Entrys--------------------------------------------------------------

entry_velocidad = Entry(frame_1)
entry_velocidad.pack()
entry_velocidad.place(x=230, y=200)


aceleracion_entry = Entry(frame_1)
aceleracion_entry.pack()
aceleracion_entry.place(x=230, y=170)

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

label = Label(frame_3)
label.place(x=0, y=0)

#-----------------------------------Labels Aceleracion y Velocidad Inicial----------------------------------------------------------

label_velocidad = Label(frame_1, 
            text = "Velocidad Inicial: ", 
            bg = "RoyalBlue3",
            font = ("Cascadia Code", 9))
label_velocidad.pack()
label_velocidad.place(x=88, y=200)

label_aceleracion = Label(frame_1, 
            text = "Aceleracion: ", 
            bg="RoyalBlue3",
            font = ("Cascadia Code", 9))
label_aceleracion.pack()
label_aceleracion.place(x=132, y=170)

text_e = Label(frame_2, 
            text = "ECUACION MRUA",
            font=("Cascadia Code", 16),
            bg="Royal Blue4",
            fg="white")
text_e.pack()

label_ecuacion = Label(frame_2, 
                    text = """    x = x₀ + v₀t + (1/2)at²    """,
                    font=("Cascadia Code", 25),
                    relief= SUNKEN,
                    border="7")
label_ecuacion.pack()
label_ecuacion.place(x=100, y=60)
#--------------------------------------------pygame--------------------------------------------------

# Configuración de la ventana de pygame
WIDTH, HEIGHT = 823, 470
FPS = 60
tiempo_simulacion = 10

# Clase para la simulación del movimiento
class MRUASimulation:
    def __init__(self, initial_velocity, acceleration):
        self.initial_velocity = initial_velocity
        self.acceleration = acceleration
        self.time = 0
        self.position = 0
        self.positiony = 0

    def update(self, dt):
        self.positiony = -1*(self.initial_velocity * self.time + 0.5 * self.acceleration * self.time**2)
        self.position_g = 1 * (self.initial_velocity * self.time + 0.5 * self.acceleration * self.time **2)
        self.time += dt
        if self.positiony > 500 or self.time > 20 or self.positiony < -500:
            self.positiony = 0
            self.time = 0

simulation = MRUASimulation(0, 0)

# Función para dibujar la tabla gráfica en pygame


def draw_graph(surface, simulation):
    surface.fill((0, 0, 0))
    pygame.draw.line(surface, (130, 160, 200), (WIDTH // 4 - 30, 0), (WIDTH // 4 - 30, HEIGHT), 1)
    pygame.draw.line(surface, (130, 160, 200), (WIDTH // 4 - 60, 0), (WIDTH // 4 - 60, HEIGHT), 1)
    pygame.draw.line(surface, (130, 160, 200), (WIDTH // 4 - 90, 0), (WIDTH // 4 - 90, HEIGHT), 1)
    pygame.draw.line(surface, (130, 160, 200), (WIDTH // 4 - 120, 0), (WIDTH // 4 - 120, HEIGHT), 1)
    pygame.draw.line(surface, (130, 160, 200), (WIDTH // 4 - 150, 0), (WIDTH // 4 - 150, HEIGHT), 3)
    pygame.draw.line(surface, (130, 160, 200), (WIDTH // 4 - 180, 0), (WIDTH // 4 - 180, HEIGHT), 1)
    pygame.draw.line(surface, (130, 160, 200), (WIDTH // 4 + 30, 0), (WIDTH // 4 + 30, HEIGHT), 1)
    pygame.draw.line(surface, (130, 160, 200), (WIDTH // 4 + 60, 0), (WIDTH // 4 + 60, HEIGHT), 1)
    pygame.draw.line(surface, (130, 160, 200), (WIDTH // 4 + 90, 0), (WIDTH // 4 + 90, HEIGHT), 1)
    pygame.draw.line(surface, (130, 160, 200), (WIDTH // 4 + 120, 0), (WIDTH // 4 + 120, HEIGHT), 1)
    pygame.draw.line(surface, (130, 160, 200), (WIDTH // 4 + 150, 0), (WIDTH // 4 + 150, HEIGHT), 3)
    pygame.draw.line(surface, (130, 160, 200), (WIDTH // 4 + 180, 0), (WIDTH // 4 + 180, HEIGHT), 1)
    pygame.draw.line(surface, (130, 160, 200), (WIDTH // 4 + 210, 0), (WIDTH // 4 + 210, HEIGHT), 1)
    pygame.draw.line(surface, (130, 160, 200), (WIDTH // 4 + 240, 0), (WIDTH // 4 + 240, HEIGHT), 1)
    pygame.draw.line(surface, (130, 160, 200), (WIDTH // 4 + 270, 0), (WIDTH // 4 + 270, HEIGHT), 1)
    pygame.draw.line(surface, (130, 160, 200), (WIDTH // 4 + 300, 0), (WIDTH // 4 + 300, HEIGHT), 3)
    pygame.draw.line(surface, (130, 160, 200), (WIDTH // 4 + 330, 0), (WIDTH // 4 + 330, HEIGHT), 1)
    pygame.draw.line(surface, (130, 160, 200), (WIDTH // 4 + 360, 0), (WIDTH // 4 + 360, HEIGHT), 1)
    pygame.draw.line(surface, (130, 160, 200), (WIDTH // 4 + 390, 0), (WIDTH // 4 + 390, HEIGHT), 1)
    pygame.draw.line(surface, (130, 160, 200), (WIDTH // 4 + 420, 0), (WIDTH // 4 + 420, HEIGHT), 1)
    pygame.draw.line(surface, (130, 160, 200), (WIDTH // 4 + 450, 0), (WIDTH // 4 + 450, HEIGHT), 3)
    pygame.draw.line(surface, (130, 160, 200), (WIDTH // 4 + 480, 0), (WIDTH // 4 + 480, HEIGHT), 1)
    pygame.draw.line(surface, (130, 160, 200), (WIDTH // 4 + 510, 0), (WIDTH // 4 + 510, HEIGHT), 1)
    pygame.draw.line(surface, (130, 160, 200), (WIDTH // 4 + 540, 0), (WIDTH // 4 + 540, HEIGHT), 1)
    pygame.draw.line(surface, (130, 160, 200), (WIDTH // 4 + 570, 0), (WIDTH // 4 + 570, HEIGHT), 1)
    pygame.draw.line(surface, (130, 160, 200), (0, HEIGHT//2 + 30), (WIDTH, HEIGHT//2 + 30), 1)
    pygame.draw.line(surface, (130, 160, 200), (0, HEIGHT//2 + 60), (WIDTH, HEIGHT//2 + 60), 1)
    pygame.draw.line(surface, (130, 160, 200), (0, HEIGHT//2 + 90), (WIDTH, HEIGHT//2 + 90), 1)
    pygame.draw.line(surface, (130, 160, 200), (0, HEIGHT//2 + 120),(WIDTH, HEIGHT//2 + 120), 1)
    pygame.draw.line(surface, (130, 160, 200), (0, HEIGHT//2 + 150), (WIDTH, HEIGHT//2 + 150), 3)
    pygame.draw.line(surface, (130, 160, 200), (0, HEIGHT//2 + 180), (WIDTH, HEIGHT//2 + 180), 1)
    pygame.draw.line(surface, (130, 160, 200), (0, HEIGHT//2 + 210), (WIDTH, HEIGHT//2 + 210), 1)
    pygame.draw.line(surface, (130, 160, 200), (0, HEIGHT//2 + 240), (WIDTH, HEIGHT//2 + 240), 1)
    pygame.draw.line(surface, (130, 160, 200), (0, HEIGHT//2 + 270), (WIDTH, HEIGHT//2 + 270), 1)
    pygame.draw.line(surface, (130, 160, 200), (0, HEIGHT//2), (WIDTH, HEIGHT//2), 3)
    pygame.draw.line(surface, (130, 160, 200), (0, HEIGHT//2 - 30), (WIDTH, HEIGHT//2 - 30), 1)
    pygame.draw.line(surface, (130, 160, 200), (0, HEIGHT//2 - 60), (WIDTH, HEIGHT//2 - 60), 1)
    pygame.draw.line(surface, (130, 160, 200), (0, HEIGHT//2 - 90), (WIDTH, HEIGHT//2 - 90), 1)
    pygame.draw.line(surface, (130, 160, 200), (0, HEIGHT//2 - 120),(WIDTH, HEIGHT//2 - 120), 1)
    pygame.draw.line(surface, (130, 160, 200), (0, HEIGHT//2 - 150), (WIDTH, HEIGHT//2 - 150), 3)
    pygame.draw.line(surface, (130, 160, 200), (0, HEIGHT//2 - 180), (WIDTH, HEIGHT//2 - 180), 1)
    pygame.draw.line(surface, (130, 160, 200), (0, HEIGHT//2 - 210), (WIDTH, HEIGHT//2 - 210), 1)
    pygame.draw.line(surface, (130, 160, 200), (0, HEIGHT//2 - 240), (WIDTH, HEIGHT//2 - 240), 1)
    pygame.draw.line(surface, (130, 160, 200), (0, HEIGHT//2 - 270), (WIDTH, HEIGHT//2 - 270), 1)
    pygame.draw.line(surface, (255, 255, 255), (0, 330), (WIDTH, 330), 3)
    pygame.draw.line(surface, (255, 255, 255), (WIDTH // 4, 0), (WIDTH // 4, HEIGHT), 3)
    pygame.draw.circle(surface, (255, 0, 0), (WIDTH // 4 + int(simulation.time)*30, 330 + int(simulation.positiony)), 5)

    pygame_image = pygame.image.tostring(surface, 'RGB')
    image = Image.frombytes('RGB', surface.get_size(), pygame_image)
    photo = ImageTk.PhotoImage(image)
    label.config(image=photo)
    label.image = photo

def iniciar():
    
    initial_velocity = float(entry_velocidad.get())
    acceleration = float(aceleracion_entry.get())
    simulation.acceleration = acceleration
    simulation.initial_velocity = initial_velocity
    simulation.update(1)
    print(simulation.time)
    surf = pygame.Surface((WIDTH,HEIGHT))
    draw_graph(surf, simulation)
    # Programar la próxima actualización
    ventana.after(5000//15, iniciar)

# Función para iniciar la simulación
def start_simulation():
    initial_velocity = float(entry_velocidad.get())
    acceleration = float(aceleracion_entry.get())
    surf = pygame.Surface((WIDTH,HEIGHT))

    # Configuración de la ventana de pygame
    iniciar()

def crear_grafico(posicion, tiempo):
    plt.plot(tiempo, posicion)
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Posición (m)')
    plt.title('Simulación de Movimiento Rectilíneo Uniforme Acelerado')
    plt.grid(True)
    plt.show()

def mostrar_grafico():
    velocidad_inicial = float(entry_velocidad.get())
    aceleracion = float(aceleracion_entry.get())
    simulation = MRUASimulation(velocidad_inicial, aceleracion)

    positions = []
    times = []

    while simulation.time < tiempo_simulacion:
        simulation.update(1)
        positions.append(simulation.position_g)
        times.append(simulation.time)
    print(positions)
    print(times)
    crear_grafico(positions, times)

#################BOTON INICIO#########################
boton_inicio = Button(frame_1, 
                text = "INICIO SIMULACIÓN", 
                command = start_simulation, 
                bg = "powder blue",
                font = ("consolas 8 bold"))#BOTON
boton_inicio.config(relief=SUNKEN)
boton_inicio.pack()
boton_inicio.place(x = 180, y= 270, width = 120, height = 60)#Pocision y tamaño del boton

#-----------------------BOTON GRAFICO---------------------------------
boton_grafico = Button(frame_1, text="MOSTRAR GRÁFICO", 
                    command=mostrar_grafico, 
                    bg="powder blue",
                    font = ("consolas 8 bold"))
boton_grafico.config(relief=SUNKEN)
boton_grafico.pack()
boton_grafico.place(x=180, y=400, width=120, height=60)



ventana.mainloop()
