from tools.load_tools import configuration_file_load
from tools.write_tools import consecutive_number_update
import random


def file_generator(path: str,data_mission_devices:dict) -> str:
    config_data: dict = configuration_file_load()
    registry_number = config_data['consecutive_number']
    mission = random.choice(config_data['mission_label'])
    with open((f'{path}/APL-{mission}-{registry_number}.log'), "w") as file_x:
        result = file_x.write(str(data_mission_devices))

    consecutive_number_update()
    return result
