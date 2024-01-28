# importación de los módulos a utilizar
# from tools.load_tools import configuration_file_load
from devices_status.random_devices_status import RandomDevice
from tools.tools import Tools
from file_handling.file_generator import file_generator
from tools.write_tools import report_statistics_number_update
from statistics.mission_statistics import mission_statistics_generator, data_statistics_generator
from statistics.report import report_statistics_generator
from typing import Optional, List
from datetime import datetime
import time
import os
import logging
import json

# configurar el nivel
logging.basicConfig(level=logging.DEBUG)


execution_date: Optional[str] = datetime.now().strftime(
    "%d-%m-%Y %H:%M:%S").replace(' ', '-')
report_statistics_number_update()

while True:

    path_configuration_file: Optional[str] = 'config.yml'

    # Verificar si la carpeta de devices y statistics_reports existen, si no, crearla
    if not os.path.exists('devices'):
        os.makedirs('devices')
        logging.info(f'--> La carpeta {"devices"} ha sido creada')
        
    if not os.path.exists('statistics_reports'):
        os.makedirs('statistics_reports')
        logging.info(f'--> La carpeta {"statistics_reports"} ha sido creada')

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

    # Fecha
    cycle_date: Optional[str] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    # Missions
    missions: List[str] = list(data_mission_devices.keys())

    # Mission labels
    mission_labels: List[str] = [
        config_data['mission_label'][mission] for mission in missions]
    missions_labels_str: Optional[str] = '-'.join(mission_labels)

    # Separator
    separator: Optional[str] = os.sep

    # Variable que contendra el path de la carpeta del ciclo
    cycle_folder: Optional[str] = f'devices{separator}CYCLE-{cycle_date}-{missions_labels_str}'.replace(
        ' ', '-')
    os.makedirs(cycle_folder)

    for key, value in data_mission_devices.items():
        dict_data_mission_devices[key] = value
        file_generator(cycle_folder, dict_data_mission_devices)

        # Se rescribe el diccionario para que no acomule los datos
        dict_data_mission_devices = {}

    # Generamos las estadisticas de las los estados de los
    # dispositivos de las misiones
    mission_statistics_generator(cycle_folder)
    file_name = data_statistics_generator(execution_date)
    report_statistics_generator(file_name)

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
