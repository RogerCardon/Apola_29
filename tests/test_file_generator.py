from conftest import tmp_dir

# Mock data for testing
data_mission_devices = {
    "mission1": {
        "fecha": "2024-01-29",
        "device1": "status1",
        "device2": "status2"
    }
}

def test_file_generator(app):
    result = app.file_generator(tmp_dir,data_mission_devices)
    assert result is not None