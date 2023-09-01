from packages.Logs.logs import *
from packages.DB_set.database import bring_layer, insert_layer_into_postgis, check_if_existe_table_in_db
from packages.JSON_process.variables import variables
from packages.Steps.calculate_score import calculate_score
from packages.Steps.normalize_score import normalize_score
from packages.Steps.layer_transformer import *

def start():
    try:
        print(check_if_existe_table_in_db("AAII_GP_Processed_new"))

        change_columns("AAII_GP_Processed_new", "gp_resulted", json_file_path)
        
        layer = bring_layer("AAII_GP_Processed_new_Renamed", "gp_resulted")
        print("----------------/Empezando puntuación/----------------")
        columns = ['id', 'depa', 'CED-ESJAV', 'CED-LTECV', 'AMBUSV', 'UAS-TERCV',
       'UAS-PRIMV', 'UAS-SEGUV', 'CERCASENV', 'COHEGEOGV', 'RVI-CAMIP', 'RVI-CALLP',
       'RVI-PASAP', 'RVI-VIRTP', 'RVI-LONGV', 'RVI-SN9000V', 'DENSPOBLV',
       'IMV-JUNTV', 'IMV-AVANV', 'IMV-MEVV', 'IMV-ANVV', 'IMV-PMBV',
       'IMV-ETMV', 'AREAPOTESV', 'CVE-NOAPV', 'CVE-DOMV', 'CVE-INDV',
       'LINECOSTV', 'CENTAPOYV', 'COOPVIVV', 'CENTINAUV', 'CENTMECV',
       'CSU-RNATP', 'CSU-RURAP', 'CSU-SUBUP', 'CSU-URBAP', 
       'ARIMPERMEP', 'CONJHABISV',  'ESPALIBRSV', 'INSTAPROSV',
       'PROYPMBV', 'DISTAGUAV',  'PARAOMNIV', 'SANEV', 'FOCOINCESV', 'SDF-OPERV', 'SDF-NOOPV',
       'TAMAASENV', 'LTE-TALTV', 'LTE-TMEDV', 'TPR-PRIVP', 'TPR-EPUBP',
       'TPR-OPUBP', 'TPR-SNDAP', 'AREASNAPV', 'geometry']
        layer_to_score = layer[columns]
        new_l = calculate_score(layer_to_score, variables)             
        print("----------------/Empezando Normalización/----------------")
        new_l = normalize_score(new_l)
        print("----------------/Finalización de Normalización/----------------")
        insert_layer_into_postgis(new_l, "aaii_gp_processed_fixed_test")

    except Exception as ex:
        print(f"Error al ejecutar 'main':  " + str(ex))
        logging.error(f"Error al ejecutar 'main':  " + str(ex))



start()

