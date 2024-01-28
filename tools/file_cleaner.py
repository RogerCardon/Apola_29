import os
import logging
from typing import Optional, List


# configurar el nivel
logging.basicConfig(level=logging.DEBUG)


def file_cleaner(carpeta_origen: str, carpeta_destino: Optional[str]):
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
