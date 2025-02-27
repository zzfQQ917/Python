# 1
for 변수 in [10, 20, 30]:
    print(변수)

# 2
for i in [10, 20, 30]:
    print(i)

# 3
for i in [10, 20, 30]:
    print(i)
    print("-------")

# 4
print("++++")
for i in [10, 20, 30]:
    print(i)

# 5
for _ in range(4):
    print("-------")

# 6
리스트 = [100, 200, 300]
for 가격 in 리스트:
    print(가격 + 10)

# 7
리스트 = ["김밥", "라면", "튀김"]
for 음식 in 리스트:
    print("오늘의 메뉴:", 음식)

# 8
리스트 = ["SK하이닉스", "삼성전자", "LG전자"]
for 종목 in 리스트:
    print(len(종목))

# 9
리스트 = ['dog', 'cat', 'parrot']
for 동물 in 리스트:
    print(동물, len(동물))

# 10
리스트 = ['dog', 'cat', 'parrot']
for 동물 in 리스트:
    print(동물[0])



# 1. 짝수/홀수 판별
num = int(input("숫자를 입력하세요: "))
if num % 2 == 0:
    print("짝수")
else:
    print("홀수")

# 2. 입력값 + 20 (최대 255 제한)
num = int(input("입력값: "))
result = num + 20
print("출력값:", min(result, 255))

# 3. 입력값 - 20 (범위 0~255)
num = int(input("입력값: "))
result = num - 20
print("출력값:", max(0, min(result, 255)))

# 4. 정각 판별
time = input("현재시간: ")
if time.endswith(":00"):
    print("정각 입니다.")
else:
    print("정각이 아닙니다.")

# 5. 과일 포함 여부 확인
fruit = ["사과", "포도", "홍시"]
fav_fruit = input("좋아하는 과일은? ")
if fav_fruit in fruit:
    print("정답입니다.")
else:
    print("오답입니다.")
