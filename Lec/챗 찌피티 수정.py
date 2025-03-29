import random
# 랜덤 단어 선택
def rand():
    word_list = ['apple', 'april', 'banana', 'blue', 'coral', 'dictionary', 'flower', 'peach',  
                 'strawberry', 'watermelon']
    return random.choice(word_list)

# 현재 게임 상태 출력
def print_status(comp_word, used, life):
    print("--------------------------------------------- ")
    print("Word:", end=" ")
    reveal_word(comp_word, used)
    print("\nUsed:", " ".join(used))
    print(f"Life: {life}")
    print("--------------------------------------------- ")

# 단어를 모두 맞췄는지 확인
def is_word_guessed(comp_word, used):
    return all(letter in used for letter in comp_word)

# 현재까지 맞춘 글자 표시
def reveal_word(comp_word, used):
    for letter in comp_word:
        print(letter if letter in used else "_", end=" ")
    print()

# 게임 실행
def main():
    print("Hangman game start!")
    while True:
        comp_word = rand()
        life = 10
        used = []
        
        while True:
            print_status(comp_word, used, life)
            buildup = input("Choose a character: ").lower()

            # 입력값 검증 (한 글자만 입력)
            if len(buildup) != 1 or not buildup.isalpha():
                print("Please enter a single letter.")
                continue

            if buildup in used:
                print("You have already checked this character. Try another one")
                continue
            
            used.append(buildup)

            if buildup not in comp_word:
                life -= 1
                if life == 0:
                    print("Hangman die!")
                    print(f"The answer was {comp_word}")
                    break
            
            if is_word_guessed(comp_word, used):
                print("Hangman Survived!")
                break

        # 게임 재시작 여부
        while True:
            Replay = input("Do you want to play another game (yes/no): ").lower()
            if Replay == "yes":
                break
            elif Replay == "no":
                print("Quit the Hangman game.")
                return
            else:
                print("Please type 'yes' or 'no'.")

main()