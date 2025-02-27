def prob_1():
    F = int(input("화씨온도: "))
    print(f"섭씨온도: {(F-32)*5/9}")
def prob_2():
    r = int(input("반지름을 입력하시오: "))
    pi = 3.141592
    print(f"원 둘레: {pi*r*2}")
    print(f"원 넓이: {pi*r**2}")
def counter():
    bribe = int(input("투입한 돈 : "))
    cost = int(input("물건값 : "))
    remain_bribe = bribe - cost
    coin_1 = remain_bribe // 500
    coin_2 = remain_bribe % 500 // 100
    print(f"거스름돈 : {remain_bribe}원")
    print(f"500원짜리 : {coin_1}개")
    print(f"100원짜리 : {coin_2}개")


def prob_3():
    create_name = input("이름을 입력하세요: ").split()
    print(f"성: {create_name[0]}")
    print(f"이름: {create_name[1]}")



def prob_4():
    fruits_ninja = input("과일을 입력하세요. ").split(',')
    print(fruits_ninja)


def prob_5():
    ddmmyy = input("날짜(연/월/일) 입력: ").split("/")
    back_to_the_future = int(ddmmyy[0]) + 10
    print(f"입력한 날짜의 10년 후는 {back_to_the_future}년 {ddmmyy[1]}월 {ddmmyy[2]}일")