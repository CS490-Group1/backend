from api.model.customer import *
from data.account_storage import store_customer

def create_customer(info):
    new_customer = Customer(info.get("email"), info.get("first_name"), info.get("last_name"), info.get("dob"), info.get("drivers_license"), 
                           info.get("phone"), info.get("password"))
    store_customer(new_customer)
    return new_customer