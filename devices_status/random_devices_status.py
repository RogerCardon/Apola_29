import random
from datetime import datetime


def random_device_status(data_config: dict) -> dict:
    # Se cargan las variables a utilizar desde data_config
    missions: list = data_config['missions']
    devices: list = data_config['devices']
    status: list = data_config['status']

    # Se seleccionan las misiones que se utilizaran
    range_selecting = random.randint(1, 5)
    selected_mission: list = random.sample(missions, range_selecting)
    print(selected_mission)

    # Este diccionario contendrá los datos sobre los
    # dispositivos y sus estados respecto a las misiones seleccionadas
    devices_status: dict = {}
    fecha = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    for mission in selected_mission:
        devices_status[mission] = {}
        for device in devices:
            devices_status[mission]['fecha'] = fecha
            devices_status[mission][device] = random.choice(status)

    return devices_status
