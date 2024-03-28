from api.model.customer import Customer
from api.model.password import Password
from services.cars import create_car
from data.account_storage import *
from data.alchemy_classes import *
import random, string, re

def create_customer(info):
    new_customer = Customer(info.get("email"), info.get("first_name"), info.get("last_name"), info.get("dob"), info.get("drivers_license"), 
                           info.get("phone"), info.get("password"))
    new_cust_id = store_customer(new_customer)
    if(new_cust_id == False):
        return {
            'status': 'fail',
            'message': 'Email already exists'
        }
    return {
        'status': 'success',
        'message': 'Successfully created',
        'cust_id': new_cust_id
    }

def edit_customer(info, user_id):
    update_customer = Customer(info.get("email"), info.get("first_name"), info.get("last_name"), info.get("dob"), info.get("drivers_license"), 
                           info.get("phone"))
    change_customer(update_customer, user_id)
    return {
        'status': 'success',
        'message': 'Successfully changed profile'
    }

def verify_drivers_license_domain(info):
    pattern = r'^[A-Z]{1,2}\d{9}$'
    if re.match(pattern, info):
        return {
            'status': 'success',
            'message': 'Valid Driver\'s License'
        }
    else:
        return {
            'status': 'fail',
            'message': 'Invalid Driver\'s License'
        }

def authenticate(info):
    stored_password = grab_customer(info.get("email"))
    for password in stored_password:
        challenge_password = {
            "password":password.password,
            "salt":password.salt
        }

    sent_password = Password(info.get("email"), info.get("password"), challenge_password["salt"])
    if(stored_password):
        if(sent_password.password == challenge_password["password"]):
            return {
                'status': 'success',
                'email': info.get("email"),
                'message': 'Logged in successfully'
            }
        else:
            return {
                'status': 'fail',
                'message': 'Incorrect password'
            }
    else:
        return {
            'status': 'fail',
            'message': 'Email does not exist'
        }

def edit_password_domain(info):
    new_password = Password(info.get("email"), info.get("new_password"))
    change_password(new_password)
    return {
        'status': 'success',
        'message': 'Successfully changed password'
    }

def grab_password(email):
    stored_password = grab_customer(email)
    for password in stored_password:
        challenge_password = {
            "email":email,
            "password":password.password,
            "new_password":''.join(random.choice(string.ascii_letters + string.digits + "!@#$%^&*()")
                                    for _ in range(20))
        }
    return challenge_password
    
def get_owned_cars_domain(user_id):
    cars = []
    cars_table = get_owned_cars(user_id)
    for car in cars_table:
        car_json = {
            "car_id":car.car_id,
            "make":car.make,
            "model": car.model,
            "year": car.year,
            "color": car.color,
            "type": car.type,
            "mpg": float(car.mpg) if car.mpg is not None else None,
            "image": car.image
        }
        cars.append(car_json)
    return cars

def add_owned_car_domain(user_id, car_info):
    car_id = create_car(car_info, available=1)
    add_owned_car_data(user_id, car_id)
    return {
        'status': 'success',
        'message': 'Successfully created new owned'
    }