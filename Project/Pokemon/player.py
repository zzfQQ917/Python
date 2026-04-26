class Player:
    def __init__(self):
        self.money = 5000
        self.item_bag = {}      # 전체 갖고 있는 아이템
        '''
            예시)
            self.item_bag = {
                '몬스터볼': [몬스터볼 객체 1, 몬스터볼 객체 2...]
                '좋은상처약': [좋은상처약 객체 1, 좋은상처약 객체 2...]
            }
        '''
        
        self.pokemon_bag = []   # 들고다니는 포켓몬 6마리
        self.pokemon_inven = [] # 전체 갖고 있는 포켓몬
        
    def add_item(self, item): 
        # TODO
        # self.item_bag에 아이템(item) 추가
        pass
    
    def use_item(self):
        # TODO
        # self.item_bag에서 아이템 선택 및 사용
        pass
    
    def view_items(self):
        # TODO
        # self.item_bag에 있는 아이템 조회
        # 아이템 선택 시 아이템에 대한 설명(Item 클래스 내에 구현 필요 및 수량 조회
        # 검색 기능 포함
        print("---- Items ----")
        ## ~~ 구현
        option = int(input("~~")) # <-- 메뉴 형식으로 구현
        pass
    
    def set_pokemon_bag(self):
        # TODO
        # self.pokemon_bag 설정 (6마리 설정)
        # pokemon_inven과 연동해서 구현 필요
        pass

    def view_pokemon_bag(self):
        # TODO
        # self.pokemon_bag에 있는 포켓몬들 조회
        pass
    
    

    
    
    
    
    
        
        