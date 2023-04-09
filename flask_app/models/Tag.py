from flask_app.config.mysqlconnection import connectToMySQL

db = 'image_archive_schema'

class Tag:
    def __init__(self, data):
        self.name = data['name']
        self.color = data['color']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    #Create
    @classmethod
    def insert_data(cls, data):
        query = "INSERT INTO tags (name, color) VALUES (%(name)s, %(color)s)"
        results = connectToMySQL(db).query_db(query, data)
        return results

    #Read (Single or All)
    @classmethod
    def get_single_data(cls, data):
        query = "SELECT * FROM tags WHERE id=%(id)s"
        results = connectToMySQL(db).query_db(query, data)
        return results

    @classmethod
    def get_all_data(cls):
        query = "SELETE * FROM tags"
        results = connectToMySQL(db).query_db(query)
        return results

    #Update
    @classmethod 
    def update_data(cls, data):
        query = "UPDATE tags SET name=%(name)s, color=%(color)s"
        results = connectToMySQL(db).query_db(query, data)
        return results

    #Delete
    def delete_data(cls, data):
        query = "DELETE from tags WHERE id=%(id)s"
        results = connectToMySQL(db).query_db(query, data)
        return results