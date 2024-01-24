# Tareas pendientes

- Realizar la función que ejecute el ciclo que simulación cada 20 min
- Realizar la función o script que limite eel rango de generacion de archivos de 1 a 100, como parametro por defecto, y dejar la opcion para que se convierta en un parametro opcional. 
- Realizar las modificaciones a las funcione o los scrips con la intencion de intrgar esta condicion:
    ```python
    'En caso de que la misión no esté previamente definida en el registro (UNKN), se deberá almacenar y asignar un identificador único a cada ejecución. En este caso, los campos proporcionados con información serán la fecha y la misión, mientras que el resto deberá marcarse como "unknown"'
    ```
- Modificar las funciones y los scripts para que  las misiones, los devices y los estados que estan predefinidas se conporten como parametros por defecto, pero que admita a su vez la posibilidad de ingresar parametros opciones en cada uno de esos items. 
- Realizar la funcion o el script que permita realizar un análisis de la cantidad de eventos por estado para cada misión y dispositivo. Para ello se cuenta con el archivo json que alimenta la funcion mission_statistics_generator cad avez que se ejecuta.
Realizar la funcion o el script que permita realizar Gestión de desconexiones. Esto implica identificar los dispositivos que presentan un mayor número 
de desconexiones, específicamente en el estado "unknown", para cada 
misión.
- Realizar la funcion o el script que permita realizar la consolidacion de las misiones. Esto implica realizar la consolidación de todas las misiones para determinar cuántos dispositivos son inoperables.
- Realizar la funcion o el script que permita realizar el calculo de porcentajes. Esto implica calcular los porcentajes de datos generados para cada
dispositivo y misión con respecto a la cantidad total de datos.
- Realizar las funcion o el script que permita realizar la gestion del tablero de control, lo cual implica desarrollar  un  archivo  que  simule  un tablero  de  control. Este archivo debe proporcionar una representación visual que permita a los líderes de otras misiones acceder a datos pertinentes y relevantes del proceso. 
