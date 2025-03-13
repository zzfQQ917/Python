import random
def rand():
    word_list = ['apple', 'april', 'banana', 'blue', 'coral', 'dictionary', 'flower', 'peach',  
'strawberry', 'watermelon']
    mashup = random.choice(word_list)
    return mashup

def print_status(comp_word, used, life):
    print("--------------------------------------------- ")
    print("Used:", end=" ")
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
            print("_ _ _ _ _ _",end=" ")

