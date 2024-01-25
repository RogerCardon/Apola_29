from devices_status.random_devices_status import RandomDevice


randonDivice = RandomDevice('config.yml')

dict = randonDivice.random_device_status()

print(dict)
