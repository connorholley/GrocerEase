from flask import Flask, jsonify
from flask_cors import CORS

from database.ControllersAndModels.UserController import UserController
from database.ControllersAndModels.RecipeController import RecipeController



app = Flask(__name__)
CORS(app, origins="http://localhost:5000")  

@app.route('/')
def hello_world():
   
    recipe_controller = RecipeController(environment="production")
    recipe_query = recipe_controller.get_all()
    recipe_array = []

    for recipe in recipe_query:
        ingredients = recipe_controller.get_ingredients_for_recipe(recipe.id)
        recipe_object = {
            "recipeName": recipe.name,
            "imagePath": '../assets/images/nachos-example.jpeg',
            "ingredients": [
                {
                    'name': ingredient.Ingredient.name,
                    'amount': ingredient.RecipeIngredientRelationship.amount,
                    'unit': ingredient.RecipeIngredientRelationship.unit
                }
                for ingredient in ingredients
            ],
            "recipeDescription": recipe.description
        }
        recipe_array.append(recipe_object)

  
    return jsonify(recipe_array=recipe_array)




if __name__ == '__main__':
 
    
    app.run(debug=True)
