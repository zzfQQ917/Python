import os
fuel_types = ['Gasoline', 'Diesel', 'Electricity', 'Hydrogen', 'Nuclear']
cap_limit = {
    'Gasoline' : 80,
    'Diesel' : 500,
    'Electricity' : 80,
    'Hydrogen' : 6,
    'Nuclear' : 1000
}
fuel_unit = {
    'Gasoline' : 'L',
    'Diesel' : 'L',
    'Electricity' : 'kWh',
    'Hydrogen' : 'kg',
    'Nuclear' : 'GW'
}

option_fuel = {
    'Gasoline': 'gasoline_price',
    'Diesel': 'diesel_price',
    'Electricity': 'electric_price',
    'Hydrogen': 'hydrogen_price',
    'Nuclear': 'nuclear_price'
}

option_tank = {
    'Gasoline': 'gasoline_tank',
    'Diesel': 'diesel_tank',
    'Electricity': 'electric_battery',
    'Hydrogen': 'hydrogen_tank',
    'Nuclear': 'nuclear_reactor'
}

car_book = {
    'Korean Car Brands': ['KIA', 'Hyundai', 'Renosamsung', 'Ssangyong'],
    'Sport Car Brands' : ['Lamborghini',  'Ferrari', 'Maserati'],
    'Japanese Car Brands' : ['Honda', 'Toyota', 'Nissan', 'Lexus'],
    'Oversea Car Brands' : ['Audi', 'BMW', 'Benz','Volkswagen','Chevrolet', 'Ford', 'Volvo'],
    'Electric Car Brands' : ['Tesla', 'BYD']
}

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

