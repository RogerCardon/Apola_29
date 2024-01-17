import os


def file_cleaner(carpeta_origen: str, carpeta_destino: str):

    # Verificar si la carpeta de backups existe, si no, crearla
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)

    # Obtener la lista de archivos en la carpeta de origen
    archivos_a_mover = os.listdir(carpeta_origen)

    # Mover cada archivo a la carpeta de backups
    for archivo in archivos_a_mover:
        ruta_origen = os.path.join(carpeta_origen, archivo)
        ruta_destino = os.path.join(carpeta_destino, archivo)
        
        # Renombrar el archivo moviéndolo
        os.rename(ruta_origen, ruta_destino)
