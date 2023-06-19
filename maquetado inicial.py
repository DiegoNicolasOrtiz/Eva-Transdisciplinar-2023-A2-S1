import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class MRUASimulation:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulación de MRUA")
        
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(side=tk.LEFT, padx=10)
        
        self.graph_frame = tk.Frame(self.root)
        self.graph_frame.pack(side=tk.LEFT, padx=10)
        
        self.simulation_frame = tk.Frame(self.root)
        self.simulation_frame.pack(side=tk.LEFT, padx=10)
        
        self.create_input_widgets()
        self.create_graph_widgets()
        self.create_simulation_widgets()
        
    def create_input_widgets(self):
        input_label = tk.Label(self.input_frame, text="Datos de entrada")
        input_label.pack()
        
        self.entry_velocity = self.create_input_entry("Velocidad inicial:")
        self.entry_acceleration = self.create_input_entry("Aceleración:")
        self.entry_time = self.create_input_entry("Tiempo:")
        
        calculate_button = tk.Button(self.input_frame, text="Calcular", command=self.calculate)
        calculate_button.pack(pady=10)
        
    def create_input_entry(self, label_text):
        entry_frame = tk.Frame(self.input_frame)
        entry_frame.pack()
        
        label = tk.Label(entry_frame, text=label_text)
        label.pack(side=tk.LEFT)
        
        entry = tk.Entry(entry_frame)
        entry.pack(side=tk.LEFT)
        
        return entry
    
    def create_graph_widgets(self):
        graph_label = tk.Label(self.graph_frame, text="Gráfica")
        graph_label.pack()
        
        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.plot = self.figure.add_subplot(111)
        
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.graph_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()
        
    def create_simulation_widgets(self):
        simulation_label = tk.Label(self.simulation_frame, text="Simulación")
        simulation_label.pack()
        
        self.canvas_simulation = tk.Canvas(self.simulation_frame, width=300, height=200, bg="white")
        self.canvas_simulation.pack(pady=10)
        
    def calculate(self):
        velocity = float(self.entry_velocity.get())
        acceleration = float(self.entry_acceleration.get())
        time = float(self.entry_time.get())
        
        t = np.linspace(0, time, num=100)
        displacement = velocity * t + 0.5 * acceleration * t**2
        
        self.plot.clear()
        self.plot.plot(t, displacement)
        self.plot.set_xlabel("Tiempo")
        self.plot.set_ylabel("Desplazamiento")
        
        self.canvas.draw()
        
        self.animate_simulation(displacement, time)
        
    def animate_simulation(self, displacement, time):
        self.canvas_simulation.delete("all")
        
        x_start = 50
        y_start = 150
        x_end = 250
        y_end = 150
        
        self.canvas_simulation.create_line(x_start, y_start, x_end, y_end)
        
        num_steps = len(displacement)
        step_duration = time / num_steps
        
        for i in range(num_steps):
            x = x_start + (x_end - x_start) * (displacement[i] / displacement[-1])
            y = y_start
            
            self.canvas_simulation.create_oval(x-5, y-5, x+5, y+5, fill="red")
            self.root.update()
            
            if i < num_steps - 1:
                self.canvas_simulation.after(int(step_duration * 1000))
                self.canvas_simulation.delete("all")
                self.canvas_simulation.create_line(x_start, y_start, x_end, y_end)
                
        self.canvas_simulation.create_oval(x-5, y-5, x+5, y+5, fill="red")        

root = tk.Tk()
simulation = MRUASimulation(root)
root.mainloop()
