import os


def file_cleaner(origin_directory: str, destination_directory: str):

    # Verificar si la carpeta de backups existe, si no, crearla
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    # Obtener la lista de archivos en la carpeta de origen
    files_to_move = os.listdir(origin_directory)

    # Mover cada archivo a la carpeta de backups
    for file in files_to_move:
        origin_path = os.path.join(origin_directory, file)
        destination_path = os.path.join(destination_directory, file)
        
        # Renombrar el archivo moviéndolo
        os.rename(origin_path, destination_path)
