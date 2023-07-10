from packages.Logs.logs import *
from packages.DB_set.database import bring_layer, insert_layer_into_postgis, engine
from packages.JSON_process.variables import variables
from packages.Steps.calculate_score import calculate_score
from packages.Steps.normalize_score import normalize_score

def start():
    try:

        layer = bring_layer("AAII_GP_Processed_new_Renamed", "gp_resulted", engine)
        new_l = calculate_score(layer, variables)             
        new_l = normalize_score(new_l)
        insert_layer_into_postgis(new_l, "prueba", engine)

    except Exception as ex:
        print(f"Error al ejecutar 'main':  " + str(ex))
        logging.error(f"Error al ejecutar 'main':  " + str(ex))



start()

