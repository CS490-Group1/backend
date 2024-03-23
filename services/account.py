from api.model.customer import *

def create_customer(info):
    new_customer = Customer(info.get("email"), info.get("first_name"), info.get("last_name"), info.get("dob"), info.get("drivers_license"), 
                           info.get("phone"), info.get("password"))
    return new_customer

def grab_customer(info):
    return None