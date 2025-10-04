import random


class Posmon:
    # 인스턴스 변수 
    def __init__(self, health, max_health, attack, defence, moves, name):
        self.health = health  # 포스몬의 체력 (int) 
        self.max_health = max_health  # 포스몬의 최대(초기) 체력 (int) 
        self.attack = attack  # 포스몬의 공격력 (int)
        self.max_attack = self.attack  # 포스몬의 가용 범위 내 최대 공격력 (int)
        self.defence = defence  # 포스몬의 방어력 (int)
        self.max_defence = self.defence  # 포스몬의 가용 범위 내 최대 방어력 (int)
        self.moves = moves  # 포스몬이 보유한 기술(Move) 리스트 (list of Move)
        self.name = name  # 포스몬의 이름(str)
        self.alive = True

    # 메서드 
    def get_name(self) -> str:
        return self.name

    # 포스몬의 이름을 반환하는 메서드 (예. 'Ponix' 반환)

    def get_max_health(self) -> int:
        return self.max_health

    # 포스몬의 최대 체력을 반환하는 메서드

    

    def get_type(self) -> str:
        return self.type  # 포스몬의 속성 혹은 타입

    # 포스몬의 타입을 반환하는 메서드로,
    # 실제 기능은 서브클래스에서 오버라이딩을 통해 구현합니다.
    # 구현 시, 포스몬의 타입에 따라 "Rock", "Paper", "Scissors", "Nothing" 중  
    # 하나를 반환합니다. (대소문자 구분할 것) 

    def reset_status(self, reset_health: bool = False):
        self.attack = self.max_attack
        self.defence = self.max_defence
        if reset_health == True:
            self.health = self.max_health
        # 포스몬의 공격력과 방어력을 생성될 때 값으로 초기화하는 메서드 
        # reset_health가 True면, 체력도 최대 체력으로 초기화합니다. 


class Ponix(Posmon):

    def __init__(self):
        super().__init__(86, 86, 20, 23, [Tackle(), Swift(), SwordDance()], 'Ponix')
        # super() 함수를 사용하여 Ponix의 체력을 86, 공격력을 20, 방어력을 23, 
        # 이름을 ‘Ponix', 보유 기술 리스트(표 참고)를 설정합니다.  
        # 예) super().__init__(health=86, …) 
        self.type = "Paper"


class Normie(Posmon):

    def __init__(self):
        super().__init__(80, 80, 20, 20, [Tackle(), Swift(), Tailwhip()], 'Normie')
        # super() 함수를 사용하여 Ponix의 체력을 80, 공격력을 20, 방어력을 20, 
        # 이름을 ‘Normie', 보유 기술 리스트(표 참고)를 설정합니다.  
        # 예) super().__init__(health=80, …) 
        self.type = "Nothing"


class Rocky(Posmon):

    def __init__(self):
        super().__init__(80, 80, 20, 20, [Tackle(), Swift(), Tailwhip()], 'Normie')
        # super() 함수를 사용하여 Ponix의 체력을 80, 공격력을 15, 방어력을 25, 
        # 이름을 ‘Rocky', 보유 기술 리스트(표 참고)를 설정합니다.  
        # 예) super().__init__(health=80, …) 
        self.type = "Rock"


class Swania(Posmon):

    def __init__(self):
        super().__init__(80, 80, 20, 20, [Tackle(), Swift(), Tailwhip()], 'Swania')
        # super() 함수를 사용하여 Ponix의 체력을 86, 공격력을 30, 방어력을 10, 
        # 이름을 ‘Swania', 보유 기술 리스트(표 참고)를 설정합니다.  
        # 예) super().__init__(health=80, …) 
        self.type = "Scissors"


class Move:
    def __init__(self, name):
        self.name = name  # 기술 이름(str) (예. 'Tackle')

    def get_name(self) -> str:  # 기술의 이름을 반환하는 메서드
        return self.name

    def get_speed(self) -> int:
        # 기술의 속도를 반환하는 메서드로, 
        # 실제 기능은 서브클래스에서 오버라이딩을 통해 구현합니다. 
        pass

    def use(self, our_posmon: Posmon, opponent_posmon: Posmon, is_player_move=True):
        # 기술을 사용하는 메서드로,  
        # 실제 기능은 서브클래스에서 오버라이딩을 통해 구체적으로 구현합니다.  
        pass


class StatusMove(Move):
    def __init___(self, name):
        self.name = name


class PhysicalMove(Move):
    # 인스턴스 변수 

    # 메서드 
    def __init__(self, power, name):
        super().__init__(name)
        self.power = power  # 해당 기술의 위력

    def get_power(self) -> int:  # 이 기술의 위력을 반환하는 메서드
        pass

    def use(self, our_posmon: Posmon, opponent_posmon: Posmon, is_player_move=True):
        # our_posmon: 무조건 우리 포스몬 / opponent_posmon: 컴퓨터 포스몬
        
        # (1) 현재 배틀 중인 포스몬(our_posmon)이 기술을 사용하여  
        #    상대편 포스몬(opponent_posmon)에게 피해를 주는 메서드입니다. 
        #    예시:  컴퓨터 Normie가 당신의 Ponix를 공격하면 
        #    our_posmon은 컴퓨터 Normie, is_player_move는 False.
        # (2) 피해를 줄 때 계산 공식은 '0.규칙 설명'을 사용합니다.  
        # (3) 체력 변화에 따른 메시지를 출력합니다. 
        # print("- %s 포스몬의 [체력] %d 감소 (%d->%d)" ...) 
        compatiblity = 1

        if our_posmon.get_type() == "Rock" and opponent_posmon.get_type() == "Scissors":
            compatiblity = 2

        elif our_posmon.get_type() == "Scissors" and opponent_posmon.get_type() == "Paper":
            compatiblity = 2

        elif our_posmon.get_type() == "Paper" and opponent_posmon.get_type() == "Rock":
            compatiblity = 2
        
        
        # 지금 밑의 로직이면 컴퓨터 포스몬이 공격을 하면 컴퓨터 포스몬 자신의 피가 깎임.
        # 밑에 있는 if else문에 체력을 깎는 로직을 넣어서 예외처리를 해줘야함.
        
        damage_eqauation = max(0, self.power + our_posmon.attack - opponent_posmon.defence) * compatiblity
        
        # 우리가 공격할 때
        if is_player_move == True:
            print(f"당신의 {our_posmon.name}: {self.name} 기술 사용")
            print(
                f"- 컴퓨터 포스몬의 [체력] {damage_eqauation} 만큼 감소 ({opponent_posmon.health} -> {opponent_posmon.health - damage_eqauation})")
            opponent_posmon.health -= damage_eqauation
            opponent_posmon.alive = False  # 포스몬의 생존 여부
        # 컴퓨터가 공격할 때
        elif is_player_move == False:
            print(f"컴퓨터 {opponent_posmon.name}: {self.name} 기술 사용")
            print(f"당신 포스몬의 [체력] {damage_eqauation} 감소 ({our_posmon.health} -> {our_posmon.health - damage_eqauation})")
            our_posmon.health -= damage_eqauation
            our_posmon.alive == False

class Tackle(PhysicalMove):
    # 메서드 
    def __init__(self):
        super().__init__(power=25, name="Tackle")

    def get_speed(self):
        return 0


class ScissorsCross(PhysicalMove):
    # 메서드 
    def __init__(self):
        super().__init__(power=30, name="SccisorsCross")

    def get_speed(self):
        return 0


class Swift(PhysicalMove):
    # 메서드 
    def __init__(self):
        super().__init__(power=30, name="Swift")

    def get_speed(self):
        return 3


class Growl(StatusMove):
    # 메서드 
    def __init__(self, name="Growl"):  # Growl 기술의 인스턴스 초기화
        # super() 함수 사용하여 코드 채우기 
        self.amount = -5
        super().__init__(name)

    def get_speed(self) -> int:  # Growl 기술의 속도를 반환하는 메서드
        return 1

    def use(self, our_posmon: Posmon, opponent_posmon: Posmon, is_player_move=True):
        # (1) 현재 배틀 중인 포스몬(our_posmon)이 기술을 사용하여  
        #  상대편 포스몬(opponent_posmon)의 공격력을 감소시키는 메서드입니다. 
        # (2) 상대 포스몬의 공격력을 감소시키는 로직 구현 (Growl 효과에 맞춰서 구현) 
        # (3) 값을 변화시킨 내용을 print를 사용하여 출력 
        # print("- %s 포스몬의 [공격력] %d 감소 (%d->%d)" ...) 
        if is_player_move == True:
            print(f"당신의 {our_posmon.name}: Growl 기술 사용")
            print(
                f"- 컴퓨터 포스몬의 [공격력] {self.amount} 감소 ({opponent_posmon.attack} -> {opponent_posmon.attack + self.amount})")
            opponent_posmon.attack += self.amount  # 상대 포스몬의 공격력 감소 수치치
        else:
            print(f"컴퓨터 {opponent_posmon.name}: Growl 기술 사용")
            print(f"- 당신 포스몬의 [공격력] {self.amount} 감소 ({our_posmon.attack} -> {our_posmon.attack + self.amount})")
            our_posmon.attack += self.amount  # 우리 포스몬의 공격력 감소 수치


class SwordDance(StatusMove):
    # 메서드 
    def __init__(self, name="SwordDance"):  # Growl 기술의 인스턴스 초기화
        # super() 함수 사용하여 코드 채우기
        self.amount = 10
        super().__init__(name)

    def get_speed(self) -> int:  # Growl 기술의 속도를 반환하는 메서드
        return 0

    def use(self, our_posmon: Posmon, opponent_posmon: Posmon, is_player_move=True):
        # (1) 현재 배틀 중인 포스몬(our_posmon)이 기술을 사용하여  
        #  상대편 포스몬(opponent_posmon)의 공격력을 감소시키는 메서드입니다. 
        # (2) 상대 포스몬의 공격력을 감소시키는 로직 구현 (Growl 효과에 맞춰서 구현) 
        # (3) 값을 변화시킨 내용을 print를 사용하여 출력 
        # print("- %s 포스몬의 [공격력] %d 감소 (%d->%d)" ...) 
        if is_player_move == True:
            print(f"당신의 {our_posmon.name}: SwordDance 기술 사용")
            print(f"- 당신 포스몬의 [공격력] {self.amount} 증가 ({our_posmon.attack} -> {our_posmon.attack + self.amount})")
            our_posmon.attack += self.amount  # 우리 포스몬의 공격력 증가 수치

        else:
            print(f"컴퓨터 {opponent_posmon.name}: SwordDance 기술 사용")
            print(
                f"- 컴퓨터 포스몬의 [공격력] {self.amount} 증가 ({opponent_posmon.attack} -> {opponent_posmon.attack + self.amount})")
            opponent_posmon.attack += self.amount  # 상대 포스몬의 공격력 증가 수치


class Tailwhip(StatusMove):
    # 메서드 
    def __init__(self, name="Tailwhip"):  # Growl 기술의 인스턴스 초기화
        # super() 함수 사용하여 코드 채우기
        super().__init__(name)
        self.amount = -5

    def get_speed(self) -> int:  # Growl 기술의 속도를 반환하는 메서드
        return 1

    def use(self, our_posmon: Posmon, opponent_posmon: Posmon, is_player_move=True):
        # (1) 현재 배틀 중인 포스몬(our_posmon)이 기술을 사용하여  
        #  상대편 포스몬(opponent_posmon)의 공격력을 감소시키는 메서드입니다. 
        # (2) 상대 포스몬의 공격력을 감소시키는 로직 구현 (Growl 효과에 맞춰서 구현) 
        # (3) 값을 변화시킨 내용을 print를 사용하여 출력 
        # print("- %s 포스몬의 [공격력] %d 감소 (%d->%d)" ...) 
        if is_player_move == True:
            print(f"당신의 {our_posmon.name}: Tailwhip 기술 사용")
            print(
                f"- 컴퓨터 포스몬의 [공격력] {self.amount} 감소 ({opponent_posmon.defence} -> {opponent_posmon.defence + self.amount})")
            opponent_posmon.defence += self.amount
        else:
            print(f"컴퓨터 {opponent_posmon.name}: Tailwhip 기술 사용")
            print(f"- 당신 포스몬의 [공격력] {self.amount} 감소 ({our_posmon.defence} -> {our_posmon.defence + self.amount})")
            our_posmon.defence += self.amount


def latest_stat(baggage):
    presumed_dead = ""
    quantity_of_survivor = 0  # 살아 남은 포스몬의 숫자
    for confirm in baggage:
        if confirm.alive == True:
            presumed_dead += "O"
            quantity_of_survivor += 1
        else:
            presumed_dead += "X"
    return presumed_dead, quantity_of_survivor


def cal_of_moves(baggage):
    vacuum = ""
    for i, num_of_moves in enumerate(baggage):
        vacuum += f"({i}) {num_of_moves.name} "
    return vacuum


def main():
    com_posmon_baggage = []  # 컴퓨터의 포스몬 목록
    posmon_baggage = [] # 유저의 포스몬 목록
    while True:
        print(" ____    ___    _____ ___ ___   ___   ____")  # 시작화면 출력
        print("|    \\  /   \\  / ___/|   T   T /   \\ |    \\")
        print("| o   )Y     Y(   \\_ | _   _ |Y     Y|  _  Y")
        print("|   _/ |  O  | \\__  T|  \\_/  ||  O  ||  |  |")
        print("|  |   |     | /  \\ ||   |   ||     ||  |  |")
        print("|  |   l     ! \\    ||   |   |l     !|  |  |")
        print("l__j    \\___/   \\___jl___j___j \\___/ l__j__j")
        print("============================================")
        print("0. 포스몬 선택")
        print("1. 배틀하기")
        print("2. 종료하기")
        print("============================================")
        while True:
            option = input("입력: ")  # 시작화면에서 선택할 수 있는 선택지들
            if option not in ['0', '1', '2']:
                print("잘못된 입력입니다. 다시 입력하세요.")
                continue

            else:
                break

        if option == "0":

            while True:
                print(f"당신이 사용할 포스몬을 선택하세요. 현재 {len(posmon_baggage)} 마리/최대 3 마리")
                print("0. Ponix")
                print("1. Normie")
                print("2. Swania")
                print("3. Rocky ")
                if len(posmon_baggage) > 0:
                    print("-1. 그만두기")
                print("============================================")
                variation = input("입력: ")
                if variation == "0":
                    posmon_ponix = Ponix()
                    posmon_baggage.append(posmon_ponix)

                elif variation == "1":
                    posmon_normie = Normie()
                    posmon_baggage.append(posmon_normie)

                elif variation == "2":
                    posmon_swania = Swania()
                    posmon_baggage.append(posmon_swania)

                elif variation == "3":
                    posmon_rocky = Rocky()
                    posmon_baggage.append(posmon_rocky)
                
                elif variation == "-1" and len(posmon_baggage) > 0:
                    break

                else:
                    # -1 입력 -> 처리 안함
                    print("잘못된 입력입니다. 다시 입력하세요.")

                if len(posmon_baggage) >= 3:
                    amagalmination = [posmon.name for posmon in posmon_baggage]
                    print(f"당신의 포스몬 목록: {" ".join(amagalmination)}")
                    print("============================================")
                    break

        elif option == "1":
            # 포스몬 선택 안하고 선택하면 문제생김

            if len(posmon_baggage) == 0:
                print("싸울 포su몬이 없습니다! 먼저 포su몬을 선택해 주세요.")

            com_posmon_type = ["Rocky", "Ponix", "Normie", "Swania"]  # 컴퓨터가 보유할 수 있는 포스몬의 종류
            for computer in range(3):
                com_obtainable = random.choice(com_posmon_type)
                if com_obtainable == "Ponix":
                    posmon_ponix = Ponix()
                    com_posmon_baggage.append(posmon_ponix)

                elif com_obtainable == "Normie":
                    posmon_normie = Normie()
                    com_posmon_baggage.append(posmon_normie)

                elif com_obtainable == "Swania":
                    posmon_swania = Swania()
                    com_posmon_baggage.append(posmon_swania)

                elif com_obtainable == "Rocky":
                    posmon_rocky = Rocky()
                    com_posmon_baggage.append(posmon_rocky)

                inevitable = [posmon.name for posmon in com_posmon_baggage]
            print("============================================")
            print(f"당신의 포스몬 목록: {" ".join(amagalmination)}")
            print(f"컴퓨터 포스몬 목록: {" ".join(inevitable)}")
            print("============================================")
            print("\n배틀이 시작됩니다.")

            com_presumed_dead, com_quantity_of_survivor = latest_stat(com_posmon_baggage)
            presumed_dead, quantity_of_survivor = latest_stat(posmon_baggage)
            frontline_com_posmon = com_posmon_baggage[0]  # 컴퓨터의 포스몬 목록에서 배틀 중 가장 앞에 있는 포스몬
            frontline_posmon = posmon_baggage[0]  # 유저의 포스몬 목록에서 배틀 중 가장 앞에 있는 포스몬

            while True:
                print("############################################")
                print(
                    f"컴퓨터 포스몬: [{com_presumed_dead}] {com_quantity_of_survivor} / {len(com_posmon_baggage)}")  # 컴퓨터가 보유한 포스몬들의 상태 정보
                print(
                    f"{frontline_com_posmon.name}           <|{frontline_com_posmon.get_type()} {frontline_com_posmon.health} / {frontline_com_posmon.max_health}|")  # 현재 배틀에 나온 컴퓨터 포스몬 정보
                print("                     VS")
                print(
                    f"{frontline_posmon.name}              <|{frontline_posmon.get_type()}   {frontline_posmon.health} / {frontline_posmon.max_health}|")
                print(f"당신의 포스몬: [{presumed_dead}] {quantity_of_survivor} / {len(posmon_baggage)}")
                print("++++++++++++++++++++++++++++++++++++++++++++")
                print(f"기술: {cal_of_moves(frontline_posmon.moves)}")
                print("############################################")
                while True:
                    commands = input("입력: ").split()

                    if commands[0] == "e":
                        for i, posmon in enumerate(posmon_baggage):
                            print(
                                f"({i}) {posmon.name}           <|{posmon.get_type()}   {posmon.health} / {posmon.max_health}|")

                        continue

                    elif commands[0] == "o":
                        max_range = len(posmon_baggage) - 1
                        if len(commands) == 2 and int(commands[1]) <= max_range:
                            user_skill_num = int(commands[1])
                            break

                        else:
                            print("선택할 수 읎는 기술입네다!")
                            continue

                    elif commands[0] == "s":
                        # s만 입력하면 오류생김

                        # posmon_baggage 안의 포스몬 객체가 만약 s 명령어 및 숫자를 입력하여 교대하기 전에 사망하였을 경우, 
                        # '포스몬을 교대시킬 수 읎습니다!'라는 반응을 출력한 후에 continue를 통해 재입력을 요구한다.
                        # s 명령어에서 사용 가능한 숫자는 명령어의 수를 len을 통해 센 후에 그것에서 1을 뺀 값을 제한으로 변수에 할당하고,
                        # 유저가 입력 받은 수가 s 명령어의 수 제한(포스몬의 갯수)보다 적거나 같을 시 while문을 탈출한다. 그러지 못하면 continue로 재개한다.
                        # 그리고 만일 s 명령어로 이미 사망했거나, 현재 포스몬을 교대하려 할 시에도 '포스몬을 교대시킬 수 읎습니다!'라는 반응을 출력한 후 재입력을 요구한다.
                        # 포스몬의 사망 여부는 Posmon 클래스의 kill 메서드가 실행되면면, 사망으로 본다.

                        ceiling = len(posmon_baggage) - 1
                        if len(commands) == 2 and int(commands[1]) <= ceiling:
                            if posmon_baggage[int(commands[1])].alive == False or posmon_baggage[
                                int(commands[1])] == frontline_posmon:
                                print("포스몬을 교대시킬 수 없습니다!")
                                continue

                            else:
                                additional_replacement = int(commands[1])
                                break

                        else:
                            print("포수몬을 교대시킬 수 없습니다!")
                            continue

                if commands[0] == "o":
                    available_skills = frontline_posmon.moves  # 사용 가능한 기술의 종류 (List)
                    com_available_skills = frontline_com_posmon.moves  # 컴퓨터 포스몬이 사용 가능한 기술의 종류 (Random)
                    chosen = available_skills[user_skill_num]  # 유저가 고른 기술 (Object)
                    com_chosen = random.choice(com_available_skills)  # 컴퓨터가 무작위로 뽑은 기술 (Object)
                    # 선제 여부는 각 기술의 속도를 비교해 결정한다 
                    # 기술을 하나 뽑으면 해당 기술 객체에 있는 use 함수를 호출한다 
                    # 컴퓨터는 랜덤 모듈을 사용해 기술 중 하나를 무작위로 뽑아 use 함수를 호출한다
                    # if문으로 각 get_speed 메서드가 반환하고 있는 속도를 비교한다 
                    # 만일 한 쪽의 속도가 더 빠르다면 속도가 빠른 포스몬의 use 메서드가 실행되고, 그 뒤에 속도가 상대적으로 느린 포스몬의 use 메서드가 실행된다
                    if chosen.get_speed() >= com_chosen.get_speed():
                        chosen.use(frontline_posmon, frontline_com_posmon, True)
                        com_chosen.use(frontline_posmon, frontline_com_posmon, False)
                        if frontline_posmon.health <= 0 and frontline_posmon.alive == False:
                            frontline_posmon = available_queues
                            print(f"당신의 {frontline_posmon}으로 교대")

                    else:
                        com_chosen.use(frontline_posmon, frontline_com_posmon, False)
                        chosen.use(frontline_posmon, frontline_com_posmon, True)
                        if frontline_com_posmon.health <= 0 and frontline_com_posmon.alive == False:
                            frontline_com_posmon = available_queues
                            print(f"컴퓨터 {frontline_com_posmon}으로 교대")

                elif commands[0] == "s":
                    # posmon_baggage 리스트 내에서 frontline_posmon을 제외한 포스몬 중 하나를 유저가 입력한 additional_replacement에 맞춰 
                    # 해당 숫자에 속하는 포스몬을 새 frontline_posmon으로 두고, 컴퓨터가 random으로 뽑은 기술이 교대한 포스몬에게 적중한다.
                    # 교대하여 품으로 돌아온 포스몬의 공격력과 방어력은 디버프의 영향이 사라진다.
                    # 그리고 frontline_posmon.kill()이 실행되어 포스몬이 쓰러졌을 경우, 자동으로 남은 포스몬 중 최전선의 포스몬으로 교대한다.
                    # posmon_baggage에서 frontline_posmon을 제외한 포스몬을 frontline_posmon 변수에 additional_replacement의 값으로 새로 지정한다.
                    # posmon_baggage로 돌아온 포스몬의 .attack과 .defense는 각 서브클래스에 지정된 원래 수치로 수정한다.
                    # if문으로 상대 포스몬의 physical_move를 상속하고 있는 기술에 적중 당해 .hp가 0이 된 후,
                    # frontline_posmon.kill()이 실행되어 frontline_posmon의 alive가 False가 될 경우, 자동으로 교대를 진행한다.
                    frontline_posmon.reset_status()
                    available_queues = posmon_baggage[additional_replacement]
                    frontline_posmon = available_queues
                    com_available_skills = frontline_com_posmon.moves
                    com_chosen = random.choice(com_available_skills)
                    com_chosen.use(frontline_posmon, frontline_com_posmon, False)
                    if frontline_posmon.health == 0 and frontline_posmon.alive == False:
                        frontline_posmon = available_queues
                        print(f"당신의 {frontline_posmon}으로 교대")

        # True인 게 하나도 없으면 게임 종료
        # for문으로 컴퓨터 포스몬 혹은 포스몬
        # 리스트에 있는 포스몬 중 alive가 True 각각의 alive가 False인지 if문으로 확인인하여 만일 그렇다면, 
        # 승리 혹은 패배 메시지를 출력한 후 보유 포스몬을 전부 리셋 시켜 다시 타이틀 화면을 띄운다.

        def vindicate(bag):
            
            existance = 0
            for define in bag:
                if define.alive == False:
                    existance == 1
                    break
        
            if existance == 0:
                print("[ 배틀 결과 ] 당신이 이겼습니다.")
            
            else:
                print("[ 배틀 결과 ] 컴퓨터가 이겼습니ㄷㅏ.")
            
        vindicate(posmon_baggage)
        vindicate(com_posmon_baggage)
        posmon_baggage == []
        com_posmon_baggage == []
        continue




main()