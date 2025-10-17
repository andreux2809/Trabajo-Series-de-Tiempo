import csv
import datetime
import random

# --- CONFIGURACIÓN ---

# 1. Definición de las columnas y el nombre del archivo de salida
NOMBRE_ARCHIVO_SALIDA = 'datos_temperatura.csv'
CABECERA = ['time', 'ciudad', 'temperatura']

# 2. Especificaciones de la serie de tiempo
FECHA_INICIO = datetime.date(2024, 11, 16)
NUMERO_DE_DIAS = 334  # 334 días * 3 provincias = 1002 registros

# 3. Especificaciones de las variables categóricas y numéricas
PROVINCIAS = ["Santo Domingo", "La Sábana", "Paraíso"]

# Diccionario con los rangos de temperatura para cada provincia
RANGOS_TEMPERATURA = {
    "Santo Domingo": (22.0, 27.0),
    "La Sábana": (23.0, 28.0),
    "Paraíso": (19.0, 26.0)
}

# --- LÓGICA DE GENERACIÓN DE DATOS ---

def generar_datos():
    """
    Función principal que genera los datos y los prepara para ser escritos en el CSV.
    """
    print("Iniciando la generación de datos...")
    
    # Lista para almacenar todas las filas de datos que se generarán
    datos_para_csv = []

    # Bucle principal que itera a través del número de días especificado
    for i in range(NUMERO_DE_DIAS):
        # Calculamos la fecha actual para esta iteración
        fecha_actual = FECHA_INICIO + datetime.timedelta(days=i)
        
        # Formateamos la fecha según el requisito "año-mes-día-hora-minuto-segundo"
        # Se usará 00:00:00 como hora, minuto y segundo estándar para cada día.
        timestamp_str = fecha_actual.strftime('%Y-%m-%d') + "-00-00-00"

        # Bucle anidado para crear un registro para cada provincia en la fecha actual
        for provincia in PROVINCIAS:
            # Obtenemos el rango de temperatura para la provincia actual
            min_temp, max_temp = RANGOS_TEMPERATURA[provincia]
            
            # Generamos un valor de temperatura aleatorio (flotante) dentro del rango
            temperatura_aleatoria = random.uniform(min_temp, max_temp)
            
            # Formateamos la temperatura a dos decimales para un aspecto más limpio
            temperatura_formateada = f"{temperatura_aleatoria:.2f}"
            
            # Creamos la fila como una lista de valores
            fila = [timestamp_str, provincia, temperatura_formateada]
            
            # Añadimos la fila a nuestra lista de datos
            datos_para_csv.append(fila)
            
    print(f"Generación de datos completada. Se crearon {len(datos_para_csv)} registros.")
    return datos_para_csv

def escribir_csv(nombre_archivo, cabecera, datos):
    """
    Función que escribe los datos generados en un archivo CSV.
    """
    print(f"Escribiendo datos en el archivo '{nombre_archivo}'...")
    try:
        # Usamos 'with' para asegurar que el archivo se cierre correctamente
        # newline='' evita filas en blanco entre los datos en Windows
        # encoding='utf-8' es una buena práctica para evitar problemas con caracteres especiales
        with open(nombre_archivo, 'w', newline='', encoding='utf-8') as archivo_csv:
            # Creamos un objeto escritor de CSV
            escritor = csv.writer(archivo_csv)
            
            # Escribimos la fila de la cabecera
            escritor.writerow(cabecera)
            
            # Escribimos todas las filas de datos de una sola vez
            escritor.writerows(datos)
            
        print(f"¡Éxito! El archivo '{nombre_archivo}' ha sido creado correctamente.")
    except IOError as e:
        print(f"Error al escribir el archivo: {e}")

# --- EJECUCIÓN DEL SCRIPT ---

if __name__ == "__main__":
    datos_generados = generar_datos()
    escribir_csv(NOMBRE_ARCHIVO_SALIDA, CABECERA, datos_generados)