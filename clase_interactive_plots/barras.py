import matplotlib.pyplot as plt
import random
from matplotlib.animation import FuncAnimation

data = []

def animate(i):
    data.append(random.randint(1, 10))
    plt.cla()
    plt.bar(range(1, len(data) + 1), data)
    plt.xlabel('Muestra')
    plt.ylabel('Valor')
    plt.title('Gráfico de Barras en Tiempo Real')

ani = FuncAnimation(plt.gcf(), animate, interval=1000)
plt.tight_layout()
plt.show()
