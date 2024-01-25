from tools.tools import Tools
import json 


tools = Tools('config.yml')

path = tools.path_configuration_file
print(path)

datos_configuracion = 