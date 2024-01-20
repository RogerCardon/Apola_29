import json
import os
import yaml


def mission_statistics_generator() -> None:
    archivo_json = 'mission_statistics.json'
    carpeta_devices: str = 'devices'

    with open(archivo_json, 'r') as archivo:
        statistics_mission_devices = json.load(archivo)

    for file_name in os.listdir(carpeta_devices):  
        with open(f'{carpeta_devices}/{file_name}', 'r') as file:
            print(f'{carpeta_devices}/{file_name}')
            data_divice = yaml.safe_load(file)
        
        for mission, detalles_mission in data_divice.items():
            for devices, status in detalles_mission.items():
                if devices != 'fecha' and devices != 'hash':
                    statistics_mission_devices[mission][devices][status] += 1
                    
                    
    # Guarda el diccionario modificado en el mismo archivo JSON
    with open(archivo_json, 'w') as archivo:
        json.dump(statistics_mission_devices, archivo, indent=4)
