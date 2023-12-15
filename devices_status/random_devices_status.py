import random
import json
from datetime import datetime



def random_device_statu(missions: list, devices: list):

    status: list = ['excellent', 'good', 'warning', 'faulty', 'killed', 'unknown'] 
    range_selecting = random.randint(1, 5)
    selected_mission: list = random.sample(missions, range_selecting)
    print(selected_mission)

    dices_status: dict = {}
    fecha = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    for mission in selected_mission:
        dices_status[mission] = {}
        for device in devices:
            dices_status[mission]['fecha'] = fecha
            dices_status[mission][device] = random.choice(status)
            
            
    return dices_status
        


#Possible states of devices.

devices: list = ['satelite', 'spacecraft', 'space vehicle', 'spacesuit','other components']
missions: list = ['OrbitOne', 'ColonyMoon', 'VacMars', 'GalaxyTwo', 'Unknow']
    

# Imprimir diccionario en formato JSON con indentación

dices_status = random_device_statu(missions, devices)
json_string = json.dumps(dices_status, indent=4)
print(json_string)

