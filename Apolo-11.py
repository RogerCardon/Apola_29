from devices_status.random_devices_status import RandomDevice
from tools.tools import Tools
from tools.data_class import Mission_Information
from file_handling.file_generator import file_generator
from tools.write_tools import report_statistics_number_update
from statistics.mission_statistics import (mission_statistics_generator,
                                           data_statistics_generator)
from statistics.report import report_statistics_generator
from typing import Optional, List, Dict, Any
from datetime import datetime
import time
import os
import logging

# Configure the logging level
logging.basicConfig(level=logging.DEBUG)

report_statistics_number_update()

# Path to the configuration file
path_configuration_file: Optional[str] = 'config.yml'

# Check if the 'devices' and 'statistics_reports'
# folders exist; if not, create them
if not os.path.exists('devices'):
    os.makedirs('devices')
    logging.info(f'--> Folder {"devices"} has been created')

if not os.path.exists('statistics_reports'):
    os.makedirs('statistics_reports')
    logging.info(f'--> Folder {"statistics_reports"} has been created')


# Get the current date and time for execution date
execution_date: Optional[str] = datetime.now().strftime(
    "%d-%m-%Y %H:%M:%S").replace(' ', '-')
report_statistics_number_update()

# Load configurations from the YAML file
tools = Tools(path_configuration_file)

# Set the separator using the setter
tools.separador = os.sep

# Separator
separator: Optional[str] = tools.separador

while True:

    config_data: dict = tools.configuration_file_load()

    # Execute the random_device_status function with the previously
    # loaded configuration data
    randomDevice = RandomDevice(path_configuration_file)
    #data_mission_devices: dict = randomDevice.random_device_status()
    data_mission_devices: dict = randomDevice()

    # Dictionary to store the data that will be written to the .log file
    dict_data_mission_devices: Dict[str, Any] = {}

    # Get the current datetime using the provided method
    cycle_date: Optional[str] = tools.get_current_datetime()

    # Extract mission information
    missions: List[str] = list(data_mission_devices.keys())
    mission_labels: List[str] = [
        config_data['mission_label'][mission] for mission in missions]
    missions_labels_str: Optional[str] = '-'.join(mission_labels)

    mission_inf = Mission_Information(
        missions=missions,
        mission_labels=mission_labels,
        missions_labels_str=missions_labels_str)

    # Path for the cycle folder
    cycle_folder: Optional[str] = \
        f'devices{separator}CYCLE-{cycle_date}-\
            {mission_inf.missions_labels_str}'.replace(
        ' ', '-')
    os.makedirs(cycle_folder)

    # Iterate over mission devices and generate files
    for key, value in data_mission_devices.items():
        dict_data_mission_devices[key] = value
        file_generator(cycle_folder, dict_data_mission_devices)

        # Reset the dictionary to avoid accumulating data
        dict_data_mission_devices: Dict[str, Any] = {}

    # Generate statistics for the states of devices in missions
    mission_statistics_generator(cycle_folder)
    file_name = data_statistics_generator(execution_date)
    report_statistics_generator(file_name)

    # After generating statistics, move the files to the 'backups' folder
    Tools.file_cleaner('devices', 'backups')

    # Wait for the specified execution time
    wait_time: int = config_data["exec_waiting_time"]
    time.sleep(wait_time)
