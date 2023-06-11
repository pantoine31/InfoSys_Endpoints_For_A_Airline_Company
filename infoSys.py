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


# ENDPOINT FOR WELCOME
@app.route('/welcome', methods=['GET','POST'])
def welcome():
    global adminHelp    
    global loginHelp
    adminHelp = False
    loginHelp = False
    return "For a new registration the endpoint is /register. <br/> For a new login the endpoint is /login."





# ENDPOINT FOR REGISTER
@app.route('/register', methods=['POST'])
def register():
    
    # Retrieve the data from the request body in postman
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


# ENDPOINT FOR LOGIN

@app.route('/login', methods=['GET','POST'])
def login():
    
    global loginHelp 
    
    # Retrieve the data from the request body in postman
    data = request.get_json()

    email = data.get('email')
    password = data.get('password')

    # Check for existing user with this email and password
    existing_user = usersC.find_one({'email': email, 'password': password} )
    
    if existing_user:
        
        loginHelp = True
        return redirect('/opt' , code=302)
    else:
        return 'Email OR password is wrong , please try again'


# ENDPOINT FOR OPTIONS
@app.route('/opt', methods=['GET','POST'])
def opt():
    global loginHelp 
    
    if loginHelp:
        return 'ALL OPTIONS ARE HERE'
    else:
        return 'Login or Register first'




# ENDPOINT FOR EXIT

@app.route('/exit', methods=['POST'])
def e():
    
   global adminHelp 
   adminHelp = False
   
   global loginHelp
   loginHelp = False
   
  
   return redirect('/welcome' , code=302)


















# my flask app running from here
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
 
 