from packages.DB_set.database import *
from packages.JSON_process.json_translator import get_columns_dictionary
from packages.DB_set.db_psql import Psql
from shapely.geometry import MultiPolygon, Polygon
from shapely.validation import explain_validity


#Class with credentials for DB connect
db_psql = Psql()
#Path to JSON file
json_file_path = f"{db_psql.project_location_path}/src/packages/JSON_process/renamed_columns.json"


def modify_columns(layer: gpd.GeoDataFrame, columns:list):
    try:
        if len(columns) > 0:
            for col in columns:
                old_col_name = col['original_column']
                new_col_name = col['renamed_column']
                if old_col_name != new_col_name:
                    col_name_changed = False
                    if old_col_name in layer.columns:
                        layer.rename(columns={old_col_name : new_col_name}, inplace= True)
                        col_name_changed = True
                    if col_name_changed:
                        print(f"Nombre de la columna '{old_col_name}' renombrado a '{new_col_name}'")
                    else:
                        print(f"No se encontró la columna '{old_col_name}' en la capa Resulted")
            return layer
        else:
            print("La lista de columnas está vacía")

    except Exception as ex:
        print(f"Error al cambiar nombres de columnas en función 'modify_columns':  " + str(ex))
        logging.error(f"Error al cambiar nombres de columnas en función 'modify_columns':  " + str(ex))


def change_columns(layer_name:str, schema:str, json_file:str):
    try:
        layer_to_modify = bring_layer(layer_name, schema)
        new_columns_dictionary = get_columns_dictionary(json_file)        
        layer_renamed = modify_columns(layer_to_modify, new_columns_dictionary)
        insert_layer_into_postgis(layer_renamed, "AAII_GP_Processed_new_Renamed")
        delete_created_index("AAII_GP_Processed_new_Renamed")
        return True
    except Exception as ex:
        print(f"Error al cambiar nombres de columnas en capa resultante {layer_name}:  " + str(ex))
        logging.error(f"Error al cambiar nombres de columnas en capa resultante  {layer_name}:  " + str(ex))
        return False
    