import yaml
import logging
# configurar el nivel
logging.basicConfig(level=logging.DEBUG)


class Tools:

    def __init__(self, path_configuration_file: str):
        self.path_configuration_file = path_configuration_file

    def configuration_file_load(self) -> dict:

        path: str = self.path_configuration_file

        try:
            # load configurations from YAML file
            with open(path, 'r', encoding="utf-8") as file:
                config_data = yaml.safe_load(file)

            # Create the variables that will contain the configuration data
            missions = config_data['list_misions']
            devices = config_data['list_divices']
            status = config_data['devices_status']
            consecutive_number = config_data['consecutive_number']
            mission_label = config_data['mission_label']

            return {
                'missions': missions,
                'devices': devices,
                'status': status,
                'consecutive_number': consecutive_number,
                'mission_label': mission_label
            }
        except Exception as e:
            logging.error(
                f'Error de tipo: {e} al cargar el archvio de configuracion')
