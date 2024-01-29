from file_handling.file_generator import file_generator
from hash_funtion.hash_gen import hash_generator
from devices_status.random_devices_status import RandomDevice
from statistics.report import report_statistics_generator
import pytest

@pytest.fixture
def tmp_dir(tmpdir):
    # Create temporary directory
    temp_dir = tmpdir.mkdir("test_dir")
    yield str(temp_dir)

@pytest.fixture(scope='session')
def app_instance():
    # Atributos dinamicos
    class App:
        pass
    
    app = App()
    
    app.file_generator = file_generator
    app.hash_generator = hash_generator
    app.report_statistics_generator = report_statistics_generator
    app.random_device_instance = RandomDevice()
    
    return app