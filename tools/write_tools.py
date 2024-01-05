import yaml


def consecutive_number_update():
    # Cargar la configuración actual desde el archivo config.yml
    with open('config.yml', 'r') as file:
        configuration = yaml.safe_load(file)

    # Incrementar el número consecutivo
    configuration['consecutive_number'] += 1

    # Actualizar el archivo config.yml con el nuevo número consecutivo
    with open('config.yml', 'w') as file:
        yaml.dump(configuration, file)
