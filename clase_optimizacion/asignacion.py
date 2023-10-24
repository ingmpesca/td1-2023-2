
# Min ∑(i=1 to n) ∑(j=1 to n) (costo[i][j] * x[i][j])
# Sujeto a: ∑(i=1 to n) x[i][j] = 1 para todo j
#           ∑(j=1 to n) x[i][j] = 1 para todo i
#           x[i][j] ∈ {0, 1} para todo i y j

import pulp

# Datos del problema
costo = [[10, 8, 9], [10, 9, 8], [8, 9, 10]]

# Crear el problema
problema = pulp.LpProblem("AsignacionOptima", pulp.LpMinimize)

# Variables binarias
x = [[pulp.LpVariable(f"x{i}_{j}", 0, 1, pulp.LpInteger) for j in range(len(costo[i]))] for i in range(len(costo))]

# Función objetivo
problema += sum(costo[i][j] * x[i][j] for i in range(len(costo)) for j in range(len(costo[i])))

# Restricciones
for i in range(len(costo)):
    problema += sum(x[i][j] for j in range(len(costo[i]))) == 1
for j in range(len(costo[i])):
    problema += sum(x[i][j] for i in range(len(costo))) == 1

# Resolver el problema
problema.solve()
print("Estado:", pulp.LpStatus[problema.status])
for i in range(len(costo)):
    for j in range(len(costo[i])):
        print(f"x{i}_{j} = {x[i][j].varValue}")
