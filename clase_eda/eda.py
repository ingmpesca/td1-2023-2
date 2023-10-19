import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris()
df = pd.DataFrame(data= np.c_[iris['data'], iris['target']], columns= iris['feature_names'] + ['target'])
# Respuesta a la Pregunta 1
longitudes_petalo_no_setosa = df[(df['target'] != 0)]['petal length (cm)'].sort_values()
tercer_valor_mas_pequeño = longitudes_petalo_no_setosa.iloc[2]
print("El tercer valor más pequeño en la longitud del pétalo de las flores que no son 'setosa' es:", tercer_valor_mas_pequeño, "cm.")

# Mostrar las primeras filas del dataframe
print(df.head())

# Obtener información general sobre el dataframe
print(df.info())

# Resumen estadístico de las variables numéricas
print(df.describe())

# Verificar si hay valores nulos en el conjunto de datos
print(df.isnull().sum())

# Histograma de las longitudes del sépalo para cada especie
sns.histplot(data=df, x="sepal length (cm)", hue="target", bins=20)
plt.title("Histograma de Longitud del Sépalo")
plt.xlabel("Longitud del Sépalo (cm)")
plt.ylabel("Frecuencia")
plt.show()

# Diagrama de dispersión de longitud del sépalo vs. ancho del sépalo
sns.scatterplot(data=df, x="sepal length (cm)", y="sepal width (cm)", hue="target")
plt.title("Diagrama de Dispersión Sépalo")
plt.xlabel("Longitud del Sépalo (cm)")
plt.ylabel("Ancho del Sépalo (cm)")
plt.show()

# Diagrama de caja de longitud del pétalo por especie
sns.boxplot(data=df, x="target", y="petal length (cm)")
plt.xticks([0, 1, 2], iris.target_names)
plt.title("Diagrama de Caja de Longitud del Pétalo por Especie")
plt.xlabel("Especie")
plt.ylabel("Longitud del Pétalo (cm)")
plt.show()

# Matriz de correlación
corr_matrix = df.corr()
sns.heatmap(corr_matrix, annot=False, cmap="coolwarm")
plt.title("Matriz de Correlación")
plt.show()
