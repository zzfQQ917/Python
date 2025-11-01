import random

class Car:
    def __init__(self, fuel_type, vehicle_type, capacity):
        self.fuel_type = fuel_type
        self.vehicle_type = vehicle_type
        self.capacity = capacity
        self.cal_fuel() 

    def cal_fuel(self):
        self.cur_fuel = int(self.capacity * random.uniform(0.1, 0.4))
        if random.randint(1, 4) == 1:
            self.full = True
            self.needed = self.capacity - self.cur_fuel
        else:
            self.full = False
            self.needed = ((self.capacity - self.cur_fuel) * random.uniform(0.5, 0.8) // 5) * 5 

    def printInfo(self, fuel_type, vehicle_type, fuel_left, capacity, driver_word):
        print("\n<Vehicle Info>")
        print(f"Fuel type: {fuel_type}, Vehicle type: {vehicle_type}, Fuel: {fuel_left} / {capacity} ")
        print(f"Driver: {driver_word}")

    def fuel(self, tried, request):
        print("Checking the conditions...")
        print(f"Requested: {request} Liters, Tried: {tried} Liters ")

class GasolineCar(Car):
    def __init__(self, vehicle_type, capacity):
        super().__init__("Gasoline", vehicle_type, capacity)
        

class SUV(GasolineCar):
    def __init__(self):
        super().__init__("SUV", 80)

class Hybrid(GasolineCar):
    def __init__(self):
        super().__init__("Hybrid", 60)

class Diesel(Car):
    def __init__(self, vehicle_type, capacity):
        super().__init__("Diesel", vehicle_type, capacity)

class Bus(Diesel):
    def __init__(self):
        super().__init__("Bus", 100)

class Truck(Diesel):
    def __init__(self):
        super().__init__("Truck", 300)
    
