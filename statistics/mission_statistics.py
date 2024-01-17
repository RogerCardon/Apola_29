import json


def mission_statistics_generator(data_mission_devices) -> None:
    archivo_json = 'mission_statistics.json'

    with open(archivo_json, 'r') as archivo:
        statistics_mission_devices = json.load(archivo)

    for mission, detalles_mission in data_mission_devices.items():
        for devices, status in detalles_mission.items():
            if devices != 'fecha' and devices != 'hash':
                statistics_mission_devices[mission][devices][status] += 1

    # Guarda el diccionario modificado en el mismo archivo JSON
    with open(archivo_json, 'w') as archivo:
        json.dump(statistics_mission_devices, archivo, indent=4)
