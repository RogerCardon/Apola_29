from tools.load_tools import configuration_file_load
from tools.write_tools import consecutive_number_update
from hash_funtion.hash_gen import hash_generator
import yaml


def file_generator(path: str, data_mission_devices: dict) -> str:
    config_data: dict = configuration_file_load()
    registry_number = config_data['consecutive_number']
    mission_name = list(data_mission_devices.keys())[0]
    mission = config_data['mission_label'][mission_name]

    # Crear el contenido en formato YAML
    yaml_content = yaml.dump(data_mission_devices, default_flow_style=False)

    # Escribir en el archivo en formato YAML
    with open(f'{path}/APL-{mission}-{registry_number}.log', "w") as file_x:
        result = file_x.write(str(yaml_content))

    consecutive_number_update()
    return result


def file_generator_2(path: str, data_mission_devices: dict) -> str:
    data_device: dict = {}
    registry_number = None
    config_data: dict = configuration_file_load()

    mission_name = list(data_mission_devices.keys())[0]
    fecha: str = data_mission_devices[mission_name]['fecha']
    mission = config_data['mission_label'][mission_name]
    hash_device: str = 'hash'

    for device, status in data_mission_devices[mission_name].items():
        config_data: dict = configuration_file_load()
        registry_number = config_data['consecutive_number']
        hash_device: str = hash_generator(fecha, mission_name, device, status)

        if device != 'fecha':
            data_device[mission_name] = {
                'fecha': fecha,
                device: status,
                'hash': hash_device[0]}

            # Crear el contenido en formato YAML
            yaml_content = yaml.dump(data_device, default_flow_style=False)

            # Escribir en el archivo en formato YAML
            with open(
                f'{path}/APL-{mission}-{registry_number}.log', "w")\
                    as file_x:
                result = file_x.write(str(yaml_content))

            consecutive_number_update()
    return result
