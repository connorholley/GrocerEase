import os
import json

def load_config( environment):
    # Get the directory of the current script
    current_dir = os.path.dirname(os.path.realpath(__file__))
    config_path = os.path.join(current_dir, 'database-config.json')
    
    with open(config_path, 'r') as config_file:
        config_data = json.load(config_file)
        return config_data.get(environment)