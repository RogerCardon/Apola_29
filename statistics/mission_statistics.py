import os
import yaml
import logging
from tools.tools import Tools
from typing import Dict, Optional, Any, List

# configurar el nivel
logging.basicConfig(level=logging.DEBUG)


def mission_statistics_generator(
        carpeta_devices: Optional[str]) -> Optional[None]:
    try:
        tools: Tools = Tools('config.yml')
        separator: Optional[str] = tools.separador
        archivo_log: Optional[str] = \
            f'statistics_reports{separator}data_statistics.log'

        with open(archivo_log, 'r') as archivo:
            statistics_mission_devices: Dict[str,
                                             Any] = yaml.safe_load(archivo)

        for file_name in os.listdir(carpeta_devices):
            with open(f'{carpeta_devices}/{file_name}', 'r') as file:
                data_divice: Dict[str, Any] = yaml.safe_load(file)

            for mission, detalles_mission in data_divice.items():
                for devices, status in detalles_mission.items():
                    if devices != 'fecha' and devices != 'hash':
                        statistics_mission_devices[mission][devices][status] += 1

        # Crear el contenido en formato YAML
        yaml_content: str = yaml.dump(
            statistics_mission_devices, default_flow_style=False)

        # Guarda el diccionario modificado en el mismo archivo JSON
        with open(archivo_log, 'w') as archivo:
            archivo.write(str(yaml_content))
    except Exception as e:
        logging.error(
            f'En la generación de los estadisticos se ha generado un error de tipo: "{e}"')


def data_statistics_generator(date: Optional[str]) -> Optional[str]:
    tools: Tools = Tools('config.yml')
    separator: Optional[str] = tools.separador
    archivo_log: Optional[str] = \
        f'statistics_reports{separator}data_statistics.log'

    # Abrimos el archivo que contiene los datos
    with open(archivo_log, 'r') as file:
        data: Dict[str, Dict[str, Dict[str, int]]] = yaml.safe_load(file)

    # 1. Generar el reporte de análisis de eventos
    report_1: Dict[str, Dict[str, Dict[str, int]]] = {}
    for mission, devices in data.items():
        mission_data: Dict[str, Dict[str, int]] = {}
        headers: List[str] = ['Excellent', 'Good',
                              'Warning', 'Faulty', 'Killed', 'Unknown']

        for device, events in devices.items():
            # Almacenar los datos de eventos en un diccionario para
            # cada dispositivo
            device_data: Dict[str, int] = {status.lower(): events.get(
                status.lower(), 0) for status in headers}
            mission_data[device] = device_data

        # Almacenar los datos de eventos en un diccionario para cada misión
        report_1[mission] = mission_data

    # 2. Generar el reporte de Gestión de desconexiones
    disconnect_report: Dict[str, Dict[str, int]] = {}
    for mission, devices in data.items():
        mission_disconnections: Dict[str, int] = {}
        for device, events in devices.items():
            # Almacenar el número de desconexiones para cada dispositivo
            disconnections: int = events.get('unknown', 0)
            mission_disconnections[device] = disconnections

        # Almacenar el número de desconexiones para cada misión
        disconnect_report[mission] = mission_disconnections

    # 3. Generar el reporte de Consolidación de misiones
    consolidated_report: Dict[str, Dict[str, int]] = {}
    for mission, devices in data.items():
        mission_inoperable_count: Dict[str, int] = {}
        for device, events in devices.items():
            # Almacenar el recuento total de dispositivos inoperables (killed + unknown) para cada dispositivo
            inoperable_count: int = events.get(
                'killed', 0) + events.get('unknown', 0)
            mission_inoperable_count[device] = inoperable_count

        # Almacenar el recuento total de dispositivos inoperables
        # para cada misión
        consolidated_report[mission] = mission_inoperable_count

    # 4. Generar el reporte de Cálculo de porcentajes
    percentage_report: Dict[str, Dict[str, Dict[str, float]]] = {}
    total_events: int = sum(
        events.get(
            'excellent', 0
        ) + events.get(
            'good', 0
        ) + events.get(
            'warning', 0
        ) + events.get(
            'faulty', 0) + events.get(
            'killed', 0) + events.get('unknown', 0)
        for devices in data.values() for events in devices.values())

    for mission, devices in data.items():
        mission_percentage: Dict[str, Dict[str, float]] = {}
        for device, events in devices.items():
            # Calcular y almacenar el porcentaje de cada estado
            # para cada dispositivo
            device_percentage: Dict[str, float] = {
                state.lower(): (
                    events.get(state.lower(), 0) / total_events) * 100
                for state in ['excellent', 'good',
                              'warning', 'faulty', 'killed',
                              'unknown']
            }
            mission_percentage[device] = device_percentage

        # Almacenar los porcentajes para cada misión
        percentage_report[mission] = mission_percentage

    config_data: Dict[str, Any] = tools.configuration_file_load()
    report_statistics_number: int = config_data['report_statistics_number']
    file_name: str = f'APLSTATS-R{report_statistics_number}-{date}'

    # Escribir el archivo YAML
    with open(f'statistics_reports{separator}{file_name}.log', 'w') as file:
        # Almacenar cada informe con un comentario descriptivo
        yaml.dump({
            '1. Events Analysis': report_1,
            '2. Disconnection Management': disconnect_report,
            '3. Mission Consolidation': consolidated_report,
            '4. Percentage Calculation': percentage_report
        }, file)

    return file_name
