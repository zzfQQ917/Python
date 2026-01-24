from DB import cars
from config import fuel_types

def add_car():

    print('########################')
    print('Menu - Adding a brand new car type')
    while True:
        type_name = input('Enter the name of adding car type')
        if cars.find_one({'type_name' : type_name}):
            continue
        else:
            break

    for i, fuel in enumerate(fuel_types):
        print(f'{i}. {fuel}')

    while True:
        try:
            dec_fuel = int(input('Please select the fuel type for adding car type in number : '))
            if dec_fuel >= 0 and dec_fuel <= len(fuel_types) - 1:
                break
            else:
                continue
        except:
            continue
    fuel_type = fuel_types[dec_fuel]

    
    print('########################')