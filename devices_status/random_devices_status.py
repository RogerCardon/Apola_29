from tools.tools import Tools
import random
from datetime import datetime
import logging
from typing import Dict, Callable, List, Optional
# configurar el nivel
logging.basicConfig(level=logging.DEBUG)


class RandomDevice(Tools):

    def random_device_status(self) -> Dict[int, str]:

        data_config: Callable[[], Dict[str, str]
                              ] = super().configuration_file_load()
        # Se cargan las variables a utilizar desde data_config
        missions: List[str] = data_config['missions']
        devices: List[str] = data_config['devices']
        status: List[str] = data_config['status']

        # Se seleccionan las misiones que se utilizaran
        range_selecting: Optional[int] = random.randint(1, 5)
        list_selected_mission: List[str] = random.sample(
            missions, range_selecting)

        selected_mission: Optional[str] = ', '.join(list_selected_mission)
        logging.info(f'--> Misiones seleccionadas: {selected_mission}')

        # Este diccionario contendrá los datos sobre los
        # dispositivos y sus estados respecto a las misiones seleccionadas
        devices_status: Dict[str] = {}
        fecha: Optional[str] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        try:
            for mission in list_selected_mission:
                devices_status[mission] = {}
                for device in devices:
                    devices_status[mission]['fecha'] = fecha
                    devices_status[mission][device] = random.choice(status)
            return devices_status
        except Exception as e:
            logging.error(
                f'Se genero el error: "{e}" en la generacion aleatoria de los estados de los dispositivos')
