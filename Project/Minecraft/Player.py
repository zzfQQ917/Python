import time, random, os, sys 
from Food import *
from Item import *
class Player:
    def __init__(self, nickname):
        self.nickname = nickname # 닉넴
        self.max_life = 20 # 최대 체력
        self.cur_life = 20 # 현재 체력
        self.max_hunger = 10 # 포화
        self.cur_hunger = 10 # 현재 배고픔 수치
        self.atk = 1 # 공격력
        self.inven = {} # 인벤토리: 저장 공간 무한함, 키 = 아이템 이름(문자열), 값 = 아이템 객체 리스트
    
    def print_stat(self):
        print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
        print(f'{'♥'*self.cur_life}{'♡'*(self.max_life-self.cur_life)} {'🍖'*self.cur_hunger}{'🤢'*(self.max_hunger-self.cur_hunger)}')
        print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
    
    def walk(self):
        if self.cur_hunger <= 0:
            self.cur_life -= 2
            if self.cur_life <= 0:
                self.die() 

        else:
            self.cur_hunger -= 2
            if self.cur_hunger <= 0:
                self.cur_hunger = 0
        

    def craft(self):
        create = {
            'Bow': [('막대기', 3), ('실', 3)],
            'TNT': [('화약', 5)],
            'Lighter':[('화약', 1), ('철', 1)],
            'Diamond Sword':[('다이아몬드', 4), ('막대기', 2)]
        }
        '''
        while문에서 if문으로 item 클래스가 상속된 아이템들을 검사해 플레이어가 만들기를 원하는 아이템에 필요한 재료가 있다면
        해당 재료가 얼마나 있는지 다시 if문으로 검사, 해당 재료의 유무와 수량이 모두 충족되면 self.inven에서 재료를 빼고, 대신 만들기를 원하는 아이템을 추가한다.
        '''
        i = 0

        while True:
            print('어느 아이템을 만드시겠습니까?:')
            for k, v in create.items():
                print(f"{i}. {k}")
                i += 1
            enter = int(input(f'0부터 {len(create)-1}까지의 수를 고르십시오.'))
            recipe = list((create.keys()))
            choice = recipe[enter]
            design = create[choice]
            print(f'{choice} : ')
            for v in design:
                print(f'{v[0]} {v[1]}개')
            response = input(f'{choice}를 제작하시겠습니까? (Y/N)')
            if response == 'Y':
                print('아이템을 제작합니다.')
                demand = v[0]
                amount = v[1]
                if demand in self.inven:
                    if amount <= len(self.inven):
                        len(self.inven) -= amount
                        if choice == 'Bow':
                            self.equip([Bow()])

                        if choice == 'TNT':
                            self.equip([TNT()])
                        
                        if choice == 'Lighter':
                            self.equip([Lighter()])
                        
                        if choice == 'Diamond Sword':
                            self.equip([Diamond_Sword()])
                        
                        print(f'제작 완료! 새 {choice}(이)가 {self.nickname}의 인벤토리에 추가되었습니다.')

            else:
                print('아이템 제작을 취소합니다.')
                break

            





            

            
    def sleep(self, map, near_monster: bool):
        if map.is_day:
            print(f'낮에는 잘 수 없습니다.')
            return 

        if near_monster:
            print(f'주변에 몬스터가 있어 잘 수 없습니다.')
            return
        
        print(f'{self.nickname}(이)가 잠에 듭니다.')
        map.is_day = True
        
        for i in range(3):
            print(i+1)
            time.sleep(1)
        print('낮이 밝았습니다.')

    def eat(self):
        '''
        Map에서 '[]'을 한 칸 씩 이동할 때마다 Walk 함수를 호출해 cur_hunger를 2 씩 감소시킨다. 
        줄어든 cur_hunger는 all_items에서 item.kind가 food인 아이템을 섭취해 
        cur_hunger에 chosen_food.fullness를 더하고, max_hunger에서 cur_hunger를 뺀 값 만큼 self.cur_life에 더한다.

        '''
        old_hunger = self.cur_hunger
        old_life = self.cur_life
        all_items = [] # 모든 아이템이 담긴 리스트
        for item in self.inven.values():
            all_items.extend(item) # 실제 아이템 객체를 리스트에 추가함
        foods = [] # item.kind에서 "food"에 해당하는 아이템 객체 필드들을 추가하는 리스트
        for item in all_items:
            if item.kind == "food":
                foods.append(item) # item.kind가 "food"인 아이템 객체 필드를 추가함

        for i, food in enumerate(foods): # i와 food에 각각 foods 리스트 내에 있는 아이템 객체 필드와 인덱스를 출력함
            print(f"{i}. {food.name}")

        choice = int(input("먹을 음식을 고르세요: "))
        chosen_food = foods[choice] # 번호가 매겨진 아이템 객체의 이름을 선택할 수 있는 변수
        if len(foods) == 0:
            print('인벤토리에 음식이 없습니다.')
            return

        print(f"\n{chosen_food.name}(을)를 선택하여 섭취합니다")
        self.cur_hunger += chosen_food.fullness
        if self.cur_hunger > self.max_hunger:
            self.cur_life += self.cur_hunger - self.max_hunger
            self.cur_hunger = self.max_hunger
              # 플레이어의 체력에 아이템이 보유한 포만감 지수를 추가함
        print(f'{self.nickname}: 👴 {old_life} -> 👦 {self.cur_life} / 🪰 {old_hunger} -> 🍖 {self.cur_hunger}')
        
    def attack(self, opponent, weapon):
        critical_chance = random.randint(1, 10)
        if critical_chance == 1:
            dmg = 1.5*(self.atk + weapon.dmg)
            is_live = opponent.hit(dmg)
            print(f'\n크리티컬!💥 {self.nickname}(이)가 {opponent.name}(을)를 공격해 {dmg}의 피해를 입혔습니다!')
        
        else:
            dmg = self.atk + weapon.dmg
            is_live = opponent.hit(dmg)
            print(f'\n{self.nickname}(이)가 {opponent.name}(을)를 공격해 {dmg}의 피해를 입혔습니다.')

        return is_live
    
    def equip(self, items):
        '''
        self.inven = {
            'steak' : [steak1, steak2],
            'pork' : [pork1, pork2]
        }
        self.inven 딕셔너리 내에 있는 아이템의 이름을 if문으로 검사해 self.inven에 있는 Key에 해당되는 객체일 시 딕셔너리의 Value에 있는 리스트에 추가한다
        Key에 해당하는 객체가 아닐 시에는 새 Key로 리스트로 추가한다 
        '''
        print('\n아이템이 추가되었습니다')
        for item in items:
            if item.name in self.inven:
                self.inven[item.name].append(item)

            else:
                self.inven[item.name] = [item]
            print(f'{item.name}의 수량: {len(self.inven[item.name]) - 1} -> {len(self.inven[item.name])}')
    
    
    def hit(self, dmg):
        self.cur_life -= dmg

        if self.cur_life <= 0:
            self.die()
            return False
        
        return True
    
    def respawn(self):
        pass
    
    def die(self):
        print('\n💀 - Game Over')
        print(f'{self.nickname}(이)가 사망하였습니다.')
        print('게임을 종료합니다.')
        sys.exit(0)
if __name__ == '__main__':
    player = Player('jipoop')
    steak = Steak()
    player.equip(steak)
    pork = Pork()
    player.equip(pork)
    player.eat()