import logging
from datetime import datetime
from packages.DB_set.db_psql import *


#Class with credentials for DB value shp folder path
db_psql = Psql()
#Parameters:
logs_folder = db_psql.logs_folder
#-----------------/Logs Method`s/--------------------------
#Function made to the save the logs inside the Log´s file:
def set_loggs():
    date_today = datetime.today().date()    
    name = logs_folder + "\Logs from " + str(date_today)
    name += ".txt"
    logging.basicConfig(filename=name, filemode='a', format='%(asctime)s - %(levelname)s -  %(message)s', datefmt='%H:%M:%S')

#Initializing
set_loggs()