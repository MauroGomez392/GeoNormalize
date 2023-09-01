import pandas as pd
import geopandas as gpd
import numpy as np
from packages.DB_set.database import *
import pdb


def calculate_score(gdf: gpd.GeoDataFrame, dictionary):
    try:
        new_columns = []  # Lista para almacenar los nombres de las nuevas columnas
        sum_columns = {}  # Diccionario para almacenar las columnas de suma
        desired_categories = set()  # Conjunto para almacenar las categorías deseadas

        # Recorrer cada columna en el dataframe 'gdf'
        for column in gdf.columns:
            if column == 'PARAOMNIV':
                # Obtener los rangos, subpuntuaciones y puntuación para PARAOMNIV una sola vez
                paraomniv_ranges = dictionary['PARAOMNIV']['ranges']
                paraomniv_subscores = dictionary['PARAOMNIV']['subscores']
                values = gdf[column].values
                paraomnis_values = []

                for i in range(len(values)):
                    if pd.isnull(values[i]):
                        # Si el valor en 'PARAOMNIV' es nulo, el resultado en 'PARAOMNIS' también debe ser nulo
                        paraomnis_values.append(np.nan)
                    else:
                        # Obtener el valor actual de 'PARAOMNIV'
                        paraomniv_value = values[i]

                        # Encontrar el rango al que pertenece el valor
                        for j in range(len(paraomniv_ranges)):
                            if paraomniv_ranges[j][0] <= paraomniv_value < paraomniv_ranges[j][1]:
                                # Usar el 'score' correspondiente al rango
                                score = paraomniv_subscores[j]
                                paraomnis_values.append(score)
                                break

                # Agregar la columna 'PARAOMNIS' al dataframe 'gdf'
                gdf['PARAOMNIS'] = paraomnis_values
                new_columns.append('PARAOMNIS')
                desired_categories.add('PARAOMNIS')
                
            elif column == 'DENSPOBLV':
                # Verificar si la columna es 'DENSPOBLV'
                is_montevideo = gdf['depa'] == 'Montevideo'
                if np.any(is_montevideo):
                    # Caso especial para 'DENSPOBLV' cuando 'depa' es igual a 'Montevideo'
                    ranges = dictionary['DENSPOBLV']['Montevideo']['ranges']
                    subscores = dictionary['DENSPOBLV']['Montevideo']['subscores']
                    score = dictionary['DENSPOBLV']['Montevideo']['score'][0]
                else:
                    # Caso para 'DENSPOBLV' cuando 'depa' es diferente a 'Montevideo'
                    ranges = dictionary['DENSPOBLV']['ranges']
                    subscores = dictionary['DENSPOBLV']['subscores']
                    score = dictionary['DENSPOBLV']['score'][0]

                # Crear el nombre de la columna de suma
                sum_column = 'DENSPOBLS'
                new_columns.append(sum_column)
                desired_categories.add(column)

                # Obtener los valores de la columna 'DENSPOBLV'
                values = gdf[column].values
                subscore_totals = []
                # Calcular la suma de las subpuntuaciones para cada valor en la columna
                for i in range(len(values)):
                    subscore_total = 0.0
                    for j in range(len(ranges)):
                        # Verificar si el valor está dentro del rango actual
                        if ranges[j][0] <= values[i] < ranges[j][1]:
                            # Calcular la subpuntuación total para el valor actual
                            subscore_total += subscores[j] * score
                    subscore_totals.append(subscore_total)
                # Agregar la columna de suma al dataframe 'gdf'
#TODO: GENERAR FUNCIÓN PARA ITERACIÓN DE RANGOS
                gdf[sum_column] = subscore_totals

            else:
                # Verificar si la columna no es 'id' ni 'geometry' ni 'depa'
                if column != 'id' and column != 'geometry' and column != 'depa':
                    # Verificar si la columna con sufijo '-S' no existe en 'gdf'
                    if column + '-S' not in gdf.columns:
                        # Verificar si la columna tiene un guion '-' en su nombre
                        if '-' in column:
                            # Dividir el nombre de la columna en categoría y subcategoría
                            category, subcategory = column.split('-')

                            # Verificar si la categoría y subcategoría están en el diccionario
                            if category in dictionary and subcategory in dictionary[category]:
                                # Obtener los rangos, subpuntuaciones y puntuación de la categoría y subcategoría
                                ranges = dictionary[category][subcategory]['ranges']
                                subscores = dictionary[category][subcategory]['subscores']
                                score = dictionary[category][subcategory]['score'][0]

                                # Crear el prefijo de la columna de suma
                                sum_column_prefix = category + '-S'
                                desired_categories.add(category)

                                # Verificar si el prefijo de la columna de suma no está en 'sum_columns'
                                if sum_column_prefix not in sum_columns:
                                    sum_columns[sum_column_prefix] = []

                                # Crear el nombre de la columna de suma
                                sum_column = sum_column_prefix + '-' + subcategory
                                new_columns.append(sum_column)

                                # Obtener los valores de la columna actual
                                values = gdf[column].values
                                subscore_totals = []
                                # Calcular la suma de las subpuntuaciones para cada valor en la columna
                                for i in range(len(values)):
                                    subscore_total = 0.0
                                    for j in range(len(ranges)):
                                        # Verificar si el valor está dentro del rango actual
                                        if ranges[j][0] <= values[i] < ranges[j][1]:
                                            # Calcular la subpuntuación total para el valor actual
                                            subscore_total += subscores[j] * score
                                    subscore_totals.append(subscore_total)
#TODO
                                # Agregar la columna de suma al dataframe 'gdf'
                                gdf[sum_column] = subscore_totals
                                # Agregar la columna de suma al diccionario 'sum_columns'
                                sum_columns[sum_column_prefix].append(sum_column)

                        else:
                            # Obtener los rangos, subpuntuaciones y puntuación de la columna
                            ranges = dictionary[column]['ranges']
                            subscores = dictionary[column]['subscores']
                            score = dictionary[column]['score'][0]

                            # Crear el nombre de la columna de suma
                            sum_column = column[:-1] + 'S'
                            new_columns.append(sum_column)
                            desired_categories.add(column)

                            # Obtener los valores de la columna actual
                            values = gdf[column].values
                            subscore_totals = []
                            # Calcular la suma de las subpuntuaciones para cada valor en la columna
                            for i in range(len(values)):
                                subscore_total = 0.0
                                for j in range(len(ranges)):
                                    # Verificar si el valor está dentro del rango actual
                                    if ranges[j][0] <= values[i] < ranges[j][1]:
                                        # Calcular la subpuntuación total para el valor actual
                                        subscore_total += subscores[j] * score
                                subscore_totals.append(subscore_total)

                            # Agregar la columna de suma al dataframe 'gdf'
                            gdf[sum_column] = subscore_totals

        # Calcular la suma de las columnas de suma y agregarlas al dataframe 'gdf'
        for prefix, columns in sum_columns.items():
            sum_values = gdf[columns].sum(axis=1)
            sum_column = prefix[:-1] + 'S'

            gdf[sum_column] = sum_values
            new_columns.append(sum_column)

        # Crear la lista de columnas resultantes
        result_columns = ['id', 'depa'] + new_columns + ['geometry']
        result_gdf = gdf[result_columns]

        # Filtrar las columnas según las categorías deseadas
        desired_columns = [column for column in result_gdf.columns if column.endswith('-S') or column.endswith('S')]

        result_gdf = result_gdf[['id', 'depa'] + desired_columns + ['geometry']]

        return result_gdf   
    except Exception as ex:
        print(f"Error al ejecutar algoritmo 'calculate_score':  " + str(ex))
        logging.error(f"Error al ejecutar algoritmo 'calculate_score':  " + str(ex))


