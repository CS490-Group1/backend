from services.cars import display_all_cars_domain

def display_all_cars_app():
    return display_all_cars_domain()

def add_car_app(info):
    return create_car(info, 0)