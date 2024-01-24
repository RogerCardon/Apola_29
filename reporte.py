import pandas as pd
import json


# Convertir el JSON a un diccionario
json_data = json.loads("mission_statistics.json")

# Crear un DataFrame vacío
df = pd.DataFrame()

# Iterar a través de las claves externas (por ejemplo, "OrbitOne", "ColonyMoon", etc.)
for outer_key, outer_value in json_data.items():
    # Iterar a través de las claves internas (por ejemplo, "satelite", "spacecraft", etc.)
    for inner_key, inner_value in outer_value.items():
        # Crear nombres de columnas basados en las claves externas e internas
        column_names = [f"{outer_key}_{inner_key}_{status}" for status in inner_value.keys()]
        # Crear un DataFrame con los valores internos y usar los nombres de columnas
        inner_df = pd.DataFrame([inner_value], columns=column_names, index=[outer_key])
        # Concatenar el DataFrame interno al DataFrame principal
        df = pd.concat([df, inner_df])

# Mostrar el DataFrame resultante
print(df)
