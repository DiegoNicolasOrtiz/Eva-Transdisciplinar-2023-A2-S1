# se importan las librerias
from tkinter import *
import matplotlib.pyplot as plt
import pygame
from pygame.locals import *
from PIL import Image, ImageTk

# Configuración de la ventana de pygame
WIDTH, HEIGHT = 800, 600
FPS = 60
tiempo_simulacion = 10
#---------------------------------------------------------------------------
#Creación de la ventana principal

ventana = Tk()
ventana.title("Simulación de Movimiento Rectilíneo Uniformemente Acelerado")
ventana.geometry("1500x1000")
ventana.config(bg="RoyalBlue4")

#Creación y configuración de los marcos (frames)
frame_1 = Frame(ventana, bg="steel blue", width="400", height="1000")
frame_1.pack(side=LEFT)
frame_1.config(border="18", relief=SUNKEN)


frame_2 = Frame(ventana, bg="SteelBlue4", width="1300", height="1000")
frame_2.pack(side=TOP)
frame_2.config(border="18", relief=SUNKEN)

#Creación de etiquetas (labels) y campos de entrada (entry)
label_ecuacion = Label(frame_2, text=" x = x₀ + v₀t + (1/2)at² ", bg="orange")
label_ecuacion.pack()
label_ecuacion.place(x=10, y=590)

label_texto = Label(frame_1, text = """Movimiento Rectilíneo Uniformemente Acelerado
(MRUA)""")
label_texto.pack()
label_texto.place(x=35, y=40)

#Creación de etiquetas (labels) y campos de entrada (entry)
label_velocidad = Label(frame_1, text="Velocidad Inicial: ", bg="steel blue")
label_velocidad.pack()
label_velocidad.place(x=35, y=200)

label_aceleracion = Label(frame_1, text="Aceleracion: ", bg="steel blue")
label_aceleracion.pack()
label_aceleracion.place(x=57, y=160)

entry_velocidad = Entry(frame_1)
entry_velocidad.pack()
entry_velocidad.place(x=130, y=200)

aceleracion_entry = Entry(frame_1)
aceleracion_entry.pack()
aceleracion_entry.place(x=130, y=160)



position_label = Label(frame_2, text='Posición: 0')
position_label.pack()
position_label.place(x=10, y=620)

time_label = Label(frame_2, text='Tiempo: 0')
time_label.pack()
time_label.place(x=10, y=650)

#actualizacion de los labels
def update_labels(position, time):
    position_label.config(text=f'Posición: {position}')
    time_label.config(text=f'Tiempo: {time}')

class MRUASimulation:
    def __init__(self, initial_velocity, acceleration):
        self.initial_velocity = initial_velocity
        self.acceleration = acceleration
        self.time = 0
        self.position = 0
        self.positiony = 0

    def update(self, dt):
        self.position = self.initial_velocity * self.time + 0.5 * self.acceleration * self.time
        self.positiony = -1 * (self.initial_velocity * self.time + 0.5 * self.acceleration * self.time ** 3)
        self.position_g = 1 * (self.initial_velocity * self.time + 0.5 * self.acceleration * self.time ** 3)
        self.time += dt

# Función para dibujar la tabla gráfica en pygame
def draw_graph(surface, simulation):
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
    pygame.draw.line(surface, (255, 255, 255), (0, 450), (WIDTH, 450), 3)
    pygame.draw.line(surface, (255, 255, 255), (WIDTH // 4, 0), (WIDTH // 4, HEIGHT), 3)
    pygame.draw.circle(surface, (255, 0, 0), (WIDTH // 4 + int(simulation.time*100), 450 + int(simulation.positiony)), 5)


# Función para iniciar la simulación en pygame
def start_simulation():
    initial_velocity = float(entry_velocidad.get())
    acceleration = float(aceleracion_entry.get())
    simulation = MRUASimulation(initial_velocity, acceleration)
    
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

        simulation.update(1 / FPS)
        draw_graph(surface, simulation)

        pygame.display.flip()
        clock.tick(FPS)

        elapsed_time = simulation.time
        update_labels(simulation.position, elapsed_time)

        if elapsed_time >= tiempo_simulacion:
            running = False

    pygame.quit()    

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
        simulation.update(1 / FPS)
        positions.append(simulation.position_g)
        times.append(simulation.time)

    crear_grafico(positions, times)

boton_inicio = Button(frame_1, text="INICIO", command=start_simulation, bg="powder blue")
boton_inicio.config(relief=SUNKEN)
boton_inicio.pack()
boton_inicio.place(x=90, y=300, width=120, height=60)

boton_grafico = Button(frame_1, text="Mostrar Gráfico", command=mostrar_grafico, bg="powder blue")
boton_grafico.config(relief=SUNKEN)
boton_grafico.pack()
boton_grafico.place(x=90, y=400, width=120, height=60)

ventana.mainloop()
