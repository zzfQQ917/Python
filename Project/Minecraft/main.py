import os
from Map import Map
from Item import *
from Mob import *

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear') 

Y, X = 9, 9

def main():
    '''
    전체 맵 크기 9, 9
    현재 좌표 5, 5
    '[.]', 플레이어 존재 여부가 True냐 False냐에 따라 '.'를 현재 좌표에 출력함
    Map 객체를 담는 리스트
    이중 반복문으로 9 x 9 2차원 리스트
    새 행에 Map의 인스턴스를 추가함
    새 행을 리스트에 추가함
    9x9에 해당하는 맵 객체 가져옴
    순회하면서 각 행과 열 마다 현재 위치에 있는 플레이어 존재 여부를 if문으로 체크해 '.' 문자열 출력
    '''
    demand = input('닉네임을 입력하시오(Jihoo80은 입력하지 마십시오): ')
    user = Player(demand)
    rec_location = 4, 4
    dom = []
    for row in range(Y):
        rev_row = []
        for column in range(X):
            rein_column = Map()
            rev_row.append(rein_column)
        dom.append(rev_row)
    '''
    while문을 사용해서 플레이어의 현재 위치(rec_location)에 traversal 함수로 [.]을 출력해 위치를 표시하고,
    movement 함수로 지속적으로 플레이어에게서 WASD로 방향을 입력 받아 rec_location의 값을 변경한 후
    다시 traversal을 호출하여 플레이어의 현재 위치를 반영한다.
    '''
    while True:
        traversal(dom, rec_location)
        rec_location = movement(rec_location)

def traversal(dom, rec_location):
    for y in range(len(dom)):
        for x in range(len(dom[0])):
            instance = dom[y][x]
            if (y, x) == rec_location:
                instance.print_mapp(True)

            else:
                instance.print_mapp(False)
        print()
def movement(rec_location):
    y, x = rec_location
    while True:
        direction = input('w/a/s/d: ')
        if direction == 'w':
            De_Y = y - 1
            if 0 <= De_Y < Y:
                rec_location = De_Y, x
                break

        elif direction == 'a':
            De_X = x - 1
            if 0 <= De_X < X:
                rec_location = y, De_X
                break
        
        elif direction == 's':
            De_Y = y + 1
            if 0 <= De_Y < Y:
                rec_location = De_Y, x
                break
        
        elif direction == 'd':
            De_X = x + 1
            if 0 <= De_X < X:
                rec_location = y, De_X
                break
    return rec_location

def print_stat(steve, mob):
    print('----------------------------------------------------------------')
    print(f'이름 : {steve.name} | ❤️: {steve.cur_life} / 💕 : {steve.max_life}')
    print('                          vs.                      ')
    print(f'이름 : {mob.name} | ❤️: {mob.life} / 💕 : {mob.max_life}')
    print('----------------------------------------------------------------')

def battle(user, n_list):
    '''
    while문을 통해 n_list를 순회하며 몹을 차례대로 변수에 할당하고
    플레이어의 Attack 함수에 의해 상대 몹의 self.life가 깎였다면
    상대가 역으로 Attack 함수로 플레이어의 self.life를 깎을 수 있다.
    '''
    for mob in n_list:
        while True:
            print_stat(user, n_list)
            

            


main()