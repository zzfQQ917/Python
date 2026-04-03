from datetime import datetime
import random
from car import *
import auth
from info import *
from config import *

class Station:
    def __init__(self):
        self.id = None

    def default_screen(self):
        enter()
        clear()
        print("---------GAS STATION---------")
        print("0. Wait for a vehicle")
        print("1. Refill tanks")
        print("2. Show current status")
        print("3. Go to the next day")
        print('4. sign-in')
        print('5. sign-up')
        print("6. End Game")
        print("7. Car custom")
        print("8. Account management")
        while True:
            try:
                obtainable_option = int(input("\nSelect: "))

                if obtainable_option in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
                    clear()
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
        print(f"Customers handled for today: {load_info(self.id, 'today_num')}")
        print(f"Diesel left: {load_info(self.id, 'diesel_tank')}{fuel_unit['Diesel']}")
        print(f"Gasoline left: {load_info(self.id, 'gasoline_tank')}{fuel_unit['Gasoline']}")
        print(f"Electricity left: {load_info(self.id, 'electric_battery')}{fuel_unit['Electricity']}")
        print(f"Hydrogen left: {load_info(self.id, 'hydrogen_tank')}{fuel_unit['Hydrogen']}")
        print(f"Radioactive left: {load_info(self.id, 'nuclear_reactor')}{fuel_unit['Nuclear']}")
    
    def refill(self):
        print("\nWhich one do you want to refill? ")
        for num, i in enumerate(fuel_types):
            print(f'\n{num}. {i}')

        while True:
            try:
                decision = int(input("\nSelect: "))
                if decision in [0, 1, 2, 3, 4]:
                    clear()
                    break
            except:
                print('\nNumber out of range.')
                continue
            
        discount_ratio = min(max(0, load_info(self.id, 'rating') / 2), 30)
        fuel_name = fuel_types[decision] # Gasoline
        tank_name = tank_field[fuel_name] # 'gasoline_tank'
        tank = load_info(self.id, tank_name)
        default_price = load_info(self.id, price_field[fuel_name]) * 0.9 
        fuel_price = default_price * (1 - discount_ratio / 100)
        def_unit = fuel_unit[fuel_name]
        money = load_info(self.id, 'money')
        

        print(f"\nBased on your rating {load_info(self.id, 'rating')}, the discount ratio is {discount_ratio}% ")
        print(f"The base unit buying price of {fuel_name} for today is $ {default_price} / {def_unit},")
        print(f"so the discount unit buying price will be $ {fuel_price} / {def_unit}")

        while True:
            desired_fuel = int(input(f"\nYou have $ {money}. Amount of {fuel_name} to buy ({def_unit}): "))
            money = load_info(self.id, 'money')
            if desired_fuel * fuel_price <= money:
                print(f"Money: $ {money} -> $ {money - (fuel_price * desired_fuel)} ")
                print(f"{fuel_name} refilled: {tank} {def_unit} -> {tank + desired_fuel} {def_unit}\n")
                adj_money(self.id, money - (fuel_price * desired_fuel))
                adj_tank(self.id, tank_name, desired_fuel)
                break
            else:
                print("\nYou don't have enough money. ")
                continue

    def serve(self):
        import time
        
        def unavailable(rating):
            print("\nCurrently, we are not available for that. ")
            print("Driver: Well, see you then! ")
            print(f"Rating: {rating} -> {rating - 1} ")
            adj_rating(self.id, -1)

        def insufficient(msg, msg2, rating, money, price):
            print(msg)
            print(f"\nMoney: ${money}, Required: ${price} ")
            print(msg2)
            print("Driver: Well, see you then! ")
            print(f"Rating: {rating} -> {rating - 1}\n")
            adj_rating(self.id, -1)
            print()

        print("Waiting...", end='')
        for i in range(3):
            print(".", end='')
        time.sleep(0.3)
        print()
        
        car = DBCar()

        car.printInfo()
        inc_consumer(self.id, 1)

        sudden_serve = random.randint(1, 5)
        
        prompt = {
            'Diesel' : 'Driver: Refill the DEF, please.\nProvide some DEF for free? (costs $50 yet increases rating by 1)',
            'Gasoline' : 'Driver: Refill the engine oil, please.\nProvide some DEF for free? (costs $2000 yet increases rating by 3)',
            'Electricity' : 'Driver: I need a substitute battery, please. \nProvide some battery replacement for free? (costs $4000 yet increases rating by 5)',
            'Hydrogen' : 'Driver: I need a substitue cooler, please. \nProvide some cooler replacement for free? (costs $8000 yet increases rating by 8)',
            'Nuclear' : 'Driver: ...Could you PLEASE get alternaitive for my Arc Reactor? \nProvide some Arc Reactor for free? (costs $25000 yet increases rating by 12)'
        }
        # 20% 확률로 운전자가 서비스를 요구했을 때
        if sudden_serve == 1:
            print(prompt[car.fuel_type])
            print("0. Yes ")
            print("1. No ")
            while True:
                try:
                    checking_approvement = int(input("Select : "))
                    if checking_approvement in [0, 1]:
                        break
                except:
                    print('\nYo cooked')
                    continue

            # 서비스를 요청한 차종이 Diesel일 때
            money = load_info(self.id, 'money')
            rating = load_info(self.id, 'rating')
            
            if car.fuel_type == "Diesel":
                if checking_approvement == 0:
                    # 우리가 서비스를 위한 충분한 돈이 있을 때
                    if load_info(self.id, 'rating') >= 50:
                        print("\nYou provided some DEF for free")
                        # 보유 금액 감소
                        print(f"Money: ${money} -> ${money - 50} ")
                        adj_money(self.id, -50)
                        print("Driver: I'm blessed to have all of these. Thanks!")
                        print(f"Rating: {rating} -> {rating + 1}\n")
                        adj_rating(self.id, 1)

                    else:
                        insufficient("Currently, we are not available for that.", "Owner: Currently, we're not available for that", rating, money, price)

                else:
                    unavailable(rating)

            # 서비스를 요청한 차종이 Gasoline일 때
            elif car.fuel_type == "Gasoline":
                price = 2000
                # 우리가 Yes를 눌렀을 때
                if checking_approvement == 0:
                    # 우리가 서비스를 위한 충분한 돈이 있을 때
                    if money >= price:
                        print("\nYou provided some engine oil for free")
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
                price = 4000
                if checking_approvement == 0:
                    if money >= price:
                        print('\nWe\'re sufficient about replacing your aged/damaged bettery.')
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
                price = 8000
                if checking_approvement == 0:
                    if money >= price:
                        print('\nWe\'re sufficient about replacing your aged/damaged cooler.')
                        print(f'Money : ${money} -> ${money - price}')
                        adj_money(self.id, -price)
                        print("Driver: I really appreciate all of those, I'm quite a lot impressed due to how you engaged!")
                        print(f"Rating: {rating} -> {rating + 8}")
                        adj_rating(self.id, 8)
                        car.cur_fuel = car.capacity
                
                    else:
                        insufficient("You're not suitable for this service! Please get in charge of essential price.", "Owner: Currently, we're not available for that", rating, money, price)
                
                else:
                    unavailable(rating)
            
            elif car.fuel_type == "Nuclear":
                price = 25000
                if checking_approvement == 0:
                    if money >= price:
                        print('\nWe\'re sufficient about replacing your aged/damaged Arc Reactor.')
                        print(f'Money : ${money} -> ${money - price}')
                        adj_money(self.id, -price)
                        print("Driver: OH MY DAYS! This gas station should be highly renowned, even the Nuclear Power Plant couldn't afford this! Literally phenomenal!!!")
                        print(f"Rating: {rating} -> {rating + 12}")
                        adj_rating(self.id, 12)
                        car.cur_fuel = car.capacity
                
                    else:
                        insufficient("You're not suitable for this service! Please get in charge of essential price.", "Driver: Well, I've not anticipated. BUT why you can't guarantee even if it is this intense?!", rating, money, price)
                
                else:
                    unavailable(rating)

        # 80% 확률로 운전자가 주유를 요구했을 때
        else:
            if car.full == True:
                print(f"\nDriver: Please make it full!")
            else:
                print(f"Driver: I'd like {car.needed} {fuel_unit[car.fuel_type]}, please. ")

            rating = load_info(self.id, 'rating')
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
                            print()
                            for num, i in enumerate(fuel_types):
                                print(f'{num}. {i}')
                            while True:
                                try:
                                    choice = int(input('\nEnter a number to select fuel type : '))
                                    if choice in [0, 1, 2, 3, 4]:
                                        break
                                except:
                                    print('\nPlease try again.')
                                    continue
                            cur_method = fuel_types[choice]
                            cur_unit = fuel_unit[cur_method]
                            print(f"\nFuel type changed: {cur_method} ")

                        # 연료 양 바꾸기
                        elif repeated_option == 1:
                            while True:
                                correct_response = input(f"\nEnter 'F' (full), or the amount of {cur_unit}s to fuel: ")

                                # 주유하려고 하는 양이 Full일 때
                                if correct_response == "F":
                                    cur_amount = car.capacity - car.cur_fuel  # Full을 만들기 위한 주유량 계산
                                    print(f"\nFueling method changed: {cur_amount}")
                                    break
                                else:
                                    try:
                                        cur_amount = int(correct_response)
                                        print(f"\nFueling method changed: {cur_amount}{cur_unit}")
                                        break
                                    except:
                                        continue
                        else:
                            break

                # 주유 시작
                elif admin_preference == "1":
                    print("\nChecking the conditions... ")
                    adj_tank(self.id, tank_field[cur_method], cur_amount)

                    overall_price = load_info(self.id, price_field[cur_method])
                    tank = load_info(self.id, tank_field[cur_method])
                    money = load_info(self.id, 'money')
                    rating = load_info(self.id, 'rating')

                    if cur_method != car.fuel_type:
                        print(f"Requested: {car.fuel_type}, Selected: {cur_method} ")
                        print("\nSystem: This is not the right fuel type! ")
                        if car.fuel_type in ["Electricity", "Hydrogen", "Nuclear"]:
                            print("\nA HUGE EXPLOSION OVER THERE!!!")
                            print(f"The gas station crisis in {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} massively affected to local society and officially mentioned by president D.J. Trump...")
                            print("This incident caused via a mischievous, reckless mistake from the worker who blown up all the fuels in gas tank...")
                            print(f"Fuel stored: {tank} -> 0")
                            adj_tank(self.id, tank_field[cur_method], -tank)
                            print()

                        # 평점 변경
                        print(f"Rating: {rating} -> {rating - 5} ")
                        adj_rating(self.id, -5)

                    # 연료 종류는 올바르지만 사용하려는 연료 양 > 주유소 연료 탱크 연료 양
                    elif cur_method == car.fuel_type and tank < cur_amount:
                        print(f"Fuel type: {car.fuel_type}")
                        print(f"Amount of {cur_method} in the tank: {tank}, Tried: {cur_amount} ")
                        print("\nSystem: There's not enough fuel in the tank! ")

                        # 평점 변경
                        print(f"\nRating: {rating} -> {rating - 1} ")
                        adj_rating(self.id, -1)

                    # 현재 차량의 연료통에 채울 수 있는 양보다 더 많은 주유량을 주유하려 할 경우
                    elif cur_amount > car.capacity - car.cur_fuel:
                        print(f"\nFuel type: {car.fuel_type} ")
                        print(f"Maximum amount to fuel: {car.capacity}, Tried: {cur_amount} ")
                        print("\nDriver: Hey, it overflows! Stop right there! You criminal scum!")

                        # 주유량 변경
                        cur_amount = car.capacity - car.cur_fuel

                        # 돈 보유량 변경
                        print(f"\nMoney: ${money} -> ${money + cur_amount * overall_price} ")
                        adj_money(self.id, cur_amount * overall_price)

                        # 탱크 보유량 변경
                        print(f"\n{cur_method}: {tank} -> {tank - (car.capacity - car.cur_fuel)} ")
                        adj_tank(self.id, tank_field[cur_method], -cur_amount)

                        # 평점 변경
                        print(f"\nRating: {rating} -> {rating - 3} ")
                        adj_rating(self.id, -3)

                        # 실제 탱크 보유량 변경
                        if cur_method == "Diesel":
                            self.diesel_tank = tank
                        else:
                            self.gasoline_tank = tank

                    # 연료 종류는 맞으나 요구한 양과 다른 양을 주유할 경우
                    elif cur_method == car.fuel_type and car.needed != cur_amount:
                        print(f"\nFuel type: {car.fuel_type} ")
                        print(f"Requested: {car.needed} {cur_unit}s, Tried: {cur_amount} {cur_unit}s ")
                        print("\nnDriver: Well, not the exact amount, but thanks anyway! ")

                        # 돈 보유량 변경
                        print(f"Money: $ {money} -> $ {money + (overall_price * cur_amount)}")
                        adj_money(self.id, overall_price * cur_amount)

                        # 탱크 보유량 변경
                        print(f"{cur_method}: {tank} {cur_unit}s -> {tank - cur_amount} {cur_unit}s ")
                        adj_tank(self.id, tank_field[cur_method], -cur_amount)

                        # 평점 변경
                        print(f"Rating: {rating} -> {rating - 1}")
                        adj_rating(self.id, -1)

                        # 실제 탱크 보유량 변경
                        if cur_method == "Diesel":
                            self.diesel_tank = tank
                        else:
                            self.gasoline_tank = tank
                        print()
                    else:
                        # 돈 보유량 변경
                        print(f"Money: $ {money} -> $ {money + (cur_amount * overall_price)}")
                        adj_money(self.id, overall_price * cur_amount)

                        # 탱크 보유량 변경
                        print(f"{cur_method}: {tank} {cur_unit}s -> {tank - cur_amount} {cur_unit}s")
                        adj_tank(self.id, tank_field[cur_method], -cur_amount)
                        print(f"\nDriver: Thanks a lot! ")

                        # 평점 변경
                        print(f"Rating: {rating} -> {rating + 1}")
                        adj_rating(self.id, 1)
                        print()
                    break

                # Let go
                else:
                    print("\nCurrently, we are not available for that.")
                    print("Driver: Well, see you then!")

                    # 평점 변경
                    print(f"Rating: {rating} -> {rating - 1}")
                    adj_rating(self.id, -1)
                    break
def main():
    print_station = Station()
    while True:
        selection = print_station.default_screen()
        if selection == 6:
            if not print_station.id:
                print("Log-in is required.")
                continue
            # 보유하고 있는 돈의 양이 5000 이상일 때
            if load_info(print_station.id, 'money')>= 100000:
                print("\n---------Summary--------- ")
                print(f"Rating: {load_info(print_station.id, 'rating')}")
                print(f"Money: ${load_info(print_station.id, 'money')}")
                print(f"Total customers handled: {load_info(print_station.id, 'total_num')}")
                print("-----------------------------")
                print("You win!")
                clear()
            else:
                print("\nYou should have at least $100000 to finish the game.")
                print(f"You have: ${load_info(print_station.id, 'money')}")

        elif selection == 3:
            if load_info(print_station.id, 'today_num') >= 3:
                pass_day(print_station.id)
                print(f"\nDay {load_info(print_station.id, 'day')} finished. ")
                todays_increment = (1 + random.uniform(-0.1, 0.1))
                for num, type in enumerate(fuel_types):
                    unit_price = load_info(print_station.id, price_field[type])
                    print(f"{num}. {type} unit selling price : ${unit_price} -> ${unit_price * todays_increment}")
                    adj_price(print_station.id, price_field[type], todays_increment)
            else:
                print(f"\nYou have to handle at least three customers. ( {print_station.today_num} / 3)")

        elif selection == 2:
            if not print_station.id:
                print("\nLog-in is required.")
                continue
            print_station.print_status()

        elif selection == 1:
            if not print_station.id:
                print("\nLog-in is required.")
                continue
            print_station.refill()

        elif selection == 4:
            if print_station.id:
                print('\nYou\'ve already logged in to the game.')
                continue
            print_station.id = auth.sign_in()

        elif selection == 5:
            if print_station.id:
                print('\nYou\'ve already logged in to the game.')
                continue
            print_station.id = auth.sign_up()
            create_info(print_station.id)
        
        elif selection == 7:
            if not print_station.id:
                print("\nLog-in is required.")
                continue
            add_car()
        
        elif selection == 8:
            if not print_station.id:
                print("\nLog-in is required.")
                continue
            print(print_station.id)
            auth.acc_delete(print_station.id)

        else:
            if not print_station.id:
                print("\nLog-in is required.")
                continue
            print_station.serve()

main()