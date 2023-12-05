import random
from datetime import datetime


#Possible states of devices.
status: list = ['excellent', 'good', 'warning', 'faulty', 'killed', 'unknown']
devices: list = ['satelite', 'spacecraft', 'space vehicle', 'Trajes','other components']
missions: list = ['OrbitOne', 'ColonyMoon', 'VacMars', 'GalaxyTwo', 'Unknow']



def mission_and_device_selector(missions: list):

    range_selecting = random.randint(1, 5)
    selected_mission: list = random.sample(missions, range_selecting)
    print(selected_mission)
    
    def random_device_status(selected_mission):
        list_data_divises: list = ['satelite', 'spacecraft', 'space vehicle', 'Trajes','other components']
        data_divises: dict = {}
        status: list = ['excellent', 'good', 'warning', 'faulty', 'killed', 'unknown']
        selected_status: str = random.choice(status)
        date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        lista = []
        
        for mission in selected_mission:
            for device in list_data_divises:
                data_divises[mission] = {
                'date_time': date_time,
                'type_divese': device,
                'status_devise': selected_status
                }

                lista.append(data_divises)
                data_divises: dict = {}
        return lista
    return random_device_status(selected_mission)

        
            

    


datos = mission_and_device_selector(missions)

print(datos)
    
    
