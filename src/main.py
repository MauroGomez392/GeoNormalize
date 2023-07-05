import pandas as pd
import geopandas as gpd
import numpy as np
from packages.DB_set.database import *
import pdb

variables = {
    'TPR': {
        'PRIVP': {
            'ranges': [(0, 50), (50, 80), (80, float('inf'))],
            'subscores': [0.25, 0.5, 1],
            'score': [0]
        },
        'SNDAP': {
            'ranges': [(0, 50), (50, 80), (80, float('inf'))],
            'subscores': [0.25, 0.5, 1],
            'score': [0]
        },
        'EPUBP': {
            'ranges': [(0, 50), (50, 80), (80, float('inf'))],
            'subscores': [0.25, 0.5, 1],
            'score': [0]
        },
        'OPUBP': {
            'ranges': [(0, 50), (50, 80), (80, float('inf'))],
            'subscores': [0.25, 0.5, 1],
            'score': [1]
        }
    },
    'CSU': {
        'RURAP': {
            'ranges': [(0, 25), (25, 50),  (50, 75), (75, float('inf'))],
            'subscores': [0.1, 0.25, 0.5, 1],
            'score': [0.8]
        },
        'RNATP': {
            'ranges': [(0, 25), (25, 50),  (50, 75), (75, float('inf'))],
            'subscores': [0.1, 0.25, 0.5, 1],
            'score': [1]
        },
        'SUBUP': {
            'ranges': [(0, 25), (25, 50),  (50, 75), (75, float('inf'))],
            'subscores': [1, 0.5, 0.25, 0.1],
            'score': [0.5]
        },
        'URBAP': {
            'ranges': [(0, 25), (25, 50),  (50, 75), (75, float('inf'))],
            'subscores': [1, 0.5, 0.25, 0.1],
            'score': [0.1]
        }
    },
    'INSTAPROSV': {
            'ranges': [(0, 1)],
            'subscores': [1, 0],
            'score': [1]
    },
    'UAS': {
        'PRIMV': {
            'ranges': [(0, 1000), (1000, 2500), (2500, float('inf'))],
            'subscores': [0.25, 0.5, 1],
            'score': [0.25]
        },
        'SEGUV': {
            'ranges': [(0, 1000), (1000, 2500), (2500, float('inf'))],
            'subscores': [0.25, 0.5, 1],
            'score': [0.50]
        },
        'TERCV': {
            'ranges': [(0, 1000), (1000, 2500), (2500, float('inf'))],
            'subscores': [0.25, 0.5, 1],
            'score': [1]
        }
    },
    'CENTAPOYV': {
            'ranges': [(0, 3000), (3000, 6000), (6000, 9000), (9000, float('inf'))],
            'subscores': [0.1, 0.25, 0.5, 1],
            'score': [1]
    },
    'CIN': {
        'CENTV': {
            'ranges': [(0, 800), (800, 1600), (1600, 4000), (4000, float('inf'))],
            'subscores': [0.1, 0.25, 0.5, 1],
            'score': [1]
        },
        'ESPAV': {
            'ranges': [(0, 8000), (8000, 16000), (16000, 32000), (32000, float('inf'))],
            'subscores': [0.1, 0.25, 0.5, 1],
            'score': [1]
        },
        'PROGV': {
            'ranges': [(0, 4000), (4000, 8000), (8000, 12000), (12000, float('inf'))],
            'subscores': [0.1, 0.25, 0.5, 1],
            'score': [1]
        },
        'SISTV': {
            'ranges': [(0, 8000), (8000, 16000), (16000, 32000), (32000, float('inf'))],
            'subscores': [0.1, 0.25, 0.5, 1],
            'score': [1]
        }
    },
    'POM': {
        'URBAV': {
            'ranges': [(0, 250), (250, 1500), (1500, float('inf'))],
            'subscores': [0.1, 0.5, 1],
            'score': [1]
        },
        'SUBUV': {
            'ranges': [(0, 250), (250, 1500), (1500, float('inf'))],
            'subscores': [0.1, 0.5, 1],
            'score': [0.75] 
        }
    },
    'BSA': {
        'BSAMV': {
            'ranges': [(0, 2500), (2500, 5000), (5000, float('inf'))],
            'subscores': [0.1, 0.5, 1],
            'score': [0.5]
        },
        'ACOMV': {
            'ranges': [(0, 2500), (2500, 5000), (5000, float('inf'))],
            'subscores': [0.1, 0.5, 1],
            'score': [0.8]
        },
        'AESPV': {
            'ranges': [(0, 4250), (4250, 9500), (9500, float('inf'))],
            'subscores': [0.1, 0.5, 1],
            'score': [1]
        }
    },
    'CED': {
        'FEDUV': {
            'ranges': [(0, 2000), (2000, 4000), (4000, 8000), (8000, float('inf'))],
            'subscores': [0.1, 0.25, 0.5, 1],
            'score': [0.25]
        },
        'PRIMV': {
            'ranges': [(0, 2000), (2000, 4000), (4000, 8000), (8000, float('inf'))],
            'subscores': [0.1, 0.25, 0.5, 1],
            'score': [1]
        },
        'SECV': {
            'ranges': [(0, 2000), (2000, 4000), (4000, 8000), (8000, float('inf'))],
            'subscores': [0.1, 0.25, 0.5, 1],
            'score': [0.75]
        },
        'TECV': {
            'ranges': [(0, 2000), (2000, 4000), (4000, 8000), (8000, float('inf'))],
            'subscores': [0.1, 0.25, 0.5, 1],
            'score': [0.5]
        }
    },
    'AREAPOBLSV': {
            'ranges': [(0, 250), (250, 500), (500, float('inf'))],
            'subscores': [0.1, 0.5, 0.75, 1],
            'score': [1]
    },
    'ESPALIBRSV': {
            'ranges': [(0, 4000), (4000, 8000), (8000, float('inf'))],
            'subscores': [0.1, 0.5, 0.75, 1],
            'score': [1]
    },
    'COHEGEOGV': {
            'ranges': [(0, 0.2), (0.2, 0.5), (0.5, 0.7), (0.7, float('inf'))],
            'subscores': [1, 0.5, 0.25, 0.1],
            'score': [1]
    },
    'RVI': {
        'CALLP': {
            'ranges': [(0, 25), (25, 50), (50, 75), (75, float('inf'))],
            'subscores': [1, 0.5, 0.25, 0.1],
            'score': [0.1]
        },
        'CAMIP': {
            'ranges': [(0, 25), (25, 50), (50, 75), (75, float('inf'))],
            'subscores': [1, 0.5, 0.25, 0.1],
            'score': [0.5]
        },
        'VIRTP': {
            'ranges': [(0, 25), (25, 50), (50, 75), (75, float('inf'))],
            'subscores': [0.1, 0.25, 0.5, 1],
            'score': [1]
        },
        'PASAP': {
            'ranges': [(0, 25), (25, 50), (50, 75), (75, float('inf'))],
            'subscores': [0.1, 0.25, 0.5, 1],
            'score': [0.75]
        },
        'SN9000V': {
            'ranges': [(0, 0.5), (0.5, 1.5), (1.5, 2.5)],
            'subscores': [0, 0.25, 1],
            'score': [1]
        }
    },
    'CERCASENV': {
            'ranges': [(0, 50), (50, 150), (150, 500), (500, 1000), (1000, float('inf'))],
            'subscores': [0.1, 0.25, 0.5, 0.75, 1],
            'score': [1]
    },
    'AREAPROTSV': {
            'ranges':[(0, 1000), (1000, 5000), (5000, float('inf'))],
            'subscores': [1, 0.5, 0.1],
            'score': [1]
    },
    'AREAPOTESV': {
            'ranges': [(0, 1000), (1000, 5000), (5000, float('inf'))],
            'subscores': [1, 0.5, 0.1],
            'score': [1]
    },
    'LINECOSTV': {
            'ranges': [(0, 200), (200, float('inf'))],
            'subscores': [1, 0],
            'score': [1]
    },
    'FOCOINCESV': {
        'ranges': [(0, 1000), (1000, float('inf'))],
        'subscores': [1, 0],
        'score': [1]
    },
    'SDI': {
        'NOOPV': {
            'ranges': [(0, 1000), (1000, 2000), (2000, float('inf'))],
            'subscores': [1, 0.5, 0.1],
            'score': [0.5]
        },
        'OPERV': {
            'ranges': [(0, 1000), (1000, 2000), (2000, float('inf'))],
            'subscores': [1, 0.5, 0.1],
            'score': [1]
        }
    },
    'CVE': {
        'DOMV': {
            'ranges': [(0, 1000), (1000, 2000), (2000, float('inf'))],
            'subscores': [1, 0.5, 0.1],
            'score': [0.5]
        },
        'INDV': {
            'ranges': [(0, 1000), (1000, 2000), (2000, float('inf'))],
            'subscores': [1, 0.5, 0.1],
            'score': [1]
        },
        'NOAPV': {
            'ranges': [(0, 1000), (1000, 2000), (2000, float('inf'))],
            'subscores': [1, 0.5, 0.1],
            'score': [0.75]
        }
    },
    'LTE': {
        'TALTV': {
            'ranges': [(0, 300), (300, 500), (500, float('inf'))],
            'subscores': [1, 0.5, 0.1],
            'score': [1]
        },
        'TMEDV': {
            'ranges': [(0, 300), (300, 500), (500, float('inf'))],
            'subscores': [1, 0.5, 0.1],
            'score': [0.25]
        }
    },
    'DISTAGUAV': {
            'ranges': [(0, 20), (20, 500), (500, float('inf'))],
            'subscores': [0.1, 0.5, 1],
            'score': [1]
    },
    'SANEV': {
            'ranges': [(0, 20), (20, 500), (500, float('inf'))],
            'subscores': [0.1, 0.5, 1],
            'score': [1]
    },
    'DENSPOBLV':{
            'Montevideo':{
                'ranges': [(0, 50), (50, 100), (100, 200), (200, 300), (300, float('inf'))],
                'subscores': [3, 2, 1, 2, 3],
                'score': [1]
            },
            'ranges': [(0, 30), (30, 70), (70, 150), (150, 300), (300, float('inf'))],
            'subscores': [3, 2, 1, 2, 3],
            'score': [1]
    },
    'COOP': {
        'AGRV': {
            'ranges': [(0, 500), (500, 1000), (1000, float('inf'))],
            'subscores': [0.1, 0.5, 1],
            'score': [0.75]
        },
        'AHCV': {
            'ranges': [(0, 500), (500, 1000), (1000, float('inf'))],
            'subscores': [0.1, 0.5, 1],
            'score': [0.75]
        },
        'ARTV': {
            'ranges': [(0, 500), (500, 1000), (1000, float('inf'))],
            'subscores': [0.1, 0.5, 1],
            'score': [0.75]
        },
        'CONSV': {
            'ranges': [(0, 500), (500, 1000), (1000, float('inf'))],
            'subscores': [0.1, 0.5, 1],
            'score': [0.75]
        },
        'SOCV': {
            'ranges': [(0, 500), (500, 1000), (1000, float('inf'))],
            'subscores': [0.1, 0.5, 1],
            'score': [0.75]
        },
        'FRURV': {
            'ranges': [(0, 500), (500, 1000), (1000, float('inf'))],
            'subscores': [0.1, 0.5, 1],
            'score': [0.75]
        },
        'TRAV': {
            'ranges': [(0, 500), (500, 1000), (1000, float('inf'))],
            'subscores': [0.1, 0.5, 1],
            'score': [0.5]
        },
        'VIVV': {
            'ranges': [(0, 500), (500, 1000), (1000, float('inf'))],
            'subscores': [0.1, 0.5, 1],
            'score': [1]
        }
    },
    'IMV': {
        'JUNTV': {
            'ranges': [(0, 1)],
            'subscores': [1, 0],
            'score': [1]
        },
        'AVANV': {
            'ranges': [(0, 1)],
            'subscores': [1, 0],
            'score': [1]
        },
        'MEVV': {
            'ranges': [(0, 1)],
            'subscores': [1, 0],
            'score': [1]
        },
        'ANVV': {
            'ranges': [(0, 1)],
            'subscores': [1, 0],
            'score': [1]
        },
        'PMBV': {
            'ranges': [(0, 1)],
            'subscores': [1, 0],
            'score': [1]
        },
        'ETMV': {
            'ranges': [(0, 1)],
            'subscores': [1, 0],
            'score': [1]
        }
    },
    'PROYPMBV': {
            'ranges': [(0, 500), (500, 1000), (1000, 2000), (2000, float('inf'))],
            'subscores': [0.1, 0.5, 0.75, 1],
            'score': [1]
    },
    'MEC': {
        'CENTV': {
            'ranges': [(0, 2500), (2500, 5000), (5000, 10000), (10000, float('inf'))],
            'subscores': [0.1, 0.5, 0.75, 1],
            'score': [1]
        },
        'CECAPV': {
            'ranges': [(0, 4000), (4000, 8000), (8000, 12000), (12000, float('inf'))],
            'subscores': [0.1, 0.5, 0.75, 1],
            'score': [1]
        },
        'USCULV': {
            'ranges': [(0, 2500), (2500, 5000), (5000, 10000), (1000, float('inf'))],
            'subscores': [0.1, 0.5, 0.75, 1],
            'score': [1]
        },
        'PASV': {
            'ranges': [(0, 4000), (4000, 8000), (8000, 12000), (12000, float('inf'))],
            'subscores': [0.1, 0.5, 0.75, 1],
            'score': [1]
        },
        'BIBLIV': {
            'ranges': [(0, 1000), (1000, 2500), (2500, 5000), (5000, float('inf'))],
            'subscores': [0.1, 0.5, 0.75, 1],
            'score': [1]
        }
    },
    'CHA': {
        'AUTOV': {
            'ranges': [(0, 500), (500, 1000), (1000, float('inf'))],
            'subscores': [0.1, 0.5, 1],
            'score': [1]
        },
        'BHUV': {
            'ranges': [(0, 500), (500, 1000), (1000, float('inf'))],
            'subscores': [0.1, 0.5, 1],
            'score': [1]
        },
        'INTEV': {
            'ranges': [(0, 500), (500, 1000), (1000, float('inf'))],
            'subscores': [0.1, 0.5, 1],
            'score': [1]
        },
        'LPROV': {
            'ranges': [(0, 500), (500, 1000), (1000, float('inf'))],
            'subscores': [0.1, 0.5, 1],
            'score': [1]
        },
        'MVOTV': {
            'ranges': [(0, 500), (500, 1000), (1000, float('inf'))],
            'subscores': [0.1, 0.5, 1],
            'score': [1]
        },
        'MEVIV': {
            'ranges': [(0, 500), (500, 1000), (1000, float('inf'))],
            'subscores': [0.1, 0.5, 1],
            'score': [1]
        }
    }
}


def calculate_score(gdf, dictionary):
    new_columns = []  # Lista para almacenar los nombres de las nuevas columnas
    sum_columns = {}  # Diccionario para almacenar las columnas de suma
    desired_categories = set()  # Conjunto para almacenar las categorías deseadas

    # Recorrer cada columna en el dataframe 'gdf'
    for column in gdf.columns:
        if column == 'DENSPOBLV':
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
            gdf[sum_column] = subscore_totals

        else:
            # Verificar si la columna no es 'id' ni 'geometry' ni 'depa'
            if column.isupper():
                # Verificar si la columna con sufijo '-S' no existe en 'gdf'
                if column + '-S' not in gdf.columns:
                    # Verificar si la columna tiene un guion '-' en su nombre
                    if '-' in column:
                        #pdb.set_trace()
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

    # Reemplazar los valores de suma iguales a 0 por None o celdas vacías en las columnas que tienen guion
    for column in desired_columns:
        if "-" in column:
            result_gdf.loc[result_gdf[column] == 0, column] = None

    result_gdf = result_gdf[['id', 'depa'] + desired_columns + ['geometry']]

    return result_gdf


layer = bring_layer("AAII_GP_Processed_new_Renamed", "gp_resulted", engine)
new_l = calculate_score(layer, variables) 
print(new_l)
insert_layer_into_postgis(new_l, "prueba", engine)



