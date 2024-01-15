### Estructura de los datos los estadististicos de las misiones

```python
datos = {
    'OrbitOne':{
        'satelite': {
            'excellent': 0,
            'good': 0,
            'warning': 0,
            'faulty': 0,
            'killed': 0,
            'unknown': 0,
        },
        'spacecraft': {
            'excellent': 0,
            'good': 0,
            'warning': 0,
            'faulty': 0,
            'killed': 0,
            'unknown': 0,
        },
        'space_vehicle': {
            'excellent': 0,
            'good': 0,
            'warning': 0,
            'faulty': 0,
            'killed': 0,
            'unknown': 0,            
        },
        'spacesuit': {
            'excellent': 0,
            'good': 0,
            'warning': 0,
            'faulty': 0,
            'killed': 0,
            'unknown': 0,            
        },
        'other_componentsdata_mission_devices':{
            'excellent': 0,
            'good': 0,
            'warning': 0,
            'faulty': 0,
            'killed': 0,
            'unknown': 0,            
        }
    },

    'ColonyMoon': {
        'satelite': {
            'excellent': 0,
            'good': 0,
            'warning': 0,
            'faulty': 0,
            'killed': 0,
            'unknown': 0,
        },
        'spacecraft': {
            'excellent': 0,
            'good': 0,
            'warning': 0,
            'faulty': 0,
            'killed': 0,
            'unknown': 0,
        },
        'space_vehicle': {
            'excellent': 0,
            'good': 0,
            'warning': 0,
            'faulty': 0,
            'killed': 0,
            'unknown': 0,            
        },
        'spacesuit': {
            'excellent': 0,
            'good': 0,
            'warning': 0,
            'faulty': 0,
            'killed': 0,
            'unknown': 0,            
        },
        'other_componentsdata_mission_devices':{
            'excellent': 0,
            'good': 0,
            'warning': 0,
            'faulty': 0,
            'killed': 0,
            'unknown': 0,            
        }
    },
    'VacMars': {
        'satelite': {
            'excellent': 0,
            'good': 0,
            'warning': 0,
            'faulty': 0,
            'killed': 0,
            'unknown': 0,
        },
        'spacecraft': {
            'excellent': 0,
            'good': 0,
            'warning': 0,
            'faulty': 0,
            'killed': 0,
            'unknown': 0,
        },
        'space_vehicle': {
            'excellent': 0,
            'good': 0,
            'warning': 0,
            'faulty': 0,
            'killed': 0,
            'unknown': 0,            
        },
        'spacesuit': {
            'excellent': 0,
            'good': 0,
            'warning': 0,
            'faulty': 0,
            'killed': 0,
            'unknown': 0,            
        },
        'other_componentsdata_mission_devices':{
            'excellent': 0,
            'good': 0,
            'warning': 0,
            'faulty': 0,
            'killed': 0,
            'unknown': 0,            
        }
    },
    'GalaxyTwo': {
        'satelite': {
            'excellent': 0,
            'good': 0,
            'warning': 0,
            'faulty': 0,
            'killed': 0,
            'unknown': 0,
        },
        'spacecraft': {
            'excellent': 0,
            'good': 0,
            'warning': 0,
            'faulty': 0,
            'killed': 0,
            'unknown': 0,
        },
        'space_vehicle': {
            'excellent': 0,
            'good': 0,
            'warning': 0,
            'faulty': 0,
            'killed': 0,
            'unknown': 0,            
        },
        'spacesuit': {
            'excellent': 0,
            'good': 0,
            'warning': 0,
            'faulty': 0,
            'killed': 0,
            'unknown': 0,            
        },
        'other_componentsdata_mission_devices':{
            'excellent': 0,
            'good': 0,
            'warning': 0,
            'faulty': 0,
            'killed': 0,
            'unknown': 0,            
        }
    },
    'Unknow': {
        'satelite': {
            'excellent': 0,
            'good': 0,
            'warning': 0,
            'faulty': 0,
            'killed': 0,
            'unknown': 0,
        },
        'spacecraft': {
            'excellent': 0,
            'good': 0,
            'warning': 0,
            'faulty': 0,
            'killed': 0,
            'unknown': 0,
        },
        'space_vehicle': {
            'excellent': 0,
            'good': 0,
            'warning': 0,
            'faulty': 0,
            'killed': 0,
            'unknown': 0,            
        },
        'spacesuit': {
            'excellent': 0,
            'good': 0,
            'warning': 0,
            'faulty': 0,
            'killed': 0,
            'unknown': 0,            
        },
        'other_componentsdata_mission_devices':{
            'excellent': 0,
            'good': 0,
            'warning': 0,
            'faulty': 0,
            'killed': 0,
            'unknown': 0,            
        }
    }
}
```

### Algoritmo para llenar los valores

La idea es que que este algoritmo lo que haga sea agregar los elmentos, primero identificando la mision y que luego identifique el estado 

```python
datos = {
    'OrbitOne': {
        'excellent': 0,
        'good': 0,
        'warning': 0,
        'faulty': 0,
        'killed': 0,
        'unknown': 0,
    },
    'ColonyMoon': {
        'excellent': 0,
        'good': 0,
        'warning': 0,
        'faulty': 0,
        'killed': 0,
        'unknown': 0,
    },
    'VacMars': {
        'excellent': 0,
        'good': 0,
        'warning': 0,
        'faulty': 0,
        'killed': 0,
        'unknown': 0,
    },
    'GalaxyTwo': {
        'excellent': 0,
        'good': 0,
        'warning': 0,
        'faulty': 0,
        'killed': 0,
        'unknown': 0,
    },
    'Unknow': {
        'excellent': 0,
        'good': 0,
        'warning': 0,
        'faulty': 0,
        'killed': 0,
        'unknown': 0,
    }
}
```