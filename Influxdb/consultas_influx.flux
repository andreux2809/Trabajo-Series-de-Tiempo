// --- Script para realizar una consulta para obtener los promedios de temperatura por ciudad ---

from(bucket: "Datos_Ciudades")
  |> range(start: 2024-11-11T00:00:00Z, stop: 2025-10-16T00:00:00Z)
  |> filter(fn: (r) => r._measurement == "temperatura" and r._field == "ambiente")
  |> group(columns: ["ciudad"])
  |> mean() // Calcula el promedio y lo guarda en la columna _value
  |> map(fn: (r) => ({ r with promedio_temp: r._value })) // Crea la nueva columna 'promedio_temp'
  |> drop(columns: ["_value"]) // Elimina la columna _value original
  |> yield(name: "temperaturas_promedio_nombrada") 


  // --- Nota: A partir de aquí se recomienda crear un nuevo script de Flux dentro del Notebook ---

// Consulta para la Temperatura Máxima por Ciudad

from(bucket: "Datos_Ciudades")
  |> range(start: 2024-11-11T00:00:00Z, stop: 2025-10-16T00:00:00Z)
  |> filter(fn: (r) => r._measurement == "temperatura" and r._field == "ambiente")
  |> group(columns: ["ciudad"])
  |> max() // Calcula el valor máximo
  |> map(fn: (r) => ({ r with temp_maxima: r._value })) // Crea la nueva columna 'temp_maxima'
  |> drop(columns: ["_value"]) // Elimina la columna _value original
  |> yield(name: "temperaturas_maximas")


  // --- Nota: A partir de aquí se recomienda crear un nuevo script de Flux dentro del Notebook ---

// Consulta para la Temperatura Mínima por Ciudad

from(bucket: "Datos_Ciudades")
  |> range(start: 2024-11-11T00:00:00Z, stop: 2025-10-16T00:00:00Z)
  |> filter(fn: (r) => r._measurement == "temperatura" and r._field == "ambiente")
  |> group(columns: ["ciudad"])
  |> min() // Calcula el valor mínimo
  |> map(fn: (r) => ({ r with temp_minima: r._value })) // Crea la nueva columna 'temp_minima'
  |> drop(columns: ["_value"]) // Elimina la columna _value original
  |> yield(name: "temperaturas_minimas")