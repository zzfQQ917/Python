import random


class Car:
    # 인스턴스 변수
    def __init__(self, fuel_type, vehicle_type, capacity, cur_fuel, needed, full):
        self.fuel_type = fuel_type  # 연료 종류(가솔린, 디젤)
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


class Station:
    def __init__(self, day, rating, money, today_num, total_num):
        self.day = day
        self.rating = rating
        self.money = money
        self.today_num = today_num
        self.total_num = total_num
        self.diesel_tank = 100
        self.gasoline_tank = 100
        self.diesel_price = 10
        self.gasoline_price = 15

    def default_screen(self):
        print("---------GAS STATION---------")
        print("0. Wait for a vehicle")
        print("1. Refill tanks")
        print("2. Show current status")
        print("3. Go to the next day")
        print("4. End Game")
        while True:
            obtainable_option = input("Select: ")

            if obtainable_option in ["1", "2", "3", "4"]:
                break
            else:
                print("Wrong input! ")
                continue
        return obtainable_option

    def print_status(self):
        print("---------STATUS--------- ")
        print(f"Day {self.day}")
        print(f"Rating: {self.rating}")
        print(f"Money: $ {self.money}")
        print(f"# Customers handled for today: {self.today_num}")

    def refill(self):
        print("Which one do you want to refill? ")
        print("0. Diesel")
        print("1. Gasoline")
        while True:
            decision = input("Select: ")
            if decision == "0" or decision == "1":
                break
            else:
                continue
        discount_ratio = min(max(0, self.rating / 2), 30)
        if decision == "0" or "1":
            fuel_name = "Diesel"
            default_price = self.diesel_price * 0.9

        else:
            fuel_name = "Gasoline"
            default_price = self.gasoline_price * 0.9

        fuel_price = default_price * (1 - discount_ratio)

        print(f"Based on your rating {self.rating}, the discount ratio is {discount_ratio}% ")
        print(f"The base unit buying price of {fuel_name} for today is $ {default_price} / L,")
        print(f"so the discount unit buying price will be $ {fuel_price} / L")

        while True:
            desired_fuel = int(input(f"You have $ {self.money}. Amount of diesels to buy (liters): "))

            if desired_fuel * fuel_price <= self.money:
                print(f"Money: $ {self.money} -> $ {self.money - fuel_price * desired_fuel} ")
                print(f"Diesel refilled: {self.diesel_tank} Liters -> {self.diesel_tank + desired_fuel} Liters ")
                break
            else:
                print("You don't have enough money. ")
                continue

    def serve(self):
        import time
        print("Waiting...", end='')
        for i in range(3):
            print(".", end='')
        time.sleep(0.3)
        print()

        car_type = random.randint(1, 6)

        if car_type == 1:
            car = SUV()
        elif car_type == 2:
            car = Hybrid()
        elif car_type == 3 or car_type == 4:
            car = Truck()
        else:
            car = Bus()

        car.printInfo()
        if car.full == True:
            print(f"Driver: Please make it full!")
        else:
            print(f"Driver: I'd like {car.needed} Liters, please. ")

        cur_method = "Diesel"
        cur_liters = "10"

        while True:
            print("\n0. Change fueling method ")
            print("1. Start fueling ")
            print("2. Let go ")
            admin_preference = input("Select: ")
            if admin_preference == "0":
                print(f"\nCurrent Method: {cur_method} / {cur_liters} Liters ")
                while True:
                    print("\n0. Toggle fuel type ")
                    print("1. Change the amount of fuel")
                    print("2. Finish ")
                    repeated_option = input("Select: ")
                    if repeated_option == "0":
                        cur_method = "Gasoline" if cur_method == "Diesel" else "Diesel"
                        print(f"\nFuel type changed: {cur_method} ")
                    elif repeated_option == "1":
                        correct_response = input("Enter 'F' (full), or the amount of liters to fuel: ")
                        if correct_response == "F":
                            cur_liters = "Full"
                            print(f"\nFueling method changed: {cur_liters}")
                        else:
                            cur_liters = int(correct_response)
                            print(f"\nFueling method changed: {cur_liters} Liters ")
                    else:
                        break

            elif admin_preference == "1":
                pass


print_station = Station(1, 0, 100000000, 0, 0)
print_station.serve()