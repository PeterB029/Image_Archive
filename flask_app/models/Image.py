from flask_app.config.mysqlconnection import connectToMySQL

db = 'image_archive_schema'

class Image:
    def __init__(self, data):
        self.name = data['name']
        self.image = data['image']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    #Create
    @classmethod
    def insert_data(cls, data):
        query = "INSERT INTO images (name, image) VALUES (%(name)s, %(image)s)"
        results = connectToMySQL(db).query_db(query, data)
        return results

    #Read (Single or All)
    @classmethod
    def get_single_data(cls, data):
        query = "SELECT * FROM images WHERE id=%(id)s"
        results = connectToMySQL(db).query_db(query, data)
        return results

    @classmethod
    def get_all_data(cls):
        query = "SELETE * FROM images"
        results = connectToMySQL(db).query_db(query)
        return results

    #Update
    @classmethod 
    def update_data(cls, data):
        query = "UPDATE images SET name=%(name)s, image=%(image)s"
        results = connectToMySQL(db).query_db(query, data)
        return results

    #Delete
    def delete_data(cls, data):
        query = "DELETE from images WHERE id=%(id)s"
        results = connectToMySQL(db).query_db(query, data)
        return results