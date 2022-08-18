[python -m] pipenv install flask pymysql
[python -m] pipenv shell
            pipenv install flask-bcrypt

[server.py](server.py)
[user.py](user.py)
[mysqlconnection.py](mysqlconnection.py)

<input type="hidden" name="id" value="{{recipe.id}}">  

SELECT first_name FROM users JOIN recipes ON users.id = recipes.user_id
WHERE recipes.user_id= 7;

view
{% if recipe.user_id == session.user_id%}
edit
delete

{% endif %}


SELECT * FROM users LEFT JOIN favorites ON users.id = favorites.user_id LEFT JOIN recipes ON favorites.recipe_id = recipes.id
 WHERE users.id = 11 ;
\

SELECT * FROM users LEFT JOIN favorites ON users.id = favorites.user2_id LEFT JOIN recipes ON favorites.recipe_id = recipes.id
 WHERE recipe_id = 10 ;

 SELECT * FROM recipes LEFT JOIN favorites ON recipes.id = favorites.user2_id LEFT JOIN users on favorites.user_id = users.id
 Where user_id = 10


 SELECT * FROM recipes LEFT JOIN favorites ON recipes.id = favorites.recipe_id LEFT JOIN users on favorites.user2_id = users.id
 Where user_id = 12


