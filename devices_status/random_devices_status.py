import random
from datetime import datetime
import json



def random_device_status(missions: list, devices: list, status: list):

    #status: list = ['excellent', 'good', 'warning', 'faulty', 'killed', 'unknown'] 
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
        



