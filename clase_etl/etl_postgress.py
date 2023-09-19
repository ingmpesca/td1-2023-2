import pandas as pd
import psycopg2


# Ruta al archivo CSV de origen
archivo_origen = "data.csv"

# Leer los datos desde el archivo CSV y especificar que la primera fila es el encabezado
datos = pd.read_csv(archivo_origen, delimiter=';', header=0)

# Puedes realizar transformaciones adicionales aquí si es necesario
datos['suma'] = datos['columna1'] + datos['columna2']


# Configurar la conexión a la base de datos PostgreSQL
conexion = psycopg2.connect(
    database="class",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)

# Crear un cursor para ejecutar comandos SQL
cursor = conexion.cursor()

# Nombre de la tabla en la base de datos
nombre_tabla = "example"

# Crear la tabla en la base de datos si no existe
# Esto es opcional, puedes omitirlo si ya tienes la tabla creada
cursor.execute(f"CREATE TABLE IF NOT EXISTS {nombre_tabla} (columna1 INT, columna2 INT, columna2 INT)")

# Iterar a través de las filas de datos y cargar en la base de datos
for indice, fila in datos.iterrows():
    columna1 = fila['columna1']
    columna2 = fila['columna2']
    suma = fila['suma']
    # Insertar la fila en la tabla
    cursor.execute(f"INSERT INTO {nombre_tabla} (columna1, columna2, suma) VALUES (%s, %s, %s)", (columna1, columna2, suma))

# Confirmar los cambios en la base de datos
conexion.commit()

# Cerrar el cursor y la conexión
cursor.close()
conexion.close()

print("Los datos se han cargado en la base de datos PostgreSQL local.")
