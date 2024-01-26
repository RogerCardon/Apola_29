import yaml
import logging
import os
from typing import Dict, Optional, Union, List
# configurar el nivel
logging.basicConfig(level=logging.DEBUG)


class Tools:

    _devices: Optional[str] = 'devices'
    __backups: Optional[str] = 'backups'

    def __init__(self, path_configuration_file: str):
        self.path_configuration_file = path_configuration_file

    def configuration_file_load(self) -> Dict[str, Union[str, int]]:

        path: Optional[str] = self.path_configuration_file

        try:
            # load configurations from YAML file
            with open(path, 'r', encoding="utf-8") as file:
                config_data = yaml.safe_load(file)

            # Create the variables that will contain the configuration data
            missions: List[str] = config_data['list_misions']
            devices: List[str] = config_data['list_divices']
            status: List[str] = config_data['devices_status']
            consecutive_number: Optional[int] = config_data['consecutive_number']
            mission_label: List[str] = config_data['mission_label']
            exec_waiting_time: Optional[int] = config_data['exec_waiting_time']

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

    def file_cleaner(self,
                     carpeta_origen: Optional[str],
                     carpeta_destino: Optional[str]) -> Optional[None]:
        # Se establece como separador de ruta aquel que arroje segun el OS
        separador_ruta: Optional[str] = os.sep

        # Verificar si la carpeta de backups existe, si no, crearla
        if not os.path.exists(carpeta_destino):
            os.makedirs(carpeta_destino)
            logging.info(f'--> La carpeta {carpeta_destino} ha sido creada')

        # Obtener la lista de archivos en la carpeta de origen
        archivos_a_mover: List[str] = os.listdir(carpeta_origen)
        archivos_movidos: Optional[int] = 0

        # Mover cada archivo a la carpeta de backups
        try:
            for archivo in archivos_a_mover:

                ruta_origen: Optional[str] = f'{carpeta_origen}{separador_ruta}{archivo}'
                ruta_destino: Optional[str] = f'{carpeta_destino}{separador_ruta}{archivo}'

                # Renombrar el archivo moviéndolo
                os.rename(ruta_origen, ruta_destino)
                archivos_movidos += 1

            logging.info(
                f'--> Se movieron {archivos_movidos} archivos a la carpeta backups.')

        except Exception as e:
            logging.error(
                f'--> No se pudo mover los archivos generados a backups por el sigueinte error: {e}')
