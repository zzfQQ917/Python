from Item import Item

class Food(Item):
    def __init__(self, name, fullness):
        super().__init__(name, "food")
        self.fullness = fullness
        
class Steak(Food):
    def __init__(self):
        super().__init__("스테이크", 7)

class Pork(Food):
    def __init__(self):
        super().__init__("돼지고기", 5)



