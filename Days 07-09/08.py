cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models
       (original order)"""
    jeep = ''
    for model in cars['Jeep']:
        jeep += model + ', '
    jeep = jeep.strip()
    return jeep[:-1]


def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    return [v[0] for _, v in cars.items()]


def get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    match = []
    for k, v in cars.items():
        for car in v:
            if grep.lower() in car.lower():
                match.append(car)

    match.sort()
    return match


def sort_car_models(cars=cars):
    """return a copy of the cars dict with the car models (values)
       sorted alphabetically"""
    new_cars = dict()
    for k, v in cars.items():
        v.sort()
        new_cars[k] = v

    return new_cars


if __name__ == '__main__':
    print(get_all_jeeps(cars))
    print(get_first_model_each_manufacturer(cars))
    print(get_all_matching_models(cars, grep='TrAiL'))
    print(sort_car_models(cars))
