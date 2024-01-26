import yaml
import logging
from typing import Dict, Optional, Union, List
# configurar el nivel
logging.basicConfig(level=logging.DEBUG)


def consecutive_number_update()-> Optional[None]:
    try:

        # Cargar la configuración actual desde el archivo config.yml
        with open('config.yml', 'r') as file:
            configuration: Dict[str, Union[str, int]] = yaml.safe_load(file)

        # Incrementar el número consecutivos
        configuration['consecutive_number'] += 1

        # Actualizar el archivo config.yml con el nuevo número consecutivo
        with open('config.yml', 'w') as file:
            yaml.dump(configuration, file)

    except Exception as e:
        logging.error(
            f'Error de tipo: {e} al generar el numero consecutivo')
