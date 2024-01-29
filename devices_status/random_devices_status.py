from tools.tools import Tools
import random
import logging
from typing import Dict, Callable, List, Optional

# Set the logging level
logging.basicConfig(level=logging.DEBUG)


class RandomDevice(Tools):

    def random_device_status(self) -> Dict[int, str]:

        data_config: Callable[[], Dict[str, str]
                              ] = super().configuration_file_load()
        # Load variables to be used from data_config
        missions: List[str] = data_config['missions']
        devices: List[str] = data_config['devices']
        status: List[str] = data_config['status']

        # Select missions to be used
        range_selecting: Optional[int] = random.randint(1, 5)
        list_selected_mission: List[str] = random.sample(
            missions, range_selecting)

        selected_mission: Optional[str] = ', '.join(list_selected_mission)
        logging.info(f'--> Missions: {selected_mission}')

        # This dictionary will contain data about devices and their states
        # with respect to the selected missions
        devices_status: Dict[str] = {}
        fecha: Optional[str] = super().get_current_datetime()
        try:
            for mission in list_selected_mission:
                devices_status[mission] = {}
                for device in devices:
                    devices_status[mission]['fecha'] = fecha
                    devices_status[mission][device] = random.choice(status)
            return devices_status
        except Exception as e:
            logging.error(
                f'Error occurred: "{e}" during random'
                f'generation of device states')

    def __call__(self, ):
        devices_status_call: Dict[str] = self.random_device_status()
        return devices_status_call
