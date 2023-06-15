import matplotlib.pyplot as plt

def movimiento_rectilineo_uniformemente_acelerado(v0, a, t):
    # Calcula la posición en función del tiempo
    x = v0 * t + 0.5 * a * t**2
    return x

# Valores iniciales
v0 = 0  # Velocidad inicial en m/s
a = 2   # Aceleración constante en m/s^2
t = range(0, 11)  # Lista de tiempos de 0 a 10 segundos

# Calcula las posiciones correspondientes a cada tiempo
posiciones = [movimiento_rectilineo_uniformemente_acelerado(v0, a, tiempo) for tiempo in t]

# Grafica la posición en función del tiempo
plt.plot(t, posiciones)
plt.xlabel('Tiempo (s)')
plt.ylabel('Posición (m)')
plt.title('Movimiento rectilíneo uniformemente acelerado')
plt.grid(True)
plt.show()
