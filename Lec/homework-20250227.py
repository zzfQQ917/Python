#6
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
Discrimination = input()


if Discrimination in warn_investment_list:
    print("투자 경고 종목입니다. ")
else:
    print("투자 경고 종목이 아닙니다. ")


#7
fruit = {"봄" : "딸기" , "여름" : "토마토", "가을" : "사과"}
user_define = input("너거가선호하는계절은 : ")


if user_define in fruit:
    print("딩동댕이여. ")
else:
    print("오답인디;; ")


#8
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
included_value = str(input("선호하는과일은? "))

if  included_value in fruit.values():
    print("요것도 딩동댕이여. ")
else:
    print("요것도 오답인디;; ")


#9
user_input = input()
stack = ""


for char in user_input:
    if char == "a":
        stack += "A"
    else:
        stack += char
print(stack)


#10
score = int(input())
aggregation = ["A", "B", "C", "D", "E"]


if score >= 81 and score <= 100:
    print(f"grade is {aggregation[0]}")
elif score >= 61 and score <= 80:
    print(f"grade is {score+aggregation[1]}")
elif score >= 41 and score <= 60:
    print(f"grade is {score+aggregation[2]}")
elif score >= 21 and score <= 40:
    print(f"grade is {aggregation[3]}")
elif score >= 0 and score <= 20:
    print(f"grade is {aggregation[4]}")



#11
list1 = [1, 2, 3]

for num in list1:
    print(f"3 x {num}")


#12
list2 = [1, 2, 3]

for integer in list2:
    print(f"3 x {integer} = {3 * integer}")


#13
charactified_list = ["가", "나", "다", "라"]

for align in range(1, len(charactified_list)):
    print(charactified_list[align])


#14
negative_int = [3, -20, -3, 44]

for neg_num in negative_int:
    if neg_num < 0:
        print(neg_num)


#15
postive_int = [3, 100, 23, 44]

for pos_num in postive_int:
    if pos_num % 3 == 0:
        print()

