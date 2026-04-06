# TODO - Skill 클래스 완성하기
# PhysicalSkill, StatusSkill 클래스로 Skill 상속하기 - 옛날에 한거랑 다르게 구현할거임 ㅇㅇ
# 

class Skill:
    def __init__(self, power: int, speed: int, land_prob: int, critical_prob: int, pp: int, name: str, type: str, required_lvl: int, required_type: list):
        '''
        TODO
        self.power(기술의 위력)
        self.speed(기술의 속도)
        self.land_prob(명중률)
        self.critcal_prob(치명타율)
        self.pp(요구 PP)
        self.name(기술의 이름)
        self.type(기술의 타입)
        self.required_lvl(요구 레벨)
        self.required_type(요구 타입)
        '''
        self.power = power
        self.speed = speed
        self.land_prob = land_prob
        self.critical_prob = critical_prob
        self.pp = pp
        self.name = name
        self.type = type
        self.required_lvl = required_lvl
        self.required_type = required_type
'''
TODO
PhysicalSkill, StatusSkill 클래스에서 Skill을 상속함
'''
class Physical_skill(Skill):
    def __init__(self, power: int, speed: int, land_prob: int, critical_prob: int, pp: int, name: str, type: str, required_lvl: int, required_type: list):
        super().__init__(power, speed, land_prob, critical_prob, pp, name, type, required_lvl, required_type)
    '''
    TODO
    (1) 현재 배틀 중인 포스몬(our_posmon)이 기술을 사용하여  
        #    상대편 포스몬(opponent_posmon)에게 피해를 주는 메서드입니다. 
        #    예시:  컴퓨터 Normie가 당신의 Ponix를 공격하면 
        #    our_posmon은 컴퓨터 Normie, is_player_move는 False.
        # (2) 피해를 줄 때 계산 공식은 '0.규칙 설명'을 사용합니다.  
        # (3) 체력 변화에 따른 메시지를 출력합니다. 
        # print("- %s 포스몬의 [체력] %d 감소 (%d->%d)" ...) 
        타입 상성(Matchup)에 따라 대미지 부가/감소 
    '''

    def use(self):
        
    pass

class Status_skill(Skill):
    def __init__(self, speed: int, land_prob: int, critical_prob: int, pp: int, name: str, type: str, required_lvl: int, required_type: list):
        super().__init__(0, speed, land_prob, critical_prob, pp, name, type, required_lvl, required_type)
    pass
