password_list = '12345'

def account_login():
    tries = 0
    while tries < 3:
        password = input('Password:')
        password_correct = password == password_list
        if password_correct:
            print('Login success!')
        else:
            print('Wrong password or invalid input!')
            tries = tries + 1
    else:
        print('your account has been suspended')

account_login()