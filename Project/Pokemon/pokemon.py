from enum import Enum

# 사용 예) Type.FIRE
class Type(Enum):
    FIRE = 0
    WATER = 1
    GRASS = 2
    ROCK = 3    

class Pokemon:
    def __init__(self, name: str, type: Type, level: int, exp: int, max_hp: int, atk: int, dfs: int):
        # 포획 확률(몬스터볼) - 나중에 구현, 진화정보(진화되었을 때 어떤 포켓몬으로 변하는지) - 나중에 구현
        self.name = name
        self.type = type
        self.level = level
        self.exp = exp
        self.hp = max_hp
        self.max_hp = max_hp
        self.atk = atk
        self.dfs = dfs
    
    def get_required_exp(self, level: int):
        return level ** 3

    def inc_exp(self, gained_exp: int):
        self.exp += gained_exp
        print(f"{self.name}(이)가 {gained_exp}의 경험치를 획득했다!")

        while True:
            next_level_exp = self.get_required_exp(self.level + 1)
            
            if self.exp >= next_level_exp:
                self.level_up()
            else:
                break

    def level_up(self):
        self.level += 1
        
        hp_up = 5
        atk_up = 2
        dfs_up = 2
        
        self.max_hp += hp_up
        self.hp += hp_up
        self.atk += atk_up
        self.dfs += dfs_up
        
        print(f"축하합니다! {self.name}(이)가 레벨 {self.level}(으)로 올랐습니다!")
        print(f"체력 +{hp_up}, 공격력 +{atk_up}, 방어력 +{dfs_up} 상승!")
    
    def adj_hp(self, val: int):
        self.hp += val

    def adj_atk(self, val: int):
        self.atk += val
    
    def adj_dfs(self, val: int):
        self.dfs += val
    
    def learn_skill(self, skill):
        # TODO - 스킬 학습 함수
        pass

    def draw(self):
        # TODO - 아스키아트로 포켓몬 출력
        print(
        """
""")
        
class 피카츄(Pokemon):
    def __init__(self):
        super().__init__()
        # TODO