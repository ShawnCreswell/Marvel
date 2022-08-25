from flask_app.config.mysqlconnection import MySQLConnection, connectToMySQL
from flask_app.models import hero
from flask_app import flash
from pprint import pprint

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

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM likes WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        like = cls(result[0])
        return like

    @classmethod
    def get_all_heros_with_user(cls):
        query = "SELECT name FROM likes JOIN heros ON hero_id = heros.id WHERE likes.user_id = %(id)s ;"
        results = connectToMySQL(DATABASE).query_db(query)
        print(results)
        heros =[]
        for hero in results:
            heros.append(cls(hero))
        return heros


    @classmethod
    def get_one_like(cls, data):
        query = "SELECT name FROM likes JOIN heros ON hero_id = heros.id WHERE likes.user_id = %(id)s ;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        like = cls(result[0])
        return like

    @classmethod
    def get_one_like_with_heros(cls, data):
        query = "SELECT name FROM users JOIN likes ON user_id = users.id JOIN heros ON hero_id = heros.id WHERE likes.user_id = %(id)s ;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        pprint(results)
        like = Like(results[0])
        for result in results:
            hero_dict = {
                'id': result['heros.id'],
                'hero_number': result['heros_number'],
                'name': result['name'],
                'description': result['description'],
                'created_at': result['heros.created_at'],
                'updated_at': result['heros.updated_at'],
            }
            like.heros.append(Hero(hero_dict))
        print(user)
        return like


    @classmethod
    def get_all_non_faves(cls, data):
        query = "SELECT likes.comment_id FROM likes WHERE likes.user_id != %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        non_faves = []
        for result in results:
            non_faves.append(result['comment_id'])
        return non_faves