import random
from Food import *
from Item import Iron, Stick, Web, Arrow, Ender_pearl, Gunpowder

class Mob:
    def __init__(self, name, life, atk, can_atk: bool):
        self.name = name
        self.life = life
        self.max_life = life
        self.atk = atk
        self.can_atk = can_atk
        self.items = []

    def attack(self, opponent):
        if self.can_atk == True:
            critical_chance = random.randint(1, 10)
            if critical_chance == 1:
                dmg = 1.5*(self.atk)
                is_live = opponent.hit(dmg)
                print(f'크리티컬!💥 {self.name}(이)가 {opponent.nickname}(을)를 공격해 {dmg}의 피해를 입혔습니다!')
            
            else:
                dmg = self.atk
                is_live = opponent.hit(dmg)
                print(f'{self.name}(이)가 {opponent.nickname}(을)를 공격해 {dmg}의 피해를 입혔습니다.')

            return is_live
        else:
            return True
        
    def drop(self):    
        pass

    def hit(self, dmg):
        self.life -= dmg

        if self.life <= 0:
            self.life = 0
            print(f'\n{self.name}(이)가 죽었습니다.')
            return False
        return True
    

class Zombie(Mob):
    def __init__(self):
        super().__init__("좀비", 20, 3, True)
    
    def drop(self):
        n_list = []
        n = random.choice([1, 2, 3])
        for i in range(n):
            n_list.append(Iron())
        return n_list

class Skeleton(Mob):
    def __init__(self):
        super().__init__("스켈레톤", 20, 4, True)
    
    def attack(self, opponent):
        strike_chance = random.randint(1, 2)
        if strike_chance == 1:
            dmg = self.atk
            opponent.hit(dmg)
            print(f'적중!💥 {opponent.nickname}(이)가 {self.name}의 화살에 맞아 {dmg}의 피해를 입혔습니다!')
            
        else:
            print(f'{self.name}(이)가 {opponent.nickname}에게 화살을 쏘았지만 빗나갔습니다.')
    
    def drop(self):
        n_list = []
        n = random.choice([1, 2, 3])
        for i in range(n):
            n_list.append(random.choice([Stick(), Web()]))
            n_list.append(Arrow())
        return n_list

class Enderman(Mob):
    def __init__(self):
        super().__init__('엔더맨', 40, 7, False)
    
    def teleport(self):
        pass

    def hit(self, dmg):
        self.life -= dmg
        decide = random.choice([1, 2])
        if decide == 1:
            self.life += dmg
            print('✖️ 엔더맨(이)가 공격을 회피했습니다.')

        if self.life <= 0:
            self.life = 0
            print(f'\n{self.name}(이)가 죽었습니다.')
            return False
        return True
    
    def drop(self):
        n_list = []
        n = random.choice([1, 2, 3])
        for i in range(n):
            n_list.append((Ender_pearl()))
        return n_list

class Creeper(Mob):
    def __init__(self):
        super().__init__('크리퍼', 20, 14, True)
    
    def attack(self, opponent):
        dmg = self.atk
        
        if random.choice([1, 2, 3, 4, 5]) == 5:
            opponent.hit(dmg)
            self.life = 0
            print(f'{self.name}(이)가 {opponent.name}(을)를 향해 자폭했습니다.')
        
    def drop(self):
        n_list = []
        n = random.choice([1, 2, 3])
        for i in range(n):
            n_list.append((Gunpowder()))
        return n_list

class Spider(Mob):
    def __init__(self):
        super().__init__('거미', 10, 4, True)
    
    def drop(self):
        n_list = []
        n = random.choice([1, 2, 3])
        for i in range(n):
            n_list.append((Web()))
        return n_list

class Pig(Mob):
    def __init__(self):
        super().__init__('돼지', 8, 0, False)
        
    def drop(self):    
        n_list = []
        n = random.choice([1, 2, 3])
        for i in range(n):
            n_list.append(Pork())
        return n_list

class Cow(Mob):
    def __init__(self):
        super().__init__('소', 10, 0, False)

    def drop(self):    
        n_list = []
        n = random.choice([1, 2, 3])
        for i in range(n):
            n_list.append(Steak())
        return n_list

class Sheep(Mob):
    def __init__(self):
        super().__init__('양', 8, 0, False)
    
    def drop(self):
        n_list = []
        n = random.choice([1, 2, 3])
        for i in range(n):
            n_list.append(Limb())
        return n_list