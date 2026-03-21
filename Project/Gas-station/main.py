import random
from car import *
import auth
from info import *
from config import *

class Station:
    def __init__(self):
        pass
        # self.day = day              # 일 수가 넘어갈 때마다 갱신되는 변수
        # rating = rating        # 평판의 점수
        # money = money          # 주유소가 자체적으로 보유하고 있는 돈
        # self.today_num = today_num  # 오늘의 고객 수
        # self.total_num = total_num  # 전체 고객 수
        # self.diesel_tank = 100      # 디젤유의 보유량
        # self.gasoline_tank = 100    # 가솔린유의 보유량
        # self.diesel_price = 10      # 디젤유의 가격
        # self.gasoline_price = 15    # 가솔린유의 가격

    def default_screen(self):
        print("---------GAS STATION---------")
        print("0. Wait for a vehicle")
        print("1. Refill tanks")
        print("2. Show current status")
        print("3. Go to the next day")
        print('4. sign-in')
        print('5. sign-up')
        '''TODO
        차종 추가하는 메뉴 추가하기 (car.py에 함수 구현해놨음)
        '''
        
        print("6. End Game")
        while True:
            try:
                obtainable_option = int(input("Select: "))

                if obtainable_option in [0, 1, 2, 3, 4, 5, 6]:
                    break
                else:
                    print("\nWrong input! ")
                    continue
            except:
                continue
        return obtainable_option

    def print_status(self):
        print("\n---------STATUS--------- ")
        print(f"Day {load_info(self.id, 'day')}")
        print(f"Rating: {load_info(self.id, 'rating')}")
        print(f"Money: ${load_info(self.id, 'money')}")
        print(f"# Customers handled for today: {load_info(self.id, 'today_num')}")
        print(f"Diesel left: {load_info(self.id, 'diesel_tank')}{fuel_unit['Diesel']}")
        print(f"Gasoline left: {load_info(self.id, 'gasoline_tank')}{fuel_unit['Gasoline']}\n")
        print(f"Electricity left: {load_info(self.id, 'electricity_battery')}{fuel_unit['Electricity']}\n")
        print(f"Hydrogen left: {load_info(self.id, 'hydrogen_tank')}{fuel_unit['Hydrogen']}\n")
        print(f"Radioactive left: {load_info(self.id, 'nuclear_reactor')}{fuel_unit['Nuclear']}\n")
    
    def refill(self):
        '''TODO
        Electricity, Hydrogen(액화수소), Nuclear fuel(플로토늄)도 보충할 수 있게 하기 (car.py에 함수 구현해놨음)
        '''
        print("\nWhich one do you want to refill? ")
        for num, i in enumerate(fuel_types):
            print(f'{num}. {i}')
            
        while True:
            try:
                decision = int(input("Select: "))
                if decision in [0, 1, 2, 3, 4]:
                    break
            except:
                continue
            
        discount_ratio = min(max(0, load_info(self.id, 'rating') / 2), 30)
        fuel_name = fuel_types[decision] # Gasoline
        tank_name = name_tank[fuel_name] # 'gasoline_tank'
        tank = load_info(self.id, tank_name)
        default_price = load_info(self.id, f'{fuel_name.lower()}_price') * 0.9
        fuel_price = default_price * (1 - discount_ratio)

        print(f"Based on your rating {load_info(self.id, 'rating')}, the discount ratio is {discount_ratio}% ")
        print(f"The base unit buying price of {fuel_name} for today is $ {default_price} / L,")
        print(f"so the discount unit buying price will be $ {fuel_price} / L")

        while True:
            desired_fuel = int(input(f"\nYou have $ {money}. Amount of {fuel_name} to buy (liters): "))
            money = load_info(self.id, 'money')
            if desired_fuel * fuel_price <= money:
                print(f"Money: $ {money} -> $ {money - (fuel_price * desired_fuel)} ")
                print(f"Diesel refilled: {tank} Liters -> {tank + desired_fuel} Liters\n")
                adj_money(self.id, money - (fuel_price * desired_fuel))
                if fuel_name == "Diesel":
                    adj_tank(self.id, 'd', desired_fuel)
                else:
                    adj_tank(self.id, 'g', desired_fuel)
                break
            else:
                print("You don't have enough money. ")
                continue

    def serve(self):
        import time
        
        def unavailable(rating):
            print("Currently, we are not available for that. ")
            print("Driver: Well, see you then! ")
            print(f"Rating: {rating} -> {rating - 1} ")
            adj_rating(self.id, -1)

        def insufficient(msg, msg2, rating, money, price):
            print(msg)
            print(f"Money: ${money}, Required: ${price} ")
            print(msg2)
            print("Driver: Well, see you then! ")
            print(f"Rating: {rating} -> {rating - 1}\n")
            adj_rating(self.id, -1)

        print("Waiting...", end='')
        for i in range(3):
            print(".", end='')
        time.sleep(0.3)
        print()
        
        car = DBCar()

        car.printInfo()

        pass_day(self.id)
        load_info(self.id, 'total_num') += 1

        sudden_serve = random.randint(1, 5)

        # 20% 확률로 운전자가 서비스를 요구했을 때
        if sudden_serve == 1:
            print("Driver: Refill the DEF, please.")
            print("Provide some DEF for free? (costs $50 yet increases rating by 3)")
            print("0. Yes ")
            print("1. No ")
            while True:
                try:
                    checking_approvement = int(input("Select : "))
                    if checking_approvement in [0, 1]:
                        break
                except:
                    print('Yo cooked')
                    continue

            # 서비스를 요청한 차종이 Diesel일 때
            money = load_info(self.id, 'money')
            rating = load_info(self.id, 'rating')
            
            if car.fuel_type == "Diesel":
                if checking_approvement == 0:
                    # 우리가 서비스를 위한 충분한 돈이 있을 때
                    if load_info(self.id, 'rating') >= 50:
                        print("You provided some DEF for free")
                        # 보유 금액 감소
                        print(f"Money: ${money} -> ${money - 50} ")
                        adj_money(self.id, -50)
                        print("Driver: I'm blessed to have all of these. Thanks!")
                        print(f"Rating: {rating} -> {rating + 3}\n")
                        adj_rating(self.id, 3)

                    else:
                        insufficient("Currently, we are not available for that.", "Owner: Currently, we're not available for that", rating, money, price)

                else:
                    unavailable(rating)

            # 서비스를 요청한 차종이 Gasoline일 때
            elif car.fuel_type == "Gasoline":
                price = 200
                # 우리가 Yes를 눌렀을 때
                if checking_approvement == 0:
                    # 우리가 서비스를 위한 충분한 돈이 있을 때
                    if money >= price:
                        print("You provided some DEF for free")
                        # 보유 금액 감소
                        print(f"Money: ${money} -> ${money - price} ")
                        adj_money(self.id, -price)
                        print("Driver: I'm blessed to have all of these. Thanks!")
                        print(f"Rating: {rating} -> {rating + 3} ")
                        adj_rating(self.id, 3)

                    else:
                        insufficient("Currently, we are not available for that.", "Owner: Currently, we're not available for that", rating, money, price)

                else:
                    unavailable(rating)
            
            elif car.fuel_type == "Electricity":
                price = 400
                if checking_approvement == 0:
                    if money >= price:
                        print('We\'re sufficient about replacing your aged/damaged bettery.')
                        print(f'Money : ${money} -> ${money - price}')
                        adj_money(self.id, -price)
                        print("Driver: I really appreciate all of those, I'm quite a lot impressed due to how you engaged!")
                        print(f"Rating: {rating} -> {rating + 5}")
                        adj_rating(self.id, 5)
                        car.cur_fuel = car.capacity
                
                    else:
                        insufficient("You're not suitable for this service! Please get in charge of essential price.", "Owner: Currently, we're not available for that", rating, money, price)
                
                else:
                    unavailable(rating)
            
            elif car.fuel_type == "Hydrogen":
                price = 500
                if checking_approvement == 0:
                    if money >= price:
                        print('We\'re sufficient about replacing your aged/damaged cooler.')
                        print(f'Money : ${money} -> ${money - price}')
                        adj_money(self.id, -price)
                        print("Driver: I really appreciate all of those, I'm quite a lot impressed due to how you engaged!")
                        print(f"Rating: {rating} -> {rating + 5}")
                        adj_rating(self.id, 5)
                        car.cur_fuel = car.capacity
                
                    else:
                        insufficient("You're not suitable for this service! Please get in charge of essential price.", "Owner: Currently, we're not available for that", rating, money, price)
                
                else:
                    unavailable(rating)
            
            elif car.fuel_type == "Nuclear":
                price = 1000
                if checking_approvement == 0:
                    if money >= price:
                        print('We\'re sufficient about replacing your aged/damaged Arc Reactor.')
                        print(f'Money : ${money} -> ${money - price}')
                        adj_money(self.id, -price)
                        print("Driver: OH MY DAYS! This gas station should be highly renowned, even the Nuclear Power Plant couldn't afford this! Literally phenomenal!!!")
                        print(f"Rating: {rating} -> {rating + 10}")
                        adj_rating(self.id, 10)
                        car.cur_fuel = car.capacity
                
                    else:
                        insufficient("You're not suitable for this service! Please get in charge of essential price.", "Driver: Well, I've not anticipated. BUT why you can't guarantee even if it is this intense?!", rating, money, price)
                
                else:
                    unavailable(rating)

        # 80% 확률로 운전자가 주유를 요구했을 때
        else:
            if car.full == True:
                print(f"Driver: Please make it full!")
            else:
                print(f"Driver: I'd like {car.needed} {fuel_unit[car.fuel_type]}, please. ")

            '''
            TODO
            Electricity, Hydrogen, Nuclear도 주유 요구할 수 있게 하기
            리터뿐만 아니라 단위 신경쓰기(config.py에 fuel_unit 불러오기)
            '''
            
            cur_method = "Gasoline"  # 현재 연료의 종류
            cur_amount = 10  # 현재 주유하려는 연료의 양
            cur_unit = fuel_unit[cur_method]

            while True:
                print("\n0. Change fueling method ")
                print("1. Start fueling ")
                print("2. Let go ")
                admin_preference = input("Select: ")

                # 주유 방식을 변경할 때
                if admin_preference == "0":
                    print(f"\nCurrent Method: {cur_method} / {cur_amount}{cur_unit}")

                    while True:

                        print("\n0. Toggle fuel type ")
                        print("1. Change the amount of fuel")
                        print("2. Finish ")
                        ans_list = [0, 1, 2]
                        while True:
                            try:
                                repeated_option = int(input("Select: "))
                                if repeated_option in ans_list:
                                    break
                            except:
                                print('Please try again.')
                                continue

                        # 연료 종류 바꾸기
                        if repeated_option == 0:
                            for num, i in enumerate(fuel_types):
                                print(f'{num}. {i}')
                            while True:
                                try:
                                    choice = int(input('Enter a number to select fuel type : '))
                                    if choice in fuel_types:
                                        break
                                except:
                                    print('Please try again.')
                                    continue
                            cur_method = fuel_types[choice]
                            print(f"\nFuel type changed: {cur_method} ")

                        # 연료 양 바꾸기
                        elif repeated_option == 1:
                            correct_response = input("Enter 'F' (full), or the amount of liters to fuel: ")

                            # 주유하려고 하는 양이 Full일 때
                            if correct_response == "F":
                                cur_amount = car.capacity - car.cur_fuel  # Full을 만들기 위한 주유량 계산
                                print(f"\nFueling method changed: {cur_amount}")
                            else:
                                cur_amount = int(correct_response)
                                print(f"\nFueling method changed: {cur_amount}{cur_unit}")
                        else:
                            break

                # 주유 시작
                elif admin_preference == "1":
                    print("\nChecking the conditions... ")
                    
                    adj_tank(self.id, cur_method, cur_amount)
                    overall_price = load_info(self.id, f'{fuel_types[cur_method]}_price')
                    tank = load_info(self.id, name_tank[cur_method])
                    # if cur_method == "Diesel":
                    #     adj_tank(self.id, 'd', cur_amount)
                    #     overall_price = load_info(self.id, 'diesel_price')

                    # 연료 종류가 잘못된 경우
                    '''
                    TODO
                    Electricity, Hydrogen, Nuclear fuel은 연료 종류나 양이 잘못됐을 때 심각한 부작용이 일어나도록 구현하기
                    '''
                    
                    if cur_method != car.fuel_type:
                        print(f"Requested: {car.fuel_type}, Selected: {cur_method} ")
                        print("\nSystem: This is not the right fuel type! ")

                        # 평점 변경
                        print(f"Rating: {rating} -> {rating - 5} ")
                        adj_rating(self.id, -5)

                    # 연료 종류는 올바르지만 사용하려는 연료 양 > 주유소 연료 탱크 연료 양
                    elif cur_method == car.fuel_type and tank < cur_amount:
                        print(f"Fuel type: {car.fuel_type}")
                        print(f"Amount of {cur_method} in the tank: {tank}, Tried: {cur_amount} ")
                        print("\nSystem: There's not enough fuel in the tank! ")

                        # 평점 변경
                        print(f"Rating: {rating} -> {rating - 1} ")
                        adj_rating(self.id, -1)


                    # 현재 차량의 연료통에 채울 수 있는 양보다 더 많은 주유량을 주유하려 할 경우
                    elif cur_amount > car.capacity - car.cur_fuel:
                        print(f"Fuel type: {car.fuel_type} ")
                        print(f"Maximum amount to fuel: {car.capacity}, Tried: {cur_amount} ")
                        print("\nDriver: Hey, it overflows! Stop right there! You criminal scum! ")

                        # 주유량 변경
                        cur_amount = car.capacity - car.cur_fuel

                        # 돈 보유량 변경
                        print(f"Money: ${money} -> ${money + cur_amount * overall_price} ")
                        money += cur_amount * overall_price

                        # 탱크 보유량 변경
                        print(f"{cur_method}: {tank} -> {tank - (car.capacity - car.cur_fuel)} ")
                        adj_tank(self.id, cur_method, -cur_amount)

                        # 평점 변경
                        print(f"Rating: {rating} -> {rating - 3} ")
                        adj_rating(self.id, -3)

                        # 실제 탱크 보유량 변경
                        if cur_method == "Diesel":
                            self.diesel_tank = tank
                        else:
                            self.gasoline_tank = tank

                    # 연료 종류는 맞으나 요구한 양과 다른 양을 주유할 경우
                    elif cur_method == car.fuel_type and car.needed != cur_amount:
                        '''
                        TODO
                        DB와 연동하기(돈, 점수, 탱크 보유량 등)
                        '''
                        print(f"Fuel type: {car.fuel_type} ")
                        print(f"Requested: {car.needed} Liters, Tried: {cur_amount} Liters ")
                        print("\nDriver: Well, not the exact amount, but thanks anyway! ")

                        # 돈 보유량 변경
                        print(f"Money: $ {money} -> $ {money + (overall_price * cur_amount)}")
                        adj_money(self.id, overall_price * cur_amount)

                        # 탱크 보유량 변경
                        print(f"{cur_method}: {tank} Liters -> {tank - cur_amount} Liters ")
                        adj_tank(self.id, cur_method, -cur_amount)

                        # 평점 변경
                        print(f"Rating: {rating} -> {rating - 1}")
                        adj_rating(self.id, -1)

                        # 실제 탱크 보유량 변경
                        if cur_method == "Diesel":
                            self.diesel_tank = tank
                        else:
                            self.gasoline_tank = tank
                    else:
                        # 돈 보유량 변경
                        print(f"Money: $ {money} -> $ {money + (cur_amount * overall_price)}")
                        adj_money(self.id, overall_price * cur_amount)

                        # 탱크 보유량 변경
                        print(f"{cur_method}: {tank} Liters -> {tank - cur_amount} Liters")
                        adj_tank(self.id, cur_method, -cur_amount)
                        print(f"\nDriver: Thanks a lot! ")

                        # 평점 변경
                        print(f"Rating: {rating} -> {rating + 1}")
                        adj_rating(self.id, 1)
                    break

                # Let go
                else:
                    print("Currently, we are not available for that.")
                    print("Driver: Well, see you then!")

                    # 평점 변경
                    print(f"Rating: {rating} -> {rating - 1}")
                    adj_rating(self.id, -1)
                    break
def main():
    print_station = Station(1, 0, 1000, 0, 0)
    while True:
        selection = print_station.default_screen()
        if selection == 6:
            # 보유하고 있는 돈의 양이 5000 이상일 때
            if print_station.money >= 5000:
                print("---------Summary--------- ")
                print(f"Rating: {print_station.rating}")
                print(f"Money: ${print_station.money}")
                print(f"Total customers handled: {print_station.total_num}")
                print("-----------------------------")
                print("You win!")
            else:
                print("You should have at least $5000 to finish the game.")
                print(f"You have: ${print_station.money}")

        elif selection == 3:
            if print_station.today_num >= 3:
                print_station.day += 1
                print(f"Day {print_station.day} finished. ")
                todays_increment = (1 + random.uniform(-0.1, 0.1))
                for num, type in enumerate(fuel_types):
                    unit_price = load_info(print_station.id, f'{type.lower()}_price')
                    print(f"{num}. {type} unit selling price : ${unit_price} -> ${unit_price * todays_increment}")
                    adj_price(print_station.id, f'{type.lower()}_price', todays_increment)
            else:
                print(f"You have to handle at least three customers. ( {print_station.today_num} / 3)")

        elif selection == 2:
            print_station.print_status()

        elif selection == 1:
            print_station.refill()

        elif selection == 4:
            print_station.id = auth.sign_in()

        elif selection == 5:
            print_station.id = auth.sign_up()
            create_info(print_station.id)
        else:
            print_station.serve()


main()