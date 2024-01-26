import yaml
import logging
import os
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

    def file_cleaner(self, carpeta_origen: str, carpeta_destino: str):
        # Se establece como separador de ruta aquel que arroje segun el OS
        separador_ruta: str = os.sep

        # Verificar si la carpeta de backups existe, si no, crearla
        if not os.path.exists(carpeta_destino):
            os.makedirs(carpeta_destino)
            logging.info(f'--> La carpeta {carpeta_destino} ha sido creada')

        # Obtener la lista de archivos en la carpeta de origen
        archivos_a_mover = os.listdir(carpeta_origen)
        archivos_movidos = 0

        # Mover cada archivo a la carpeta de backups
        try:
            for archivo in archivos_a_mover:

                ruta_origen = f'{carpeta_origen}{separador_ruta}{archivo}'
                ruta_destino = f'{carpeta_destino}{separador_ruta}{archivo}'

                # Renombrar el archivo moviéndolo
                os.rename(ruta_origen, ruta_destino)
                archivos_movidos += 1

            logging.info(
                f'--> Se movieron {archivos_movidos} archivos a la carpeta backups.')

        except Exception as e:
            logging.error(
                f'--> No se pudo mover los archivos generados a backups por el sigueinte error: {e}')
