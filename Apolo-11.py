# importación de los modulos a utilizar
from devices_status.random_devices_status import random_device_status
import json
import yaml
from tools.load_tools import configuration_file_load
from tools.write_tools import consecutive_number_update


# Cargar configuraciones desde el archivo YAML
configuration_data: dict = configuration_file_load()

# Ejecutar las funcion random_device_status ingresando los datos de configuracion previamente cargados 
data_mission_devices:dict= random_device_status(configuration_data['missions'],
                                                configuration_data['devices'],
                                                configuration_data['status'])



# Imprimimos el diccionario que retorna la funcion random_device_status
json_string = json.dumps(dices_status, indent=4)
print(json_string)

print('---------------------------------------------------------------')