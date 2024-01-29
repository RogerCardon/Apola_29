# **APOLO 11**



<img src="https://www.nasa.gov/wp-content/uploads/2015/04/s69-34875_0.jpg" alt="reporte" border="0" width="350"/>





Este proyecto fundamenta el trabajo final del Bootcamp Coding Up My Future, de SoftServe.

## Tabla de contenido

- [Contexto](#Contexto)
- [Ejecución del proyecto](#id2)
- [Paquetes](#Paquetes)

## Contexto

La Administración Nacional de la Aeronáutica y el Espacio, conocida comúnmente como 
NASA (National Aeronautics and Space Administration) por sus siglas en inglés), es una
agencia del gobierno de los Estados Unidos encargada de supervisar el programa 
espacial civil, además de llevar a cabo investigaciones en los campos de la aeronáutica y 
la astronáutica.

En su etapa más reciente, la NASA busca recobrar su capacidad de inspirar a nivel 
mundial y recuperar el protagonismo que ostentó durante las décadas de los años 70 y 90. Con este objetivo en mente, actualmente se encuentra en desarrollo de cuatro de 
los proyectos más ambiciosos en toda su historia, los cuales son:


1. **OrbitOne**: Modernizar toda la flota de satélites con el objetivo de potenciar su 
desempeño y mejorar la cobertura y las comunicaciones
2. **ColonyMoon**: Establecer una colonia en la Luna
3. **VacMars**: Llevar a personas en viajes turísticos a Marte
4. **GalaxyTwo**: Explorar la posibilidad de visitar otras galaxias

Estos proyectos harán uso de la más innovadora tecnología desarrollada por la 
humanidad y, al mismo tiempo, suscitarán una destacada expectación y atención a nivel 
internacional. En virtud de esta realidad, la NASA se encuentra plenamente consciente 
de la importancia de evitar cualquier margen de error, y considera que la gestión de 
anomalías constituye un elemento de vital relevancia para el éxito de las distintas misiones.

Con el propósito de enfrentar este desafío, la NASA se encuentra en proceso de 
implementar un sistema de monitoreo unificado basado en la transmisión de archivos, el cual operará a intervalos de 20 segundos. Este sistema permitirá mantener un control 
minucioso sobre el estado operativo de cada uno de los satélites, naves espaciales, 
vehículos espaciales y otros componentes clave. Esta aproximación implementará un 
control más efectivo y, en caso de cualquier eventualidad, habilitará acciones
preventivas tanto en el espacio como en la Tierra, lo que ayudará a la seguridad y 
supervivencia de los astronautas y turistas involucrados en estas trascendentales 
misiones.




<div id='id2' />
## Ejecución del proyecto
Este sistema se encuentra alojado dentro de un repositorio de github: [Apola 29](https://github.com/RogerCardon/Apola_29.git)

Para proceder con la ejecución del mismo, es necesario acceder a él y descargarlo. Una vez descargado se ejecutarán los siguientes comandos en terminal para asegurar su correcto funcionamiento:

### Entorno virtual
1. Se debe crear inicialmente el entorno virtual dentro del cual se ejecutará el proyecto, para esto usaremos el siguiente comando:
```
python3 -m vevn vevn
```

2. Posteriormente debe activarse, de la siguiente manera:
```
source venv/bin/activate
```

### Manejo de paquetes y dependencias
Con el fin de tener instaladas las dependecias y librerias necesarias vamos a ejecutar el siguiente comando:
```
pip install -r 'requirement.txt'
```

### Inicio de ejecución
Una vez se hayan completados los pasos anteriores, podremos ejecutar nuestro sistema de monitoreo usando python y apuntando la ejecución hacia el archivo principal `Apolo-11.py`.

Para esta ejecución, el Entry Point requiere 2 argumentos posicionales:

- **ET:**Un valor entero para establecer el intervalo de tiempo de ejecución, en segundos, para la simulación de reportes.

- **FL:** Un valor entero para establecer el máximo permitido para los archivos .log de la simulación de reportes.

## Paquetes

### devices_status
En este paquete encontramos un módulo llamado *random_devices_status* en el que se cargan de manera aleatoria los estados de los dispositivos, creando diccionarios a partir de las misiones seleccionadas.

Los estados posibles para cada dispositivo son: **excellent** (excelente), **good**
(bueno), **warning** (advertencia), **faulty** (defectuoso), **killed** (inoperable) y
**unknown** (desconocido)

### file_handling

En este paquete encontramos un módulo llamado *file_generator*, el cual genera logs en formato YAML.

Para esto usa una función que requiere 2 argumentos: 
1. **Path**: Que es la ruta donde se guardarán los archivos
2. **data_mission_devices**: Que es un diccionari0o con la infomación de los dispositivos de las misiones.

Luego de cada generación de logs se actualiza el número del consecutivo de registros que se han efectuado.

### hash_function

En este paquete encontramos un módulo llamado *hash_gen*, el cual a través de la función *hash_generator* transforma a hash la combinación de datos de se le ingresan como argumentos, estos son:
- **Fecha**
- **Misión**
- **Tipo de dispositivo**
- **Estado del dispositivo**

### statistics
En este paquete encontramos dos módulos, uno llamado *mission_statistics* y otro llamado *report*.

#### mission_statistics
En este módulo tenemos 2 funciones: *mission_statistics_generator* y *data_statistics_generator*, ambas diseñadas para generar informes de estadísticas basados en datos de dispositivos de misión.

#### report
En este módulo tenemos una función llamada *report_statistics_generator* que genera un informe en formato Markdown basado en los datos estadísticos proporcionados en un archivo YAML.

Estos reportes están estilizados en formato de tablas, a través de la librería **tabulate**.

### tests
En este paquete tendremos módulos en los que se hacen pruebas unitarias para algunos de los módulos de la librería, especialmente evaluando el retorno de las funciones, que estas tengan un output acorde a lo solicitado.

### tools

En este paquete encontramos cuatro módulos:
- data_class: A través de Pydantic, valida los tipos de datos de las misiones.
- date_provider: Genera la fecha y hora actuales, que se usan en tools.
- tools: Realiza la limpieza de los archivos
- write_tools: Actualiza el número del consecutivo los números de los reportes.