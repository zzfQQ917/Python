'''
Item 클래스를 Pokemon과 Player로 나눠서 상속
Player 측에는
기술머신
회복제
몬스터볼
스프레이
탈출버튼
기합의띠
Pokemon 측에는
포켓몬의 능력치를 강화해주는 아이템들
예:
실크스카프 등등
'''

class Context:
    def __init__(self, player, enemy, player_mon, enemy_mon):
        self.player = player # 플레이어 자신
        self.enemy = enemy   # 상대방(체육관 관장/챔피언)
        self.player_mon = player_mon
        self.enemy_mon = enemy_mon
        
class Item:
    def __init__(self, name):
        self.name = name

