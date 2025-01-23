def blah():
    num1 = int(input())
    num2 = int(input())
    print(num1>num2)
    return blah()
def blah2():
    even_num = int(input())
    if even_num%2 == 0:
        print("짝수입니다! ")
    else:
        print("홀수입니다! ")
def blah3():
    grade = int(input())
    if grade >= 90:
        print("A")
        if grade >= 95:
            print("A+")
        else:
            print("A-")
    else:
        print("F")
def blah4():
    a = [1,2,3,4,5]
    print(len(a)) # 5
    if len(a) != 5:                # if 밑에있는 elif랑 else는 if에서 조건을 만족하지 않을 때 실행
        print("5개보다 큽니다.")
    elif len(a) == 5:
        print("hello")
    elif len(a) > 4:              # 위에서 만족을 이미 해버리면 그 if-elif-else문 전체는 끝남
        print("bye")
    else:                         # else는 위에있는 if랑 elif가 모두 조건을 만족하지 않을 때 실행
        print("else")

    print("끝")
