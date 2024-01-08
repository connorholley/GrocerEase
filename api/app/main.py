from flask import Flask, jsonify
from flask_cors import CORS

from database.ControllersAndModels.RecipeController import RecipeController
from database.ControllersAndModels.Models import Recipe



app = Flask(__name__)
CORS(app, origins="http://localhost:5000")  

@app.route('/')
def hello_world():
    recipe_controller = RecipeController(environment="production")
   
    
    

    # Get recipes that contain these ingredients
    list_of_ingredients_in_pantry= ["true", "false"]

    recipe_query = recipe_controller.get_recipes_with_ingredients(list_of_ingredients_in_pantry)

    recipe_array = []

    for recipe in recipe_query:
        recipe_ingredients = recipe_controller.get_ingredients_for_recipe(recipe.id)
        print(recipe_ingredients)
        ingredients_list = []

        for ingredient in recipe_ingredients:
            ingredient_data = {
                'name': ingredient['name'],
                'amount': ingredient['amount'],  # Include amount from the relationship
                'unit': ingredient['unit']       # Include unit from the relationship
            }
            ingredients_list.append(ingredient_data)

        recipe_object = {
            "recipeName": recipe.name,
            "imagePath": '../assets/images/nachos-example.jpeg',
            "ingredients": ingredients_list,
            "recipeDescription": recipe.description
        }
        recipe_array.append(recipe_object)

    return jsonify(recipe_array=recipe_array)




if __name__ == '__main__':
 
    
    app.run(debug=True)
