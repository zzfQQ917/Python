first_num = int(input("첫 번째 숫자를 입력하시오. "))
operator = input("연산자를 입력하시오. (+,-,*,/) ")
second_num = int(input("두 번째 숫자를 입력하시오. "))
if operator == "+":
    print(first_num+second_num)
elif operator == "-":
    print(first_num-second_num)
elif operator == "*":
    print(first_num*second_num)
else:
    print(first_num/second_num)