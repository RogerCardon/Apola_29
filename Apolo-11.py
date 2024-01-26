# importación de los módulos a utilizar
# from tools.load_tools import configuration_file_load
from devices_status.random_devices_status import RandomDevice
from tools.tools import Tools
from file_handling.file_generator import file_generator
from statistics.mission_statistics import mission_statistics_generator
from typing import Dict, Callable, List, Optional
import time
import os
import logging

# configurar el nivel
logging.basicConfig(level=logging.DEBUG)

while True:

    path_configuration_file: Optional[str] = 'config.yml'

    # Verificar si la carpeta de backups existe, si no, crearla
    if not os.path.exists('devices'):
        os.makedirs('devices')
        logging.info(f'--> La carpeta {"devices"} ha sido creada')

    # Cargar configuraciones desde el archivo YAML
    # config_data: dict = configuration_file_load()

    tools = Tools(path_configuration_file)

    config_data: dict = tools.configuration_file_load()
    # Ejecutar las función random_device_status ingresando los
    # datos de configuración previamente cargados

    randomDevice = RandomDevice(path_configuration_file)
    data_mission_devices: dict = randomDevice.random_device_status()

    # Diccionario que contendra el dicicionario que se escribira en el .log
    dict_data_mission_devices = {}

    for key, value in data_mission_devices.items():
        dict_data_mission_devices[key] = value
        file_generator('devices', dict_data_mission_devices)

        # Se rescribe el diccionario para que no acomule los datos
        dict_data_mission_devices = {}

    # Generamos las estadisticas de las los estados de los
    # dispositivos de las misiones
    mission_statistics_generator()

    # Luego de ejecutar la funcion que genera los estadisticos
    # de ejecuta la funcion que mueve los archvios a la carpeta buckups

    tools.file_cleaner('devices', 'backups')
    # file_cleaner('devices', 'backups')

    # Imprimimos el diccionario que retorna la función random_device_status
    # json_string = json.dumps(data_mission_devices, indent=4)
    # print(json_string)
    # print('---------------------------------------------------------------')
    wait_time: int = config_data["exec_waiting_time"]
    time.sleep(wait_time)
