"""Esta librería permite manipular archivos .yml"""
import yaml


def configuration_file_load() -> None:
    """_summary_

    Returns:
        _type_: _description_
    """

    # load configurations from YAML file
    with open('config.yml', 'r', encoding="utf-8") as file:
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
