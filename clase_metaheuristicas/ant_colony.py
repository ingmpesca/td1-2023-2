import random
import numpy as np
import matplotlib.pyplot as plt

# Parámetros del problema
num_cities = 20
num_ants = 10
alpha = 1.0  # Peso de la feromona
beta = 2.0   # Peso de la visibilidad
rho = 0.1   # Tasa de evaporación de feromona
q0 = 0.9    # Probabilidad de explotación
max_iterations = 100

# Generación de ciudades aleatorias
random.seed(42)
cities = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(num_cities)]

# Cálculo de distancias entre ciudades
distances = np.zeros((num_cities, num_cities))
for i in range(num_cities):
    for j in range(num_cities):
        distances[i, j] = np.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)

# Inicialización de feromona
pheromone = np.ones((num_cities, num_cities))

# Función para calcular la visibilidad de una arista
def visibility(i, j):
    return 1.0 / distances[i, j]

# Función para seleccionar la siguiente ciudad basada en probabilidad
def select_next_city(current_city, allowed_cities):
    allowed_cities_list = list(allowed_cities)
    if random.random() < q0:
        # Explotación: elige la ciudad con la mayor probabilidad
        return max(allowed_cities_list, key=lambda city: pheromone[current_city][city] * visibility(current_city, city))
    else:
        # Exploración: elige aleatoriamente según las probabilidades
        total_prob = sum(pheromone[current_city][city] * visibility(current_city, city) for city in allowed_cities_list)
        probabilities = [(pheromone[current_city][city] * visibility(current_city, city)) / total_prob for city in allowed_cities_list]
        return allowed_cities_list[np.random.choice(len(allowed_cities_list), p=probabilities)]

# Función para una hormiga
def ant_tour():
    tour = [random.randint(0, num_cities - 1)]
    allowed_cities = set(range(num_cities))
    allowed_cities.remove(tour[0])
    
    for _ in range(num_cities - 1):
        next_city = select_next_city(tour[-1], allowed_cities)
        tour.append(next_city)
        allowed_cities.remove(next_city)
    
    return tour

# Función para calcular la longitud del recorrido de una hormiga
def tour_length(tour):
    length = 0
    for i in range(num_cities):
        length += distances[tour[i]][tour[(i + 1) % num_cities]]
    return length

# Función para actualizar feromona
def update_pheromone(delta_pheromone):
    for i in range(num_cities):
        for j in range(num_cities):
            pheromone[i][j] = (1 - rho) * pheromone[i][j] + delta_pheromone[i][j]

# Algoritmo principal
best_tour = None
best_length = float('inf')

for iteration in range(max_iterations):
    ant_tours = [ant_tour() for _ in range(num_ants)]
    delta_pheromone = np.zeros((num_cities, num_cities))
    
    for tour in ant_tours:
        tour_len = tour_length(tour)
        if tour_len < best_length:
            best_length = tour_len
            best_tour = tour
        
        for i in range(num_cities):
            for j in range(num_cities):
                delta_pheromone[i][j] += 1.0 / tour_len
    
    update_pheromone(delta_pheromone)

# Gráfico de la mejor ruta
best_tour.append(best_tour[0])  # Volver al punto de partida
best_cities = [cities[i] for i in best_tour]
x, y = zip(*best_cities)

plt.figure(figsize=(8, 6))
plt.plot(x, y, 'bo-')
plt.title(f'Mejor Ruta (Longitud: {best_length:.2f})')
plt.xlabel('Coordenada X')
plt.ylabel('Coordenada Y')
plt.grid(True)
plt.show()
