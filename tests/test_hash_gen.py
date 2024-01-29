# Mock data
date = "2024-01-29"
mission = "mission1"
device_type = "device1"
device_status = "status1"

def test_hash_generator(app):
    hashed_result, salt = app.hash_generator(date, mission, device_type, device_status)

    # Verifica que exista hash y sea tipo string
    assert hashed_result is not None
    assert isinstance(hashed_result, str)

    assert salt is not None
    assert isinstance(salt, bytes)
