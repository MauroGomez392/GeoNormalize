import geopandas as gpd
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from packages.Logs.logs import *
from .db_psql import *
import psycopg2
#Class with credentials for DB connect
db_psql = Psql()

#-----------------/Connecting with Database/--------------------------
try:
    engine = create_engine(db_psql.get_url_connect())
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
def send_query_to_db(engine, query):
    conn = engine.connect()
    try:
        conn.execute(query)
        conn.close()
        return True
    except Exception as ex:
        print(str(ex))
        return False

#Method that search the layer in the db and returns true if it is found and false if it´s not       
def check_if_existe_table_in_db(engine, layer_cod):
    query = f'SELECT * FROM public."{layer_cod}"'
    return send_query_to_db(engine, query)

def rename_to_correct_table_in_db(engine, layer_cod):
    old_name = layer_cod + "_new"    
    query = f'ALTER TABLE public."{old_name}" RENAME TO "{layer_cod}"'
    return send_query_to_db(engine, query)

def delete_old_table(engine, layer_cod):
    query = f'DROP TABLE public."{layer_cod}"'
    return send_query_to_db(engine, query)

#Method to change the url from the DataBase CapaFuente
def update_urls_in_db(session, Table, codCapa, newURL, i = 0):
    try:
        stmts = session.query(Table).filter(Table.codCapa == codCapa).all() 
        stmt = stmts[i]
        print(stmt)
        stmt.urlDescarga = newURL
        session.add(stmt)
        session.commit()
        print("Cambio realizado exitosamente.")
        print(stmt)
    except Exception as ex:
        print(str(ex))
        logging.error(str(ex))

#delet the entry that matches with the layerCod passed in the table passed (capsDescriptor o LayerSource)
def delete_entry(session, layerCod, Table):
    try:
        stmt = session.query(Table).filter(Table.codCapa == layerCod).first()     #Syntax from ORM SQLAlqhemy // read doc
        session.delete(stmt)
        session.commit()
        print("Entrada eliminada correctamente") 
    except Exception as ex:
        print(str(ex)) 
        logging.error(str(ex)) 

#Everytime we update a layer in the DB a index is made and we change the table_name but not the index_name, so this method ´ll update the name of the index, deleting the lastone and leaving space for the newone
def alter_index_created(engine, layer_cod, is_an_update):    
    try:
        layer_cod_lower = layer_cod.lower()
        if(is_an_update):
            query = f"ALTER INDEX idx_{layer_cod_lower}_new_geometry RENAME TO idx_{layer_cod_lower}" #If it´s true is because already existed one shape before and the rename´ll have a "_new"
        else:
            print(layer_cod_lower)
            query = f"ALTER INDEX idx_{layer_cod_lower}_geometry RENAME TO idx_{layer_cod_lower}"
            print(query)
        send_query_to_db(engine, query)
        print("NOMBRE DE INDEX CAMBIADO!!??¿?¿?¿¿%&%$&·%/!%¿?")    
    except Exception as ex:
        print(ex)
        
def bring_layer(layer_name: str, schema: str, engine):
    try:
        query = f'SELECT * FROM "{schema}"."{layer_name}";'
        layer = gpd.read_postgis(query, engine, "geometry")
        return layer
    except Exception as ex:
        print(f"Error al traer capa {layer_name}:  " + str(ex))
        logging.error(f"Error al traer capa {layer_name}:  " + str(ex))

#-----------------/Post Layer into DB/--------------------------
def insert_layer_into_postgis(layer:gpd.GeoDataFrame, table_name: str, engine, schema_ : str = 'gp_resulted'):
    try:
        #-----------------/Connection with Geopandas/--------------------------
        connection_geoP = engine.connect()
        layer.to_postgis(table_name, connection_geoP, schema_ , if_exists = 'replace', index = False, index_label = None, chunksize = None, dtype = None)
        print("Proceso insert_layer_into_postgis realizado")             
    except Exception as ex:
        print("Error al ejecutar algoritmo insert_layer_into_postgis:     " + str(ex))
        logging.error("Error al ejecutar algoritmo insert_layer_into_postgis:     " + str(ex))  

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



