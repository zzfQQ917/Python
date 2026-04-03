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

price_field = {
    'Gasoline': 'gasoline_price',
    'Diesel': 'diesel_price',
    'Electricity': 'electricity_price',
    'Hydrogen': 'hydrogen_price',
    'Nuclear': 'nuclear_price'
}

tank_field = {
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

def enter():
    while True:
        print("\nPress enter to continue...")
        enter = input("")
        if enter == "":
            import platform
            if platform.system() == 'Linux' or platform.system() == 'Darwin':
                os.system('clear')
            else:   
                os.system('cls')
            break

