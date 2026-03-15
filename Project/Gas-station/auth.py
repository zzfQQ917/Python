from db import players, verifies
from mail import sendEmail
import random, hashlib, os
from datetime import datetime, timezone, timedelta
import requests 

def menu():
    print('1. Current IP check')
    print('2. Sign-up')
    print('3. Sign-in')
    print('4. Account delete')
    while True:
        try:
            option = int(input('Enter a number(1-4) to proceed with certain functions : '))
            if option == 1:
                print(getUserLocation(detail=True))
                continue
            elif option == 2:
                sign_up()
            elif option == 3:
                sign_in()
            elif option == 4:
                ent_id = input('Input your account id to progress : ')
                acc_delete(players[ent_id])
            else:
                print('The option number that you entered wasn\'t exist.')
        except:
            continue

def getUserLocation(detail=False):
    try:
        response = requests.get("https://ipinfo.io")
        data = response.json()
        returnData = f"| {data.get("ip")} | {data.get("city")}"
        if detail == True:
            returnData = f"{data.get("ip")} | {data.get("city")} | {data.get('region')} | {data.get('country')} | {data.get('loc')}"
        return returnData
    except requests.RequestException as e:
        return ""

def validate_date(date_text):
    try:
        datetime.strptime(date_text, '%Y.%m.%d')
        return True
    except ValueError:
        return False
    
def hash_password(pw, salt):
    return hashlib.sha256(salt + pw.encode()).hexdigest()

def verify_email(email):
    while True:
        #TODO
        # 이메일 인증 횟수 제한 5회 구현(5회 카운트)
        '''
        if 사용자 A가 이메일 인증을 시도
        1. 랜덤 코드 생성
        2. verify col 에서 사용자 A의 이메일 조회
        if 인증 횟수가 5번 미만 or 사용자 이메일이 verify col에 없을 때
            3. 1에서 생성한 랜덤 코드를 verify col에 직접 저장 + 인증 횟수 1 증가
            3.1. 이메일 보내긔
        elif 인증 횟수가 5 이상일 때 or 대기 시간(30분)이 남았을 때
            4. 이메일 인증 거부
        elif 인증 횟수가 5 이상 and 대기 시간이 남지 않았을 때 --> 대기 시간이 끝났을 때
            5. 인증 횟수 1로 초기화 + 1에서 생성한 랜덤 코드 저장
            5.1. 이메일 보내기
        '''

        random_pw = ''.join(random.choices('0123456789', k=6))
        verify_history = verifies.find_one({
            'email' : email
        })
        if not verify_history:
            verifies.insert_one({
                'email' : email,
                'code' : random_pw,
                'timestamp' : datetime.now(tz=timezone.utc),
                'cnt' : 1
            })
        elif verify_history['cnt'] < 5:
            verifies.update_one({
                'email' : email
            }, {
                '$inc' : {'cnt' : 1},
                '$set' : {'timestamp' : datetime.now(tz=timezone.utc), 'code' : random_pw}
            })
        elif verify_history['cnt'] >= 5 and datetime.now(timezone.utc) - verify_history['timestamp'].replace(tzinfo=timezone.utc) <= timedelta(minutes=30):
            print('You have to await until the awaiting time run out.')
            return False
        else:
            verifies.update_one({
                'email' : email
            }, {
                '$set' : {'cnt' : 1, 'timestamp' : datetime.now(timezone.utc), 'code' : random_pw}
            })
        msg = f"Hello, this is the gas station game sign-in office. \nWe found that you're signing up to the game, \nthen please enter the 6-words code that we sent below to finalize your sign-up process.\nThis is the requiring code \n'{random_pw}'"
        sendEmail(email, 'Gas station second verification e-mail', msg)
        authentication = input('\nPlease enter the 6-words code that you derived : ')
        # 6자리 코드 부합 시
        if authentication == random_pw:
            print('\nYour verification process has successfully done.')
            return True
        # 코드가 불일치할 시
        elif authentication != random_pw:
            print("\nThe verification code and the code that you typed aren't match, please re-enter the code to finalize your account registration.")
            inspection = input(f'     \nDid we sent the code to the wrong e-mail? Current e-mail is {email} (Y/n) : ')
            if inspection.lower() == 'y':
                email = input("\nPlease re-enter your email for the personal identification and second authentication : ")
                if '@' not in email:
                    print('\nIt is ESSENTIAL to put @ in your email, please enter your email once again.')
                    continue
            qualify = input('\nDo you want to re-verify? (Y/n) : ')
            if qualify.lower() == 'y':
                continue
            else:
                return False
    
def sign_up():
    while True:
        id = input('\nPlease enter your id for newly creating account(Make sure your id is under 10 letters) : ')
        # 아이디가 10자를 초과할 시
        if len(id) > 10:
            print('Re-enter your id and make sure it is under 10 letters.')
            continue
        # 해당하는 아이디가 이미 존재할 시
        elif players.find_one({
            'id' : id
        }):
            print('\nCorresponding id is already existing, please try again.')
        else:
            break

    while True:
        email = input("\nPlease enter your email for the personal identification and second authentication : ")
        # 골뱅이가 입력 받은 이메일에 부재(不在)할 시
        if '@' not in email:
            print('It is ESSENTIAL to put @ in your email, please enter your email once again.')
            continue
        # 해당 이메일이 이미 존재할 시
        elif players.find_one({
            'email' : email
        }):
            print('\nCorresponding email is already existing, please try again.')
        else:
            break
    
    if not verify_email(email):
        return

    while True:
        pw = input('\nInput your password to create your account(under 10 letters and at least over 3 letters) : ')
        # 비번이 요건(要件)을 모두 충족했을 시
        if 10 > len(pw) > 3:
            print('\nYou have successfully created a password.')
        # 요건을 충족하지 못 할 시
        else:
            print('\nYour password is not fulfill demanding, please try again.')
            continue
        final_pw = input('\nInput your password once again to fully verify : ')
        # 재확인을 위한 최종 비번이 동일하지 않을 시
        if final_pw != pw:
            print("\nTo finalize, you unconditionally enter 'exact' same password. Please try again.")
            continue
        else:
            break
    salt = os.urandom(16)
    hash_pw = hash_password(pw, salt)
    while True:
        user_name = input("\nEnter your 'real' name to continue : ")
        user_input = input("\nEnter the date that you have borned (E.g. yyyy.mm.dd) : ")
        if validate_date(user_input):
            break
        else:
            print("\nIt is inadequate form or invalid date.")
            continue
        
    players.insert_one({
        'salt' : salt,
        'hash_pw' : hash_pw,
        'name' : user_name,
        'birth' : user_input,
        'email' : email,
        'id' : id,
        'logs' : []
    })
    return id
def add_location(id):
    ip_pursuit = getUserLocation(True)
    players.update_one({
        'id' : id
    }, {
        '$push' : {
            'logs' : {
            'location' : ip_pursuit,
            'date_time' : datetime.strftime(datetime.now(), '%Y.%m.%d %H:%M:%S')
            }
        }
    })

def sign_in():
    id_cnt = 0
    while True:
        id = input('\nPlease enter your id : ')
        info = players.find_one({'id' : id})
        
        # 로그인 실패 시
        if not info:
            id_cnt += 1
            print('Id that you entered was invalid, please try again.')
            if id_cnt == 3:
                ans = input("\nWould you like to see hint for your id? (Y/n) : ")
                if ans.lower() == 'y':
                    pwned('id')
                else:
                    return False
        
        # 로그인 성공 시
        else:
            break
        
    pw_cnt = 0
    while True:
        pw = input('\nPlease enter your password : ')
        hash_pw = hash_password(pw, info['salt'])
        if hash_pw == info['hash_pw']:
            print("Log in succeed.")
            add_location(id)
            return True
        else:
            pw_cnt += 1
            print("\nLog in failed, PLEASE TRY AGAIN")
            if pw_cnt == 3:
                acc_reset = input('\no mah days watchu doin ig ya might create a brand new ass huh? (Y/n) : ')
                if acc_reset.lower() == 'y':
                    print('k i gtg for yo acc reset')
                    pwned('pw')
                else:
                    print('ya gotta give up log in, dissapointment failed')
                return False

def pwned(option):
    while True:
        e_mail = input('\nType yo email homie : ')
        acc = players.find_one({'email' : e_mail})
        if not acc:
            print('Bruh, wth is wrong with ya')
        else:
            if not verify_email(e_mail):
                return False
            break
    if option == 'id':
        origin_id = acc['id']
        target = origin_id[2:-2]
        hint = origin_id.replace(target, '*'*len(target))
        print(hint)
        return True
    else:
        input_pw = input('\ndude type yo paswad : ')
        re_input = input('\ntype again to kick yo ass : ')
        if input_pw == re_input:
            print('k gud job')
            salt = os.urandom(16)
            hash_pw = hash_password(re_input, salt)
            players.update_one({'id' : acc['id']}, {
                '$set':
                    {
                        'hash_pw' : hash_pw,
                        'salt' : salt
                    }
            })
        print('fortunately yo pw has changed')
        return True
def acc_delete(id):
    info = players.find_one({'id' : id})
    while True:
        pw = input('Type your password to proceed : ')
        hash_pw = hash_password(pw, info['salt'])
        if hash_pw == info['hash_pw']:
            print("Log in succeed.")
            break
        else:
            print('The password was incorrect.')
    deliberation = input('The procedure is irreversible. Are you sure that you SERIOUSLY thinking about deleting account? (Y/n) : ')
    if deliberation.lower() == 'y':
        print('Your account has been successfully surceased.')
        players.delete_one({'id' : id})
        os.exit(0)
    else:
        return

if __name__ == '__main__':
    sign_up()