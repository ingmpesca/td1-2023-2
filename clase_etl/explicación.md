# Tutorial de Pandas

Este tutorial proporciona una introducción detallada a la biblioteca Pandas de Python, utilizada para el análisis y manipulación de datos.

## Contenido

1. [Instalación de Pandas](#instalación-de-pandas)
2. [Introducción a Pandas](#introducción-a-pandas)
    - 2.1 [Importar Pandas](#importar-pandas)
    - 2.2 [Estructuras de Datos en Pandas](#estructuras-de-datos-en-pandas)
3. [Carga de Datos](#carga-de-datos)
    - 3.1 [Cargar desde un archivo CSV](#cargar-desde-un-archivo-csv)
    - 3.2 [Cargar desde un DataFrame Existente](#cargar-desde-un-dataframe-existente)
4. [Exploración de Datos](#exploración-de-datos)
    - 4.1 [Visualización de Datos](#visualización-de-datos)
    - 4.2 [Resumen Estadístico](#resumen-estadístico)
5. [Manipulación de Datos](#manipulación-de-datos)
    - 5.1 [Selección de Datos](#selección-de-datos)
    - 5.2 [Filtrado de Datos](#filtrado-de-datos)
    - 5.3 [Modificación de Datos](#modificación-de-datos)
6. [Operaciones en Columnas](#operaciones-en-columnas)
    - 6.1 [Agregar una Nueva Columna](#agregar-una-nueva-columna)
    - 6.2 [Aplicar Funciones a Columnas](#aplicar-funciones-a-columnas)
7. [Agrupación y Agregación de Datos](#agrupación-y-agregación-de-datos)
    - 7.1 [Agrupación de Datos](#agrupación-de-datos)
    - 7.2 [Agregación de Datos](#agregación-de-datos)
8. [Manejo de Datos Faltantes](#manejo-de-datos-faltantes)
9. [Exportar Datos](#exportar-datos)

## Instalación de Pandas

Si aún no tienes pandas instalado, puedes hacerlo usando pip:

```bash
pip install pandas
```

# Introducción a Pandas
## Importar Pandas

```python
import pandas as pd
```

# Estructuras de Datos en Pandas
*  DataFrame: Una tabla bidimensional con etiquetas en filas y columnas.
* Series: Una estructura unidimensional similar a una columna en un DataFrame.

# Carga de Datos
## Cargar desde un archivo CSV

```python
data = pd.read_csv('archivo.csv')
```

## Cargar desde un DataFrame Existente
```python
df2 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
```

# Exploración de Datos
## Visualización de Datos

```python
df.head()          # Muestra las primeras filas del DataFrame
df.tail()          # Muestra las últimas filas del DataFrame
df.sample(5)       # Muestra una muestra aleatoria de filas
```

## Resumen Estadístico
```python
df.describe()      # Proporciona estadísticas resumidas
df.info()          # Proporciona información sobre el DataFrame
```

# Manipulación de Datos
## Selección de Datos
```python
df['columna']                # Selecciona una columna
df[['col1', 'col2']]         # Selecciona múltiples columnas
df.loc[etiqueta_fila]        # Selecciona filas por etiqueta
df.iloc[indice_fila]         # Selecciona filas por índice
```
## Filtrado de Datos
```python
df[df['columna'] > 10]       # Filtra filas basadas en una condición
```
## Modificación de Datos
```python
df['columna'] = nueva_data    # Modifica una columna
```

## Operaciones en Columnas
# Agregar una Nueva Columna
```python
df['nueva_col'] = df['col1'] + df['col2']  # Agrega una nueva columna
```

# Aplicar Funciones a Columnas
```python
df['col'] = df['col'].apply(funcion)       # Aplica una función a una columna
```

# Agrupación y Agregación de Datos
## Agrupación de Datos
```python
grupo = df.groupby('columna')              # Agrupa por valores en una columna
```
## Agregación de Datos
```python
grupo['columna'].agg(['sum', 'mean'])      # Realiza operaciones de agregación
```
## Manejo de Datos Faltantes
```python
df.isnull()            # Comprueba valores nulos
df.dropna()            # Elimina filas con valores nulos
df.fillna(valor)       # Rellena valores nulos con un valor específico
```
## Exportar Datos
```python
df.to_csv('nuevo_archivo.csv', index=False)  # Exporta DataFrame a un archivo CSV
```
