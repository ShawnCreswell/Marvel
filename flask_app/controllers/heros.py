# from ..models.hero import Hero
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
    return render_template("Landing.html", my_characters=my_characters, coms=coms)


@app.route('/hero/detail')
def hero_detail():
    characters = marvel.characters
    comics = marvel.comics
    morecomic = marvel.comics
    my_characters = characters.all(nameStartsWith = session['name'])['data']["results"]
    heroName = session['name']
    coms = comics.all(title = session['name'])['data']["results"]

    url = f"https://youtube.googleapis.com/youtube/v3/search?part=snippet&maxResults=1&order=relevance&q={session['name']}%20marvel%20character%20stats&safeSearch=moderate&key=AIzaSyDmNcGpYoh7kWzRRdoNFY8C9xQS4V1sIyk"
    data = requests.get(url)
    
    pprint(data.json()['items'][0]['id']['videoId'])
    pprint("------------")

    return render_template("hero_detail.html", my_characters=my_characters, coms=coms, data=data)