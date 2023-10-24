# Max ∑(i=1 to n) (valor[i] * x[i])
# Sujeto a: ∑(i=1 to n) (peso[i] * x[i]) <= capacidad
#           x[i] ∈ {0, 1} para todo i


import pulp

# Datos del problema
capacidad = 50
pesos = [10, 20, 30]
valores = [60, 100, 120]

# Crear el problema
problema = pulp.LpProblem("Mochila", pulp.LpMaximize)

# Variables binarias
x = [pulp.LpVariable(f"x{i}", 0, 1, pulp.LpBinary) for i in range(len(pesos))]

# Función objetivo
problema += sum(valores[i] * x[i] for i in range(len(pesos)))

# Restricción de capacidad
problema += sum(pesos[i] * x[i] for i in range(len(pesos))) <= capacidad

# Resolver el problema
problema.solve()
print("Estado:", pulp.LpStatus[problema.status])
for i in range(len(pesos)):
    print(f"x{i} = {x[i].varValue}")


