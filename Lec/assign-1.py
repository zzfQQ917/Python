import random
def rand():
    word_list = ['apple', 'april', 'banana', 'blue', 'coral', 'dictionary', 'flower', 'peach',  
'strawberry', 'watermelon']
    mashup = random.choice(word_list)
    return mashup

def print_status(comp_word, used, life):
    print("--------------------------------------------- ")
    print("Word:", end=" ")
    reveal_word(comp_word, used)
    print("\nUsed:", end=" ")
    string = " ".join(used)
    print(string)
    print(f"Life: {life}")
    print("--------------------------------------------- ")

def is_word_guessed(comp_word, used):
    for examination in comp_word:
        if examination in used:
            continue
        else:
            return False
    return True

def reveal_word(comp_word, used):
    for chosen in comp_word:
        if chosen in used:
            print(chosen,end=" ")
        else:
            print("_", end=" ")

def main():
    print("Hangman game start! ")
    while True:
        comp_word = rand()
        life = 10
        used = []
        while True:
            print_status(comp_word, used, life)
            buildup = input("Choose a character: ")
            if buildup in used:
                print("You have already checked this character. Try another one")
                continue
            used.append(buildup)
            if buildup in comp_word:
                pass
            else:
                life -= 1
                if life == 0:
                    print("Hangman die! ")
                    print(f"The answer was {comp_word}")
                    break
            if is_word_guessed(comp_word, used):
                print("Hangman Survived")
            else:
                continue
            break
        Replay = input("Do you want to play another game: ")
        if Replay == "yes":
            continue
        elif Replay == "no":
            print("Quit the Hangman game. ")
            return True
main()