from api.model.car import Car
from data.car_storage import store_car, get_available_cars


def display_all_cars_domain():
    cars = []
    cars_table = get_available_cars()
    for car in cars_table:
        car_json = {
            "car_id":car.car_id,
            "make":car.make,
            "model": car.model,
            "year": car.year,
            "color": car.color,
            "available": car.available,
            "type": car.type,
            "mpg": float(car.mpg) if car.mpg is not None else None,
            "image": car.image
        }
        cars.append(car_json)
    return cars

def create_car(info, available=1):
    new_car = Car(info.get("make"), info.get("model"), info.get("year"), info.get("color"), info.get("type"), 
                  info.get("mpg"), 0 if info.get("price") is None else info.get("price"), available, info.get("image"))
    new_car_id = store_car(new_car)
    return {
        'status': 'success',
        'message': 'Successfully created',
        'car_id': new_car_id
    }