import os


def file_cleaner(carpeta_origen: str, carpeta_destino: str):
    separador_ruta: str = os.sep

    # Verificar si la carpeta de backups existe, si no, crearla
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)

    # Obtener la lista de archivos en la carpeta de origen
    archivos_a_mover = os.listdir(carpeta_origen)

    # Mover cada archivo a la carpeta de backups
    for archivo in archivos_a_mover:
        ruta_origen = f'{carpeta_origen}{separador_ruta}{archivo}'
        ruta_destino = f'{carpeta_destino}{separador_ruta}{archivo}'
        
        # Renombrar el archivo moviéndolo
        os.rename(ruta_origen, ruta_destino)
