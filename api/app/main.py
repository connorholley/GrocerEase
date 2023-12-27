from flask import Flask, jsonify
from flask_cors import CORS
from database.ControllersAndModels.UserController import UserController

app = Flask(__name__)
CORS(app, origins="http://localhost:5000")  

@app.route('/')
def hello_world():
    # user_controller = UserController("production")
    # recipe_name=user_controller.get_user_recipes_by_id(1)[0].name
    # return jsonify(message=recipe_name)
    return jsonify(message="test message" )

if __name__ == '__main__':
 
    
    app.run(debug=True)
