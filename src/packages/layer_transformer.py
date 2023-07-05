from DB_set.database import *
from JSON_process.json_translator import get_columns_dictionary
import pdb


#Path to JSON file
json_file_path = "C:\\Users\\maurogomez\\Desktop\\Mauro_DINOT\\Develop\\GeoNormalize\\src\\packages\\JSON_process\\renamed_columns.json"


def modify_columns(layer: gpd.GeoDataFrame, columns:list):
    try:
        if len(columns) > 0:
            for col in columns:
                old_col_name = col['original_column']
                new_col_name = col['renamed_column']
                #if old_col_name.lower() in layer.columns or old_col_name.upper() in layer.columns:
                for layer_column in layer.columns:
                    if old_col_name.lower() == layer_column.lower():
                        # Realizar la acción correspondiente si hay una coincidencia
                        layer = layer.rename(columns = {old_col_name : new_col_name})
                        print(f"Se cambió el nombre de la columna '{old_col_name}' a '{new_col_name}'")
                    else:
                        print(f"No se encontró la columna '{old_col_name}' en la capa R")
            
            return layer
        else:
            print("La lista de columnas está vacía")

    except Exception as ex:
        print(f"Error al cambiar nombres de columnas en función 'modify_columns':  " + str(ex))
        logging.error(f"Error al cambiar nombres de columnas en función 'modify_columns':  " + str(ex))


def change_columns(layer_name:str, schema:str, json_file:str, engine):
    try:
        layer_to_modify = bring_layer(layer_name, schema, engine)
        new_columns_dictionary = get_columns_dictionary(json_file)        
        layer_renamed = modify_columns(layer_to_modify, new_columns_dictionary)
        insert_layer_into_postgis(layer_renamed, "AAII_GP_Processed_new_Renamed", engine)
        delete_created_index("AAII_GP_Processed_new_Renamed")
    except Exception as ex:
        print(f"Error al cambiar nombres de columnas en capa resultante {layer_name}:  " + str(ex))
        logging.error(f"Error al cambiar nombres de columnas en capa resultante  {layer_name}:  " + str(ex))


change_columns("AAII_GP_Processed_new", "gp_resulted", json_file_path, engine)