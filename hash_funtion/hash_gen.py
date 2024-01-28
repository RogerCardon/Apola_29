# hash: nombre+fecha+tipoDispo de 16
import hashlib
import os
import logging
from typing import Optional

# configurar el nivel
logging.basicConfig(level=logging.DEBUG)


def hash_generator(fecha, mision, tipo_dispositivo, estado_dispositivo):
    try:
        # Generar salt
        salt = os.urandom(16)

        # Concatenar los datos con el salt
        datos_concatenados: Optional[str] = \
            f"{fecha}-{mision}-{tipo_dispositivo}\
            -{estado_dispositivo}-{salt}".encode('utf-8')

        # Aplicar el hash
        hash_resultante: Optional[str] = \
            hashlib.sha256(datos_concatenados).hexdigest()

        return hash_resultante, salt
    except Exception as e:
        logging.error(f'En la generación del hash se \
            genero un error de tipi: "{e}"')
