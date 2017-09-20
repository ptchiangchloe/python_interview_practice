# Here is some starter code for a Flask Web Application. Expand on that and include
# a route that simulates rolling two dice and returns the result in JSON.
# You should include a brief explanation of your code.

from flask import Flask
app = Flask(__name__)

import json
import random

@app.route('/')
def hello_world():
 return 'Hello World!'

@app.route('/roll_dice')
def roll_dice():
    if request.method == "GET":
        dice_1 = random.int(1, 6)
        dice_2 = random.int(1, 6)
        result = {
                'dice_1': dice_1,
                'dice_2': dice_2
            }
        return jsonify(result)

# Create an api that take a GET request and return a json file.

if __name__ == '__main__':
 app.debug = True
 app.run()
