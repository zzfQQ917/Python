from Items import Item

class Food(Item):
    def __init__(self, name, fullness):
        super().__init__(name, "food")
        self.fullness = fullness
        
class Steak(Food):
    def __init__(self):
        super().__init__("스테이크", 10)

class Pork(Food):
    def __init__(self):
        super().__init__("돼지고기", 7)

class Rotten_flesh(Food):
    def __init__(self):
        super().__init__("썩은 고기", 5)

class Limb(Food):
    def __init__(self):
        super().__init__("양고기", 8)