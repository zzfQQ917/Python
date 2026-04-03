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
    
    def inc_exp(self):
        # TODO - 경험치 늘리는 함수, 특정 경험치 이상이면 레벨업 기능 포함, 경험치에 따른 레벨을 딕셔너리로 정의해둬야함
        # {1: 100, 2: 200}
        pass
    
    def adj_hp(self, val):
        # TODO - 체력 조정 함수
        pass

    def adj_atk(self, val):
        # TODO - 공격력 조정 함수
        pass
    
    def adj_dfs(self, val):
        # TODO - 방어력 조정 함수
        pass
    
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