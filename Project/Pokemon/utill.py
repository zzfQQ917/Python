from pokemon import *
import random
import time
import sys

def game_print(text, speed=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    
    sys.stdout.write(" ▼")
    sys.stdout.flush()
    input()

def get_value_with_probability(value, non_value, probability):
    if random.random() < probability:
        return value
    return non_value

if __name__ == '__main__':       
    game_print("오박사: 포켓몬의 세계에 온 것을 환영한다!")
    game_print("오박사: 이 앞은 위험하니 내 포켓몬 중 하나를 골라보렴.")
    game_print("피카츄: 피카피카!!")




