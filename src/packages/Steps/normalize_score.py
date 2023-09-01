import pandas as pd
from packages.Logs.logs import *
import geopandas as gpd

def normalize_score(gdf_score: gpd.GeoDataFrame):
    try:
        # Crea una copia del GeoDataFrame para no modificar el original
        gdf_normalized = gdf_score.copy()

        # Guarda las columnas 'id', 'depa' y 'geometry' para luego agregarlas nuevamente
        columns_to_ignore = ['id', 'depa', 'geometry']

        # Obtén la lista de columnas a normalizar (todas excepto las de ignorar)
        columns_to_normalize = [col for col in gdf_normalized.columns if col not in columns_to_ignore]

        # Normaliza las columnas especificadas utilizando el método Min-Max
        for column in columns_to_normalize:
            gdf_normalized[column] = (gdf_normalized[column] - gdf_normalized[column].min()) / (gdf_normalized[column].max() - gdf_normalized[column].min())

            # Cambia la última letra de "S" a "N" en el nombre de la columna
            new_column_name = column[:-1] + 'N'
            gdf_normalized = gdf_normalized.rename(columns={column: new_column_name})

        return gdf_normalized   
    except Exception as ex:
        print(f"Error al ejecutar algoritmo 'normalize_score':  " + str(ex))
        logging.error(f"Error al ejecutar algoritmo 'normalize_score':  " + str(ex))