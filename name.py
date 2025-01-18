def blah():
    n1 = int(input())
    n2 = int(input())
    multiplication = n1*n2
    five = n2%10
    eight = (n2//10)%10
    three = n2//100
    print(n1*five)
    print(n1*eight)
    print(n1*three)
    print(multiplication)
def output():
    num1 = int(input())
    print(f"입력받은 숫자는 {num1} 입니다. ")
    return num1 
num1 = output()
num2 = output()
num3 = output()
num4 = output()
num5 = output()
list1 = [num1,num2,num3,num4,num5]
average = sum(list1)/5
print(f"입력된 숫자들의 평균은 {average} 입니다. ")
lowest = min(list1)
highest = max(list1)
print(f"입력된 숫자들 중 가장 작은 숫자는 {lowest} 입니다.")
print(f"입력된 숫자들 중 가장 큰 숫자는 {highest} 입니다.")
list1[0],list1[-1] = list1[-1],list1[0]
print(f"첫 번째와 마지막 숫자의 위치를 바꾸었습니다. 현재 리스트는 {list1} 입니다.")
questionaire = int(input("몇 번째 숫자를 알고 싶습니까?"))
print(list1[questionaire])
print(f"{questionaire} 번째 숫자는 {list1[questionaire]} 입니다.")
del(list1[questionaire])
print(f"이 숫자를 제거한 리스트는 {list1}입니다.")