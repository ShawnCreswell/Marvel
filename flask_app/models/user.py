
from ast import Import
from flask_app import flash
from flask_app.config.mysqlconnection import connectToMySQL
import re

from flask_app.models.recipe import Recipe
from pprint import pprint


DATABASE = 'recipes'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.recipes = []
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # ! READ ALL
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(DATABASE).query_db(query)
        print(results)
        users = []
        for user in results:
            users.append( cls(user) )
        return users

    # ! READ/RETRIEVE ONE
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        user = User(result[0])
        return user

    # @classmethod
    # def get_one_name(cls,data):
    #     query = "SELECT first_name FROM users LEFT JOIN recipes ON users.id = recipes.user_id WHERE recipes.user_id= 7;"
    #     result = connectToMySQL(DATABASE).query_db(query, data)
    #     print(result)
    #     user_names = User(result[0])
    #     return user_names

    @classmethod
    def get_one_with_recipes(cls, data):
        query = "SELECT * FROM users LEFT JOIN recipes ON users.id = recipes.user_id WHERE users.id = %(id)s ;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        pprint(results)
        user = User(results[0])
        for result in results:
            recipe_dict = {
                'id': result['recipes.id'],
                'name': result['name'],
                'description': result['description'],
                'instruction': result['instruction'],
                'under': result['under'],
                'date_made': result['date_made'],
                'user_id': result['user_id'],
                'created_at': result['recipes.created_at'],
                'updated_at': result['recipes.updated_at'],
            }
            user.recipes.append(Recipe(recipe_dict))
        print(user)
        return user

    # @classmethod
    # def save(cls, data ):
    #     query = "INSERT INTO users (name, created_at, updated_at ) VALUES ( %(name)s, NOW() , NOW() );"
    #     return connectToMySQL(DATABASE).query_db(query, data )

    # ! CREATE
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users ( first_name , last_name , email, password, created_at, updated_at ) VALUES ( %(first_name)s , %(last_name)s , %(email)s , %(password)s , NOW() , NOW() );"
        return connectToMySQL(DATABASE).query_db( query, data )

    # ! UPDATE
    @classmethod
    def update(cls, data):
        query = "UPDATE users SET name = %(name)s WHERE id = %(id)s ;"
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def update(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s ;"
        results = connectToMySQL(DATABASE).query_db(query, data)

    # ! DELETE
    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)


    @staticmethod
    def validate_user(user):
        is_valid = True
        if len(user['name']) < 3:
            is_valid = False


    @staticmethod
    def validate_user(user):
        is_valid = True # we assume this is true
        if len(user['first_name']) < 3:
            is_valid = False
            flash("First Name must be at least 3 characters.", 'first_name')
        if len(user['last_name']) < 3:
            is_valid = False
            flash("Last Name must be at least 3 characters.", 'last_name')
        if not EMAIL_REGEX.match(user['email']): 
            is_valid = False
            flash("Invalid email address!", 'email')
        if user['password'] != user['password_confirm']:
            is_valid = False
            flash("Passwords must match", 'password')
        
        return is_valid


    @staticmethod
    def validate_user_password( user ):
        is_valid = True
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(user['password']): 
            flash("Invalid password!", 'password')
            is_valid = False
        return is_valid

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(DATABASE).query_db(query,data)
        # Didn't find a matching user
        if len(result) < 1:
            return False
        return cls(result[0])

    # @classmethod
    # def destroy(cls, data):
    #     query = "DELETE FROM recipes WHERE id = %(id)s ;"
    #     results = connectToMySQL(DATABASE).query_db(query, data)

    # @classmethod
    # def favorites(cls, data):
    #     query = "SELECT * FROM users LEFT JOIN favorites ON users.id = favorites.user_id LEFT JOIN recipes ON favorites.recipe_id = recipes.id WHERE users.id = %(id)s ;"
    #     # query = "SELECT * FROM users LEFT JOIN recipes ON users.id = recipes.user_id WHERE users.id = %(id)s ;"

    #     results = connectToMySQL(DATABASE).query_db(query, data)