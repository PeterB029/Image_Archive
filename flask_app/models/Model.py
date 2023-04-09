from flask_app.config.mysqlconnection import connectToMySQL

db = 'name_of_shcema'

class Model:
    def __init__(self, data):
        pass

    #Create
    @classmethod
    def insert_data(cls, data):
        query = "INSERT INTO data_table () VALUES (%()s)"
        results = connectToMySQL(db).query_db(query, data)
        return results

    #Read (Single or All)
    @classmethod
    def get_single_data(cls, data):
        query = "SELECT * FROM data_table WHERE id=%(id)s"
        results = connectToMySQL(db).query_db(query, data)
        return results

    @classmethod
    def get_all_data(cls, data):
        query = "SELETE * FROM data_table"
        results = connectToMySQL(db).query_db(query)
        return results

    #Update
    @classmethod 
    def update_data(cls, data):
        query = "UPDATE data_table SET data=%(data)s%"
        results = connectToMySQL(db).query_db(query, data)
        return results

    #Delete
    def delete_data(cls, data):
        query = "DELETE from data_table WHERE id=%(id)s"
        results = connectToMySQL(db).query_db(query, data)
        return results