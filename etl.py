import pandas as pd

# ETL: Extract, Transform, Load

# Ruta al archivo CSV de origen
archivo_origen = "data.csv"

# Leer los datos desde el archivo CSV y especificar que la primera fila es el encabezado
datos = pd.read_csv(archivo_origen, delimiter=';', header=0)

# Verificar los primeros registros
print(datos.head())
print(datos.columns)
# Agregar una nueva columna 'suma' que contenga la suma de dos columnas existentes
# Asumiendo que las columnas se llaman 'columna1' y 'columna2' en tu archivo CSV
datos['suma'] = datos['columna1'] + datos['columna2']

# Verificar los cambios
print(datos.head())

# Ruta al archivo CSV de destino
archivo_destino = "datos_transformados.csv"

# Guardar los datos transformados en un nuevo archivo CSV
datos.to_csv(archivo_destino, index=False)

# Verificar que se haya guardado correctamente
print(f"Los datos transformados se han guardado en {archivo_destino}")
