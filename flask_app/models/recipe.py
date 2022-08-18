
from flask_app.config.mysqlconnection import connectToMySQL




DATABASE = 'recipes'
class Recipe:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instruction = data['instruction']
        self.under = data['under']
        self.date_made = data['date_made']
        self.user_id = data['user_id']
        if 'first_name' in data:    
            self.first_name = data ['first_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # ! Read ALL
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL(DATABASE).query_db(query)
        print(results)
        recipes = []
        for recipe in results:
            recipes.append( cls(recipe) )
        return recipes 

    @classmethod
    def get_all_with_user(cls):
        query = "SELECT * FROM recipes JOIN users ON recipes.user_id = users.id;"
        results = connectToMySQL(DATABASE).query_db(query)
        print(results)
        recipes =[]
        for recipe in results:
            recipes.append(cls(recipe))
        return recipes

    # ! READ/RETRIEVE ONE
    # @classmethod
    # def get_one(cls, data):
    #     query = "SELECT * FROM recipes WHERE id = %(id)s ;"
    #     results = connectToMySQL(DATABASE).query_db(query, data)
    #     print(results)
    #     recipe = Recipe(results[0])
    #     return recipe

    @classmethod
    def get_one_recipe(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(id)s ;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        print(results)
        recipe = Recipe(results[0])
        return recipe

    # ! Create
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO recipes (name, description, instruction, under, date_made, user_id, created_at, updated_at ) VALUES ( %(name)s , %(description)s , %(instruction)s, %(under)s, %(date_made)s, %(user_id)s, NOW() , NOW() );"
        return connectToMySQL(DATABASE).query_db( query, data )

    # ! Delete
    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s ;"
        return  connectToMySQL(DATABASE).query_db(query, data)

    # ! Update
    @classmethod
    def update2(cls, data):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instruction = %(instruction)s, under = %(under)s, date_made = %(date_made)s, user_id = %(user_id)s WHERE id = %(id)s ;"
        return connectToMySQL(DATABASE).query_db(query, data)

    
    @classmethod
    def favorites2(cls, data):
        # query = "SELECT first_name FROM recipes LEFT JOIN favorites ON recipes.id = favorites.recipe_id LEFT JOIN users ON favorites.user2_id = users.id WHERE recipe_id = %(id)s ;"
        query = "SELECT first_name FROM recipes LEFT JOIN favorites ON recipes.id = favorites.recipe_id LEFT JOIN users ON favorites.user2_id = users.id WHERE recipe_id = %(id)s ;"
        return connectToMySQL(DATABASE).query_db(query, data)    
        print(results)

    # @classmethod
    # def favorites(cls):
    #     query = "SELECT * FROM recipes LEFT JOIN favorites ON recipes.id = favorites.recipe_id LEFT JOIN users ON favorites.user2_id = users.id WHERE recipe_id = %(id)s ;"
    #     results = connectToMySQL(DATABASE).query_db(query)
    #     print(results)
    #     recipes =[]
    #     for recipe in results:
    #         recipes.append(cls(recipe))
    #     return recipes



    # @classmethod
    # def get_one_with_favorites(cls, data):
    #     query = "SELECT * FROM recipes LEFT JOIN favorites ON recipes.id = favorites.recipe_id LEFT JOIN users ON favorites.user2_id = users.id WHERE recipe_id = %(id)s ;"
    #     results = connectToMySQL(DATABASE).query_db(query, data)
    #     recipe = Recipe(results[0])
    #     for result in results:
    #         user_dict = {
    #             'id': result['users.id'],
    #             'first_name': result['first_name'],
    #             'last_name': result['last_name'],
    #             'email': result['email'],
    #             'password': result['password'],
    #             'created_at': result['recipes.created_at'],
    #             'updated_at': result['recipes.updated_at'],
    #         }
    #         recipe.users.append(User(user_dict))
    #     print(recipe)
    #     return recipe
    # @classmethod
    # def update(cls, data):
    #     query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instruction = %(instruction)s, date_made = %(date_made)s, user_id = %(user_id)s WHERE id = %(id)s ;"
    #     results = connectToMySQL(DATABASE).query_db(query, data)