from flask import Flask, request, Response, redirect
import json

from flask import jsonify

import pymongo
from pymongo import MongoClient

#arxikopoiisi global metavliton 
#elegxos gia to an einai registered / login oi xristes
#prin opoiadipote energeia

adminHelp = False
loginHelp = False



app = Flask(__name__)

client = MongoClient('localhost:27017')

db = client['DigitalAirlines']
usersC = db['usernames']

flightsC = db['flights']

rsvC = db['rsv']



@app.route('/welcome', methods=['POST'])
def welcome():
    # Retrieve the data from the request body
    
    return "Welcome to Digital Airlines! Type /login for login or /register for register"






@app.route('/register', methods=['POST'])
def register():
    # Retrieve the data from the request body
    data = request.get_json()

    # Extract the parameters from the data
    username = data.get('username')
    last_name = data.get('last_name')
    email = data.get('email')
    password = data.get('password')
    date_of_birth = data.get('date_of_birth')
    country = data.get('country')
    passport_number = data.get('passport_number')

    # Check for existing user with the same email
    existing_user = usersC.find_one({'email': email})
    if existing_user:
        return jsonify({'Message': 'User with the same email already exists. Try for an other email.'}), 400

    # Check for existing user with the same username
    existing_user = usersC.find_one({'username': username})
    if existing_user:
        return jsonify({'Message': 'Username is already in Use. Try with an other Username.'}), 400

    # Create a new user
    new_user = {
        'username': username,
        'last_name': last_name,
        'email': email,
        'password': password,
        'date_of_birth': date_of_birth,
        'country': country,
        'passport_number': passport_number
    }

    # Insert the new user into the database
    result = usersC.insert_one(new_user)

    return jsonify({'message': 'A new user has been successfully registered! Welcome to our family!', 'New user has user_id': str(result.inserted_id)}), 200



# my flask app running from here
if __name__ == '__main__':
 app.run(debug=True, host='0.0.0.0', port=5000)
 
 