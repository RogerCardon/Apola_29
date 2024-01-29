from devices_status.random_devices_status import RandomDevice


random_device = RandomDevice()

def test_random_device_status(random_device):
    devices_status = random_device.random_device_status()

    # Check if the returned value is a dictionary
    assert isinstance(devices_status, dict)

    # Check if each mission has its status
    for mission, mission_data in devices_status.items():
        assert 'fecha' in mission_data
        assert isinstance(mission_data['fecha'], str)
        assert len(mission_data) > 1

def test_call_method(random_device_instance):
    devices_status_call = random_device_instance()

    # Check if the returned value is a dictionary
    assert isinstance(devices_status_call, dict)
