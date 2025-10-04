import os
from Map import Mapp
from Item import *

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear') 


def main():
    chunk = Mapp.make_chunk()
    # N, M = map(int, ["9", "9"]) # 리스트에 있는 각각 요소에 int를 씌워서 매핑 
    # mapp = [['[ ]'] * N for i in range(M)] # 문자열 '[ ]'에 N을 곱하고, M번 만큼 추가함

    cur_y, cur_x = 8,8 # 현재 좌표
    chunk[cur_y][cur_x] = "[.]" # "[.]" 문자열을 현재 좌표에 추가함



    while True:
        clear_screen()
        N = int(16)
        M = int(16)
        # 맵 출력
        for line in chunk:
            print(" ".join(line)) 

        d = input("방향을 입력하세요(w/a/s/d): ")
        chunk[cur_y][cur_x] = "[ ]" # 우리가 원래 있던 칸은 빈칸이 됨(이동했으니까)

        if d == 'w': # w를 키보드에서 입력할 시, 인덱스가 감소했을 때 범위에 있는지 검사함
            if cur_y - 1 >= 0: 
                cur_y -= 1
            else:
                print("맵의 범위를 벗어납니다")
        elif d == 'a': # a를 키보드에서 입력할 시, 인덱스가 감소했을 때 범위에 있는지 검사함
            if cur_x - 1 >= 0:
                cur_x -= 1
            else:
                print("맵의 범위를 벗어납니다")

        elif d == 's': # s를 키보드에서 입력할 시, 인덱스가 증가했을 때 범위에 있는지 검사함
            if cur_y + 1 <= N-1:
                cur_y += 1
            else:
                print("맵의 범위를 벗어납니다")
        elif d == 'd': # d를 키보드에서 입력할 시, 인덱스가 증가했을 때 범위에 있는지 검사함
            if cur_x + 1 <= M-1:
                cur_x += 1
            else:
                print("맵의 범위를 벗어납니다")

        chunk[cur_y][cur_x] = "[.]" 
main()
    # map 한칸한칸에 map 객체를 박아둘거임
    # map 객체에는 몬스터, 바이옴, 맵 이미지, 출력하는건 [] 만 출력되게