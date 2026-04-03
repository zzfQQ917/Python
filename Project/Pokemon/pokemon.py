from enum import Enum

# 사용 예) Type.FIRE
class Type(Enum):
    FIRE = 0
    WATER = 1
    GRASS = 2
    ROCK = 3    

class Pokemon:
    def __init__(self):
        # TODO
        # 각 타입(자료형) 제대로 정하기
        # 포켓몬 이름, 레벨, 경험치, 체력, 최대 체력, 공격력, 방어력, 포켓몬 타입(불, 물, 풀, 바위), 보유 기술, 포획 확률(몬스터볼), 진화정보(진화되었을 때 어떤 포켓몬으로 변하는지)
        pass
    
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