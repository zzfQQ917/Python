import random
from DB import players, levels

class Hangman:
    def __init__(self):
        self.nickname = None
        self.word_list = None
        pass

    def rand(self):
        word_list = ['apple', 'april', 'banana', 'blue', 'coral', 'dictionary', 'flower', 'peach', 'strawberry', 'watermelon']
        mashup = random.choice(word_list)
        return mashup # 함수로 하면 낭비 

    def print_status(self,comp_word, used, life):
        print("--------------------------------------------- ")
        print("Word:", end=" ")
        self.reveal_word(comp_word, used)
        print("\nUsed:", end=" ")
        string = " ".join(used)
        print(string)
        print(f"Life: {life}")
        print("--------------------------------------------- ")

    def is_word_guessed(self, comp_word, used):
        for examination in comp_word:
            if examination in used:
                continue
            else:
                return False
        return True

    def reveal_word(self, comp_word, used):
        for chosen in comp_word:
            if chosen in used:
                print(chosen,end=" ")
            else:
                print("_", end=" ")

    def main(self):
        print("Hangman game start! ")
        while True:
            comp_word = self.rand()
            life = 10
            used = []
            while True:
                self.print_status(comp_word, used, life)
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
                if self.is_word_guessed(comp_word, used):
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

hangman = Hangman()
hangman.main()