import os
from decouple import config

#-----------------/Class with the ENV credentials/--------------------------
class Psql:
    def __init__(self):
        self.passW = config('DB_SECRET_KEY')
        self.db_name = config('DB_NAME')
        self.db_user = config('DB_USER')
        self.db_host = config('DB_HOST')
        self.db_port = config('DB_PORT')
        self.logs_folder = config('LOGS_LOCAL_FOLDER')
        self.project_location_path = config('PTOJECT_LOCATION_PATH')
#-----------------/Builds the URL for the connect/--------------------------
    def get_url_connect(self):
        #"postgresql://postgres:" + self.passW + "@localhost:5432/PruebaAsentamiento"
        db_connection = "postgresql://" + self.db_user + ":" + self.passW + "@" + self.db_host + ":" + self.db_port + "/" + self.db_name 
        return db_connection
