# import re
# from flask_app import app, render_template, redirect, request, session
# from flask_app.models.hero import Hero
# from flask_app.models.user import User





# # ! Create heros
# @app.route("/create_hero")
# def resultss():
#     print("hello")
#     return render_template("create.html", users = User.get_all())

# @app.route("/create_hero", methods=['post'])
# def create():
#     data = {
#         "name": request.form['name'],
#         "description": request.form['description'],
#         "instruction": request.form['instruction'], 
#         "under": request.form['under'], 
#         "date_made": request.form['date_made'], 
#         "user_id": session['user_id']
#     }
#     user = session['user_id']
#     Hero.save(data)
#     print(request.form)
#     # hero = Hero.save(request.form)
#     # return redirect(f"/dashboard/{request.form['user_id']}")
#     return redirect(f"/dashboard/{user}")


# # ! Read all
# @app.route("/dashboard/<int:id>")
# def index3(id):
#     data = {
#         "id": id
#     }
#     # user = User.get_one(data)
#     user = User.get_one_with_heros(data)
#     heros =  Hero.get_all_with_user()
#     # user_names = User.get_one_name(data)
#     # print("****************")
#     # print(user_names)
#     print(user)
#     return render_template("dashboard.html", user = user, heros=heros)

# # @app.route("/dashboard/<int:id>")
# # def dashboard_hero(id):
# #     hero = Hero.get_all()
# #     print(hero)
# #     return render_template("dashboard.html", hero = hero)



# # # ! READ ONE
# # @app.route("/dashboard/hero/<int:id>")
# # def show_hero(id):
# #     data = {'id': id}
# #     hero = Hero.get_one(data)
# #     return render_template('show.html', hero = hero)

# # ! READ ONE
# # @app.route("/dashboard/hero/<int:id>")
# # def favorites(id):
    

# #     data = {
# #         "hero_id": hero_id
# #     }

# #     hero = Hero.favorites(data)
# #     user = session['user_id']
# #     # hero = Hero.get_one(data)

# #     # return render_template("show.html", user = user, hero = hero)
# #     return redirect(f"/dashboard/{user}")

    
# # # ! Show Favorites





# # @app.route("/show/<int:id>")
# # def show1(id):
# #     data = {
# #         "id": id, 
# #     }
# #     hero = hero.get_one(data)
# #     return render_template("show.html", hero = hero)





# # # ! EDIT
# # @app.route("/edit/<int:id>")
# # def edit_hero(id):
# #     data = {"id": id}
# #     return render_template("edit.html", hero = hero.get_one(data))

# # @app.route("/update/hero", methods = ['post'])
# # def update_hero():
# #     Hero.update(request.form)
# #     return redirect(f"/show/{request.form['id']}")

# @app.route("/edit_hero/<int:id>")
# def edit_hero(id):
#     data = {
#         "id": id
#     }
#     return render_template("edit.html", hero = Hero.get_one_hero(data))

# # @app.route("/edit_hero/<int:id>")
# # def edit_hero2(id):
# #     data = {
# #         "id": id
# #     }
# #     return redirect("/dashboard/{{user_id}}")




# @app.route("/update/hero", methods=['post'])
# def update():
#     data = {
#         "name": request.form['name'],
#         "description": request.form['description'],
#         "instruction": request.form['instruction'],
#         "date_made": request.form['date_made'],
#         "under": request.form['under'],
#         "user_id": session['user_id'],
#         "id": request.form['id']
#     }

#     print(request.form)
    
#     Hero.update2(data)
#     user = session['user_id']
#     return redirect(f"/dashboard/{user}")



    
# # # ! Delete 
# @app.route('/delete/<int:id>')
# def delete_hero(id):
#     Hero.destroy({'id': id})
#     user = session['user_id']
#     return redirect(f"/dashboard/{user}")


# # @app.route("/")
# # def home():
# #     print("hello")
# #     return redirect("/")

# if __name__ == "__main__":
#     app.run(debug=True)
