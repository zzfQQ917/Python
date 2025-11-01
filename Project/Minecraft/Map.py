import random
from Mob import *
class Map:
    '''
    바이옴, 몹, 바이옴에 따른 몹 스폰, 선택지
    '''
    def __init__(self):
        self.biomes = ['Plains', 'Peaks', 'Forest', 'Desert', 'Snowy Taiga']
        self.spawn = 1
        self.variation = []
        self.n_list = []
        self.visited = False
        self.biome_choice()

    def biome_choice(self):
        self.damage_per_biome = 0
        self.biome = random.choice(self.biomes)
        if self.biome == 'Plains':
            self.variation = [Zombie(), Cow(), Pig()]
            self.damage_per_biome = 0
        
        elif self.biome == 'Peaks':
            self.variation = [Cow(), Skeleton(), Zombie()]
            self.damage_per_biome = 0
        
        elif self.biome == 'Forest':
            self.variation = [Cow(), Pig(), Enderman(), Zombie(), Skeleton()]
            self.damage_per_biome = 0
        
        elif self.biome == 'Desert':
            self.variation = [Zombie(), Creeper()]
            self.damage_per_biome = 5
        
        elif self.biome == 'Snowy Taiga':
            self.variation = [Zombie(), Skeleton()]
            self.damage_per_biome = 7
        self.n_list = random.sample(self.variation, random.choice([1, 2]))
        
    def print_mapp(self, player_exist: bool):
        if player_exist == True:
            print('■', end=' ')
            self.visited = True
        
        else:
            print('□', end=' ')
        

