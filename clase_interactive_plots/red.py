import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo dirigido
G = nx.DiGraph()

# Agregar nodos (personajes) con atributos
G.add_node("Homer", relation="Padre")
G.add_node("Marge", relation="Madre")
G.add_node("Bart", relation="Hijo")
G.add_node("Lisa", relation="Hija")
G.add_node("Maggie", relation="Hija")
G.add_node("Abe", relation="Abuelo")
G.add_node("Mona", relation="Abuela")

# Agregar relaciones familiares (aristas)
family_relations = [
    ("Homer", "Bart"),
    ("Homer", "Lisa"),
    ("Homer", "Maggie"),
    ("Marge", "Bart"),
    ("Marge", "Lisa"),
    ("Marge", "Maggie"),
    ("Abe", "Homer"),
    ("Abe", "Mona"),
]

G.add_edges_from(family_relations)

# Definir opciones de estilo
node_color = 'lightblue'  # Color de los nodos
edge_color = 'gray'       # Color de las aristas
node_size = 300           # Tamaño de los nodos
font_size = 10            # Tamaño de la fuente
font_color = 'black'     # Color de la fuente
with_labels = True        # Mostrar etiquetas de los nodos
node_shape = 'o'          # Forma de los nodos ('o' para círculos)
edge_width = 1.0          # Grosor de las aristas

# Crear el gráfico con estilo personalizado y disposición shell_layout
plt.figure(figsize=(8, 8))  # Tamaño de la figura
pos = nx.shell_layout(G)

# Dibujar nodos
nx.draw_networkx_nodes(G, pos, node_color=node_color, node_size=node_size, node_shape=node_shape)
nx.draw_networkx_labels(G, pos, font_size=font_size, font_color=font_color)

# Dibujar aristas
nx.draw_networkx_edges(G, pos, edge_color=edge_color, width=edge_width)

# Mostrar el gráfico
plt.axis('off')  # Ocultar ejes
plt.title("Árbol Genealógico de los Simpson")
plt.show()
