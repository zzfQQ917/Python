val = 10

#1
for i in range(10, 31 ,10):
    print(i)

#3
for _ in range(10, 31, 10):
    print(_)
    print("______")

#6
aggregation = [100, 200, 300]

for additional_tax in aggregation:
    additional_tax += 10
    print(additional_tax)

#7
every = ["김밥", "라면", "튀김"]

for stored in every:
    print(f"오늘의 메뉴: {stored}")

#8 
length = ["SK하이닉스", "삼성전자", "LG전자"]

for count in length:
    count = len(length)
    print(count)

#10
type_of_animal = ["dog", "cat", "parrot"]

for a_letter in type_of_animal:
    a_letter = a_letter[0]
    print(a_letter)

#if - 1
integer = int(input())

if integer % 2 == 0:
    print("짝수")
elif integer % 2 != 0:
    print("홀수")

#if - 2
originated = int(input())
originated += 20

if originated > 255:
    print(255)
else:
    print(originated)

#if - 3
value = int(input())
value -= 20

if value < 0:
    print(0)
elif value > 255:
    print(255)
else:
    print(value)

#if - 4
o_clock = input().split(":")

if o_clock[1] == "00":
    print("정각입니다. ")
else:
    print("정각이 아닙니다. ")

#if - 5
user_def_val = input("좋아하는 과일은? ")
fruit = ["사과", "포도", "홍시"]
if user_def_val in fruit:
    print("정답입니다. ")