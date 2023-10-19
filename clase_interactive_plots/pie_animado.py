import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

fig, ax = plt.subplots()

def animate_pie(i):
    ax.clear()
    data = [random.randint(1, 10) for _ in range(5)]
    ax.pie(data, autopct='%1.1f%%')
    ax.axis('equal')

ani = FuncAnimation(fig, animate_pie, interval=1000)
plt.show()
