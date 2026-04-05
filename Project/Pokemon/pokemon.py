from enum import Enum
from ascii import image_to_ascii

# 사용 예) Type.FIRE
class Type(Enum):
    FIRE = 0
    WATER = 1
    GRASS = 2
    ROCK = 3    

class Pokemon:
    def __init__(self, name: str, type: Type, level: int, exp: int, max_hp: int, max_pp: int, atk: int, dfs: int):
        # 포획 확률(몬스터볼) - 나중에 구현
        self.name = name
        self.type = type
        self.level = level
        self.exp = exp
        self.hp = max_hp
        self.max_hp = max_hp
        self.pp = max_pp
        self.max_pp = max_pp
        self.atk = atk
        self.dfs = dfs
        self.evol = None
        self.evol_level = None
    
    def get_required_exp(self, level: int):
        return level ** 3
    
    def inc_exp(self, gained_exp: int):
        self.exp += gained_exp
        print(f"{self.name}(이)가 {gained_exp}의 경험치를 획득했다!")

        # TODO - 로직 이해하고 주석 적기
        # 내가 얻은 경험치로 어느 레벨까지 레벨업할 수 있는지 계산
        target_level = 0
        for lvl in range(1, 101):
            if self.get_required_exp(lvl) > self.exp:
                target_level = lvl - 1
                break
        
        # 만약 레벨업이 가능하다면(내가 오를 수 있는 레벨이 현재 레벨보다 높다면)
        if target_level > self.level:
            self.level_up(target_level)

    def level_up(self, target_level):
        # TODO - 로직 이해하고 주석 적기
        change = target_level - self.level
        self.level = target_level
        
        if self.evol_level and self.level >= self.evol_level:
            print(f'...오잉!? {self.name}의 모습이...!')
            self.evol.draw()
            print(f'축하합니다! {self.name}는 {self.evol.name}로 진화했습니다!')
            return self.evol
        
        hp_up = 5 * change
        atk_up = 2 * change
        dfs_up = 2 * change
        
        hp_temp = self.max_hp
        atk_temp = self.atk
        dfs_temp = self.dfs
        
        self.max_hp += hp_up
        self.atk += atk_up
        self.dfs += dfs_up
        
        print(f"축하합니다! {self.name}(이)가 레벨 {self.level}(으)로 올랐습니다!")
        print("-----STAT-----")
        # TODO # 예) 체력: {} -> {}
    
    def adj_pp(self, val: int):
        temp = self.pp
        self.pp += val
        if self.pp > self.max_pp:
            self.pp = self.max_pp
        elif self.pp < 0:
            self.pp = 0
        return f'{temp} -> {self.pp}'
    
    def adj_hp(self, val: int):
        temp = self.hp
        self.hp += val
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        elif self.hp < 0:
            self.hp = 0
        return f'{temp} -> {self.hp}'

    def adj_atk(self, val: int):
        temp = self.atk
        self.atk += val
        if self.atk < 0:
            self.atk = 0
        return f'{temp} -> {self.atk}'
        
    def adj_dfs(self, val: int):
        temp = self.dfs
        self.dfs += val
        if self.dfs < 0:
            self.dfs = 0
        return f'{temp} -> {self.dfs}'
    
    def learn_skill(self, skill):
        # TODO - 스킬 학습 함수
        pass

    def draw(self):
        image_to_ascii(self.name)

class 파이리(Pokemon):
    def __init__(self):
        super().__init__(name="파이리", type=Type.FIRE, level=1, exp=1, max_hp=39, max_pp=20, atk=52, dfs=43)
        self.evol = 리자드()
        self.evol_level = 16
        
class 리자드(Pokemon):
    def __init__(self):
        super().__init__(name="리자드", type=Type.FIRE, level=16, exp=4096, max_hp=58, max_pp=35, atk=64, dfs=58)
        self.evol = 리자몽()
        self.evol_level = 36

class 리자몽(Pokemon):
    def __init__(self):
        super().__init__(name="리자몽", type=Type.FIRE, level=36, exp=46656, max_hp=78, max_pp=50, atk=84, dfs=78)

class 아차모(Pokemon):
    def __init__(self):
        super().__init__(name="아차모", type=Type.FIRE, level=1, exp=1, max_hp=45, max_pp=20, atk=60, dfs=40)
        self.evol = 영치코()
        self.evol_level = 16

class 영치코(Pokemon):
    def __init__(self):
        super().__init__(name="영치코", type=Type.FIRE, level=16, exp=4096, max_hp=60, max_pp=35, atk=85, dfs=60)
        self.evol = 번치코()
        self.evol_level = 36

class 번치코(Pokemon):
    def __init__(self):
        super().__init__(name="번치코", type=Type.FIRE, level=36, exp=46656, max_hp=80, max_pp=50, atk=120, dfs=70)

class 불꽃숭이(Pokemon):
    def __init__(self):
        super().__init__(name="불꽃숭이", type=Type.FIRE, level=1, exp=1, max_hp=44, max_pp=20, atk=58, dfs=44)
        self.evol = 파이숭이()
        self.evol_level = 14

class 파이숭이(Pokemon):
    def __init__(self):
        super().__init__(name="파이숭이", type=Type.FIRE, level=14, exp=2744, max_hp=64, max_pp=35, atk=78, dfs=52)
        self.evol = 초염몽()
        self.evol_level = 36
        
class 초염몽(Pokemon):
    def __init__(self):
        super().__init__(name="초염몽", type=Type.FIRE, level=36, exp=46656, max_hp=76, max_pp=50, atk=104, dfs=71)

class 가디(Pokemon):
    def __init__(self):
        super().__init__(name="가디", type=Type.FIRE, level=1, exp=1, max_hp=55, max_pp=25, atk=70, dfs=45)
        self.evol = 윈디()
        self.evol_level = 30

class 윈디(Pokemon):
    def __init__(self):
        super().__init__(name="윈디", type=Type.FIRE, level=30, exp=27000, max_hp=90, max_pp=50, atk=110, dfs=80)

class 활화르바(Pokemon):
    def __init__(self):
        super().__init__(name="활화르바", type=Type.FIRE, level=1, exp=1, max_hp=55, max_pp=20, atk=85, dfs=55)
        self.evol = 불카모스()
        self.evol_level = 59

class 불카모스(Pokemon):
    def __init__(self):
        super().__init__(name="불카모스", type=Type.FIRE, level=59, exp=205379, max_hp=85, max_pp=55, atk=60, dfs=65)
        
class 꼬부기(Pokemon):
    def __init__(self):
        super().__init__(name="꼬부기", type=Type.WATER, level=1, exp=1, max_hp=44, max_pp=20, atk=48, dfs=65)
        self.evol = 어니부기()
        self.evol_level = 16
        
class 어니부기(Pokemon):
    def __init__(self):
        super().__init__(name="어니부기", type=Type.WATER, level=16, exp=4096, max_hp=59, max_pp=35, atk=63, dfs=80)
        self.evol = 거북왕()
        self.evol_level = 36

class 거북왕(Pokemon):
    def __init__(self):
        super().__init__(name="거북왕", type=Type.WATER, level=36, exp=46656, max_hp=79, max_pp=50, atk=83, dfs=100)

class 개구마르(Pokemon):
    def __init__(self):
        super().__init__(name="개구마르", type=Type.WATER, level=1, exp=1, max_hp=41, max_pp=20, atk=56, dfs=40)
        self.evol = 개굴반장()
        self.evol_level = 16

class 개굴반장(Pokemon):
    def __init__(self):
        super().__init__(name="개굴반장", type=Type.WATER, level=16, exp=4096, max_hp=54, max_pp=35, atk=72, dfs=47)
        self.evol = 개굴닌자()
        self.evol_level = 36

class 개굴닌자(Pokemon):
    def __init__(self):
        super().__init__(name="개굴닌자", type=Type.WATER, level=36, exp=46656, max_hp=72, max_pp=50, atk=95, dfs=67)

class 물짱이(Pokemon):
    def __init__(self):
        super().__init__(name="물짱이", type=Type.WATER, level=1, exp=1, max_hp=50, max_pp=20, atk=70, dfs=50)
        self.evol = 늪라그()
        self.evol_level = 16

class 늪라그(Pokemon):
    def __init__(self):
        super().__init__(name="늪라그", type=Type.WATER, level=16, exp=4096, max_hp=70, max_pp=35, atk=85, dfs=70)
        self.evol = 대짱이()
        self.evol_level = 36

class 대짱이(Pokemon):
    def __init__(self):
        super().__init__(name="대짱이", type=Type.WATER, level=36, exp=46656, max_hp=100, max_pp=50, atk=110, dfs=90)

class 잉어킹(Pokemon):
    def __init__(self):
        super().__init__(name="잉어킹", type=Type.WATER, level=1, exp=1, max_hp=20, max_pp=10, atk=10, dfs=55)
        self.evol = 갸라도스()
        self.evol_level = 20

class 갸라도스(Pokemon):
    def __init__(self):
        super().__init__(name="갸라도스", type=Type.WATER, level=20, exp=8000, max_hp=95, max_pp=40, atk=125, dfs=79)

class 별가사리(Pokemon):
    def __init__(self):
        super().__init__(name="별가사리", type=Type.WATER, level=1, exp=1, max_hp=30, max_pp=20, atk=45, dfs=55)
        self.evol = 아쿠스타()
        self.evol_level = 30

class 아쿠스타(Pokemon):
    def __init__(self):
        super().__init__(name="아쿠스타", type=Type.WATER, level=30, exp=27000, max_hp=60, max_pp=50, atk=75, dfs=85)

class 이상해씨(Pokemon):
    def __init__(self):
        super().__init__(name="이상해씨", type=Type.GRASS, level=1, exp=1, max_hp=45, max_pp=20, atk=49, dfs=49)
        self.evol = 이상해풀()
        self.evol_level = 16

class 이상해풀(Pokemon):
    def __init__(self):
        super().__init__(name="이상해풀", type=Type.GRASS, level=16, exp=4096, max_hp=60, max_pp=35, atk=62, dfs=63)
        self.evol = 이상해꽃()
        self.evol_level = 32

class 이상해꽃(Pokemon):
    def __init__(self):
        super().__init__(name="이상해꽃", type=Type.GRASS, level=32, exp=32768, max_hp=80, max_pp=50, atk=82, dfs=83)

class 나무지기(Pokemon):
    def __init__(self):
        super().__init__(name="나무지기", type=Type.GRASS, level=1, exp=1, max_hp=40, max_pp=20, atk=45, dfs=35)
        self.evol = 나무돌이()
        self.evol_level = 16

class 나무돌이(Pokemon):
    def __init__(self):
        super().__init__(name="나무돌이", type=Type.GRASS, level=16, exp=4096, max_hp=50, max_pp=35, atk=65, dfs=45)
        self.evol = 나무킹()
        self.evol_level = 36

class 나무킹(Pokemon):
    def __init__(self):
        super().__init__(name="나무킹", type=Type.GRASS, level=36, exp=46656, max_hp=70, max_pp=50, atk=85, dfs=65)

class 모부기(Pokemon):
    def __init__(self):
        super().__init__(name="모부기", type=Type.GRASS, level=1, exp=1, max_hp=55, max_pp=20, atk=68, dfs=64)
        self.evol = 수풀부기()
        self.evol_level = 18

class 수풀부기(Pokemon):
    def __init__(self):
        super().__init__(name="수풀부기", type=Type.GRASS, level=18, exp=5832, max_hp=75, max_pp=35, atk=89, dfs=85)
        self.evol = 토대부기()
        self.evol_level = 32

class 토대부기(Pokemon):
    def __init__(self):
        super().__init__(name="토대부기", type=Type.GRASS, level=32, exp=32768, max_hp=95, max_pp=50, atk=109, dfs=105)

class 아라리(Pokemon):
    def __init__(self):
        super().__init__(name="아라리", type=Type.GRASS, level=1, exp=1, max_hp=60, max_pp=20, atk=40, dfs=80)
        self.evol = 나시()
        self.evol_level = 30

class 나시(Pokemon):
    def __init__(self):
        super().__init__(name="나시", type=Type.GRASS, level=30, exp=27000, max_hp=95, max_pp=50, atk=95, dfs=85)

class 버섯꼬(Pokemon):
    def __init__(self):
        super().__init__(name="버섯꼬", type=Type.GRASS, level=1, exp=1, max_hp=60, max_pp=20, atk=40, dfs=60)
        self.evol = 버섯모()
        self.evol_level = 23

class 버섯모(Pokemon):
    def __init__(self):
        super().__init__(name="버섯모", type=Type.GRASS, level=23, exp=12167, max_hp=60, max_pp=40, atk=130, dfs=80)

class 꼬마돌(Pokemon):
    def __init__(self):
        super().__init__(name="꼬마돌", type=Type.ROCK, level=1, exp=1, max_hp=40, max_pp=20, atk=80, dfs=100)
        self.evol = 데구리()
        self.evol_level = 25

class 데구리(Pokemon):
    def __init__(self):
        super().__init__(name="데구리", type=Type.ROCK, level=25, exp=15625, max_hp=55, max_pp=35, atk=95, dfs=115)
        self.evol = 딱구리()
        self.evol_level = 40

class 딱구리(Pokemon):
    def __init__(self):
        super().__init__(name="딱구리", type=Type.ROCK, level=40, exp=64000, max_hp=80, max_pp=50, atk=120, dfs=130)

class 애버라스(Pokemon):
    def __init__(self):
        super().__init__(name="애버라스", type=Type.ROCK, level=1, exp=1, max_hp=50, max_pp=20, atk=64, dfs=50)
        self.evol = 데기라스()
        self.evol_level = 30

class 데기라스(Pokemon):
    def __init__(self):
        super().__init__(name="데기라스", type=Type.ROCK, level=30, exp=27000, max_hp=70, max_pp=35, atk=84, dfs=70)
        self.evol = 마기라스()
        self.evol_level = 55

class 마기라스(Pokemon):
    def __init__(self):
        super().__init__(name="마기라스", type=Type.ROCK, level=55, exp=166375, max_hp=100, max_pp=55, atk=134, dfs=110)

class 뿔카노(Pokemon):
    def __init__(self):
        super().__init__(name="뿔카노", type=Type.ROCK, level=1, exp=1, max_hp=80, max_pp=20, atk=85, dfs=95)
        self.evol = 코뿌리()
        self.evol_level = 42

class 코뿌리(Pokemon):
    def __init__(self):
        super().__init__(name="코뿌리", type=Type.ROCK, level=42, exp=74088, max_hp=105, max_pp=35, atk=130, dfs=120)
        self.evol = 거대코뿌리()
        self.evol_level = 55

class 거대코뿌리(Pokemon):
    def __init__(self):
        super().__init__(name="거대코뿌리", type=Type.ROCK, level=55, exp=166375, max_hp=115, max_pp=50, atk=140, dfs=130)

class 티고라스(Pokemon):
    def __init__(self):
        super().__init__(name="티고라스", type=Type.ROCK, level=1, exp=1, max_hp=58, max_pp=20, atk=89, dfs=77)
        self.evol = 견고라스()
        self.evol_level = 39

class 견고라스(Pokemon):
    def __init__(self):
        super().__init__(name="견고라스", type=Type.ROCK, level=39, exp=59319, max_hp=82, max_pp=45, atk=121, dfs=119)

class 프테라(Pokemon):
    def __init__(self):
        super().__init__(name="프테라", type=Type.ROCK, level=1, exp=1, max_hp=80, max_pp=40, atk=105, dfs=65)

if __name__ == '__main__':  
    a = 파이리()
    a.draw()
    a.inc_exp(100)
    a.inc_exp(10000)
