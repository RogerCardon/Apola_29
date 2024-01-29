import yaml
from tools.date_provider import DateTimeProvider
from datetime import datetime
import logging
import os
from typing import Dict, Optional, Union, List, Any
# configurar el nivel
logging.basicConfig(level=logging.DEBUG)


class Tools(DateTimeProvider):

    _devices: Optional[str] = 'devices'
    __backups: Optional[str] = 'backups'
    _separators: Optional[str] = os.sep

    def __init__(self, path_configuration_file: str):
        self.path_configuration_file = path_configuration_file

    def __repr__(self):
        return f'Tools(path_configuration_file= \
            {self.path_configuration_file!r})'

    def __str__(self):
        return f'Tools object with configuration file path:\
            {self.path_configuration_file}'

    @property
    def separador(self):
        return self._separators

    @separador.setter
    def separador(self, value):
        self._separators = value

    def configuration_file_load(self) -> Dict[str, Union[Any, str]]:

        path: Optional[str] = self.path_configuration_file

        try:
            # load configurations from YAML file
            with open(path, 'r', encoding="utf-8") as file:
                config_data = yaml.safe_load(file)

            # Create the variables that will contain the configuration data
            missions: List[str] = config_data['list_misions']
            devices: List[str] = config_data['list_divices']
            status: List[str] = config_data['devices_status']
            consecutive_number: Optional[int] = \
                config_data['consecutive_number']
            report_statistics_number: Optional[int] = \
                config_data['report_statistics_number']
            mission_label: List[str] = config_data['mission_label']
            exec_waiting_time: Optional[int] = config_data['exec_waiting_time']

            return {
                'missions': missions,
                'devices': devices,
                'status': status,
                'consecutive_number': consecutive_number,
                'report_statistics_number': report_statistics_number,
                'mission_label': mission_label,
                'exec_waiting_time': exec_waiting_time
            }
        except Exception as e:
            logging.error(
                f'Error de tipo: {e} al cargar el archvio de configuracion')

    @staticmethod
    def file_cleaner(carpeta_origen: Optional[str],
                     carpeta_destino: Optional[str]) -> Optional[None]:
        # Se establece como separador de ruta aquel que arroje segun el OS
        separador_ruta: Optional[str] = os.sep

        # Verificar si la carpeta de backups existe, si no, crearla
        if not os.path.exists(carpeta_destino):
            os.makedirs(carpeta_destino)
            logging.info(f'--> La carpeta {carpeta_destino} ha sido creada')

        # Obtener la lista de archivos en la carpeta de origen
        archivos_a_mover: List[str] = os.listdir(carpeta_origen)

        # Mover cada archivo a la carpeta de backups
        try:
            for archivo in archivos_a_mover:

                ruta_origen: Optional[str] = \
                    f'{carpeta_origen}{separador_ruta}{archivo}'
                ruta_destino: Optional[str] = \
                    f'{carpeta_destino}{separador_ruta}{archivo}'

                # Renombrar el archivo moviéndolo
                os.rename(ruta_origen, ruta_destino)

            logging.info(
                '--> Se movieron los archivos de "devices" a "backups".')

        except Exception as e:
            logging.error(
                f'--> No se pudo mover los archivos generados\
                    a backups por el sigueinte error: {e}')

    def get_current_datetime(self):
        return datetime.now().strftime("%d-%m-%Y %H:%M:%S")
