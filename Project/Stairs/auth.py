import hashlib
import os

user_info = {
    'id': '',
    'password': '',
    'salt': ''
}

def sign_up():
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
    
    user_info['id'] = ask_id
    user_info['password'] = hash_password(password, salt)
    user_info['salt'] = salt

def sign_in():
    id = input("ID: ")
    pw = input("PW: ")
    
    hash_pw = hash_password(pw, user_info['salt'])
    if id == user_info['id'] and hash_pw == user_info['password']:
        print("로그인 되었습니다.")
    else:
        print("로그인에 실패했습니다")
    

def hash_password(password, salt):
    return hashlib.sha256(salt + password.encode()).hexdigest()



'''
hash알고리즘에서 똑같은 암호문을 만들어내는 재료!
'''
sign_up()

sign_in()