from Mob import *
from Player import *

'''
Player
오버월드(53종)

육지 일반/산악·고지

Plains

Peaks

숲·초원 계열

Forest

사막·사바나

Desert

설원·특수

Snowy Taiga

해안·강

Beach

-------------------------------------------------------------------

Map
Item
-Ender eye
-Weapon
	-Sword
	-Bow
    -Arrow
-Food
    -Rotten Flesh
    -Steak
    -Pork

''' 
import time, random, os 

class Item:
    def __init__(self, name, kind):
        self.kind = kind 
        self.name = name

class Ender_pearl(Item):
    def __init__(self):
        super().__init__('엔더 진주', 'Item')
    
    def teleport(self):
        pass

class Stick(Item):
    def __init__(self):
        super().__init__('막대기', 'Item')

class Iron(Item):
    def __init__(self):
        super().__init__('철', 'Item')

class Web(Item):
    def __init__(self):
        super().__init__('실', 'Item')

class Gunpowder(Item):
    def __init__(self):
        super().__init__('화약', 'Item')

class Lighter(Item):
    def __init__(self):
        super().__init__('라이터', 'Item')

class Weapon(Item):
    def __init__(self, name, dmg):
        super().__init__(name, 'Weapon')
        self.dmg = dmg
    
    def get_dmg(self):
        return self.dmg

class Sword(Weapon):
    def __init__(self):
        super().__init__('검', 7)
    
class Bow(Weapon):
    def __init__(self):
        super().__init__('활', 10)

class Arrow(Weapon):
    def __init__(self):
        super().__init__('화살', 0)

class TNT(Weapon):
    def __init__(self):
        super().__init__('TNT', 0)

    def Explosion(self, user, mob):
        if '라이터' in user.inven:
            user.life / 2

            

