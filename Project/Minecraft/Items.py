import sys
import time

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

class Item:
    def __init__(self, name, kind):
        self.kind = kind 
        self.name = name

class Ender_pearl(Item):
    def __init__(self):
        super().__init__('엔더 진주', 'Item')
    
    def teleport(self):
        pass

class Diamond(Item):
    def __init__(self):
        super().__init__('다이아몬드', 'Item')

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
        super().__init__('검', 5)

class Diamond_Sword(Weapon):
    def __init__(self):
        super().__init__('다이아몬드 검', 10)
    
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
            print(f'🤯퍼엉! {self.name}(이)가 폭발하여 {user.nickname}의 체력이 현재의 절반으로 닳고, 주변 몹이 모두 사망했습니다!')
            user.life /= 2
            mob.life == 0
        
        else:
            pass

class Ender_Egg(Item):
    def __init__(self):
        super().__init__('엔더 알', 'Item')
        self.credits = [
            "THE END\n"
            "",
            "Minecraft Python Game",
            "Created by: Hedgehog, Yorius\n",
            "Special Thanks To Mojang\n",
            "Powered by Python"
        ]
        
        self.RESET = "\033[0m"
        self.COLORS = {
            "green": "\033[32m",
            "yellow": "\033[33m",
            "red": "\033[31m",
            "white": "\033[37m"
        }
    
    def type_write(self, text, speed=0.05):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(speed)
        print()

    def render(self, default_color="green", highlight=None, speed=0.05):
        """
        lines       → ["text1", "text2", "Special Thanks To Mojang"]
        default_color  → "green"
        highlight   → {"Special Thanks To Mojang": "yellow"}
        speed       → 0.05 (타이핑 속도)
        """

        color_default = self.COLORS.get(default_color, self.COLORS["white"])

        print("\n" * 3)

        for line in self.credits:
            # 특별 색상 적용
            if highlight and line in highlight:
                color = self.COLORS.get(highlight[line], color_default)
            else:
                color = color_default

            self.type_write(color + line + self.RESET, speed)
            time.sleep(0.4)

if __name__ == "__main__":
    아이템 = Ender_Egg()
    아이템.render(
        default_color="green",
        highlight={"Special Thanks To Mojang\n": "yellow", "THE END\n": "red", "Powered by Python": "red"},  # 특정 문장 강조
        speed=0.05
    )