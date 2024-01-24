import random
from datetime import datetime
import logging

# configurar el nivel
logging.basicConfig(level=logging.DEBUG)


def random_device_status(data_config: dict) -> dict:
    # Se cargan las variables a utilizar desde data_config
    missions: list = data_config['missions']
    devices: list = data_config['devices']
    status: list = data_config['status']

    # Se seleccionan las misiones que se utilizaran
    range_selecting = random.randint(1, 5)
    list_selected_mission: list = random.sample(missions, range_selecting)
    
    selected_mission: str = ', '.join(list_selected_mission)
    logging.info(f'--> Misiones seleccionadas: {selected_mission}')

    # Este diccionario contendrá los datos sobre los
    # dispositivos y sus estados respecto a las misiones seleccionadas
    divices_status: dict = {}
    fecha = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    try:
        for mission in list_selected_mission:
            divices_status[mission] = {}
            for device in devices:
                divices_status[mission]['fecha'] = fecha
                divices_status[mission][device] = random.choice(status)
        return divices_status
    except Exception as e:
        logging.error(
            f'Se genero el error: "{e}" en la generacion aleatoria de los estados de los dispositivos')
