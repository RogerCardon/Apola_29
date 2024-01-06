# importación de los módulos a utilizar
from tools.load_tools import configuration_file_load
from devices_status.random_devices_status import random_device_status
from file_handling.file_generator import file_generator
import json


# Cargar configuraciones desde el archivo YAML
config_data: dict = configuration_file_load()

# Ejecutar las función random_device_status ingresando los
# datos de configuración previamente cargados
data_mission_devices: dict = random_device_status(config_data)

# Ejecutamos la función file_generator
# para generar los archivos de las misiones
file_generator('devices',data_mission_devices)

# Imprimimos el diccionario que retorna la función random_device_status
json_string = json.dumps(data_mission_devices, indent=4)
#print(json_string)
#print('---------------------------------------------------------------')
