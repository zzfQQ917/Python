class Skill:
    def __init__(self, power: int, speed: int, land_prob: int, critical_prob: int, pp: int, name: str, type: str, required_lvl: int, required_type: list):
        self.power = power
        self.speed = speed
        self.land_prob = land_prob
        self.critical_prob = critical_prob
        self.pp = pp
        self.name = name
        self.type = type
        self.required_lvl = required_lvl
        self.required_type = required_type
        
class PhysicalSkill(Skill):
    def __init__(self, power: int, speed: int, land_prob: int, critical_prob: int, pp: int, name: str, type: str, required_lvl: int, required_type: list):
        super().__init__(power, speed, land_prob, critical_prob, pp, name, type, required_lvl, required_type)
    # TODO - use_skill과 연동되게 만들어야함. use_skill에서 필요한 필드 추가 및 제외
    
class StatusSkill(Skill):
    def __init__(self, speed: int, land_prob: int, critical_prob: int, pp: int, name: str, type: str, required_lvl: int, required_type: list):
        super().__init__(0, speed, land_prob, critical_prob, pp, name, type, required_lvl, required_type)
    
    # TODO - use_skill과 연동되게 만들어야함. use_skill에서 필요한 필드 추가 및 제외
