import tkinter as tk
import pygame
from PIL import Image, ImageTk

class MRUASimulacion:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Simulación MRUA")
        
        self.velocidad = 0
        self.aceleracion = 0
        self.tiempo = 0
        self.posicion = 0
        
        self.crear_widgets()
        
    def crear_widgets(self):
        # Frame de entrada
        entrada = tk.Frame(self.ventana)
        entrada.pack(pady=10)
        
        # Etiquetas y campos de entrada
        tk.Label(entrada, text="Velocidad inicial (m/s):").grid(row=0, column=0, padx=5, pady=5)
        self.velocidad_entrada = tk.Entry(entrada)
        self.velocidad_entrada.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(entrada, text="Aceleración (m/s^2):").grid(row=1, column=0, padx=5, pady=5)
        self.aceleracion_entrada = tk.Entry(entrada)
        self.aceleracion_entrada.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(entrada, text="Tiempo (s):").grid(row=2, column=0, padx=5, pady=5)
        self.tiempo_entrada = tk.Entry(entrada)
        self.tiempo_entrada.grid(row=2, column=1, padx=5, pady=5)
        
        # Botón de simulación
        simulacion = tk.Button(self.ventana, text="Simular", command=self.simulacion)
        simulacion.pack(pady=10)
        
        # Widget de imagen
        self.image_label = tk.Label(self.ventana)
        self.image_label.pack(pady=10)
        
    def simulacion(self):
        try:
            self.velocidad = float(self.velocidad_entrada.get())
            self.aceleracion = float(self.aceleracion_entrada.get())
            self.time = float(self.tiempo_entrada.get())
            
            self.posicion = self.velocidad * self.tiempo + 0.5 * self.aceleracion * self.tiempo**2
            self.velocidad += self.aceleracion * self.tiempo
            
            pygame.init()
            surface = pygame.Surface((600, 600))
            pygame.draw.circle(surface, (255, 0, 0), (50, 50), 20)
            py_Mage = pygame.image.tostring(surface, "RGB")
            
            imagen = Image.frombytes("RGB", surface.get_size(), py_Mage)
            foto = ImageTk.PhotoImage(imagen)
            
            self.image_label.config(image=foto)
            self.image_label.image = foto
            
            pygame.quit()
        except ValueError:
            self.image_label.config(image=None)
        
if __name__ == "__main__":
    ventana = tk.Tk()
    mrua = MRUASimulacion(ventana)
    ventana.mainloop()
