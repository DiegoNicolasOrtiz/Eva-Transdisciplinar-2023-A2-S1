import pygame
from tkinter import *
from matplotlib import pyplot as plt

# Configuración de la ventana de pygame
WIDTH, HEIGHT = 800, 600
FPS = 60

# Configuración de la ventana de Tkinter
ventana = Tk()
ventana.title("Simulación de Movimiento Rectilíneo Uniformemente Acelerado")
ventana.geometry("900x600")
ventana.config(bg="RoyalBlue4")

# Variables de movimiento
velocidad_inicial = 0
aceleracion = 0

# Función para iniciar la simulación
def start_simulation():
    global velocidad_inicial, aceleracion
    velocidad_inicial = float(entry_velocidad.get())
    aceleracion = float(aceleracion_entry.get())

    # Configuración de la ventana de pygame
    pygame.init()
    clock = pygame.time.Clock()
    ventana = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Simulación de Movimiento Rectilíneo Uniformemente Acelerado")

    tiempo_simulacion = 10  # Tiempo total de la simulación en segundos
    time_interval = 1 / FPS

    simulation = MRUASimulation(velocidad_inicial, aceleracion)

    running = True
    posicion = []
    tiempo = []
    elapsed_time = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Actualizar y dibujar la simulación
        simulation.update(time_interval)
        posicion.append(simulation.position)
        tiempo.append(elapsed_time)
        elapsed_time += time_interval

        ventana.fill((0, 0, 0))
        start_simulation(ventana, simulation)

        pygame.display.flip()
        clock.tick(FPS)

        # Detener la simulación después de cierto tiempo
        if elapsed_time >= tiempo_simulacion:
            running = False

    # Mostrar el gráfico al final de la simulación
    crear_grafico(posicion, tiempo)

    pygame.quit()

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

def crear_grafico(posicion, tiempo):
    plt.plot(tiempo, posicion)
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Posición (m)')
    plt.title('Simulación de Movimiento Rectilíneo Uniforme Acelerado')
    plt.grid(True)
    plt.show()

# Etiquetas y campos de entrada de Tkinter
frame_1 = Frame(ventana, bg="steel blue", width=300, height=600, border=15, relief=SUNKEN)
frame_1.pack(side=LEFT)

label_velocidad = Label(frame_1, text="Velocidad Inicial: ", bg="steel blue")
label_velocidad.pack()
label_velocidad.place(x=35, y=200)

label_aceleracion = Label(frame_1, text="Aceleración: ", bg="steel blue")
label_aceleracion.pack()
label_aceleracion.place(x=57, y=160)

entry_velocidad = Entry(frame_1)
entry_velocidad.pack()
entry_velocidad.place(x=130, y=200)

aceleracion_entry = Entry(frame_1)
aceleracion_entry.pack()
aceleracion_entry.place(x=130, y=160)

frame_2 = Frame(ventana, bg="SteelBlue4", width=600, height=150, border=15, relief=SUNKEN)
frame_2.pack(side=BOTTOM)

frame_3 = Frame(ventana, bg="SteelBlue4", width=600, height=450, border=15, relief=SUNKEN)
frame_3.pack(side=TOP)

position_label = Label(frame_2, text='Posición: 0')
position_label.pack()

time_label = Label(frame_2, text='Tiempo: 0')
time_label.pack()

boton_inicio = Button(frame_2, text="INICIO", command=start_simulation, bg="powder blue", relief=SUNKEN)
boton_inicio.pack()
boton_inicio.place(x=90, y=270, width=120, height=60)

ventana.mainloop()
