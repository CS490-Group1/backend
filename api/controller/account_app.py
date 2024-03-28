from services.account import *
import json

def generate_customer(info):
    drivers_license = info.get("drivers_license")
    if drivers_license is not None:
        response = verify_drivers_license_app(drivers_license)
        if(response["status"] == "success"):
            return create_customer(info)
        else: return response
    

def challenge_password(info):
    response = authenticate(info)
    return response

def edit_profile(info, user_id):
    drivers_license = info.get("drivers_license")
    if drivers_license is not None:
        response = verify_drivers_license_app(drivers_license)
        if(response["status"] == "success"):
            return edit_customer(info, user_id)
        else: return response
    else:
        return edit_customer(info, user_id)

def edit_password_app(info):
    response = challenge_password(info)
    if(response["status"] == "Fail"):
        return response
    return edit_password_domain(info)

def forgot_password_app(email):
    info = json.loads(json.dumps(grab_password(email)))
    response = edit_password_app(info)
    if(response["status"] == "Fail"):
        return response
    return {
        'status':'success',
        'message':'Successfully Forgot Password',
        'new_password':info.get("new_password")
    }

def verify_drivers_license_app(info):
    return verify_drivers_license_domain(info)

def get_owned_cars_app(user_id):
    return get_owned_cars_domain(user_id)

def add_owned_car_app(user_id, info):
    add_owned_car_domain(user_id, info)
    return None