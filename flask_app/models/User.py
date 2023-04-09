from flask_app.config.mysqlconnection import connectToMySQL

db = 'image_archive_schema'

class User:
    def __init__(self, data):
        self.username = data['username']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    #Create
    @classmethod
    def insert_data(cls, data):
        query = "INSERT INTO users (username) VALUES (%(username)s)"
        results = connectToMySQL(db).query_db(query, data)
        return results

    #Read (Single or All)
    @classmethod
    def get_single_data(cls, data):
        query = "SELECT * FROM users WHERE id=%(id)s"
        results = connectToMySQL(db).query_db(query, data)
        return results

    @classmethod
    def get_all_data(cls):
        query = "SELECT * FROM users"
        results = connectToMySQL(db).query_db(query)
        return results

    #Update
    @classmethod 
    def update_data(cls, data):
        query = "UPDATE users SET username=%(username)s"
        results = connectToMySQL(db).query_db(query, data)
        return results

    #Delete
    def delete_data(cls, data):
        query = "DELETE from users WHERE id=%(id)s"
        results = connectToMySQL(db).query_db(query, data)
        return results