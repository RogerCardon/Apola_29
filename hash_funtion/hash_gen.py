# hash: nombre+fecha+tipoDispo de 16
import hashlib
import os


def hash_generator(fecha, mision, tipo_dispositivo, estado_dispositivo):
    # Generar salt
    salt = os.urandom(16)

    # Concatenar los datos con el salt
    datos_concatenados = f"{fecha}-{mision}-{tipo_dispositivo}\
        -{estado_dispositivo}-{salt}".encode('utf-8')

    # Aplicar el hash
    hash_resultante = hashlib.sha256(datos_concatenados).hexdigest()

    return hash_resultante, salt
