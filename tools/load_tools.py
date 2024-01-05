"""Esta librería permite manipular archivos .yml"""
import yaml


def configuration_file_load()->None:
    """_summary_

    Returns:
        _type_: _description_
    """

    # load configurations from YAML file
    with open('config.yml', 'r', encoding="utf-8") as file:
        config_data = yaml.safe_load(file)

    # Create the variables that will contain the configuration data
    missions = config_data['missions']
    devices = config_data['devices']
    status = config_data['divices_statug']
    consecutive_number = config_data['consecutive_number']

    return {
        'missions': missions,
        'devices': devices,
        'status': status,
        'consecutive_number': consecutive_number
    }
