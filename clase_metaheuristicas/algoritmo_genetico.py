import random

# Función de aptitud (fitness): cuenta el número de unos en la cadena
def fitness(chromosome):
    return chromosome.count(1)

# Función para generar una población inicial aleatoria
def generate_population(pop_size, chromosome_length):
    population = []
    for _ in range(pop_size):
        chromosome = [random.randint(0, 1) for _ in range(chromosome_length)]
        population.append(chromosome)
    return population

# Función de selección de padres (ruleta)
def select_parents(population, num_parents):
    parents = []
    fitness_sum = sum(fitness(chromosome) for chromosome in population)
    
    for _ in range(num_parents):
        roulette_wheel = random.uniform(0, fitness_sum)
        spin_sum = 0
        for chromosome in population:
            spin_sum += fitness(chromosome)
            if spin_sum >= roulette_wheel:
                parents.append(chromosome)
                break
    
    return parents

# Función de cruce (crossover): punto de cruce
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Función de mutación: cambia un bit aleatorio en el cromosoma
def mutate(chromosome, mutation_rate):
    if random.random() < mutation_rate:
        mutation_point = random.randint(0, len(chromosome) - 1)
        chromosome[mutation_point] = 1 - chromosome[mutation_point]

# Algoritmo Genético principal
def genetic_algorithm(pop_size, chromosome_length, generations, mutation_rate):
    population = generate_population(pop_size, chromosome_length)
    
    for generation in range(generations):
        parents = select_parents(population, pop_size // 2)
        new_population = []
        
        while len(new_population) < pop_size:
            parent1, parent2 = random.sample(parents, 2)
            child1, child2 = crossover(parent1, parent2)
            mutate(child1, mutation_rate)
            mutate(child2, mutation_rate)
            new_population.extend([child1, child2])
        
        population = new_population
    
    best_chromosome = max(population, key=fitness)
    return best_chromosome, fitness(best_chromosome)

# Parámetros del Algoritmo Genético
pop_size = 100
chromosome_length = 50
generations = 100
mutation_rate = 0.01

best_solution, best_fitness = genetic_algorithm(pop_size, chromosome_length, generations, mutation_rate)

print("Mejor cromosoma encontrado:", best_solution)
print("Valor de aptitud (número de unos):", best_fitness)
