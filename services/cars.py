from data.car_storage import get_available_cars


def display_all_cars_domain():
    cars = []
    cars_table = get_available_cars()
    for car in cars_table:
        car_json = {
            "car_id":car.car_id,
            "make":car.make,
            "model": car.model,
            "year": car.year.isoformat() if car.year else None,
            "color": car.color,
            "available": car.available,
            "type": car.type,
            "mpg": float(car.mpg) if car.mpg is not None else None,
            "image": car.image
        }
        cars.append(car_json)
    return cars