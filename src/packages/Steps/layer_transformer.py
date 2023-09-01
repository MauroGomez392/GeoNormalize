from packages.DB_set.database import *
from packages.JSON_process.json_translator import get_columns_dictionary
from shapely import wkb, wkt
import pdb
from shapely.geometry import MultiPolygon, Polygon
from shapely.validation import explain_validity



#Path to JSON file
json_file_path = "C:/Users/maurogomez/Desktop/Mauro_DINOT/Develop/GeoNormalize/GeoNormalize/src/packages/JSON_process/renamed_columns.json"


def modify_columns(layer: gpd.GeoDataFrame, columns:list):
    try:
        print(type(layer), "    pre MODIFICACIÓN de COLUMNAS")
        if len(columns) > 0:
            print(layer)
            for col in columns:
                old_col_name = col['original_column']
                new_col_name = col['renamed_column']
                if old_col_name != new_col_name:
                    #if old_col_name.lower() in layer.columns or old_col_name.upper() in layer.columns:
                    col_name_changed = False
                    if old_col_name in layer.columns:
                        layer.rename(columns={old_col_name : new_col_name}, inplace= True)
                        col_name_changed = True
                    """ for layer_column in layer.columns:
                        if old_col_name.lower() == layer_column.lower():
                            # Realizar la acción correspondiente si hay una coincidencia
                            layer_column = new_col_name                            
                            col_name_changed = True """
                    if col_name_changed:
                        print(f"Nombre de la columna '{old_col_name}' renombrado a '{new_col_name}'")
                    else:
                        print(f"No se encontró la columna '{old_col_name}' en la capa Resulted")
            print(type(layer), "    post MODIFICACIÓN de COLUMNAS")
            print(layer)
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
        #layer_renamed = convert_hex_to_wkt_geometries(layer_renamed)
        #print(type(layer_renamed), "    print post MODIFY y pre INSERTAR 1")
        #layer_renamed = fix_geometries_in_layer(layer_renamed)
        #print(type(layer_renamed), "    print post MODIFY y pre INSERTAR 2")
        insert_layer_into_postgis(layer_renamed, "AAII_GP_Processed_new_Renamed")
        delete_created_index("AAII_GP_Processed_new_Renamed")
    except Exception as ex:
        print(f"Error al cambiar nombres de columnas en capa resultante {layer_name}:  " + str(ex))
        logging.error(f"Error al cambiar nombres de columnas en capa resultante  {layer_name}:  " + str(ex))


def change_geometry_type(hexa_geom):
    try:
        # Decodificar el valor hexadecimal en una representación binaria
        binary_geometry = bytes.fromhex(hexa_geom)
        # Convertir la representación binaria a una geometría Shapely
        shapely_geometry = wkb.loads(binary_geometry)
        # Convertir la geometría Shapely a formato WKT
        wkt_geometry = wkt.dumps(shapely_geometry)

        return wkt_geometry
    except Exception as ex:
        print(f"Error al convertir geometría hexadecimal a WKT: {ex}")
        logging.error(f"Error al convertir geometría hexadecimal a WKT: {ex}")
        return None

def convert_hex_to_wkt_geometries(geoDataFrame):
    try:
        new_geoDataFrame = geoDataFrame.copy()
        
        # Aplicar la función hex_to_wkt a la columna de geometría
        new_geoDataFrame['geometry'] = new_geoDataFrame['geometry'].apply(change_geometry_type)
        #new_geoDataFrame = gpd.GeoDataFrame(new_geoDataFrame, geometry=new_geoDataFrame['geometry'])
        return new_geoDataFrame
    except Exception as ex:
        print(f"Error al convertir geometrías hexadecimales a WKT en GeoDataFrame: {ex}")
        logging.error(f"Error al convertir geometrías hexadecimales a WKT en GeoDataFrame: {ex}")
        return None

def fix_geometries_in_layer(layer:gpd.GeoDataFrame):
    if layer['geometry'].any():
        for i, geom in enumerate(layer["geometry"]):
            try:
                shap_geom = wkt.loads(geom)
                if not shap_geom.is_valid:
                    fixed_geom = shap_geom.buffer(0)
                    layer.at[i, 'geometry'] = wkt.dumps(fixed_geom)
            except Exception as ex:
                print(f"problema al corregir capa en index/valor  {i}:  {ex}")
                logging.error(f"problema al corregir capa en index/valor  {i}:  {ex}")       
        return layer
    elif layer['geom'].any():
        for i, geom in enumerate(layer["geom"]):
            try:
                shap_geom = wkt.loads(geom)
                if not shap_geom.is_valid:
                    fixed_geom = shap_geom.buffer(0)
                    layer.at[i, 'geom'] = wkt.dumps(fixed_geom)
            except Exception as ex:
                print(f"problema al corregir capa en index/valor  {i}:  {ex}")
                logging.error(f"problema al corregir capa en index/valor  {i}:  {ex}")                
        return layer
    else:
        print(f"No hay columna con nombre 'geom' o 'geometry' en capa  {layer}:  {ex}")
        logging.error(f"No hay columna con nombre 'geom' o 'geometry' en capa  {layer}: {ex}")
