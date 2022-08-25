from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask_app.models import hero
from flask_app import flash

DATABASE = 'marvel'


class Like:

    def __init__(self, data):
        self.id = data['id'],
        self.user_id = data['user_id'],
        self.comment_id = data['hero_id']

    # @classmethod
    # def save(cls, data):
    #     query = "INSERT INTO likes (user_id, comment_id) VALUES (%(user_id)s, %(comment_id)s);"
    #     connectToMySQL(DATABASE).query_db(query, data)

    # @classmethod
    # def get_one(cls, data):
    #     query = "SELECT * FROM likes WHERE id = %(id)s;"
    #     result = connectToMySQL(DATABASE).query_db(query, data)
    #     like = cls(result[0])
    #     return like

    @classmethod
    def get_all_non_faves(cls, data):
        query = "SELECT likes.comment_id FROM likes WHERE likes.user_id != %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        non_faves = []
        for result in results:
            non_faves.append(result['comment_id'])
        return non_faves