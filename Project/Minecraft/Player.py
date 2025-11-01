import time, random, os 
from Food import *
class Player:
    def __init__(self, nickname):
        self.nickname = nickname # 닉넴
        self.max_life = 20 # 최대 체력
        self.cur_life = 20 # 현재 체력
        self.max_hunger = 20 # 포화
        self.cur_hunger = 20 # 현재 배고픔 수치
        self.atk = 1 # 공격력
        self.inven = {} # 인벤토리: 저장 공간 무한함, 키 = 아이템 이름(문자열), 값 = 아이템 객체 리스트
    
    def print_stat(self):
        print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
        print(f'{'♥'*self.cur_life}{'♡'*(self.max_life-self.cur_life)} {'🍖'*self.cur_hunger}{'🤢'*(self.max_hunger-self.cur_hunger)}')
        print('■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■')
    
    def walk(self):
        pass

    def craft(self):
        create = {
            'Sword': [('Stick', 1), ('Iron', 2)],
            'Bow': [('Stick', 3), ('Web', 3)],
            'TNT': [('Gunpowder', 5)]
        }

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

        print(f"{chosen_food.name}을 선택하여 섭취합니다")
        self.cur_life += chosen_food.fullness # 플레이어의 체력에 아이템이 보유한 포만감 지수를 추가함
        print(f'{self.nickname}: {self.cur_life - chosen_food.fullness} -> {self.cur_life}')
        
    def attack(self, opponent, weapon):
        critical_chance = random.randint(1, 10)
        if critical_chance == 1:
            dmg = 1.5*(self.atk + weapon.damage)
            opponent.hit(dmg)
            print(f'크리티컬!💥 {self.nickname}(이)가 {opponent.name}을 공격해 {dmg}의 피해를 입혔습니다!')
        
        else:
            dmg = self.atk + weapon.damage
            opponent.hit(dmg)
            print(f'{self.nickname}(이)가 {opponent.name}을 공격해 {dmg}의 피해를 입혔습니다.')

    def equip(self, item):
        '''
        self.inven = {
            'steak' : [steak1, steak2],
            'pork' : [pork1, pork2]
        }
        self.inven 딕셔너리 내에 있는 아이템의 이름을 if문으로 검사해 self.inven에 있는 Key에 해당되는 객체일 시 딕셔너리의 Value에 있는 리스트에 추가한다
        Key에 해당하는 객체가 아닐 시에는 새 Key로 리스트로 추가한다 
        '''
        if item.name in self.inven:
            self.inven[item.name].append(item)

        else:
            self.inven[item.name] = [item]
        print(f'{item.name}(이)가 인벤토리에 추가되었습니다 ( {item.name}의 수량: {len(self.inven[item.name]) - 1} -> {len(self.inven[item.name])} )')
    
    
    def hit(self, dmg):
        self.life -= dmg

        if self.life <= 0:
            print(f'{self.nickname}(이)가 사망하였습니다, 마지막 스폰 포인트로 돌아갑니다.')

    def respawn(self):
        pass
    

if __name__ == '__main__':
    player = Player('jipoop')
    steak = Steak()
    player.equip(steak)
    pork = Pork()
    player.equip(pork)
    player.eat()