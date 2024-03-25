from services.account import *

def generate_customer(info):
    return create_customer(info)

def challenge_password(info):
    response = authenticate(info)
    return response

def edit_profile(info, user_id):
    return edit_customer(info, user_id)

def edit_password_app(info):
    response = challenge_password(info)
    if(response.status == "Fail"):
        return response
    return edit_password_domain(info)

def get_owned_cars_app(user_id):
    return get_owned_cars_domain(user_id)

def add_owned_car_app(user_id, car_info):
    return add_owned_car_domain(user_id, car_info)