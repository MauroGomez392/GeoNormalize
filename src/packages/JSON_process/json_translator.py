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
        print(columns_dictionary)
        return columns_dictionary
    except Exception as ex:
        print(f"Error al traducir JSON con nombres de columnas:  " + str(ex))
        logging.error(f"Error al traducir JSON con nombres de columnas:  " + str(ex))
    """
        print(f"--------------/ Categoría: {category} /--------------")
        print("--------------")
        original_column = column["original_column"]
        renamed_column = column["renamed_column"]
        print(f"Columna original : {original_column}")
        print(f"Columna renombrada : {renamed_column}")
        print("--------------")
        """

