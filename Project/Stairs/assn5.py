import os, random
import hashlib
from DB import players, games
from llm import llm_answer
from datetime import datetime

class stairs:
    def __init__(self):
        self.id = None

    def print_scissors(self):
        print('                   ■■')
        print('       ■■        ■■■■■■')
        print('     ■■■■■■    ■■■■■■■■')
        print('    ■■■■■■■■■■■■■■■■■■')
        print('  ■■■■■■■■■■■■■■■■■■')
        print('■■■■■■■■■■■■■■')
        print('■■■■■■■■■■■■■■■■■')
        print(' ■■■■■■■■■■■■■■■■■■')
        print('   ■■■■■■■■■■  ■■■■■■■')
        print('    ■■■■■■■■    ■■■■■■')
        print('     ■■■■■        ■■■')


    def print_rock(self):
        print('   ■■■■■■')
        print('  ■■■■■■■■■■■')
        print(' ■■■■■■■■■■■■■')
        print('■■■■■■■■■■■■■■')
        print('■■■■■■■■■■■■■■■')
        print('■■■■■■■■■■■■■■■')
        print('■■■■■■■■■■■■■■■')
        print('■■■■■■■■■■■■■■')
        print(' ■■■■■■■■■■■■')
        print('  ■■■■■■■■■')


    def print_paper(self):
        print('   ■■■■■■')
        print(' ■■■■')
        print(' ■■■■■■■■■■■■■■■■■■')
        print('■■■■■■■■■■■■')
        print('■■■■■■■■■■■■■■■■■■■■')
        print('■■■■■■■■■■■■')
        print('■■■■■■■■■■■■■■■■■■■')
        print('■■■■■■■■■■■■')
        print(' ■■■■■■■■■■■■■■■■■')
        print('  ■■■■■■')


    def print_stairs(self, total, player_intent, computer_intent):
        square = 1  # 짝수, 홀수 모두 공용하는 한 행 당 계단의 수
        allStairs = []  # 최종적으로 계단과 공백을 출력하는 리스트

        first_row = [' ' for i in range(total + 1)]  # 계단의 첫줄 공백
        allStairs.append(first_row)

        if total // 2 != 0:
            space = total - 1  # 계단의 총 수가 홀수일 때 공백을 출력하는데 쓰이는 변수
            for i in range((total + 1) // 2):  # total이 홀수일 때 계단의 높이를 지정하는 for 문
                newList = []  # 공백과 네모를 담는 리스트
                for j in range(square):  # square만큼 네모 기호를 추가하는 for 문
                    newList.append('■')

                for k in range(space):  # space만큼 공백을 추가하는 for 문
                    newList.append(' ')

                for l in range(square):  # square만큼 반대쪽에 네모 기호를 추가하는 for 문
                    newList.append('■')
                allStairs.append(newList)
                square += 1  # 계단의 가로 폭을 1씩 증가시키는 코드
                space -= 2  # 공백의 가로 폭을 2씩 감소시키는 코드


        else:
            space = total  # 계단의 총 수가 짝수일 때 공백을 출력하는데 쓰이는 변수
            for i in range(total // 2):  # 계단의 총 수가 짝수일 때 계단의 높이를 지정한 for 문
                newList = []
                for j in range(square):
                    newList.append('■')

                for k in range(space):
                    newList.append(' ')

                for l in range(square):
                    newList.append('■')
                allStairs.append(newList)  # 공백과 네모 기호를 allStairs 리스트에 추가하는 코드
                square += 1
                space -= 2

        # 공식: 사용자가 내려가는 칸수 = (player_intent, player_intent), 사용자가 올라가는 칸수 = (total - player_intent, player_intent)
        # 컴퓨터가 내려가는 칸수 = (total - computer_intent, computer_intent), 컴퓨터가 올라가는 칸수 = (computer_intent, computer_intent)
        player_circle = '○'  # 플레이어의 동그라미 
        computa_circle = '●'  # 컴퓨터의 동그라미
        combined_circle = '◐'  # 플레이어가 이동하는 칸수와 컴퓨터가 이동하는 칸수의 합이 계단의 총 수와 같을 때 출력하는 동그라미
        if player_intent + computer_intent != total:  # 플레이어가 이동하는 칸수와 컴퓨터가 이동하는 칸수의 합이 계단의 총 수와 같지 않을 때의 코드
            if player_intent <= total // 2:  # 플레이어가 내려가고 있을 때의 코드
                allStairs[player_intent][player_intent] = player_circle

            else:  # 플레이어가 올라가고 있을 때의 코드
                allStairs[total - player_intent][player_intent] = player_circle

            if computer_intent < total // 2:  # 컴퓨터가 내려가고 있을 때의 코드
                allStairs[computer_intent][-computer_intent - 1] = computa_circle

            else:  # 컴퓨터가 올라가고 있을 때의 코드
                allStairs[total - computer_intent][-computer_intent - 1] = computa_circle

        else:  # 플레이어가 이동하는 칸수와 컴퓨터가 이동하는 칸수의 합이 계단의 총 수와 같을 때의 코드
            if player_intent <= total // 2:  # 결합된 구가 내려가고 있을 때의 코드
                allStairs[player_intent][player_intent] = combined_circle

            else:  # 결합된 구가 올라가고 있을 때의 코드
                allStairs[total - player_intent][player_intent] = combined_circle
        print(f'총 계단 수: {total}')
        print(f'PLAYER:    {player_circle}  < {player_intent}>')
        print(f'COMPUTER:  {computa_circle} < {computer_intent}>')

        if player_intent >= total or computer_intent >= total:
            player_intent == total

        for stairs in allStairs:  # allStairs를 stairs로 푸는 for 문
            print(' '.join(stairs))


    def computer_choice(self):
        rpc = ['가위', '바위', '보']
        election = random.choice(rpc)
        return election


    def ai_choice(self):
        rpc = ['가위', '바위', '보']
        determiner = llm_answer(f"{rpc} 리스트를 기반으로 세 단어 '가위', '바위', '보' 중 하나를 골라 출력해줘.")
        return determiner


    def clear_screen():
        os.system('cls')  # Windows 콘솔 창에서 실행 시 주석 해제
        return


    def enter(self):  # 엔터키 입력받았을 때 clear
        while True:
            print("\n계속하려면 엔터를 눌러주세요...")
            enter = input("")
            if enter == "":
                os.system('cls')
                break


    def rsp(self): # --> 가위바위보를 한 번 수행하고, 누가 이겼는지의 결과를 숫자로 반환하는 함수. 공격권 결정, 묵찌빠 상황에서 쓰인다.
        rpc = input('가위, 바위, 보 중 하나 선택: ') # 가위, 바위, 보 중 하나의 문자열을 입력 받는 변수
        com_rpc = self.computer_choice() # 가위, 바위, 보가 들어 있는 리스트를 랜덤 모듈로 고르는 변수
        print('[컴퓨터 선택]')

        if com_rpc == '가위':
            self.print_scissors()
        elif com_rpc == '바위':
            self.print_rock()
        else:
            self.print_paper()

        print('[플레이어 선택]')
        if rpc == '가위':
            self.print_scissors()
        elif rpc == '바위':
            self.print_rock()
        else:
            self.print_paper()

        if rpc == '가위' and com_rpc == '보':
            num = 1
        elif rpc == '바위' and com_rpc == '보':
            num = 2
        elif rpc == '보' and com_rpc == '바위':
            num = 1
        elif rpc == '가위' and com_rpc == '바위':
            num = 2
        elif rpc == '바위' and com_rpc == '가위':
            num = 1
        elif rpc == '보' and com_rpc == '가위':
            num = 2
        else:
            num = 0

        return num


    def main(self):
        player_movement = 0 # 플레이어가 이동하는 칸 수를 저장하는 변수
        computer_movement = 0 # 컴퓨터가 이동하는 칸 수를 저장하는 변수
        print('================')
        print('[묵찌빠 계단 오르기]')
        print('================')
        
        # TODO
        # 게임을 새로 생성할지 OR 게임을 불러올지 선택
        
        
        self.print_stairs(11, 0, 0)

        while True:
            enter_stair_num = int(input('게임을 위한 계단의 개수를 입력해주세요. <10 ~ 30> >> ')) # 게임을 새로 생성하는 경우
            if enter_stair_num >= 10 and enter_stair_num <= 30:
                break
        self.clear_screen()
        self.print_stairs(enter_stair_num, player_movement, computer_movement)
        self.enter()

        while True:
            print('[공격권 결정 가위바위보]')
            result = self.rsp() # result가 1이면 플레이어 승리, 2이면 컴퓨터 승리, 0이면 무승부
            # result는 누가 공격권을 먼저 가져가는지 저장해놓는 변수

            if result == 1:
                print('[결과] 플레이어 공격, 컴퓨터 수비입니다.')
                break
            elif result == 2:
                print('[결과] 컴퓨터 공격, 플레이어 수비입니다.')
                break
            else:
                print('[결과] 무승부입니다.')
                self.enter()

        self.enter()
        movement = 1
        while True:
            print('[묵찌빠]')
            print(f'승리 시 이동 칸 수: {movement}')
            if result == 1:
                print('플레이어 공격, 컴퓨터 수비입니다.')
            else:
                print('컴퓨터 공격, 플레이어 수비입니다.')
                
            '''
            while True로 승부가 날 때까지 과정 반복
            if문으로 다시 가위 바위 보 작성
            둘이 다른 걸 내면 else에서 매 턴마다 이동 칸 수 1씩 증가
            승부가 안 나면 이동 칸 수 1씩 증가, 
            한 번 이기면 다음 턴에서도 기존 승자가 공격권을 가져감
            둘이 같은 걸 내면 그대로 묵찌빠 종료, 공격권을 유지한 쪽이 승리 시 칸 수 만큼 이동함
            승부가 결정되면 플레이어가 엔터 입력 시,
            화면 지우기 후 현재 계단에서의 위치 출력
            그 뒤 바로 다음 판 진행
            '''
            
            # TODO
            # 이 아래 부터 게임의 모든 기록을 업데이트(밑에서 만들어놓은 업데이트 함수들 호출해서)
            
            ended_up = self.rsp()
            if ended_up == 1:
                print('[결과] 플레이어 공격, 컴퓨터 수비입니다.')
                movement += 1
                continue
            elif ended_up == 2:
                print('[결과] 컴퓨터 공격, 플레이어 수비입니다.')
                movement += 1
                continue
            else:
                print('[결과] 묵찌빠 종료')
                if pre_ended_up == 1:
                    print(f'플레이어 승, {movement} 칸 이동합니다.')
                    player_movement += movement

                elif pre_ended_up == 2:
                    print(f'컴퓨터 승, {movement} 칸 이동합니다.')
                    computer_movement += movement
                    
            self.enter()
            self.print_stairs(enter_stair_num, player_movement, computer_movement)
            self.enter()
            pre_ended_up = ended_up
            if player_movement >= enter_stair_num:
                print('▨▨▨▨▨▨▨▨▨▨▨▨▨')
                print('플레이어 최종 승리!!!')
                print('▨▨▨▨▨▨▨▨▨▨▨▨▨')
                print('\n게임을 종료합니다...')
                return
                
            elif computer_movement >= enter_stair_num:
                print('▨▨▨▨▨▨▨▨▨▨▨▨▨')
                print('컴퓨터 최종 승리!!!')
                print('▨▨▨▨▨▨▨▨▨▨▨▨▨')
                print('\n게임을 종료합니다...')
                return


    def craft_game(self):
        if not self.id:
            print('게임 데이터 생성에는 로그인이 필요합니다.')
            self.sign_in()
            return
        
        import uuid

        game_id = str(uuid.uuid4())

        optional = input('AI와 무작위 알고리즘 중 어느 작동 방식을 고르시겠습니까? (AI/r): ')
        if optional.lower() == 'ai':
            print('AI를 채택합니다.')
            games.insert_one({
                'user' : self.id,
                'option' : 'AI',
                'history' : [],
                'stair_case' : 0,
                'com_stair_case' : 0,
                'game_id' : game_id,
                'stair_cnt' : self.enter_stair_num,
                'created_at' : datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            })
        
        elif optional.lower() == 'r':
            print('무작위 알고리즘을 채택합니다.')
            games.insert_one({
                'user' : self.id,
                'option' : 'Random',
                'history' : [],
                'stair_case' : 0,
                'com_stair_case' : 0,
                'game_id' : game_id,
                'stair_cnt' : self.enter_stair_num,
                'created_at' : datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            })
            
    # 게임 중에 사용자와 상대가 계단 칸수 변화했을 때 DB 업데이트
    def upd_stair_case(self, stair_case, com_stair_case):
        games.update_one({
            'game_id' : self.game_id
        }, {
            '$set' : {
                'stair_case' : stair_case,
                'com_stair_case' : com_stair_case
            }
        })
    
    
    def upd_history(self, history):
        games.update_one({
            'game_id' : self.game_id
        }, {
            '$push' : {
                'history' : history
            }
        })
    
    
    def load_game(self):
        Accumulate = games.find_one({
            'game_id' : self.game_id
        }, {
            'user' : 0
        })

        self.enter_stair_num = Accumulate['stair_cnt']
        self.stair_case = Accumulate['stair_case']
        self.com_stair_case = Accumulate['com_stair_case']
        
        
    def sign_up(self):
        ask_id = input('아이디를 입력해주십시오 : ')
        
        while True:
            password = input('비밀번호를 입력해주십시오 : ')
            re_type = input('비밀번호를 재입력해주십시오 : ')
            if re_type != password:
                print('비밀번호가 동일하지 않습니다, 다시 입력해주십시오.')
                continue
            
            else:
                print('계정이 생성되었습니다.')
                break

        salt = os.urandom(16)

        players.insert_one({
            'id' : ask_id,
            'password' : self.hash_password(password, salt),
            'salt' : salt
        })
        
        self.id = ask_id
        return


    def sign_in(self):
        while True:
            id = input("ID: ")
            pw = input("PW: ")

            user_info = players.find_one({
                    'id' : id
                })
            
            if not user_info:
                print('[ERROR 404] 계정 정보가 존재하지 않습니다, 회원 가입 창으로 이동합니다.')
                self.sign_up()
                return
            
            hash_pw = self.hash_password(pw, user_info['salt'])
            if id == user_info['id'] and hash_pw == user_info['password']:
                print("로그인 되었습니다.")
                self.id = id
                return

            else:
                print("로그인에 실패했습니다")
                suggest = input('다시 로그인하시겠습니까?(Y/n) : ')
                if suggest.lower() == 'y':
                    continue
                

                elif suggest.lower() == 'n':
                    print('게임을 종료합니다.')
                    return


    def hash_password(self,password, salt):
        return hashlib.sha256(salt + password.encode()).hexdigest()


계단 = stairs()

'''
JihooYoon 
Jihoo0510
Kwh
zzfqqlol
'''