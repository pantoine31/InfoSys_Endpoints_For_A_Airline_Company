from flask import Flask, request, Response
import json

from flask import jsonify

import pymongo
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')

db = client['DigitalAirlines']
users_collection = db['usernames']

flights_collection = db['flights']

rvts_collection = db['rsv']

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
    existing_user = users_collection.find_one({'email': email})
    if existing_user:
        return jsonify({'Message': 'User with the same email already exists. Try for an other email.'}), 400

    # Check for existing user with the same username
    existing_user = users_collection.find_one({'username': username})
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
    result = users_collection.insert_one(new_user)

    return jsonify({'message': 'A new user has been successfully registered! Welcome to our family!', 'New user has user_id': str(result.inserted_id)}), 200
# η συνεχεια αυριο
if __name__ == '__main__':
 app.run(debug=True, host='0.0.0.0', port=5000)
 
 #terma to terma , savvato simera