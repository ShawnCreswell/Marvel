from flask_app import app
from flask_app.controllers import recipes
from flask_app.controllers import users
from marvel import Marvel
# from import PUBLIC_KEY, PRIVATE_KEY

marvel = Marvel(PUBLIC_KEY="0b340cd6701075fffe6b41aeec6947b3" , PRIVATE_KEY= "a72560e27f40a5eec919b7f04feca520215feb16")

characters = marvel.characters

# my_characters = characters.all(name = "Black Panther")['data']["results"]


# print(my_characters[0]["name"])
# print(my_characters[0]["id"])
# print(my_characters[0]["comics"])

my_characters = characters.all(nameStartsWith = "Capt")['data']["results"]
print(my_characters[0]["name"])

# for char in my_characters:
#     print(char['name'])
    
for char in my_characters:
    print(char['id'], char["name"])
    for comic in char["comics"]["items"]:
        print(comic['name'])
    print("--------------------")




if __name__ == "__main__":
    app.run(debug=True)