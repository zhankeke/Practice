def account_login():
    password = input('Password:')
    password_correct = password == '12345'
    if password_correct:
        print('Login success!')
    else:
        print('Wrong password or invalid input!')
        account_login()

account_login()