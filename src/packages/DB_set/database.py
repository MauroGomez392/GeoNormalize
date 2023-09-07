import geopandas as gpd
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from packages.Logs.logs import *
from .db_psql import Psql
import psycopg2
#from shapely.geos import *

#Class with credentials for DB connect
db_psql = Psql()

#-----------------/Connecting with Database/--------------------------
try:
    con_string = db_psql.get_url_connect()
    engine = create_engine(con_string)
    logging.warning("----------------------------------------------------------------------------------------------")
    logging.warning("Conexión con Postgres establecida")
    print("Conexión con Postgres establecida")
except Exception as ex:
    logging.error(str(ex))
    print(str(ex))

#-----------------/Needed for the ORM/--------------------------
Session = sessionmaker(bind = engine)
session = Session()

#-----------------/Helpers Method`s related to DB/--------------------------

#This method will send the SQL query to the db. It has to be called after a SQL sentence and need to be passed as second parameter. The firstone´ll be the engine needed for the conection with db
def execute_query(query):
    conn = engine.connect()
    try:
        conn.execute(query)
        conn.close()
        return True
    except Exception as ex:
        print(str(ex))
        return False

#Method that search the layer in the db and returns true if it is found and false if it´s not       
def check_if_existe_table_in_db(layer_cod):
    query = f'SELECT * FROM "gp_resulted"."{layer_cod}"'
    return execute_query(text(query))
      
#Brings the layer and return it in memory
def bring_layer(layer_name: str, schema: str):
    try:
        query = text(f'SELECT * FROM "{schema}"."{layer_name}";')        
        layer = gpd.read_postgis(query, engine, geom_col="geometry")                
        print(type(layer) , "    print al TRAER la capa")
        return layer

    except Exception as ex:
        print(f"Error al traer capa {layer_name}:  " + str(ex))
        logging.error(f"Error al traer capa {layer_name}:  " + str(ex))

#-----------------/Post Layer into DB/--------------------------
#Persist the geodataframe format layer in the database using postgis
def insert_layer_into_postgis(layer:gpd.GeoDataFrame, table_name: str, schema_ : str = 'gp_resulted'):
    try:
        #-----------------/Connection with Geopandas/--------------------------
        print(type(layer), "    print al INSERTAR")
        print(layer.crs)
        l = gpd.GeoDataFrame(layer)
        l.to_postgis(table_name, engine, schema_ , if_exists = 'replace', index = False, index_label = None, chunksize = None, dtype = None)
        print("Proceso insert_layer_into_postgis realizado")             
    except Exception as ex:
        print("Error al ejecutar algoritmo insert_layer_into_postgis:     " + str(ex))
        logging.error("Error al ejecutar algoritmo insert_layer_into_postgis:     " + str(ex))  

#every time we bring up a layer in Postgres, an index is made for that layer and we don't need it, so we delete it
def delete_created_index(table_name: str):
    try:
        # Establecer la conexión con la base de datos
        connection = psycopg2.connect(
            host = db_psql.db_host,
            database = db_psql.db_name,
            user = db_psql.db_user,
            password = db_psql.passW
        )
        # Crear un cursor para ejecutar consultas
        cursor = connection.cursor()
        # Ejecutar la consulta DROP INDEX
        query = f'DROP INDEX "gp_resulted"."idx_{table_name}_geometry";'
        cursor.execute(query)
        # Confirmar los cambios
        connection.commit()
        # Cerrar el cursor y la conexión
        cursor.close()
        connection.close()
    except Exception as ex:
        print("Error al ejecutar el PROCESS_HANDLER(): " + str(ex))
        return None



