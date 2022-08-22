from ..models.recipe import Recipe
from flask_app import app, render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
from pprint import pprint
import requests

from marvel import Marvel   
marvel = Marvel(PUBLIC_KEY="0b340cd6701075fffe6b41aeec6947b3" , PRIVATE_KEY= "a72560e27f40a5eec919b7f04feca520215feb16")
bcrypt = Bcrypt(app)

# ! Home page

@app.route("/")
def home4():
    print("hello")
    characters = marvel.characters
    my_characters = characters.all()['data']["results"]


    return render_template("home.html", my_characters=my_characters)

@app.route('/search', methods = ['POST'])
def search():
    session['name'] = request.form['hero']
    print("hello")
    return redirect("/hero")

@app.route("/hero")
def index():
    characters = marvel.characters
    comics = marvel.comics
    # img = marvel.image
    my_characters = characters.all(name = session['name'])['data']["results"]
    coms = comics.all(title = session['name'])['data']["results"]


    # for com in coms:
    #     pprint("-----------------")
    #     pprint(com['prices'][0]['price'])

        
            

    # images = characters.all(path = "http://i.annihil.us/u/prod/marvel/i/mg/6/60/5261a80a67e7d")['data']["results"]
    # {'path': 'http://i.annihil.us/u/prod/marvel/i/mg/6/60/5261a80a67e7d', 'extension': 'jpg'}
    # my_characters = characters.all(nameStartsWith = "Black")['data']["results"]
    # pprint("-----------------")
    # pprint(my_characters)
    return render_template("Landing.html", my_characters=my_characters, coms=coms)


# ! Create User
@app.route('/register', methods = ['POST'])
def register():
    print(request.form)
    if not User.validate_user(request.form):
        return redirect('/')

    hashed_pw = bcrypt.generate_password_hash(request.form['password'])
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'], 
        "password": hashed_pw
    }
    user = User.save(data)
    ## Log them in by add them to session
    session['user_id'] = user
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']

    print(hashed_pw)
    return redirect(f"/dashboard/{user}")

# ! Read ALl
@app.route("/dashboard/<int:id>")
def index2(id):
    data = {
        "id": id
    }
    # user = User.get_one(data)
    user = User.get_one_with_recipes(data)
    recipes =  Recipe.get_all_with_user()
    print(user)
    return render_template("dashboard.html", user = user, recipes=recipes)



# ! login user
@app.route('/login', methods = ['POST'])
def login():
    # see if the username provided exists in the database
    data = { "email" : request.form["email"] }
    user_in_db = User.get_by_email(data)
    # user is not registered in the db
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        # if we get False after checking the password
        flash("Invalid Email/Password")
        return redirect('/')
    # if the passwords matched, we set the user_id into session
    session['user.id'] = user_in_db.id
    session['user_id'] = user_in_db.id
    session['first_name'] = user_in_db.first_name
    # never render on a post!!!
    return redirect(f"/dashboard/{user_in_db.id}")

# ! UPDATE

@app.route("/create_recipe")
def create_recipe():
    print("hello")
    return render_template("create.html")
# def index2():

# ! READ ONE
@app.route("/dashboard/recipe/<int:id>")
def show_recipe(id):
    data = {
        "id": id
    }

    user = User.get_one_with_recipes(data)
    print(data)

    # recipe = Recipe.get_one(data)
    # return render_template("show.html", user = user, recipe = recipe)
    return render_template("show.html", user = user)
    

@app.route("/dashboard/recipe/<int:id>", methods = ['POST'])
def show_recipe_favorites(id):
    data = {
        "id": id
    }
    print(data)
    user = session['user_id']
    # recipe = Recipe.get_one(data)
    # return render_template("show.html", user = user, recipe = recipe)
    return redirect (f"dashboard/recipe/{user}", recipe = Recipe.favorites2(data))

@app.route("/")
def home():
    print("hello")
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
