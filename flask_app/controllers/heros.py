# from ..models.recipe import Recipe
# from flask_app import app, render_template, redirect, request, session, flash
# from flask_app.models.user import User
# from flask_bcrypt import Bcrypt

# from marvel import Marvel
# marvel = Marvel(PUBLIC_KEY="0b340cd6701075fffe6b41aeec6947b3" , PRIVATE_KEY= "a72560e27f40a5eec919b7f04feca520215feb16")
# characters = marvel.characters
# bcrypt = Bcrypt(app)

# @app.route("/")
# def heros():
#     my_characters = characters.all(nameStartsWith = "Capt")['data']["results"]
#     return render_template("Landing.html", my_characters=my_characters)

# @app.route("/")
# def home2():
#     print("hello")
#     return redirect("/")

# if __name__ == "__main__":
#     app.run(debug=True)