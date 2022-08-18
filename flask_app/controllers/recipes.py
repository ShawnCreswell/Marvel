import re
from flask_app import app, render_template, redirect, request, session
from flask_app.models.recipe import Recipe
from flask_app.models.user import User





# ! Create recipes
@app.route("/create_recipe")
def resultss():
    print("hello")
    return render_template("create.html", users = User.get_all())

@app.route("/create_recipe", methods=['post'])
def create():
    data = {
        "name": request.form['name'],
        "description": request.form['description'],
        "instruction": request.form['instruction'], 
        "under": request.form['under'], 
        "date_made": request.form['date_made'], 
        "user_id": session['user_id']
    }
    user = session['user_id']
    Recipe.save(data)
    print(request.form)
    # recipe = Recipe.save(request.form)
    # return redirect(f"/dashboard/{request.form['user_id']}")
    return redirect(f"/dashboard/{user}")


# ! Read all
@app.route("/dashboard/<int:id>")
def index3(id):
    data = {
        "id": id
    }
    # user = User.get_one(data)
    user = User.get_one_with_recipes(data)
    recipes =  Recipe.get_all_with_user()
    # user_names = User.get_one_name(data)
    # print("****************")
    # print(user_names)
    print(user)
    return render_template("dashboard.html", user = user, recipes=recipes)

# @app.route("/dashboard/<int:id>")
# def dashboard_recipe(id):
#     recipe = Recipe.get_all()
#     print(recipe)
#     return render_template("dashboard.html", recipe = recipe)



# # ! READ ONE
# @app.route("/dashboard/recipe/<int:id>")
# def show_recipe(id):
#     data = {'id': id}
#     recipe = Recipe.get_one(data)
#     return render_template('show.html', recipe = recipe)

# ! READ ONE
# @app.route("/dashboard/recipe/<int:id>")
# def favorites(id):
    

#     data = {
#         "recipe_id": recipe_id
#     }

#     recipe = Recipe.favorites(data)
#     user = session['user_id']
#     # recipe = Recipe.get_one(data)

#     # return render_template("show.html", user = user, recipe = recipe)
#     return redirect(f"/dashboard/{user}")

    
# # ! Show Favorites





# @app.route("/show/<int:id>")
# def show1(id):
#     data = {
#         "id": id, 
#     }
#     recipe = recipe.get_one(data)
#     return render_template("show.html", recipe = recipe)





# # ! EDIT
# @app.route("/edit/<int:id>")
# def edit_recipe(id):
#     data = {"id": id}
#     return render_template("edit.html", recipe = recipe.get_one(data))

# @app.route("/update/recipe", methods = ['post'])
# def update_recipe():
#     Recipe.update(request.form)
#     return redirect(f"/show/{request.form['id']}")

@app.route("/edit_recipe/<int:id>")
def edit_recipe(id):
    data = {
        "id": id
    }
    return render_template("edit.html", recipe = Recipe.get_one_recipe(data))

# @app.route("/edit_recipe/<int:id>")
# def edit_recipe2(id):
#     data = {
#         "id": id
#     }
#     return redirect("/dashboard/{{user_id}}")




@app.route("/update/recipe", methods=['post'])
def update():
    data = {
        "name": request.form['name'],
        "description": request.form['description'],
        "instruction": request.form['instruction'],
        "date_made": request.form['date_made'],
        "under": request.form['under'],
        "user_id": session['user_id'],
        "id": request.form['id']
    }

    print(request.form)
    
    Recipe.update2(data)
    user = session['user_id']
    return redirect(f"/dashboard/{user}")



    
# # ! Delete 
@app.route('/delete/<int:id>')
def delete_recipe(id):
    Recipe.destroy({'id': id})
    user = session['user_id']
    return redirect(f"/dashboard/{user}")


# @app.route("/")
# def home():
#     print("hello")
#     return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
