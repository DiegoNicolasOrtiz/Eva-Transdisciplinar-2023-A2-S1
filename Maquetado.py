from tkinter import *
from tkinter import messagebox
import tkinter
import matplotlib.pyplot as plt
import pygame
from pygame.locals import *
from PIL import Image, ImageTk

WIDTH, HEIGHT = 665, 435
FPS = 60
tiempo_simulacion = 10
#--------------------------------------tkinter---------------------------------------------------------------------
pygame.init()

ventana = Tk()

frame = Frame(ventana)
frame.pack()
ventana.title("Proyecto")#El titulo modificado

ventana.geometry("1150x800")#Dimension 

ventana.config(bg="RoyalBlue4")#Color de fondo


#---------------------------frame1----------------------------------------------------
frame_1 = Frame(ventana)
frame_1.pack()

frame_1.config(bg = "steel blue")

frame_1.config(width ="300", height ="300")    

frame_1.place(x=30, y=200)

frame_1.config(border = "15")

frame_1.config(relief = SUNKEN)
#---------------------------FRAME 2-------------------------------------------------------------------------

frame_2 = Frame(ventana)
frame_2.pack()

frame_2.config(bg = "steel blue")

frame_2.config(width ="450", height ="100")    

frame_2.place(x=510, y=520)

frame_2.config(border = "15")

frame_2.config(relief = SUNKEN)
#-----------------------------------Labels Aceleracion y Velocidad Inicial----------------------------------------------------------

label_texto = Label(ventana, text = """Movimiento Rectilíneo Uniformemente Acelerado
(MRUA)""")
label_texto.pack()
label_texto.config(border = "7")
label_texto.config(relief = SUNKEN)
label_texto.place(x=47, y=95)

label_texto = Label(frame_2, text = """    x = x₀ + v₀t + (1/2)at² 
(MRUA)""")
label_texto.pack()
label_texto.config(border = "7")
label_texto.config(relief = SUNKEN)
label_texto.place(x=200, y=5)

label_velocidad = Label(ventana, text = "Velocidad Inicial: ", bg="steel blue")
label_velocidad.pack()
label_velocidad.place(x=55, y=300)

label_aceleracion = Label(ventana, text = "Aceleración: ", bg="steel blue")
label_aceleracion.pack()
label_aceleracion.place(x=77, y=260)

#----------------------------Entrys--------------------------------------------------------------

entry_velocidad = Entry(ventana)
entry_velocidad.pack()
entry_velocidad.place(x=150, y=300)

aceleracion_entry = Entry(ventana)
aceleracion_entry.pack()
aceleracion_entry.place(x=150, y=260)



#--------------------------------Frame 3--------------------------------------------------------

frame_3 = Frame(ventana)
frame_3.pack()

frame_3.config(bg = "SteelBlue4")

frame_3.config(width ="700", height ="470")    

frame_3.place(x=370, y=30)

frame_3.config(border = "15")

frame_3.config(relief = SUNKEN)

label = tkinter.Label(ventana)
label.place(x=385, y=45)

#--------------------------------------------pygame--------------------------------------------------

# Configuración de la ventana de pygame

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
    pygame.draw.line(surface, (130, 160, 200), (WIDTH // 5 - 30, 0), (WIDTH // 5 - 30, HEIGHT), 1)
    pygame.draw.line(surface, (130, 160, 200), (WIDTH // 5 - 60, 0), (WIDTH // 5 - 60, HEIGHT), 1)
    pygame.draw.line(surface, (130, 160, 200), (WIDTH // 5 - 90, 0), (WIDTH // 5 - 90, HEIGHT), 1)
    pygame.draw.line(surface, (130, 160, 200), (WIDTH // 5 - 120, 0), (WIDTH // 5 - 120, HEIGHT), 1)
    pygame.draw.line(surface, (130, 160, 200), (WIDTH // 5 - 150, 0), (WIDTH // 5 - 150, HEIGHT), 3)
    pygame.draw.line(surface, (130, 160, 200), (WIDTH // 5 - 180, 0), (WIDTH // 5 - 180, HEIGHT), 1)
    pygame.draw.line(surface, (130, 160, 200), (WIDTH // 5 + 30, 0), (WIDTH // 5 + 30, HEIGHT), 1)
    pygame.draw.line(surface, (130, 160, 200), (WIDTH // 5 + 60, 0), (WIDTH // 5 + 60, HEIGHT), 1)
    pygame.draw.line(surface, (130, 160, 200), (WIDTH // 5 + 90, 0), (WIDTH // 5 + 90, HEIGHT), 1)
    pygame.draw.line(surface, (130, 160, 200), (WIDTH // 5 + 120, 0), (WIDTH // 5 + 120, HEIGHT), 1)
    pygame.draw.line(surface, (130, 160, 200), (WIDTH // 5 + 150, 0), (WIDTH // 5 + 150, HEIGHT), 3)
    pygame.draw.line(surface, (130, 160, 200), (WIDTH // 5 + 180, 0), (WIDTH // 5 + 180, HEIGHT), 1)
    pygame.draw.line(surface, (130, 160, 200), (WIDTH // 5 + 210, 0), (WIDTH // 5 + 210, HEIGHT), 1)
    pygame.draw.line(surface, (130, 160, 200), (WIDTH // 5 + 240, 0), (WIDTH // 5 + 240, HEIGHT), 1)
    pygame.draw.line(surface, (130, 160, 200), (WIDTH // 5 + 270, 0), (WIDTH // 5 + 270, HEIGHT), 1)
    pygame.draw.line(surface, (130, 160, 200), (WIDTH // 5 + 300, 0), (WIDTH // 5 + 300, HEIGHT), 3)
    pygame.draw.line(surface, (130, 160, 200), (WIDTH // 5 + 330, 0), (WIDTH // 5 + 330, HEIGHT), 1)
    pygame.draw.line(surface, (130, 160, 200), (WIDTH // 5 + 360, 0), (WIDTH // 5 + 360, HEIGHT), 1)
    pygame.draw.line(surface, (130, 160, 200), (WIDTH // 5 + 390, 0), (WIDTH // 5 + 390, HEIGHT), 1)
    pygame.draw.line(surface, (130, 160, 200), (WIDTH // 5 + 420, 0), (WIDTH // 5 + 420, HEIGHT), 1)
    pygame.draw.line(surface, (130, 160, 200), (WIDTH // 5 + 450, 0), (WIDTH // 5 + 450, HEIGHT), 3)
    pygame.draw.line(surface, (130, 160, 200), (WIDTH // 5 + 480, 0), (WIDTH // 5 + 480, HEIGHT), 1)
    pygame.draw.line(surface, (130, 160, 200), (WIDTH // 5 + 510, 0), (WIDTH // 5 + 510, HEIGHT), 1)
    pygame.draw.line(surface, (130, 160, 200), (WIDTH // 5 + 540, 0), (WIDTH // 5 + 540, HEIGHT), 1)
    pygame.draw.line(surface, (130, 160, 200), (WIDTH // 5 + 570, 0), (WIDTH // 5 + 570, HEIGHT), 1)
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
    pygame.draw.line(surface, (255, 255, 255), (0, HEIGHT//2 + 150), (WIDTH, HEIGHT//2 + 150), 3)
    pygame.draw.line(surface, (255, 255, 255), (WIDTH // 5, 0), (WIDTH // 5, HEIGHT), 3)
    pygame.draw.circle(surface, (255, 0, 0), (WIDTH // 5 + int(simulation.time)*30, HEIGHT//2 + 150 + int(simulation.positiony)), 5)

    # Agregar números a las líneas
    font = pygame.font.Font(None, 20)
    number = 120
    for y in range(0, HEIGHT, 30):
        if number != 0:
            text = font.render(str(number), True, (255, 255, 255))
            surface.blit(text, (WIDTH // 5 - 30, y))
        number -= 10
        

    number = 0
    for x in range(WIDTH // 4 - 9, WIDTH, 30):
        text = font.render(str(number), True, (255, 255, 255))
        surface.blit(text, (x, HEIGHT // 6 + 300))
        number += 1
        
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

#Boton para iniciar la simulación
boton_inicio = Button(ventana, text = "Iniciar Simulación", command = start_simulation, bg = "powder blue")#BOTON
boton_inicio.config(relief=SUNKEN)
boton_inicio.pack()
boton_inicio.place(x = 100, y = 370, width = 160, height = 60)#Pocision del boton

#Boton para el grafico
boton_grafico = Button(ventana, text="Mostrar Gráfico", command=mostrar_grafico, bg="powder blue")
boton_grafico.config(relief=SUNKEN)
boton_grafico.pack()
boton_grafico.place(x=600, y=545, width=120, height=50)

ventana.mainloop()