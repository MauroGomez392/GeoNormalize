import pandas as pd
from packages.Logs.logs import *
import geopandas as gpd

def normalize_score(gdf_score: gpd.GeoDataFrame):
    try:
        new_gdf = gdf_score[['id', 'depa', 'geometry']].copy()  # Crear un nuevo GeoDataFrame con 'id' y 'geometry'

        # Filtrar las columnas a normalizar
        columns_to_normalize = [column for column in gdf_score.columns if column != 'geometry' and column != 'id' and column != 'depa']

        # Iterar sobre las columnas y realizar la normalización por min-max
        for column in columns_to_normalize:
            if '-' in column:
                new_column = column[:-1] + 'N'  # Reemplazar la última letra por 'N'
                new_gdf[new_column] = gdf_score[column].apply(lambda x: x if pd.isnull(x) else (round((x - gdf_score[column].min()) / (gdf_score[column].max() - gdf_score[column].min()), 6)))
            else:
                min_value = gdf_score[column].min()
                max_value = gdf_score[column].max()
                new_column = column[:-1] + 'N'  # Reemplazar la última letra por 'N'
                new_gdf[new_column] = round((gdf_score[column] - min_value) / (max_value - min_value), 6)

        return new_gdf
    except Exception as ex:
        print(f"Error al ejecutar algoritmo 'normalize_score':  " + str(ex))
        logging.error(f"Error al ejecutar algoritmo 'normalize_score':  " + str(ex))