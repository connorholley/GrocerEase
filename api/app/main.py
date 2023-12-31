from flask import Flask, jsonify
from flask_cors import CORS
from database.ControllersAndModels.UserController import UserController

app = Flask(__name__)
CORS(app, origins="http://localhost:5000")  

@app.route('/')
def hello_world():
    user_controller = UserController(environment="production")
    recipe_query=user_controller.get_user_recipes_by_id(2)
    recipe_array=[]
    for recipe in recipe_query:
    
        recipe_object={
            "recipeName":recipe.name,
            "imagePath":'../assets/images/nachos-example.jpeg',
            "ingredients":[
    {'name': ingredient.name, 'amount': ingredient.amount, 'unit': ingredient.unit}
    for ingredient in recipe.ingredients
],
            "recipeDescription":recipe.description
        }
        recipe_array.append(recipe_object)
    print(recipe_array)
    return jsonify(recipe_array=recipe_array)
#     [
#     {
#       recipeName: 'Cheesy Nachos',
#       imagePath: require('../assets/images/nachos-example.jpeg'),
#       ingredients: [
#         { name: 'cheese', amount: '100', unit: 'g' },
#         { name: 'chips', amount: '500', unit: 'g' },
#       ],
#       recipeDescription:"Delicious chips covered in cheese. Baked to perfection."
#     },
#     {
#       recipeName: 'Tasty Burger',
#       imagePath: require('../assets/images/burger.jpeg'),
#       ingredients: [
#         { name: 'cheese', amount: '100', unit: 'g' },
#         { name: 'ground beef', amount: '1', unit: 'kg' },
#       ],
#       recipeDescription:"Damn that is a tasty Burger!"
#     },
#   ];


if __name__ == '__main__':
 
    
    app.run(debug=True)
