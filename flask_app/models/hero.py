from flask_app import flash
from flask_app.config.mysqlconnection import connectToMySQL
import re

# from flask_app.models.hero import Hero
from pprint import pprint


DATABASE = 'marvel'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class Hero:
    def __init__( self , data ):
        self.id = data['id']
        self.hero_number = data['hero_number']
        self.name = data['name']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.users = []
        if 'first_name' in data:    
            self.first_name = data ['first_name']
        if 'first_name' in data:    
            self.last_name = data ['last_name']    

#     # ! Read ALL
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM heros;"
        results = connectToMySQL(DATABASE).query_db(query)
        print(results)
        heros = []
        for hero in results:
            heros.append( cls(hero) )
        return heros 

#     # @classmethod
#     # def get_all_with_user(cls):
#     #     query = "SELECT * FROM heros JOIN users ON heros.user_id = users.id;"
#     #     results = connectToMySQL(DATABASE).query_db(query)
#     #     print(results)
#     #     heros =[]
#     #     for hero in results:
#     #         heros.append(cls(hero))
#     #     return heros

#     # ! READ/RETRIEVE ONE
#     # @classmethod
#     # def get_one(cls, data):
#     #     query = "SELECT * FROM heros WHERE id = %(id)s ;"
#     #     results = connectToMySQL(DATABASE).query_db(query, data)
#     #     print(results)
#     #     hero = Hero(results[0])
#     #     return hero

#     @classmethod
#     def get_one_hero(cls, data):
#         query = "SELECT * FROM heros WHERE id = %(id)s ;"
#         results = connectToMySQL(DATABASE).query_db(query, data)
#         print(results)
#         hero = Hero(results[0])
#         return hero

    @classmethod
    def get_hero_with_users(cls, data):
        query = "SELECT * FROM heros LEFT JOIN likes ON likes.hero_id = hero.id LEFT JOIN users ON likes.user_id = users.id WHERE heros.id = %(id)s;"
        results = connectToMySQL('recipes').query_db(query, data)
        # results will be a list of recipe objects with the user attached to each row.
        hero = cls(results[0])
        for row_from_db in results:
            # Now we parse the recipe data to make instances of recipes ="keyword from-rainbow">and add them into our list.
            user_data = {
                "id": row_from_db["users.id"],
                "first_name": row_from_db["first_name"],
                "last_name": row_from_db["last_name"],
                "email": row_from_db["email"],
                "password": row_from_db["password"],
                "created_at": row_from_db["users.created_at"],
                "updated_at": row_from_db["users.updated_at"]
            }
            if row_from_db['first_name']:
                hero.users.append(user.User(user_data))
        return hero



#     # ! Create
#     @classmethod
#     def save(cls, data ):
#         query = "INSERT INTO heros (name, description, instruction, under, date_made, user_id, created_at, updated_at ) VALUES ( %(name)s , %(description)s , %(instruction)s, %(under)s, %(date_made)s, %(user_id)s, NOW() , NOW() );"
#         return connectToMySQL(DATABASE).query_db( query, data )

#     # ! Delete
#     @classmethod
#     def destroy(cls, data):
#         query = "DELETE FROM heros WHERE id = %(id)s ;"
#         return  connectToMySQL(DATABASE).query_db(query, data)

#     # ! Update
#     @classmethod
#     def update2(cls, data):
#         query = "UPDATE heros SET name = %(name)s, description = %(description)s, instruction = %(instruction)s, under = %(under)s, date_made = %(date_made)s, user_id = %(user_id)s WHERE id = %(id)s ;"
#         return connectToMySQL(DATABASE).query_db(query, data)

    
#     @classmethod
#     def favorites2(cls, data):
#         # query = "SELECT first_name FROM heros LEFT JOIN favorites ON heros.id = favorites.hero_id LEFT JOIN users ON favorites.user2_id = users.id WHERE hero_id = %(id)s ;"
#         query = "SELECT first_name FROM heros LEFT JOIN favorites ON heros.id = favorites.hero_id LEFT JOIN users ON favorites.user2_id = users.id WHERE hero_id = %(id)s ;"
#         return connectToMySQL(DATABASE).query_db(query, data)    
#         print(results)

#     # @classmethod
#     # def favorites(cls):
#     #     query = "SELECT * FROM heros LEFT JOIN favorites ON heros.id = favorites.hero_id LEFT JOIN users ON favorites.user2_id = users.id WHERE hero_id = %(id)s ;"
#     #     results = connectToMySQL(DATABASE).query_db(query)
#     #     print(results)
#     #     heros =[]
#     #     for hero in results:
#     #         heros.append(cls(hero))
#     #     return heros



#     # @classmethod
#     # def get_one_with_favorites(cls, data):
#     #     query = "SELECT * FROM heros LEFT JOIN favorites ON heros.id = favorites.hero_id LEFT JOIN users ON favorites.user2_id = users.id WHERE hero_id = %(id)s ;"
#     #     results = connectToMySQL(DATABASE).query_db(query, data)
#     #     hero = Hero(results[0])
#     #     for result in results:
#     #         user_dict = {
#     #             'id': result['users.id'],
#     #             'first_name': result['first_name'],
#     #             'last_name': result['last_name'],
#     #             'email': result['email'],
#     #             'password': result['password'],
#     #             'created_at': result['heros.created_at'],
#     #             'updated_at': result['heros.updated_at'],
#     #         }
#     #         hero.users.append(User(user_dict))
#     #     print(hero)
#     #     return hero
#     # @classmethod
#     # def update(cls, data):
#     #     query = "UPDATE heros SET name = %(name)s, description = %(description)s, instruction = %(instruction)s, date_made = %(date_made)s, user_id = %(user_id)s WHERE id = %(id)s ;"
#     #     results = connectToMySQL(DATABASE).query_db(query, data)