# hash: name+date+deviceType of 16
import hashlib
import os
import logging
from typing import Optional

# Set the logging level
logging.basicConfig(level=logging.DEBUG)


def hash_generator(date, mission, device_type, device_status):
    try:
        # Generate salt
        salt = os.urandom(16)

        # Concatenate data with salt
        concatenated_data: Optional[str] = \
            f"{date}-{mission}-{device_type}\
            -{device_status}-{salt}".encode('utf-8')

        # Apply hash
        hashed_result: Optional[str] = \
            hashlib.sha256(concatenated_data).hexdigest()

        return hashed_result, salt
    except Exception as e:
        logging.error(f'Error occurred during hash generation: "{e}"')
