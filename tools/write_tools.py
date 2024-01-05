from tools.load_tools import cargar_configuracion
import yaml


def consecutive_number_update():
    # Get the current configuration
    configuration = cargar_configuracion()

    # Incrementar el número consecutivo
    configuration['consecutive_number'] += 1

    # Actualizar el archivo config.yml con el nuevo número consecutivo
    with open('config.yml', 'w') as file:
        yaml.dump(configuration, file)