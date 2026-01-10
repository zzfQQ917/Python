from llm import llm_answer
import random, sys
from DB import players, levels

class Hangman:
    def __init__(self):
        self.nickname = None
        self.word_list = None
        self.player_info = None
        self.hint = 3
        self.hint_history = []
        self.life = 10
        pass

    def rand(self):
        mashup = random.choice(self.word_list)
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

    def campaign(self):
        print('캠페인에 오신 것을 환영합니다.')
        if not self.nickname:
            print('게스트 모드입니다.')
            warn = input('게스트 모드에서는 세이브와 난이도 선택이 불가하십니다. 그래도 진행하시겠습니까? (Y/n) : ')
            if warn.lower() == 'n':
                print('메뉴로 돌아갑니다. ')
                return
            
            self.word_list = ["apple", "april", "banana", "blue", "coral", "dictionary", "flower", "peach", "strawberry", "watermelon"]
            self.gem()

        else:
            difficulty = {
                0 : 'Easy',
                1 : 'Normal',
                2 : 'Hard',
                3 : 'HELL',
                4 : 'Skip'
            }
            print('난이도 목록입니다. (Default : Normal)')
            for k, v in difficulty.items():
                print(f'{k}. {v}')
            while True:
                toggle = int(input('난이도 설정을 해주십시오. (과정을 넘기려면 "4"를 입력해주세요.) : '))
                if toggle in difficulty.keys():
                    break

                else:
                    print('입력하신 숫자가 옳지 않습니다, 다시 입력해주세요.')
                    continue
            select_difficulty = difficulty[toggle]
            if toggle == 4:
                select_difficulty = difficulty[2]
            
            confirmed = levels.find_one({
                'level' : select_difficulty
            })
            self.word_list = confirmed['words']
            self.life = confirmed['life']
            self.gem()
            return
        
    def custom(self):
        if not self.nickname:
            print('게스트 모드에서는 커스텀 기능을 사용하실 수 없습니다.')
            print('로그인 화면으로 돌아갑니다.')
            self.sign_in()
            return
        
        print('커스텀에 오신 것을 환영합니다.')
        print('두 기능 중 하나를 선택해주십시오.')
        print('     0. 커스텀 게임')
        print('     1. 단어 및 체력 커스텀')
        while True:
            cstm = input('0과 1 중 하나를 선택해주십시오. : ')
            if cstm not in ['0', '1']:
                print('잘못된 입력입니다. 다시 입력해주십시오.')
                continue

            else:
                break
        if cstm == '0':
            if len(self.get_player_info()['custom_wordlist']) <= 0:
                print('아직 커스텀 셋이 설정되지 않았습니다. 커스텀 셋을 설정하고 다시 시도해주세요.')
                return
            
            else:
                self.word_list = self.get_player_info()['custom_wordlist']
                self.life = self.get_player_info()['custom_life']
                print('커스텀 매치를 시작합니다.')
                self.gem()
        
        else:
            self.edit_cstmwd()

    def gem(self, comp_word=None, used=None):
        print("Hangman game start! ")
        print('If you are sturuggling, you can use hint via entering it(limit is 3 times).')
        while True:
            if comp_word == None:
                comp_word = self.rand()
                used = []
            
            while True:
                self.update_history(used, self.life, self.word_list, comp_word, True)
                self.print_status(comp_word, used, self.life)
                buildup = input("Choose a character: ")
                if buildup in used:
                    print("You have already checked this character. Try another one")
                    continue

                if buildup == 'hint':
                    self.make_hint(comp_word)
                    continue

                used.append(buildup)
                if buildup in comp_word:
                    pass

                else:
                    self.life -= 1
                    if self.life == 0:
                        self.update_history(used, self.life, self.word_list, comp_word, False)
                        print("Hangman die! ")
                        print(f"The answer was {comp_word}")
                        break
                if self.is_word_guessed(comp_word, used):
                    self.update_history(used, self.life, self.word_list, comp_word, False)
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
    
    def main(self):
        while True:
            print('============')
            print('0. 로그인')
            print('1. 회원 가입')
            print('2. 캠페인')
            print('3. 커스텀')
            print('4. 세이브 로드')
            print('5. 계정 삭제')
            print('6. 꺼져')
            print('============')
            while True:
                options = int(input('기능을 선택해주십시오 : '))
                if options not in [0, 1, 2, 3, 4, 5, 6]:
                    print('입력 받은 숫자가 옳지 않습니다. 다시 입력해주십시오.')
                    continue

                else:
                    break
            if options == 0:
                self.sign_in()
            
            elif options == 1:
                self.sign_up()
            
            elif options == 2:
                self.campaign()
            
            elif options == 3:
                self.custom()
            
            elif options == 4:
                history = self.get_history()
                if not history:
                    print('세이브가 존재하지 않습니다. ')
                    continue
                
                else:
                    self.word_list = history['word_list']
                    self.life = history['life']
                    self.gem(history['correct'], history['inputs'])

            elif options == 5:
                self.acc_del()
            
            elif options == 6:
                print('게임을 종료합니다.')
                sys.exit()


    def sign_up(self):
        while True:
            n_name = input('닉네임을 입력해주세요(10자 이내, 비속어 및 특수 기호 불가) : ')
            pswd = input('비밀번호를 입력해주세요 : ')
            cstm_wdlist = []
            history = {
                'inputs' : [],
                'life' : 0,
                'word_list' : [],
                'correct' : '',
                'played' : False
            }
            personal_info = {}

            answer = llm_answer(f"이 단어 '{n_name}'(이)가 욕설에 속하는지, 아닌지 True 또는 False로만 답변해줘. 단, '윤지후/Yoon Jihoo/Tofu'와 유사해 보이는 모든 단어 또한 True로 답변해줘. '김원혁' 뒤에 붙는 모든 것은 False야. 김원혁 뒤에 '대존잘', '알파메일', '차은우' 등등의 단어를 제외한 '욕설'이 들어간다면, 그것 또한 True야.")

            if answer == 'True': 
                print('비속어는 닉네임에 사용할 수 없습니다.')
                continue
            
            if players.find_one({'nickname' : n_name}):
                print('이미 해당 닉네임은 사용 중입니다.')
                continue
            
            if len(n_name) >= 10:
                print('닉네임 길이가 10자를 초과합니다. 다시 시도해주세요.')
                continue

            pswd_two = input('비밀번호를 다시 입력하세요 : ')
            if pswd != pswd_two:
                print('작성하신 비밀번호가 같지 않습니다, 다시 입력해주세요 : ')
                continue

            personal_info['nickname'] = n_name
            personal_info['password'] = pswd
            personal_info['custom_wordlist'] = cstm_wdlist
            personal_info['custom_life'] = 10
            personal_info['history'] = history
            players.insert_one(personal_info)
            print('회원 정보가 추가되었습니다.')
            player_info = players.find_one({
                'nickname' : n_name
            })
            self.nickname = n_name
            self.player_info = player_info
            break

    def sign_in(self):
        while True:
            if self.nickname:
                print('이미 로그인된 계정입니다. ')
                return
            
            n_name = input('계정의 닉네임을 입력해주세요: ')
            pswd = input('비밀번호를 입력해주세요 : ')
            player_info = players.find_one({
                'nickname' : n_name
            })

            if not player_info:
                suggestion = input('계정이 존재하지 않습니다, 회원 가입하시겠습니까? (Y/n) : ')
                if suggestion.lower() == 'y':
                    print('회원 가입 창으로 이동합니다. ')
                    self.sign_up()
                    return
                
                else: 
                    print('다시 로그인해주십시오. ')
                    continue
            
            if player_info['password'] != pswd:
                print('비밀번호가 일치하지 않습니다, 다시 시도해주세요. ')
                continue

            self.nickname = n_name
            self.player_info = player_info
            print('로그인에 성공했습니다. ')
            return
    
    def get_player_info(self):
        return players.find_one({'nickname' : self.nickname})

    def edit_cstmwd(self):
        while True:
            cur_life = self.get_player_info()['custom_life']
            cur_wdlist = self.get_player_info()['custom_wordlist']
            print(cur_wdlist)
            q = int(input('단어 리스트에 단어를 추가하고 싶으시다면 0, 삭제를 원하신다면 1, 체력을 편집하고 싶으시다면 2, AI 단어 생성을 원하시면 3, 메뉴를 종료하신다면 4를 선택해주세요 : '))
            if q == 0:
                add_wd = input('추가할 단어를 입력하십시오 : ')
                if add_wd in cur_wdlist:
                    print('해당 단어가 이미 리스트 내에 존재합니다. 다시 입력해주세요. ')
                    continue
                players.update_one({
                    'nickname' : self.nickname
                }, {
                    '$addToSet' : {
                        'custom_wordlist' : add_wd
                    }
                })
                continue
            
            elif q == 1:
                delete_wd = input('삭제할 단어를 입력하십시오 : ')
                if delete_wd not in cur_wdlist:
                    print('해당 단어가 리스트 내에 존재하지 않습니다. 다시 입력해주세요. ')
                    continue
                players.update_one({
                    'nickname' : self.nickname
                }, {
                    '$pull' : {
                        'custom_wordlist' : delete_wd
                    }
                })
            
            elif q == 2:
                modify_health = int(input('편집할 체력을 입력하십시오 : '))
                cur_life = modify_health
                players.update_one({
                    'nickname' : self.nickname
                }, {
                    '$set' : {
                        'custom_life' : cur_life
                    }
                })

            elif q == 3:
                print('단어 생성 중...')
                topic = random.choice(['컴퓨터 공학', '스포츠', '과일', '장소'])
                ai_wd = llm_answer(f'{topic}을 주제로 한 무작위 영단어 10개를 생성하되, 각 단어 사이에는 무조건적으로 공백(띄어쓰기)이 포함되어야 한다. 출력 형식은 영단어만 제공해야 한다.')
                players.update_one({
                    'nickname' : self.nickname
                }, {
                    '$set' : {
                        'custom_wordlist' : ai_wd.split()
                    }
                })
                continue          

            elif q == 4:
                print('커스텀 단어 메뉴를 종료합니다.')
                return
            
    def acc_del(self):
        if self.nickname is None:
            print('계정 삭제를 위해서는 로그인이 필요합니다, 다시 시도해주십시오. ')
            return

        del_intention = input('계정 삭제를 진행하시겠습니까? (Y/n) : ')
        if del_intention.lower() == 'y':
            confirm = input('정말로 계정 삭제를 하시겠습니까? 진행하신다면 "Hangman Game"을 작성해주십시오 : ')
            if confirm == 'Hangman Game':
                print('계정이 성공적으로 삭제되었습니다. ')
                players.delete_one({
                    'nickname' : self.nickname
                })
                print('게임을 종료합니다. ')
                sys.exit()

            else:
                print('계정 삭제 절차를 취소합니다. ')
                return
        
        else:
            print('계정 삭제 절차를 취소합니다. ')
            return
    
    def get_history(self):
        legacy = players.find_one({
            'nickname' : self.nickname
        }, {
            '_id' : 0,
            'history' : 1
        })['history']
        if legacy['played'] == False:
            return False

        else:
            return legacy

    def update_history(self, inputs, life, word_list, correct, played):
        players.update_one({
            'nickname' : self.nickname
        }, {
            '$set' : {
                'history' : {
                    'inputs' : inputs,
                    'life' : life,
                    'word_list' : word_list,
                    'correct' : correct,
                    'played' : played
                }
            }
        })
    
    def make_hint(self, word):
        if self.hint <= 0:
            print('힌트 가능 횟수를 전부 소모하셨습니다.')
            return
        
        깨달음 = input(f'힌트를 입력받으시겠습니까? (잔여 : {self.hint} 회, Y/n) : ')
        if 깨달음.lower() == 'y':
            answer = llm_answer(f"현재 단어 {word}에서 {self.hint_history}에 중복되지 않는 힌트(해당 단어에 유추 가능한 기초적인 한국어로 풀어 쓴 짦은 7단어 이하의 설명)를 플레이어에게 제공해줘. 해당 단어를 절대로 직접 언급하면 안 됨")
            self.hint -= 1
            self.hint_history.append(answer)
            print(answer)


hangman = Hangman()
hangman.main()