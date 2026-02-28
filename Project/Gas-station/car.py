from db import cars
from config import *
import random

class Car:
    # 인스턴스 변수
    def __init__(self, fuel_type, vehicle_type, capacity, cur_fuel, needed, full):
        self.fuel_type = fuel_type  # 연료 종류(가솔린, 전기, 디젤, 수소, 핵융합)
        self.vehicle_type = vehicle_type  # 자동차 종류(트럭, 버스, SUV, 하이브리드)
        self.capacity = capacity  # 연료통 크기
        self.cur_fuel = cur_fuel  # 현재 남은 용량
        self.needed = needed  # 주유 요구 시, 채워달라고 요청하는 연료의 양
        self.full = full  # 주유 요구 시, 연료통을 가득 채워달라고 하는지 여부
        # 메서드
        self.cal_fuel()

    def cal_fuel(self):  # 남은 기름의 양 계산 및 full 여부
        self.cur_fuel = int(self.capacity * random.uniform(0.1, 0.4))
        if random.randint(1, 4) == 1:
            self.full = True
            self.needed = self.capacity - self.cur_fuel
        else:
            self.full = False
            self.needed = ((self.capacity - self.cur_fuel) * random.uniform(0.5,
                                                                            0.8) // 5) * 5

    def printInfo(self):  # 차량 정보 출력
        print("\n<<Vehicle Info>>")
        print(
            f"Fuel type: {self.fuel_type}, Vehicle Type: {self.vehicle_type}, Fuel: {self.cur_fuel} / {self.capacity}")

    def fuel(self):  # 지정한 주유 방식대로 차량에 기름을 넣는 함수
        print("Checking the conditions...")


class Gasoline_Car(Car):
    # 메서드
    def __init__(self, vehicle_type, capacity, cur_fuel, needed, full):
        super().__init__("Gasoline", vehicle_type, capacity, cur_fuel, needed, full)


class Diesel_Car(Car):
    # 메서드
    def __init__(self, vehicle_type, capacity, cur_fuel, needed, full):
        super().__init__("Diesel", vehicle_type, capacity, cur_fuel, needed, full)

    def upgrade_claim(self):  # 업그레이드 요청
        print("Driver: Refill the DEF, please.")
        print("Provide some DEF for free? (costs $50 yet increases rating by 3)")

    def upgrade(self):  # 업그레이드 요청에 응했을 때 실행되는 부분
        print("You provided some DEF for free")


class SUV(Gasoline_Car):
    def __init__(self):
        super().__init__("SUV", 80, 0, 0, False)

    def upgrade_claim(self):  # 업그레이드 요청
        print("Driver: An oil change, please.")
        print("Change the engine oil for free? (costs $100 yet increases rating by 3)")

    def upgrade(self):  # 업그레이드 요청에 응했을 때 실행되는 부분
        print("You replaced the engine oil for free")


class Hybrid(Gasoline_Car):
    def __init__(self):
        super().__init__("Hybrid", 60, 0, 0, False)

    def upgrade_claim(self):  # 업그레이드 요청
        print("Driver: My car has flat tires...")
        print("Change the tires for free? (costs $300 yet increases rating by 3)")

    def upgrade(self):  # 업그레이드 요청에 응했을 때 실행되는 부분
        print("You provided some tires for free")


class Bus(Diesel_Car):
    # 메서드
    def __init__(self):
        super().__init__("Bus", 100, 0, 0, False)


class Truck(Diesel_Car):
    # 메서드
    def __init__(self):
        super().__init__("Truck", 300, 0, 0, False)

def add_car():

    print('########################')
    print('Menu - Adding a brand new car type')
    while True:
        type_name = input('\nEnter the name of adding car type : ')
        if cars.find_one({'type_name' : type_name}):
            print('The car type is already existing.')
            continue

        elif type_name == 'random':
            print('Random is unavailable name for the car type.')
            continue
        else:
            clear()
            break

    for i, fuel in enumerate(fuel_types):
        print(f'{i}. {fuel}')

    while True:
        try:
            dec_fuel = int(input('\nPlease select the fuel type for adding car type in number : '))
            if 0 <= dec_fuel <= len(fuel_types) - 1:
                clear()
                break
            else:
                continue
        except:
            continue
    fuel_type = fuel_types[dec_fuel]
    for k, v in cap_limit.items():
        print('Maximum capacity per fuel types are : ')
        print(f'    {k} - {v}{fuel_unit[k]}')
    
    while True:
        try:
            enter_cap = int(input('\nEnter the capacity of adding car type : '))
            max_cap = cap_limit[fuel_type]
            if enter_cap > max_cap:
                print('\nThe maximum capacity you entered was greater than capacity limit.')
                continue
            else:
                clear()
                break
        except:
            continue
    brand_cat_nums = list(car_book.keys())
    while True:
        print('\nPlease set the brand category of adding car.')
        for i, k in enumerate(brand_cat_nums):
            print(f'\n{i}. {k}')
        try: 
            cat_num = int(input('Choose the brand category of adding car type in number, according to the brand checklist : '))
            if not (0 <= cat_num <= len(brand_cat_nums) - 1):
                continue
            cat_name = brand_cat_nums[cat_num]
            if cat_name == 'Electric Car Brands' and fuel_type != 'Electricity':
                clear()
                print("[!WARNING!] Your fuel type is not electricity! It'll cause a massive incident if you continue and might even take your life!")
                continue
            cat_list = car_book[cat_name]
            print(f'\nChoose the car brands {cat_name}')
            for i, brand in enumerate(cat_list):
                print(f'\n{i}. {brand}')
            brand_num = input('\nEnter the specific brand in number : ')
            if brand_num == 'q':
                print('\nReturning to the category choosing...')
                continue
            elif not (0 <= int(brand_num) <= len(cat_list) - 1):
                continue
            brand_name = cat_list[int(brand_num)]
            clear()
            print(f'\nThe brand of your car type labeled as {brand_name}.')
            break
        except:
            continue
    while True:
        interest = input('Enter the rating interest of car type (Press r to set in random numerals) : ')
        if interest.lower() == 'r':
            print('Using random method.')
            interest = random.randint(1, 6)
            break
        else:
            print('Using integer method.')
            try:
                interest = int(interest)
                break
            except:
                continue

    cars.insert_one({
        'name' : type_name,
        'capacity' : enter_cap,
        'fuel_type' : fuel_type,
        'brand' : brand_name,
        'interest' : interest,
        'load_cnt' : 0
    })
    print('########################')

def load_car(type_name, field = 'all'):
    if type_name == 'random':
        car_types = list(cars.find({}))
        single_ct = random.choice(car_types)
        if field == 'all':
            return single_ct
        else:
            return single_ct[field]
    
    else:
        cars.find_one({
            'name' : 1
        })

def inc_loadcnt(type_name):
    cars.update_one({
        'name' : type_name
    }, {"$inc" : {'load_cnt' : 1}})

class DBCar:
    def __init__(self):
        r_loadcar = load_car('random')
        inc_loadcnt(r_loadcar['name'])
        self.name = r_loadcar['name']
        self.capacity = r_loadcar['capacity']
        self.fuel_type = r_loadcar['fuel_type']
        self.brand = r_loadcar['brand']
        self.interest = r_loadcar['interest']
        self.load_cnt = r_loadcar['load_cnt']
        self.cal_fuel()

    def cal_fuel(self):  # 남은 기름의 양 계산 및 full 여부
        self.cur_fuel = int(self.capacity * random.uniform(0.1, 0.4))
        if random.randint(1, 4) == 1:
            self.full = True
            self.needed = self.capacity - self.cur_fuel
        else:
            self.full = False
            self.needed = ((self.capacity - self.cur_fuel) * random.uniform(0.5,
                                                                            0.8) // 5) * 5
    
    def printInfo(self):  # 차량 정보 출력
        print("\n<<Vehicle Info>>")
        print(
            f"Type name : {self.name} | Fuel type : {self.fuel_type} | Brand : {self.brand} | Fuel : {self.cur_fuel} / {self.capacity} | Interest : {self.interest}")

    def fuel(self):  # 지정한 주유 방식대로 차량에 기름을 넣는 함수
        print("Checking the conditions...")

if __name__ == '__main__':
    DB_Car = DBCar()
    DB_Car.printInfo()