import random
from car import *
import auth
from info import *



class Station:
    def __init__(self, day, rating, money, today_num, total_num):
        self.day = day              # 일 수가 넘어갈 때마다 갱신되는 변수
        self.rating = rating        # 평판의 점수
        self.money = money          # 주유소가 자체적으로 보유하고 있는 돈
        self.today_num = today_num  # 오늘의 고객 수
        self.total_num = total_num  # 전체 고객 수
        self.diesel_tank = 100      # 디젤유의 보유량
        self.gasoline_tank = 100    # 가솔린유의 보유량
        self.diesel_price = 10      # 디젤유의 가격
        self.gasoline_price = 15    # 가솔린유의 가격

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
        print(f"Diesel left: {load_info(self.id, 'diesel_tank')} Liters")
        print(f"Gasoline left: {load_info(self.id, 'gasoline_tank')} Liters\n")

    def refill(self):
        '''TODO
        Electricity, Hydrogen(액화수소), Nuclear fuel(플로토늄)도 보충할 수 있게 하기 (car.py에 함수 구현해놨음)
        '''
        print("\nWhich one do you want to refill? ")
        print("0. Diesel")
        print("1. Gasoline")
        while True:
            decision = input("Select: ")
            if decision == "0" or decision == "1":
                break
            else:
                continue
        discount_ratio = min(max(0, load_info(self.id, 'rating') / 2), 30)
        if decision == "0":
            fuel_name = "Diesel"
            tank = load_info(self.id, 'diesel_tank')
            default_price = load_info(self.id, 'diesel_price') * 0.9

        else:
            fuel_name = "Gasoline"
            tank = load_info(self.id, 'gasoline_tank')
            default_price = load_info(self.id, 'gasoline_price') * 0.9

        fuel_price = default_price * (1 - discount_ratio)

        print(f"Based on your rating {load_info(self.id, 'rating')}, the discount ratio is {discount_ratio}% ")
        print(f"The base unit buying price of {fuel_name} for today is $ {default_price} / L,")
        print(f"so the discount unit buying price will be $ {fuel_price} / L")

        while True:
            desired_fuel = int(input(f"\nYou have $ {self.money}. Amount of {fuel_name} to buy (liters): "))
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
            checking_approvement = input("Select : ")
            print()

            # 서비스를 요청한 차종이 Diesel일 때
            money = load_info(self.id, 'money')
            rating = load_info(self.id, 'rating')
            
            if car.fuel_type == "Diesel":
                if checking_approvement == "0":
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
                        print("You don't have enough Money! ")
                        print(f"Money: ${money}, Required: $50 ")
                        print("Owner: Currently, we are not available for that. ")
                        print("Driver: Well, see you then! ")
                        print(f"Rating: {rating} -> {rating - 1}\n")
                        adj_rating(self.id, -1)

                else:
                    print("Owner: Currently, we are not available for that. ")
                    print("Driver: Well, see you then! ")
                    print(f"Rating: {self.rating} -> {self.rating - 1}\n")
                    adj_rating(self.id, -1)

            # 서비스를 요청한 차종이 Gasoline일 때
            elif car.fuel_type == "Gasoline":
                price = 200
                # 우리가 Yes를 눌렀을 때
                if checking_approvement == "0":
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
                        print("You don't have enough Money! ")
                        print(f"Money: ${money}, Required: ${price} ")
                        print("Owner: Currently, we are not available for that. ")
                        print("Driver: Well, see you then! ")
                        print(f"Rating: {rating} -> {rating - 1} ")
                        adj_rating(self.id, -1)

                else:
                    print("Currently, we are not available for that. ")
                    print("Driver: Well, see you then! ")
                    print(f"Rating: {rating} -> {rating - 1} ")
                    adj_rating(self.id, -1)
            
            elif car.fuel_type == "electricity":
                price = 400
                if checking_approvement == '0':
                    if money >= price:
                        print('We\'re sufficient about replacing your aged/damaged bettery.')
                        print(f'Money : ${money} -> ${money - price}')
                        adj_money(self.id, -price)
                        print("Driver: I really appreciate all of those, I'm quite a lot impressed due to how you engaged!")
                        print(f"Rating: {rating} -> {rating + 5}")
                        adj_rating(self.id, 5)
                        car.cur_fuel = car.capacity
                
                    else:
                        print("You're not suitable for this service! Please get in charge of essential price.")
                        print(f'Money: ${money}, Required: ${price}')
                        print(f"Owner: Currently, we're not available for that.")
                        print("Driver: Well, see you then!")
                        print(f"Rating: {rating} -> {rating - 2}")
                        adj_rating(self.id, -2)
            
            '''TODO
            Hydrogen, Nuclear fuel도 서비스 요구할 수 있게 하기
            '''
            
        # 80% 확률로 운전자가 주유를 요구했을 때
        else:
            if car.full == True:
                print(f"Driver: Please make it full!")
            else:
                print(f"Driver: I'd like {car.needed} Liters, please. ")

            '''TODO
            Electricity, Hydrogen, Nuclear fuel도 주유 요구할 수 있게 하기
            리터뿐만 아니라 단위 신경쓰기(config.py에 fuel_unit 불러오기)
            '''
            
            cur_method = "Gasoline"  # 현재 연료의 종류
            cur_liters = 10  # 현재 주유하려는 연료의 양

            while True:
                print("\n0. Change fueling method ")
                print("1. Start fueling ")
                print("2. Let go ")
                admin_preference = input("Select: ")

                # 주유 방식을 변경할 때
                if admin_preference == "0":
                    print(f"\nCurrent Method: {cur_method} / {cur_liters} Liters ")

                    while True:

                        print("\n0. Toggle fuel type ")
                        print("1. Change the amount of fuel")
                        print("2. Finish ")
                        repeated_option = input("Select: ")

                        # 연료 종류 바꾸기
                        if repeated_option == "0":
                            cur_method = "Gasoline" if cur_method == "Diesel" else "Diesel"
                            print(f"\nFuel type changed: {cur_method} ")

                        # 연료 양 바꾸기
                        elif repeated_option == "1":
                            correct_response = input("Enter 'F' (full), or the amount of liters to fuel: ")

                            # 주유하려고 하는 양이 Full일 때
                            if correct_response == "F":
                                cur_liters = car.capacity - car.cur_fuel  # Full을 만들기 위한 주유량 계산
                                print(f"\nFueling method changed: {cur_liters}")
                            else:
                                cur_liters = int(correct_response)
                                print(f"\nFueling method changed: {cur_liters} Liters ")
                        else:
                            break

                # 주유 시작
                elif admin_preference == "1":
                    print("\nChecking the conditions... ")
                    if cur_method == "Diesel":
                        tank = self.diesel_tank
                        overall_price = self.diesel_price
                    else:
                        tank = self.gasoline_tank
                        overall_price = self.gasoline_price

                    # 연료 종류가 잘못된 경우
                    '''TODO
                    Electricity, Hydrogen, Nuclear fuel은 연료 종류나 양이 잘못됐을 때 심각한 부작용이 일어나도록 구현하기
                    '''
                    if cur_method != car.fuel_type:
                        '''TODO
                        DB와 연동하기(돈, 점수, 탱크 보유량 등)
                        '''
                        print(f"Requested: {car.fuel_type}, Selected: {cur_method} ")
                        print("\nSystem: This is not the right fuel type! ")

                        # 평점 변경
                        print(f"Rating: {self.rating} -> {self.rating - 5} ")
                        self.rating -= 5

                    # 연료 종류는 올바르지만 사용하려는 연료 양 > 주유소 연료 탱크 연료 양
                    elif cur_method == car.fuel_type and tank < cur_liters:
                        '''TODO
                        DB와 연동하기(돈, 점수, 탱크 보유량 등)
                        '''
                        print(f"Fuel type: {car.fuel_type}")
                        print(f"Amount of {cur_method} in the tank: {tank}, Tried: {cur_liters} ")
                        print("\nSystem: There's not enough fuel in the tank! ")

                        # 평점 변경
                        print(f"Rating: {self.rating} -> {self.rating - 1} ")
                        self.rating -= 1


                    # 현재 차량의 연료통에 채울 수 있는 양보다 더 많은 주유량을 주유하려 할 경우
                    elif cur_liters > car.capacity - car.cur_fuel:
                        '''TODO
                        DB와 연동하기(돈, 점수, 탱크 보유량 등)
                        '''
                        print(f"Fuel type: {car.fuel_type} ")
                        print(f"Maximum amount to fuel: {car.capacity}, Tried: {cur_liters} ")
                        print("\nDriver: Hey, it overflows! Stop right there! You criminal scum! ")

                        # 주유량 변경
                        cur_liters = car.capacity - car.cur_fuel

                        # 돈 보유량 변경
                        print(f"Money: ${self.money} -> ${self.money + cur_liters * overall_price} ")
                        self.money += cur_liters * overall_price

                        # 탱크 보유량 변경
                        print(f"{cur_method}: {tank} -> {tank - (car.capacity - car.cur_fuel)} ")
                        tank -= cur_liters

                        # 평점 변경
                        print(f"Rating: {self.rating} -> {self.rating - 3} ")
                        self.rating -= 3

                        # 실제 탱크 보유량 변경
                        if cur_method == "Diesel":
                            self.diesel_tank = tank
                        else:
                            self.gasoline_tank = tank

                    # 연료 종류는 맞으나 요구한 양과 다른 양을 주유할 경우
                    elif cur_method == car.fuel_type and car.needed != cur_liters:
                        '''TODO
                        DB와 연동하기(돈, 점수, 탱크 보유량 등)
                        '''
                        print(f"Fuel type: {car.fuel_type} ")
                        print(f"Requested: {car.needed} Liters, Tried: {cur_liters} Liters ")
                        print("\nDriver: Well, not the exact amount, but thanks anyway! ")

                        # 돈 보유량 변경
                        print(f"Money: $ {self.money} -> $ {self.money + (overall_price * cur_liters)}")
                        self.money += overall_price * cur_liters

                        # 탱크 보유량 변경
                        print(f"{cur_method}: {tank} Liters -> {tank - cur_liters} Liters ")
                        tank -= cur_liters

                        # 평점 변경
                        print(f"Rating: {self.rating} -> {self.rating - 1}")
                        self.rating -= 1

                        # 실제 탱크 보유량 변경
                        if cur_method == "Diesel":
                            self.diesel_tank = tank
                        else:
                            self.gasoline_tank = tank

                    else:
                        '''TODO
                        DB와 연동하기(돈, 점수, 탱크 보유량 등)
                        '''
                        # 돈 보유량 변경
                        print(f"Money: $ {self.money} -> $ {self.money + (cur_liters * overall_price)}")
                        self.money += cur_liters * overall_price

                        # 탱크 보유량 변경
                        print(f"{cur_method}: {tank} Liters -> {tank - cur_liters} Liters")
                        tank -= cur_liters

                        print(f"\nDriver: Thanks a lot! ")

                        # 평점 변경
                        print(f"Rating: {self.rating} -> {self.rating + 1}")
                        self.rating += 1

                        # 실제 탱크 보유량 변경
                        if cur_method == "Diesel":
                            self.diesel_tank = tank
                        else:
                            self.gasoline_tank = tank
                    break

                # Let go
                else:
                    print("Currently, we are not available for that.")
                    print("Driver: Well, see you then!")

                    # 평점 변경
                    print(f"Rating: {self.rating} -> {self.rating - 1}")
                    self.rating -= 1
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
                print(
                    f"Gasoline unit selling price: ${print_station.gasoline_price} -> ${print_station.gasoline_price * todays_increment}")
                print(
                    f"Diesel unit selling price: ${print_station.diesel_price_price} -> ${print_station.diesel_price * todays_increment}")
                print_station.gasoline_price *= todays_increment
                print_station.diesel_price *= todays_increment

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