import yaml
import os
from typing import Optional
from tabulate import tabulate


def report_statistics_generator(report_file_name: Optional[str]):

    separator: Optional[str] = os.sep
    archivo_log: Optional[str] = f'statistics_reports{separator}data_statistics.log'

    # Abrimos el archvio que contiene los datos

    with open(archivo_log, 'r') as file:
        data = yaml.safe_load(file)

    # 1. Generar el reporte de analisis de eventos
    markdown_tables = []
    report_1 = f'## 1. Events Analysis \n\n'

    for mission, devices in data.items():
        mission_table = f"### {mission}\n\n"
        headers = ['Device', 'Excellent', 'Good',
                   'Warning', 'Faulty', 'Killed', 'Unknown']
        rows = []

        for device, events in devices.items():
            row_data = [device] + \
                [events.get(state.lower(), 0) for state in headers[1:]]
            rows.append(row_data)

        device_table = tabulate(rows, headers, tablefmt='pipe') + "\n\n"
        mission_table += device_table
        markdown_tables.append(mission_table)

    # 2. Generar el reporte de Gestión de desconexiones

    disconnect_table = "## 2. Disconnection Management\n\n"
    disconnect_headers = ['Device', 'Mission', 'Disconnections']
    disconnect_rows = []

    for mission, devices in data.items():
        for device, events in devices.items():
            disconnections = events.get('unknown', 0)
            disconnect_rows.append([device, mission, disconnections])

    # Sort the table by the number of disconnections in descending order
    disconnect_rows = sorted(
        disconnect_rows, key=lambda x: x[2], reverse=True)

    # Take the top 20 if there are more than 20 devices with disconnections
    top_20 = disconnect_rows[:20] if len(
        disconnect_rows) > 20 else disconnect_rows

    disconnect_table += tabulate(top_20,
                                 disconnect_headers, tablefmt='pipe') + "\n\n"

    # 3. Generar el reporte de Consolidación de misiones

    consolidated_table = "## 3. Mission Consolidation\n\n"
    consolidated_headers = [
        'Device', 'Total Inoperable (Killed + Unknown)']
    consolidated_rows = []

    for mission, devices in data.items():
        for device, events in devices.items():
            inoperable_count = events.get(
                'killed', 0) + events.get('unknown', 0)
            consolidated_rows.append(
                [f"{mission} - {device}", inoperable_count])

    consolidated_table += tabulate(consolidated_rows,
                                   consolidated_headers, tablefmt='pipe') + "\n\n"

    # 4. Generar el reporte de Calculo de porcentajes
    percentage_table = "## 4. Percentage Calculation\n\n"
    percentage_headers = ['Device', 'Mission'] + ['Percentage ' + state for state in [
        'Excellent', 'Good', 'Warning', 'Faulty', 'Killed', 'Unknown']]
    percentage_rows = []

    total_events = sum(events.get('excellent', 0) + events.get('good', 0) +
                       events.get('warning', 0) + events.get('faulty', 0) +
                       events.get('killed', 0) + events.get('unknown', 0)
                       for devices in data.values() for events in devices.values())

    # Listas para almacenar las sumas de cada columna
    column_sums = [0] * len(percentage_headers)

    for mission, devices in data.items():
        for device, events in devices.items():
            device_percentage = [(events.get(state, 0) / total_events) * 100 for state in [
                'excellent', 'good', 'warning', 'faulty', 'killed', 'unknown']]

            # Actualizar las sumas de cada columna
            column_sums = [sums + percentage for sums,
                           percentage in zip(column_sums, device_percentage)]

            percentage_rows.append(
                [device, mission] + [f"{percentage:.2f}%" for percentage in device_percentage])

    # Agregar la fila de sumas al final
    column_sums_row = ['**Total**', ''] + \
        [f"**{sum_percentage:.2f}%**" for sum_percentage in column_sums]
    percentage_rows.append(column_sums_row)

    percentage_table += tabulate(percentage_rows,
                                 percentage_headers, tablefmt='pipe') + "\n\n"

    # Escribir el archivo markdown
    with open(f'statistics_reports{separator}{report_file_name}.md', 'w') as file:
        file.write(report_1)

        for table in markdown_tables:
            file.write(table)

        file.write(disconnect_table)
        file.write(consolidated_table)
        file.write(percentage_table)
