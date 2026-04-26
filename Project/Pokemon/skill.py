class Skill:
    def __init__(self, power: int, speed: int, critical_prob: int, pp: int, name: str, type: str, required_lvl: int, required_type: list, required_pp: int):
        self.power = power
        self.speed = speed
        self.critical_prob = critical_prob
        self.pp = pp
        self.max_pp = pp
        self.name = name
        self.type = type
        self.required_lvl = required_lvl
        self.required_type = required_type
        self.required_pp = required_pp
    
    def use(self):
        if self.pp < self.required_pp:
            return False
        self.pp -= self.required_pp
        if self.pp <= 0:
            self.pp = 0
            return True
        
'''

'''

class PhysicalSkill(Skill):
    def __init__(self, power: int, speed: int, critical_prob: int, pp: int, name: str, type: str, required_lvl: int, required_type: list, required_pp: int):
        super().__init__(power, speed, pp, name, type, required_lvl, required_type, required_pp)
        self.critical_prob = critical_prob
    # TODO - use_skill과 연동되게 만들어야함. use_skill에서 필요한 필드 추가 및 제외
    
class StatusSkill(Skill):
    def __init__(self, power: int, speed: int, pp: int, name: str, type: str, required_lvl: int, required_type: list, required_pp: int, target: int, field: str):
        super().__init__(0, power, speed, pp, name, type, required_lvl, required_type, required_pp)
        self.target = target
        self.field = field # 예 : 'attack', 'defense', 'hp', 'pp', 'speed'
        
    # TODO - use_skill과 연동되게 만들어야함. use_skill에서 필요한 필드 추가 및 제외
