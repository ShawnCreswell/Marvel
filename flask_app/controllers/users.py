# from ..models.hero import Hero
from flask_app import app, render_template, redirect, request, session, flash
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
from pprint import pprint
import requests

from marvel import Marvel   
marvel = Marvel(PUBLIC_KEY="0b340cd6701075fffe6b41aeec6947b3" , PRIVATE_KEY= "a72560e27f40a5eec919b7f04feca520215feb16")
bcrypt = Bcrypt(app)

@app.route("/signin")
def home():
    print("hello")
    return render_template("index.html")

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
    user = User.get_one(data)
    # user = User.get_all_heros_with_user()
    # user = User.get_one_with_heros(data)
    # user = User.favorites(data)
    # user = User.get_one_with_heros(data)
    # heros =  Hero.get_all_with_user()
    print(user)
    # return render_template("dashboard.html", user = user, heros=heros)
    return render_template("dashboard.html", user = user)




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
@app.route("/edit/user/<int:id>")
def edit_user(id):
    data = {
        "id": session['user_id']
    }
    print("hello")
    return render_template("edit_user.html", user = User.get_one(data) )

@app.route("/edit/user", methods=['post'])
def update_user():
    users = session['user_id']
    if not User.validate_user(request.form):
        return redirect(f'/edit/user/{users}')
    hashed_pw = bcrypt.generate_password_hash(request.form['password'])
    data = {
        "id": session['user_id'],
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'], 
        "password": hashed_pw
    }
    User.update(data)
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']

    print(request.form)
    return redirect(f"/dashboard/{users}")


# @app.route("/create_hero")
# def create_hero():
#     print("hello")
#     return render_template("create.html")
# # def index2():

# # ! READ ONE
# @app.route("/dashboard/hero/<int:id>")
# def show_hero(id):
#     data = {
#         "id": id
#     }

#     user = User.get_one_with_heros(data)
#     print(data)

#     # hero = Hero.get_one(data)
#     # return render_template("show.html", user = user, hero = hero)
#     return render_template("show.html", user = user)
    

# @app.route("/dashboard/hero/<int:id>", methods = ['POST'])
# def show_hero_favorites(id):
#     data = {
#         "id": id
#     }
#     print(data)
#     user = session['user_id']
#     # hero = Hero.get_one(data)
#     # return render_template("show.html", user = user, hero = hero)
#     return redirect (f"dashboard/hero/{user}", hero = Hero.favorites2(data))

# @app.route("/")
# def home():
#     print("hello")
#     return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
