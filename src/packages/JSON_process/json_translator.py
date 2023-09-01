import json
import logging



def get_columns_dictionary(json_path:str):
    try:
        #Load Json file
        with open(json_path) as file:
            data = json.load(file)
        columns_dictionary = []
        #for columns in data.items():
        for columns in data.values():
            for column in columns:
                columns_dictionary.append(column)
        return columns_dictionary
    except Exception as ex:
        print(f"Error al traducir JSON con nombres de columnas:  " + str(ex))
        logging.error(f"Error al traducir JSON con nombres de columnas:  " + str(ex))


