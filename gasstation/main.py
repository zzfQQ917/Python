from car import *
import random
import math 
import os
import time
import sys
from mathquestion import *
import threading
import msvcrt  # Windows용 (mac은 별도 대체 코드 필요)
import module
#클래스

# 텍스트를 천천히 타이핑하듯 출력하는 함수
def type_text(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# 색상 코드 (터미널 지원 시)
class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    CYAN = '\033[96m'
    YELLOW = '\033[93m'
    MAGENTA = '\033[95m'
    RESET = '\033[0m'


class Station: 
    # 인스턴스 변수
    def __init__(self): 
        self.day = 0
        self.rating = 1
        self.money = float(500.00)
        self.today_num = 0 
        self.total_num = 0 
        self.customer = 0
        self.diesel = 0
        self.gasoline = 0
        self.selling_price = float(10.00)
        self.loaned = False
        self.gun = False
        self.ammo = 0
        self.armor = 0 #내구도
        self.rader = 00 #내구도
        self.loan_safer = 0 #1.1배 or 1.2배

    # 메서드 
    def state_update(self, day, rating, money, today_num):
        self.day += day
        self.rating += rating
        self.money += money
        self.today_num += today_num
        self.total_num += today_num


    def refill(self):
        print("어떤 연료를 보충하시겠습니까?")
        print("0. Diesel")
        print("1. Gasoline") 
        select = module.input_int(0, 1, "선택: ", "잘못된 입력입니다!")
        if select == 0:
            fuel_print = "Diesel"
            orginal_fuel = self.diesel
        elif select == 1:
            fuel_print = "Gasoline"
            self.selling_price = float(15.00)
            orginal_fuel = self.gasoline

        discount_rate = min(max(0, self.rating/2), 30)
        price = self.selling_price * 0.9
        final_price = price * (1 - (discount_rate / 100))

        print(f"당신의 평판 {self.rating}을(를) 기준으로, 할인율은 {discount_rate}% 입니다.")
        print(f"오늘의 {fuel_print} 기본 단가: ${price},\n\
따라서 할인 적용 단가는 ${final_price} 입니다.")
        print()
        buy_amount = module.input_int(1, 999999999999, f"현재 잔액은 ${self.money}입니다. 구매할 {fuel_print}의 양(L)을 입력하세요: ", "잘못된 입력입니다")
        if buy_amount * final_price > self.money:
            print("돈이 부족합니다.")
            module.enter()
        else:
            orginal_money = self.money
            self.money -= buy_amount * final_price
            print(f"돈: ${orginal_money} -> ${self.money}")
            if select == 0:
                self.diesel += buy_amount
                print(f"{fuel_print} 보충 완료: {orginal_fuel}L -> {self.diesel}L")
            elif select == 1:
                self.gasoline += buy_amount  
                print(f"{fuel_print} 보충 완료: {orginal_fuel}L -> {self.gasoline}L")  
            module.enter()

    def print_status(self):
        print("-----현재 상태-----")
        print(f"{self.day}일차")
        print(f"평판: {self.rating}")
        print(f"잔액: ${self.money}")
        print(f"오늘 응대한 손님 수: {self.today_num}")
        print(f"남은 Diesel: {self.diesel} 리터")
        print(f"남은 Gasoline: {self.gasoline} 리터")
        print('총 보유중' if self.gun else '총 없음')
        module.enter()
        print(f'남은 총알 갯수: {self.ammo}')
        print(f'남은 방탄복 내구도: {self.armor}')
        print(f'남은 레이더 내구도: {self.rader}')

    def default_screen(self):

        print("-----주유소-----")
        print("0. 차량을 기다린다")
        print("1. 연료 탱크를 보충한다")
        print("2. 현재 상태 보기")
        print("3. 다음 날로 넘어간다")
        print("4. 상점으로 간다")
        print("5. 도박장으로 간다")
        print("6. 게임 종료")

        select = module.input_int(0, 6, "선택: ", "잘못된 입력입니다!")
        os.system('cls')
        return select

    def timing_game(self, bpm=200, length=7, target_index=3):
        """
        []가 좌우로 움직이며 플레이어가 타이밍에 맞춰 키를 누르면
        성공(True) 또는 실패(False)를 반환
        """
        beat_duration = 60 / bpm  # 속도 조절
        pos = 0
        direction = 1
        self.success = False

        print("🎯 타이밍 게임 시작!")
        print("[]가 중앙에 올 때 아무 키나 누르세요!")
        print("--------------------------------")
        time.sleep(1)

        while True:
            module.clear()

            # 문자열 구성
            line = []
            for i in range(length):
                if i == pos:
                    line.append("[a]")
                else:
                    line.append("a")
            print(" ".join(line))
            print(f"현재 위치: {pos+1}/{length} | 정답 위치: {target_index+1}")
            print("(타이밍 맞춰 키를 누르세요!)")

            # 키 입력 감지
            if msvcrt.kbhit():
                msvcrt.getch()  # 입력 소비
                if pos == target_index:
                    print("\n✅ PERFECT! 타이밍 정확함!")
                    self.success = True
                else:
                    print("\n❌ MISS! 타이밍 빗나감!")
                time.sleep(1)
                break

            # 위치 이동 (양쪽 끝에서 반사)
            pos += direction
            if pos >= length - 1:
                direction = -1
            elif pos <= 0:
                direction = 1

            time.sleep(beat_duration)

        module.clear()


    def ending_credit():
        module.clear()
        print("\n" * 5)
        type_text(f"{Color.CYAN}===== GAME STAFF ====={Color.RESET}", 0.07)
        time.sleep(1)

        credits = [
            ("기획", "윤지후"),
            ("메인코드", "윤지후"),
            ("서브코드", "문요준"),
            ("Gamble 함수", "ChatGPT"),
            ("타이밍 게임", "서승환 & ChatGPT"),
            ("테스터", "윤지윤 & 윤지후")
        ]

        for role, name in credits:
            type_text(f"{Color.YELLOW}{role:<15}{Color.RESET}: {Color.GREEN}{name}{Color.RESET}", 0.04)
            time.sleep(0.4)

        print()
        time.sleep(1)
        type_text(f"{Color.MAGENTA}Thank you for playing.{Color.RESET}", 0.07)
        time.sleep(0.7)
        print()
        type_text(f"{Color.RED}Ending 1: Bad Ending...{Color.RESET}", 0.1)
        time.sleep(2)
        print("\n" * 3)
        type_text(f"{Color.CYAN}게임을 종료합니다.{Color.RESET}", 0.07)
        time.sleep(1.5)
        module.clear()
        time.sleep(1.5)
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        sys.exit()


    def serve(self): 
        self.fueling_method = 'Diesel'
        self.fueling_amount = 10
        self.method_condition = False
        self.fueling_condition = False
        print("차량을 기다리는 중...", end='', flush=True)  # flush 추가
        for _ in range(random.randint(1, 10)):
            print(".", end='', flush=True)
            time.sleep(1)
        print()

        car= random.choice([SUV(), Hybrid(), Bus(), Truck()])
        refuel = module.chance(80)
        service = module.chance(20)
        while True:
            print("<<차량 정보>>")
            print(f"연료 종류: {random.choice(['Gasoline', 'Diesel'])}, 차량 종류: {random.choice(['SUV', 'Hybrid', 'BUS', 'Truck'])}, 연료량: {car.cur_fuel} / {random.choice(['60', '80', '100', '300'])}")
            if refuel:
                if car.full:
                    print("운전자: 가득 채워주세요!")
                else:
                    print(f"운전자: {car.needed}리터만 넣어주세요.")
            if service:
                print(f"")
            print()
            print('0. Change fueling method')
            print('1. Start fueling')
            print('2. Let go ')
            print('3. 아이템을 사용한다.')
            select = module.input_int(0, 3, 'Select:', '잘못된 입력입니다.')
            if select == 0:
                print(f'Current Method: {self.fueling_method} / {self.fueling_amount} 리터.')
                
                print()

                while True:
                    print('0. Toggle fuel type')
                    print('1. Change the amount of fuel')
                    print('2. Finish')
                    select = module.input_int(0, 2, 'Select:', '잘못된 입력입니다.')
                    if select == 0:
                        if self.fueling_method == 'Diesel':
                            self.fueling_method = 'Gasoline'
                        else:
                            self.fueling_method = 'Diesel'
                        print(f'Fuel type changed: {self.fueling_method}')
                        module.enter()
                    if select == 1:
                        if self.fueling_method == 'Gasoline':
                            fuel_type = self.gasoline
                        else:
                            fuel_type = self.diesel
                        select = module.input_all(1, fuel_type, "Enter 'F' (full), or the amount of liters to fuel: ", '잘못된 입력입니다.', ['f', 'F'])                    
                        if select == 'f' or select == 'F':
                            print('Fueling method changed: Full')
                            self.fueling_amount = car.needed
                            module.enter()
                        else:
                            print(f'Fueling method changed: {select}')
                            self.fueling_amount = select
                            module.enter()
                    if select == 2:
                        break
            
            elif select == 1:
                print('Checking the conditions...')
                time.sleep(3)
                if car.fuel_type == self.fueling_method:
                    self.method_condition = True
                if car.needed == self.fueling_amount:
                    self.fueling_condition = True
                if self.method_condition == True and self.fueling_condition == True:
                    steal = module.chance(30)
                    if steal == False:
                        if self.method_condition == 'Gasoline':
                            self.cur_money = self.money
                            self.money += self.fueling_amount * self.selling_price
                            self.cur_gasline = self.gasoline
                            self.gasoline -= self.fueling_amount
                            self.cur_rating = self.rating
                            self.rating += 1
                            print(f'Money: ${self.cur_money} -> {self.money}')
                            print(f'Gasoline: {self.cur_gasline} -> {self.gasoline}')
                            print()
                            print(f'driver: Thanks a lot!')
                            print(f'Rating: {self.cur_rating} -> {self.rating}')
                            module.enter()
                            break
                        else:
                            self.cur_money = self.money
                            self.money += self.fueling_amount * self.selling_price
                            self.cur_diesel = self.diesel
                            self.diesel -= self.fueling_amount
                            self.cur_rating = self.rating
                            self.rating += 1
                            print(f'Money: ${self.cur_money} -> {self.money}')
                            print(f'Gasoline: {self.cur_diesel} -> {self.diesel}')
                            print()
                            print(f'driver: Thanks a lot!')
                            print(f'Rating: {self.cur_rating} -> {self.rating}')
                            module.enter()
                            break
                    else:
                        if self.fueling_method == 'Gasoline':
                            self.cur_gasline = self.gasoline
                            self.gasoline -= self.fueling_amount
                            print(f'Driver: Do you think i will pay?')
                            time.sleep(0.5)
                            print(f'System: The dirver ran away. ')
                            print(f'Gasoline {self.cur_gasline} -> {self.gasoline}')
                            module.enter()
                            break
                        else:
                            self.cur_diesel = self.diesel
                            self.diesel -= self.fueling_amount
                            print(f'Driver: Do you think i will pay?')
                            time.sleep(0.5)
                            print(f'System: The dirver ran away. ')
                            print(f'Gasoline {self.cur_diesel} -> {self.diesel}')
                            module.enter()
                            break                      

                elif self.method_condition != True or self.fueling_amount != True:
                    self.shoot = module.chance(40)
                    self.cur_rating = self.rating
                    self.rating -= 5
                    if self.shoot == True:
                        print(f'Requsted: {car.fuel_type}, Selected: {self.fueling_method}')
                        print(f'Requested: {car.needed}, Tried: {self.fueling_amount}')
                        print()
                        time.sleep(0.5)
                        print(f'System: The Driver is angry, pls prepare for a fight.')
                        if self.gun == True and self.ammo > 0:
                            time.sleep(2)
                            module.clear()
                            Station.timing_game(self)
                            if self.success == True:
                                time.sleep(2)
                                print(f'System: 반격에 성공했습니다.')
                                print(f'차주가 사망하였습니다.')
                                module.enter()
                                break
                            else:
                                time.sleep(2)
                                print(f'System: 반격에 실패하였습니다.')
                                print(f'System: 사망하셨습니다.')
                                time.sleep(3)
                                Station.ending_credit()
                        else:
                            time.sleep(5)
                            module.clear()
                            print(f'Requsted: {car.fuel_type}, Selected: {self.fueling_method}')
                            print(f'Requested: {car.needed}, Tried: {self.fueling_amount}')
                            time.sleep(1)
                            print(f'Driver is angry.')
                            time.sleep(0.5)
                            print(f'Driver: Die!!')
                            time.sleep(1)
                            print(f'System: you had shot by the driver.')
                            time.sleep(0.3)
                            print(f'System: Your are died.')
                            time.sleep(3)
                            module.clear()
                            Station.ending_credit()




                    else:
                        print(f'Requsted: {car.fuel_type}, Selected: {self.fueling_method}')
                        print(f'Requested: {car.needed}, Tried: {self.fueling_amount}')
                        print()
                        time.sleep(0.5)
                        print(f'System: This is not the right fuel type!')
                        print(f'Rating {self.cur_rating} -> {self.rating}')
                        module.enter()
                        break            

                elif self.fueling_amount > car.needed: 
                    explos = module.chance(50)
                    if explos == False:
                        shoot = module.chance(40)
                    else:
                        print(f'Fuel type: {car.fuel_type}')
                        print(f'maximum amount to fuel: {car.needed} Liters, Tried: {self.fueling_amount} Liters')                    
                        time.sleep(0.5)
                        print(f'System: 자동차가 연로 과다 주입으로 폭발했습니다.')
                        time.sleep(0.5)
                        Station.ending_credit()
                    if shoot == True:
                        print('System: dirver is angry, but...')
                        time.sleep(3)
                        print('개발 안함 귀찮음')
                        module.enter()
                        break
                    else:
                        self.cur_money = self.money
                        self.money += (self.selling_price * car.needed) / 2
                        self.cur_rating = self.rating
                        self.cur_gasline -= self.gasoline
                        self.gasoline -= car.needed
                        print(f'Fuel type: {car.fuel_type}')
                        print(f'maximum amount to fuel: {car.needed} Liters, Tried: {self.fueling_amount} Liters')
                        print()
                        time.sleep(0.3)
                        print(f'Driver: Hey, it overflows! Stop there!')
                        print(f'Money: {self.cur_money} * {self.money}')
                        print(f'Gasoline')

            elif select == 2:
                shoot = module.chance(40)
                if shoot == True:
                    print('Driver: What did you said! not avaible?!')
                    time.sleep(0.3)
                    print('Driver: I will kill you')
                    time.sleep(0.3)
                    print(f'System: The Driver is angry, pls prepare for a fight.')
                    if self.gun == True and self.ammo > 0:
                        time.sleep(2)
                        module.clear()
                        Station.timing_game(self)
                        if self.success == True:
                            time.sleep(2)
                            print(f'System: 반격에 성공했습니다.')
                            print(f'차주가 사망하였습니다.')
                            module.enter()
                        else:
                            time.sleep(2)
                            print(f'System: 반격에 실패하였습니다.')
                            print(f'System: 사망하셨습니다.')
                            time.sleep(3)
                            Station.ending_credit()
                else:
                    self.cur_rating = self.rating
                    self.rating -= 1
                    print('Owner: Currently, we are not avaible for that.')
                    print('Driver: Well, see you then!')
                    print(f'Rating {self.cur_rating} -> {self.rating}')
                    module.enter()
                    break
            elif select == 3:
                if self.rader > 0:
                    select = module.input_int(0, 1, '차량 감지기를 사용하시려면 1번, 취소하려면 0번을 눌러주세요.', '잘못된 입력입니다.')
                    if select == 0:
                        module.enter()
                    else:
                        self.rader -= 1
                        print('System: 차량 감지기를 사용합니다.')
                        time.sleep(0.2)
                        print('사용중...')
                        time.sleep(3)
                        print(f"연료 종류: {car.fuel_type}, 차량 종류: {car.vehicle_type}, 연료량: {car.cur_fuel} / {car.capacity}")
                        print(f'pls rember the information or else you could use the item again.')
                        module.enter()


        
    def shop(self): 
        self.name1 = random.choice(['김원혁', '윤지윤', '김도혁', '윤지후', '전설의 용사 문요준', '희대의 사기꾼 노상천이 아닌 김원혁', '마왕 윤지윤', '거룩한 광휘 문요준', '순수한 악 윤지윤', '악의 정수 김도혁', '마신 한유리', '찬란한 빚 윤지후'])
        self.name2 = random.choice(['김원혁', '윤지윤', '김도혁', '윤지후', '전설의 용사 문요준', '희대의 사기꾼 노상천이 아닌 김원혁', '마왕 윤지윤', '거룩한 광휘 문요준', '순수한 악 윤지윤', '악의 정수 김도혁', '마신 한유리', '찬란한 빚 윤지후'])
        print('블랙 마켓에 오신걸 환영합니다. ')
        print('블랙 마켓에 오신걸 환영합니다. ')
        print('내부에서 일어나는 불상사는 저희 블랙마켓이 책임지지 않음을 알려드립니다. ')
        module.enter()
        select = module.input_int(1, 2, '총기상점으로 갈려면 1번, 특수 상점 2번을 선택해주세요: ', '잘못된 입력입니다.')
        print(f'tip: {random.choice(['truck은 디젤 차량입니다.', '총기상은 정신이 온전치 못합니다. 꼭 주의 하세요.', '블랙마켓의 모든 상점주들은 정신이 온전치 못합니다.', 'rpg는 방탄복을 찢어.'])}')
        if select == 1:
            print(f'총기상 {self.nam1}: 총기상점에 온걸 환영하네. ')
            ammo_price = random.choice(list(math_problems.keys())) 
            ammo_price_ans = math_problems[ammo_price]
            gun_price = random.choice(list(math_problems.keys())) 
            gun_price_ans = math_problems[ammo_price]
            print(f'현재 총알 가격은 {ammo_price}입니다.')
            print(f'현재 총 가격은 {gun_price}입니다.')
            buy = module.input_int(1,2, '총알 구매를 원하시면 1번, 총기 구매를 원하시면 2번을 선택해주세요: ', '잘못된 입력입니다.')
            if buy == 1:
                buy_ammount = module.input_int(1, 9999999999999999999999999, '구매할 양을 입력하세요: ', '잘못된 입력입니다.')
                steal = module.chance(30)
                buy_price = ammo_price_ans * buy_ammount
                pay = module.input_int(1, 9999999999999999999999, '지불할 금액을 정하시오 잔돈은 없습니다. 현명하게 선택하세요.', '잘못된 입력입니다.')
                if steal == False:
                    if pay < buy_price:
                        time.sleep(1)
                        module.clear()
                        print(f'총기상 {self.name1}: 돈이 부족하잖아!!!!!!!!!!!! 죽여버리겠다.')
                        time.sleep(1)
                        print('탕 *이거 rpg임 ㅅㄱ')
                        time.sleep(2)
                        print('사망하셨습니다.')
                        module.enter()
                        Station.ending_credit()
                    else:
                        self.money -= buy_price
                        self.ammo += buy_ammount
                        print(f'총기상 {self.name1}: 구매해 주셔서 감사합니다.')
                        module.enter()
                        
                else:
                    print('니 돈은 내거다. 이걸 속노.')
                    time.sleep(3)
                    for _ in range(50):
                        print('lol')
                        time.sleep(0.3)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        time.sleep(0.3)
                    self.money -= pay

            else:
                pay = module.input_int(1, 9999999999999999999999, '지불할 금액을 정하시오 잔돈은 없습니다. 현명하게 선택하세요.', '잘못된 입력입니다.')
                steal = module.chance(60)
                buy_price = gun_price_ans
                if steal == False:
                    if pay < buy_price:
                        time.sleep(1)
                        module.clear()
                        print(f'총기상 {self.name1}: 돈이 부족하잖아!!!!!!!!!!!! 죽여버리겠다.')
                        time.sleep(1)
                        print('탕 *이거 유탄발사기임 ㅅㄱ')
                        time.sleep(2)
                        print('사망하셨습니다.')
                        module.enter()
                        Station.ending_credit()
                    else:
                        self.money -= buy_price
                        self.gun = True
                        print(f'총기상 {self.name1}: 구매해 주셔서 감사합니다.')
                        module.enter()
                        
                else:
                    print('니 돈은 내거다. 이걸 속노.')
                    time.sleep(3)
                    for _ in range(50):
                        print('lol')
                        time.sleep(0.3)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        time.sleep(0.3)
                    self.money -= pay

        else:
            print(f'특수상점주 {self.name2}: 특수상점에 온 걸 환영하네. ')
            rader_price = random.choice(list(math_problems.keys())) 
            rader_price_ans = math_problems[rader_price]
            time.sleep(1)
            select = module.input_int(0, 1, '차량 감지기를 구매하고 싶으면 1번, 취소하려면 0번을 타이핑 해주세요.', '잘못된 입력입니다.')
            if select == 0:
                module.enter()
            else:
                print(f'오늘의 차량 감지기 가격은 {random.choice(rader_price)}입니다.')
                pay = module.input_int(0, self.money, '지불할 금액을 선택하세요. 잔돈은 없습니다 신중히 선택하세요.', '잘못된 입력입니다.')
                if pay < rader_price_ans:
                    print(f'특수 상점주: 돈이 부족하잖아.')
                    time.sleep(0.2)
                    print('탕 *이거 유탄 발사기임 ㅅㄱ')
                    time.sleep(0.7)
                    print('System: 사망하셨습니다.')
                    time.sleep(5)
                    Station.ending_credit
                else:
                    print('특수 상점주: 구매해주셔서 감사합니다.')
                    self.rader += 1
                    self.money -= self.payback
                    module.enter()
            

    def gamble(self):
        print("도박장에 오신 것을 환영합니다.")
        self.payback = True
        self.steal = False
        if self.loaned == True:
            select = module.input_int(1, 2, '돈을 갚기 원하시면 1번, 도박을 원하시면 2번을 적어주세요.', '잘못된 입력입니다.')
            module.enter()
        else:
            select = module.input_int(1, 2, '대출을 원하시면 1번, 도박을 원하시면 2번을 적어주세요.', '잘못된 입력입니다.')
            module.enter()
        if select == 1 and self.loaned == False:
            self.loan_amount = module.input_int(1000, 100**(self.rating+1), "대출 받을 금액을 적어주세요. *최소치 1000달러: ", "범위 밖입니다.")
            print("30일 안에 돈을 갚지 않을시 일어날 불상사는 개인의 상상에 맡기겠습니다. 꼭 돈을 제시간안에 갚아주세요.")
            self.loaned = True
            self.payback = False
            self.money += self.loan_amount
            self.time_left = 30
            module.enter()
        elif select == 1 and self.loaned == True:
            self.steal = module.chance(30)
            if self.steal == True and self.money > self.loan_amount:
                print("돈을 도둑 맞았습니다.")
                time.sleep(1)
                print('돈을 다시 갚으싶시오.')
                self.money -= self.loan_amount
                module.enter()
            else:
                print('돈을 갚습니다.')
                time.sleep(1)
                if self.money >= self.loan_amount and self.time_left > 0:
                    self.money -= self.loan_amount
                    self.payback = True
                    self.loaned = False
                    print('돈을 정상적으로 갚았습니다.')
                    module.enter()
                elif self.money < self.loan_amount:
                    print('돈이 부족합니다.')
                    module.enter()
                elif self.time_left <= 0:
                    print('약속되 시간이 지났습니다. 돈을 3배로 내시면 살려 드립니다.')
                    module.enter()
                    if self.money >= self.loan_amount * 3:
                        self.money -= self.loan_amount * 3
                        self.payback = True
                        self.loaned = False
                        print('돈을 정상적으로 갚았습니다.')
                        module.enter()
                    else:
                        print("돈을 갚지 못하여 사망하였습니다.")
                        module.enter()
                        Station.ending_credit()
                        
        else:
            def clear():
                os.system('cls' if os.name == 'nt' else 'clear')

            def roulette_effect(result_value):
                slots = ['x0', 'x1', 'x2', 'x3', 'x4', 'x5']
                total_spins = random.randint(40, 70)  # 전체 회전 수 (랜덤)
                index = 0

                print("🎰 룰렛이 시작됩니다...\n")
                time.sleep(1)

                for i in range(total_spins):
                    clear()

                    # 속도 제어 (가속 → 감속)
                    if i < total_spins * 0.2:
                        sleep_time = 0.03  # 빠르게
                    elif i < total_spins * 0.7:
                        sleep_time = 0.07  # 일정 속도
                    else:
                        sleep_time = 0.15 + (i - total_spins * 0.7) * 0.015  # 감속

                    print("🎡 룰렛이 돌고 있습니다...\n")

                    for j, slot in enumerate(slots):
                        if j == index:
                            print(f">>> {slot} <<<")
                        else:
                            print(f"    {slot}")

                    sys.stdout.flush()
                    time.sleep(sleep_time)
                    index = (index + 1) % len(slots)

                # 마지막 칸을 결과칸으로 설정
                clear()
                print("🎯 결과가 결정되었습니다!\n")
                time.sleep(0.5)

                # 슬로우 모션 결과 강조
                for _ in range(4):
                    clear()
                    print("\n\n\n")
                    print(f"      >>> {result_value} <<<")
                    time.sleep(0.3)
                    clear()
                    time.sleep(0.2)

                print(f"🏆 최종 결과: {result_value}\n")

            def gamble():
                print("""도박 확률:
                x0: 31%
                x1: 31%
                x2: 21%
                x3: 11%  
                x4: 4%
                x5: 2%
                """)

                module.enter()
                
                gamble_chance = random.randint(0, 100)
                gamble_info = {
                    (0, 31): 0,
                    (32, 62): 1,
                    (63, 83): 2,
                    (84, 94): 3,
                    (95, 98): 4,
                    (99, 100): 5
                }
                for key, value in gamble_info.items():
                    if key[0] <= gamble_chance <= key[1]:
                        result = f"x{value}"
                        roulette_effect(result)
                        return value
                    
            time_stay = 0
            # 🔽 이 부분만 기존 "for _ in range(180)" 구간 대신 추가
            def start_timer():
                global time_stay
                time_stay = 0
                for _ in range(180):  # 3분 카운트
                    time_stay += 1
                    time.sleep(1)

            # 💥 타이머를 스레드로 실행
            timer_thread = threading.Thread(target=start_timer, daemon=True)
            timer_thread.start()
            # 🔼 여기까지가 추가된 부분


            while True:
                while True:
                    self.betting_money = module.input_int(100, 99999999999999, '베팅할 금액을 입력하세요. *최소 금액은 100달러입니다, 나가려면 101을 입력해주세요: ', '보유한 금액을 초과하였습니다.')
                    if self.betting_money <= self.money:
                        self.money -= self.betting_money
                        break
                    elif self.betting_money == 101:
                        break

                if time_stay >= 180:
                    print('롤렛에서 안비켜! 3분동안 뭘하는거야')
                    time.sleep(1.5)
                    print('삥 뜯겼습니다. 돈의 절반이 증발했습니다.')
                    self.money *= 0.5
                    module.enter()
                    break
                elif self.betting_money == 101:
                    module.clear()
                    break

                bet = self.betting_money
                multiplier = gamble()
                final_money = bet * multiplier
                print(f"\n💰 배팅금: ${bet}")
                print(f"💥 배율: x{multiplier}")
                print(f"🏆 결과 금액: ${final_money}")
                module.enter()
                self.money += final_money

    def price_udate(self):
        pass 

    def next(self):
        pass

    def restart(self):
        pass

#메인

print("나는 이상한 나라에 떨어졌다.")
print("어떻게든 살아남아야 한다, 그래서 주유소를 열었다.")
random.choice(["tip: 폭발에 주의하세요.", "tip: bus는 디젤 차량입니다.", '총기상 중 전설의 용사 문요준은 이스터에그이다.'])
module.enter()

diffculty = module.input_str("게임 난이도를 선택하시오. (easy, medium, hard, hardcore, hell): ", "잘못된 입력입니다", ["hell"])
if diffculty == "hell":
    print("게임 난이도 선택 완료. 난이도 'HELL'로 설정되었습니다. 게임을 시작합니다.")
    print(random.choice(["tip: 폭발에 주의하세요.", "tip: suv는 가솔린 차량입니다."]))
module.enter()

def main():   
    station = Station()
    while True:
        select = station.default_screen()
        if select == 0:
            station.serve()
        elif select == 1:
            station.refill()
        elif select == 2:
            station.print_status()
        elif select == 4:
            station.shop()
        elif select == 5:
            station.gamble()
        else:
            print("잘못된 입력입니다!")
    
             
if __name__ == '__main__':
    main()
