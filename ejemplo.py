import tkinter as tk
import pygame
from pygame.locals import *

# Configuración de la ventana de pygame
WIDTH, HEIGHT = 1000, 600
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
        self.position = self.initial_velocity * self.time + 0.5 * self.acceleration * self.time
        self.positiony = -1*(self.initial_velocity * self.time + 0.5 * self.acceleration * self.time**3)
        self.time += dt

# Función para dibujar la tabla gráfica en pygame
def draw_graph(surface, simulation):
    pygame.draw.line(surface, (255, 255, 255), (0, 450), (WIDTH, 450), 2)
    pygame.draw.line(surface, (255, 255, 255), (WIDTH // 4, 0), (WIDTH // 4, HEIGHT), 2)
    pygame.draw.circle(surface, (255, 0, 0), (WIDTH // 4 + int(simulation.time*100), 450 + int(simulation.positiony)), 5)

# Función para iniciar la simulación
def start_simulation():
    initial_velocity = float(velocity_entry.get())
    acceleration = float(acceleration_entry.get())
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

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

# Crear la interfaz con tkinter
root = tk.Tk()
root.title("Simulación MRUA")

# Etiquetas
velocity_label = tk.Label(root, text="Velocidad inicial:")
velocity_label.pack()
velocity_entry = tk.Entry(root)
velocity_entry.pack()

acceleration_label = tk.Label(root, text="Aceleración:")
acceleration_label.pack()
acceleration_entry = tk.Entry(root)
acceleration_entry.pack()

# Botón para iniciar la simulación
start_button = tk.Button(root, text="Iniciar simulación", command=start_simulation)
start_button.pack()

root.mainloop()
