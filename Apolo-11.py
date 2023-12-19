# importación de los modulos a utilizar
from devices_status.random_devices_status import random_device_status
import json
import yaml



# Cargar configuraciones desde el archivo YAML
with open('config.yml', 'r') as file:
    config_data = yaml.safe_load(file)

    
# Crear las variables que contienen los datos de configuracion 
missions: list =  config_data['list_misions']
devices: list =  config_data['list_divices']
status: list =  config_data['devices_status']


# Ejecutar las funcion random_device_status ingresando los datos de configuracion previamente cargados 
dices_status = random_device_status(missions, devices, status)


# Imprimimos el diccionario que retorna la funcion random_device_status
json_string = json.dumps(dices_status, indent=4)
print(json_string)

print('---------------------------------------------------------------')