import matplotlib.pyplot as plt
from itertools import count
import random
from matplotlib.animation import FuncAnimation

x = []
y = []

index = count()

def animate(i):
    x.append(next(index))
    y.append(random.randint(0, 100))
    plt.cla()
    plt.plot(x, y, label='Datos en tiempo real')
    plt.xlabel('Tiempo')
    plt.ylabel('Valor')
    plt.legend()

ani = FuncAnimation(plt.gcf(), animate, interval=1000)
plt.tight_layout()
plt.show()