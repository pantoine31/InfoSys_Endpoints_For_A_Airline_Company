from flask import Flask, request, Response, redirect
import json
from bson.objectid import ObjectId

from flask import jsonify

import pymongo
from pymongo import MongoClient

#arxikopoiisi global metavliton 
#elegxos gia to an einai registered / login oi xristes
#prin opoiadipote energeia

adminHelp = False
userHelp = False

adminName = 'admin@admin.gr'
adminPassword = '123321'


app = Flask(__name__)

client = MongoClient('localhost:27017')

db = client['DigitalAirlines']

usersC = db['usernames']

flightsC = db['flights']

rsvC = db['rsv']


# ENDPOINT FOR WELCOME (same for User - Admin)
@app.route('/welcome', methods=['GET','POST'])
def welcome():
    global adminHelp    
    global userHelp
    adminHelp = False
    userHelp = False
    return "For a new registration the endpoint is /register\n For a new login the endpoint is /login.", 200


# ENDPOINT FOR LOGIN (same for ADMIN - USER)

@app.route('/login', methods=['GET','POST'])
def login():
    
    global userHelp 
    global adminHelp 
    global adminName
    global adminPassword
    
    # Retrieve the data from the request body in postman
    data = request.get_json()

    email = data.get('email')
    password = data.get('password')

    # Check for existing user with this email and password
    existing_user = usersC.find_one({'email': email, 'password': password} )
    
    

    if existing_user:
        userHelp = True
        adminHelp = False
        return redirect('/opt' , code=302)
    elif email==adminName and password == adminPassword:
        adminHelp = True
        return redirect('/optAdmin' , code=302)
    else:
        return 'Email OR password is wrong , please try again' , 400
    
    
    

# !!!!!!!!  !!!!!!!! !!!!!!!! !!!!!!!! 
# !!!!!!!!  !!!!!!!!!!!!!!!!! !!!!!!!!
# ENDPOINTS FOR USERS ONLY    !!!!!!!!
# !!!!!!!!  !!!!!!!! !!!!!!!! !!!!!!!! 
# !!!!!!!!  !!!!!!!!!!!!!!!!! !!!!!!!!


# ENDPOINT FOR REGISTER (User's endpoint)
@app.route('/register', methods=['POST'])
def register():
    
    # take data from the request body in postman
    data = request.get_json()

    # put data from json into variables
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

    return jsonify({'message': 'A new user has been successfully registered! Welcome to our family!', 'New user has user_id': str(result.inserted_id)}), 201



   



# ENDPOINT FOR OPTIONS USER (user's endpoint)
@app.route('/opt', methods=['GET','POST'])
def opt():
    global userHelp 
    global adminHelp 
    
    if userHelp and adminHelp==False:
        return 'Ακολουθεί το μενού επιλογών για έναν απλό Χρήστη:\n\n1. Endpoint για την έξοδο: /exit\n 2. Endpoint για την αναζήτηση πτήσεων: /srch\n 3. Endpoint για την εμφάνιση στοιχείων πτήσης: /det\n 4. Endpoint για την κράτηση εισιτηρίου: /hold\n 5. Endpoint για την εμφάνιση των κρατήσεων: /reserv\n 6. Endpoint για την εμφάνιση στοιχείων κράτησης: /ResDet\n 7. Endpoint για την ακύρωση κράτησης: /canF.\n 8. Endpoint για την διαγραφή του λογαριασμού: /delete', 200
    else:
        return 'You are not a simple user. Register or login as a simple user', 400




# ENDPOINT FOR HOLDING FLIGHTS (only user)
@app.route('/hold/<flight_id>', methods=['POST'])
def hold(flight_id):
    global userHelp
    
    if userHelp:
        # Take data from the request body in Postman
        data = request.get_json()

        # Extract required information from the data
        firstName = data.get('firstName')
        lastName = data.get('lastName')
        passportNumber = data.get('passportNumber')
        dateOfBirth = data.get('dateOfBirth')
        email = data.get('email')
        ticketClass = data.get('ticketClass')

        # Find the flight with the provided flight_id
        flight = flightsC.find_one({'_id': ObjectId(flight_id)})

        if flight:
            # Check if the selected ticket class is available
            if ticketClass == 'business' and flight['availableTicketsB'] > 0:
                # Reduce the available business tickets count by 1
                
                flightsC.update_one({'_id': ObjectId(flight_id)}, {'$set':{'availableTicketsB': (flight['availableTicketsB'] - 1) } })
                
            elif ticketClass == 'economy' and int (flight['availableTicketsE']) > 0:
                
                # Reduce the available economy tickets count by 1
                
                flightsC.update_one({'_id': ObjectId(flight_id)}, {'$set':{'availableTicketsE': int(flight['availableTicketsE']) - 1}})
            else:
                return jsonify({'message': 'Selected ticket class is not available.'}), 400

            # Create a new ticket reservation
            new_reservation = {
                'flight_id': flight_id,
                'name': firstName,
                'surname': lastName,
                'passport_number': passportNumber,
                'birth_date': dateOfBirth,
                'email': email,
                'ticket_class': ticketClass
            }

            # Insert the new reservation into the database
            result = rsvC.insert_one(new_reservation)

            return jsonify({'message': 'Ticket reservation successful!', 'reservation_id': str(result.inserted_id)}), 200
        else:
            return jsonify({'message': 'Flight not found.'}), 404
    else:
        return 'Login/Register as simple user first', 400
    


# ENDPOINT FOR SEARCHING FLIGHTS (only user)
@app.route('/srch', methods=['GET','POST'])
def srch():
    global userHelp
    

    if userHelp:
        # Retrieve data from the request
        data = request.get_json()

        # Retrieve search criteria
        airport_from = data.get('airportFrom')
        airport_to = data.get('airportTo')
        flight_date = data.get('flightDate')

        # Create the search query
        baseSearch = {}

        if airport_from and airport_to and flight_date:
            baseSearch = {'airportFrom': airport_from, 'airportTo': airport_to, 'flightDate': flight_date}
        elif airport_from and airport_to:
            baseSearch = {'airportFrom': airport_from, 'airportTo': airport_to}
        elif flight_date:
            baseSearch = {'flightDate': flight_date}
        else:
            baseSearch = {}

        # Perform the search in the database
        flights = flightsC.find(baseSearch)

        # Prepare the response
        flight_list = []
        for flight in flights:
            flight_data = {
                '_id': str(flight['_id']),
                'flightDate': flight['flightDate'],
                'airportFrom': flight['airportFrom'],
                'airportTo': flight['airportTo']
            }
            flight_list.append(flight_data)

        return jsonify({'flights': flight_list}), 200
    else:
        return jsonify({'message': 'Please log in as an simple user first.'}), 401  
    
    


# ENDPOINT FOR DETAILS OF FLIGHTS (only user)
@app.route('/det/<flight_id>', methods=['GET','POST'])
def det(flight_id):
    global userHelp 
   

    if userHelp:
        # Find the flight in the database by its ID
        flight = flightsC.find_one({'_id': ObjectId(flight_id)})

        if flight:

            # Extract flight details
            flight_data = {
                'flightDate': flight['flightDate'],
                'airportFrom': flight['airportFrom'],
                'airportTo': flight['airportTo'],
                'availableTicketsB': flight['availableTicketsB'],
                'costB': flight['costB'],
                'availableTicketsE': flight['availableTicketsE'],
                'costE': flight['costE']
            }

            return jsonify({'flight': flight_data}), 200
        else:
            return jsonify({'message': 'Flight not found.'}), 404
    else:
        return jsonify({'message': 'Please log in as an simple user  first.'}), 401
    
    
# ENDPOINT FOR SHOWING RESEVATIONS  (only user)
@app.route('/reserv/<email>', methods=['GET','POST'])
def reserv(email):
    global userHelp 
    
    if userHelp:
    
        # Find the reservations for the specified user_id
        reservations = rsvC.find({'email': email})
        

        if reservations:
            
        # Prepare the response
            rsv_list = []
            for r in reservations:
                rsv_data = {
                    '_id': str(r['_id']),
                    'flight_id': (r['flight_id']),
                    'name': (r['name']),
                    'surname': (r['surname']) ,
                    'passport_number': (r['passport_number']),
                    'birth_date': (r['birth_date']),
                    'email': (r['email']),
                    'ticket_class':  (r['ticket_class'])
                }
                rsv_list.append(rsv_data)

            return jsonify({'Reservations': rsv_list}), 200
        
        else:
            return 'No reservations for this email' , 404
    else:
        return 'Login as a simple user first', 400


# ENDPOINT FOR SHOWING DETAILS OF RESERVATION
@app.route('/ResDet/<reservation_id>', methods=['GET','POST'])
def ResDet(reservation_id):
    global userHelp 
    global adminHelp 
    
    if userHelp:
        # Find the reservation
        reservation = rsvC.find_one({'_id': ObjectId(reservation_id)})
        
        
        list = []
        
        if reservation:

            # Extract flight details
            data = {
                'name': reservation['name'],
                'surname': reservation['surname'] ,
                'passport_number':reservation['passport_number'],
                'birth_date': reservation['birth_date'],
                'email': reservation['email'],
                'ticket_class': reservation['ticket_class']
            }
        

            list.append(data)

            return jsonify({'Reservation details': list}), 200
    
    
    else:
        return "Login/Register as user First." , 400
    




# ENDPOINT FOR CANCELING RESERVATION
@app.route('/canF/<reservation_id>', methods=['GET','POST'])
def canF(reservation_id):
    global userHelp 
    
    
    if userHelp:
           # Find the reservation
            reservation = rsvC.find_one({'_id': ObjectId(reservation_id)})
            if reservation:
                # Get the flight ID from the reservation
                flight_id = reservation['flight_id']
                ticket_class = reservation['ticket_class']
            
                # Update the available tickets count for the flight based on the ticket class
                if ticket_class == 'business':
                    flightsC.update_one({'_id': ObjectId(flight_id)}, {'$inc': {'availableTicketsB': 1}})
                elif ticket_class == 'economy':
                    flightsC.update_one({'_id': ObjectId(flight_id)}, {'$inc': {'availableTicketsE': 1}})
            
                # Delete the reservation
                
                rsvC.delete_one({'_id': ObjectId(reservation_id)})
                
                return jsonify({'message': 'Ticket cancellation successful.'}), 200
            
            else:
                return jsonify({'message': 'Reservation not found.'}), 404
            
    else:
        return "Login/Register as user First." , 400

# ENDPOINT FOR DELETE ACCOUNT
@app.route('/delete/<user_id>', methods=['GET','POST'])
def delete(user_id):
    global userHelp 
    
    if userHelp:
    
        user = usersC.find_one({'_id': ObjectId(user_id)})
        if user:
            # Delete the user account from the 'usernames' collection
            usersC.delete_one({'_id': ObjectId(user_id)})
            return jsonify({'message': 'Account deleted successfully.'}), 200
        else:
            return jsonify({'message': 'User not found.'}), 404
    else:
        return 'Login or Register as user first' , 400









 


# !!!!!!!!  !!!!!!!! !!!!!!!! !!!!!!!! 
# !!!!!!!!  !!!!!!!!!!!!!!!!! !!!!!!!!
# ENDPOINTS FOR ADMIN ONLY    !!!!!!!!
# !!!!!!!!  !!!!!!!! !!!!!!!! !!!!!!!! 
# !!!!!!!!  !!!!!!!!!!!!!!!!! !!!!!!!!

# ENDPOINT FOR ADMIN OPTIONS
@app.route('/optAdmin', methods=['GET','POST'])
def opta():
    global userHelp 
    global adminHelp 
    
    if adminHelp:
        return 'Ακολουθεί το μενού επιλογών για τον διαχειριστή του συστήματος:\n\n1. Endpoint για την έξοδο: /exit\n 2. Endpoint για τη δημιουργία πτήσης: /create\n 3. Endpoint για την ανανέωση τιμών: /price\n 4. Endpoint για τη διαγραφή πτήσης: /delFlight\n 5. Endpoint για αναζήτηση πτήσεων: /searchFlights\n 6. Endpoint για εμφάνιση στοιχείων πτήσεων: /Details\n' , 400
    else:
        return 'login as admin First' , 400 





# ENDPOINT FOR Create new flight
@app.route('/create', methods=['GET','POST'])
def create():
    global userHelp 
    global adminHelp 
    
    
    if adminHelp:
        
        # take data from the request body in postman
        data = request.get_json()

        # put data from json into variables
        airportFrom = data.get('airportFrom')
        airportTo = data.get('airportTo')
        flightDate = data.get('flightDate')
        availableTicketsB = data.get('availableTicketsB')
        costB = data.get('costB')
        availableTicketsE = data.get('availableTicketsE')
        costE = data.get('costE')


        
        # Create a new flight
        new_flight = {
            'airportFrom': airportFrom,
            'airportTo': airportTo,
            'flightDate': flightDate,
            'availableTicketsB': availableTicketsB,
            'costB': costB,
            'availableTicketsE': availableTicketsE,
            'costE': costE
        }

        # Insert the new user into the database
        result2 = flightsC.insert_one(new_flight)

        return jsonify({'message': 'A new flight has been successfully created!', 'New flights id is': str(result2.inserted_id)}), 201

    else:
        return "Login as admin First.", 400
    
    
    
# ENDPOINT FOR UPDATE PRICES
@app.route('/price/<flight_id>', methods=['GET','POST'])
def price(flight_id):
    global userHelp 
    global adminHelp 
    
    if adminHelp:
        # Λαμβάνουμε τα δεδομένα από το json
        data = request.get_json()

        # Λαμβάνουμε το νέο κόστος των εισιτηρίων από το json
        new_cost_b = data.get('costB')
        new_cost_e = data.get('costE')

        # Update the costs in the database for the specific flight
        flightsC.update_one({'_id': ObjectId(flight_id)}, {'$set': {'costB': new_cost_b, 'costE': new_cost_e}})

        return jsonify({'message': 'Το κόστος των εισιτηρίων ενημερώθηκε με επιτυχία.'}), 200
    
    
    else:
        return "Login as admin First." , 400
    
    
    
# ENDPOINT FOR DELETING FLIGHTS
@app.route('/delFlight/<flight_id>', methods=['GET','POST'])
def delFlight(flight_id):
    
    global adminHelp 
    
  
    
    if adminHelp:
    
        f = flightsC.find_one({'_id': ObjectId(flight_id)})
        if f:
            # Delete the flight from the 'flights' collection
            flightsC.delete_one({'_id': ObjectId(flight_id)})
            return jsonify({'message': 'Flight deleted successfully.'}), 200
        else:
            return jsonify({'message': 'Flight not found.'}), 404
    else:
        return 'Login or Register as admin first' , 400
    
    
    
# ENDPOINT FOR SEARCHING FLIGHTS
@app.route('/searchFlights', methods=['GET','POST'])
def searchFlights():
    global adminHelp
  

    if adminHelp:
        # Retrieve data from the request
        data = request.get_json()

        # Retrieve search criteria
        airport_from = data.get('airportFrom')
        airport_to = data.get('airportTo')
        flight_date = data.get('flightDate')

        # Create the search query
        baseSearch = {}

        if airport_from and airport_to and flight_date:
            baseSearch = {'airportFrom': airport_from, 'airportTo': airport_to, 'flightDate': flight_date}
        elif airport_from and airport_to:
            baseSearch = {'airportFrom': airport_from, 'airportTo': airport_to}
        elif flight_date:
            baseSearch = {'flightDate': flight_date}
        else:
            baseSearch = {}

        # Perform the search in the database
        flights = flightsC.find(baseSearch)

        # Prepare the response
        flight_list = []
        for flight in flights:
            flight_data = {
                '_id': str(flight['_id']),
                'flightDate': flight['flightDate'],
                'airportFrom': flight['airportFrom'],
                'airportTo': flight['airportTo']
            }
            flight_list.append(flight_data)

        return jsonify({'flights': flight_list}), 200
    else:
        return jsonify({'message': 'Please log in as an admin first.'}), 401    
    
    
# ENDPOINT FOR SEARCHING DETAILS OF FLIGHTS
@app.route('/Details/<flight_id>', methods=['GET','POST'])
def Details(flight_id):
   
    global adminHelp 
    
    if adminHelp:
            # Find the reservation
            fl = flightsC.find_one({'_id': ObjectId(flight_id)})
            
            
            list = []
            
            if fl:

                # Extract flight details
                data = {
                    'airportFrom': fl['airportFrom'],
                    'airportTo': fl['airportTo'] ,
                    'flightDate':fl['flightDate'],
                    'availableTicketsB': fl['availableTicketsB'],
                    'availableTicketsE': fl['availableTicketsE'],
                    'costB': fl['costB'],
                    'costE': fl['costE']
                }
            

                list.append(data)

                return jsonify({'Flight details': list}), 200
        
        
    else:
        return "Login/Register as admin First." , 400
    

# ENDPOINT FOR EXIT  (same for USER - ADMIN)

@app.route('/exit', methods=['POST'])
def e():
    
   global adminHelp 
   adminHelp = False
   
   global userHelp
   userHelp = False
   
  
   return redirect('/welcome' , code=302)

# my flask app running from here
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
 
