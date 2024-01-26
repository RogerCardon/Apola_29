"""Esta librería permite manipular archivos .yml"""
import yaml
import logging
from typing import Dict, Optional, Union
# configurar el nivel
logging.basicConfig(level=logging.DEBUG)


def configuration_file_load() -> Dict[str, Union[str, int]]:
    """_summary_

    Returns:
        _type_: _description_
    """
    try:
        # load configurations from YAML file
        with open('config.yml', 'r', encoding="utf-8") as file:
            config_data: Dict[str, Union[str, int]] = yaml.safe_load(file)

        # Create the variables that will contain the configuration data
        missions: Optional[str] = config_data['list_misions']
        devices: Optional[str] = config_data['list_divices']
        status: Optional[str] = config_data['devices_status']
        consecutive_number: Optional[int] = config_data['consecutive_number']
        mission_label: Optional[str] = config_data['mission_label']
        exec_waiting_time: Optional[str] = config_data['exec_waiting_time']

        return {
            'missions': missions,
            'devices': devices,
            'status': status,
            'consecutive_number': consecutive_number,
            'mission_label': mission_label,
            'exec_waiting_time': exec_waiting_time
        }
    except Exception as e:
        logging.error(
            f'Error de tipo: {e} al cargar el archvio de configuracion')
