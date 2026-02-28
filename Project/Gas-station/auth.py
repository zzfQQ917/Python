from db import players
from mail import sendEmail
import random, hashlib, os
from datetime import datetime

def validate_date(date_text):
    try:
        datetime.strptime(date_text, '%Y.%m.%d')
        return True
    except ValueError:
        return False
def hash_password(pw, salt):
    return hashlib.sha256(salt + pw.encode()).hexdigest()

def sign_up():
    while True:
        id = input('\nPlease enter your id for newly creating account(Make sure your id is under 10 letters) : ')
        if len(id) > 10:
            print('Re-enter your id and make sure it is under 10 letters.')
            continue
        elif players.find_one({
            'id' : id
        }):
            print('\nCorresponding id is already existing, please try again.')
        else:
            break

    while True:
        email = input("\nPlease enter your email for the personal identification and second authentication : ")
        if '@' not in email:
            print('It is ESSENTIAL to put @ in your email, please enter your email once again.')
            continue
        elif players.find_one({
            'email' : email
        }):
            print('\nCorresponding email is already existing, please try again.')
        else:
            break
    
    while True:
        #TODO
        # 이메일 인증 횟수 제한 5회 구현(5회 카운트)

        random_pw = ''.join(random.choices('0123456789', k=6))
        msg = f"Hello, this is the gas station game sign-in office. \nWe found that you're signing up to the game, \nthen please enter the 6-words code that we sent below to finalize your sign-up process.\nThis is the requiring code \n'{random_pw}'"
        sendEmail(email, 'Gas station second verification e-mail', msg)
        authentication = input('Please enter the 6-words code that you derived : ')
        if authentication == random_pw:
            print('\nYour verification process has successfully done.')
            break
            
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
                return
    
    while True:
        pw = input('\nInput your password to create your account(under 10 letters and at least over 3 letters) : ')
        if 10 > len(pw) > 3:
            print('\nYou have successfully created a password.')
        else:
            print('\nYour password is not fulfill demanding, please try again.')
            continue
        final_pw = input('\nInput your password once again to fully verify : ')
        if final_pw != pw:
            print("\nTo finalize, you unconditionally enter 'exact' same password. Please try again.")
            continue
        else:
            break
    salt = os.urandom(16)
    hash_pw = hash_password(pw, salt)
    while True:
        user_name = input("Enter your 'real' name to continue : ")
        user_input = input("Enter the date that you have borned (E.g. yyyy.mm.dd) : ")
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
        'id' : id
    })

def sign_in():
    id_cnt = 0
    while True:
        id = input('Please enter your id : ')
        info = players.find_one({'id' : id})
        if not info:
            id_cnt += 1
            print('Id that you entered was invalid, please try again.')
            if id_cnt == 3:
                pwned(id)
            continue
        else:
            break
    pw_cnt = 0
    while True:
        pw = input('Please enter your password : ')
        hash_pw = hash_password(pw, info['salt'])
        if hash_pw == info['hash_pw']:
            print("Log in succeed.")
            return
        else:
            pw_cnt += 1
            print("Log in failed, PLEASE TRY AGAIN")
            if pw_cnt == 3:
                acc_reset = input('o mah days watchu doin ig ya might create a brand new ass huh? (Y/n) : ')
                if acc_reset.lower() == 'y':
                    print('k i gtg for yo acc reset')
                    pwned(pw)
                else:
                    print('ya gotta give up log in, dissapointment failed')
                return False
            continue

def pwned(option):
    while True:
        e_mail = input('Type yo email homie : ')
        acc = players.find_one({'email' : e_mail})
        if not acc:
            print('Bruh, wth is wrong with ya')
            continue
        else:
            while True:
                random_pw = ''.join(random.choices('0123456789', k=6))
                msg = f"Hello, this is the gas station game sign-in office. \nWe found that you're signing up to the game, \nthen please enter the 6-words code that we sent below to finalize your sign-up process.\nThis is the requiring code \n'{random_pw}'"
                sendEmail(e_mail, 'Gas station second verification e-mail', msg)
                authentication = input('Please enter the 6-words code that you derived : ')
                if authentication == random_pw:
                    print('\nYour verification process has successfully done.')
                    break
                    
                elif authentication != random_pw:
                    print("\nThe verification code and the code that you typed aren't match, please re-enter the code to finalize your account registration.")
                    inspection = input(f'     \nDid we sent the code to the wrong e-mail? Current e-mail is {e_mail} (Y/n) : ')
                    if inspection.lower() == 'y':
                        e_mail = input("\nPlease re-enter your email for the personal identification and second authentication : ")
                        if '@' not in e_mail:
                            print('\nIt is ESSENTIAL to put @ in your email, please enter your email once again.')
                            continue
                    qualify = input('\nDo you want to re-verify? (Y/n) : ')
                    if qualify.lower() == 'y':
                        continue
                    else:
                        return
            break
    if option == 'id':
        origin_id = acc['id']
        target = origin_id[2:-2]
        hint = origin_id.replace(target, '*'*len(target))
        print(hint)
    else:
        input_pw = input('dude type yo paswad : ')
        re_input = input('type again to kick yo ass : ')
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
        return
pwned('id')