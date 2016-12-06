import  random  #摇骰子
def roll_dice(numbers=3,points=None):
    print('<<<<< ROLL THE RICE! >>>>>')
    if points is None:
        points = []
    while numbers > 0:
        point = random.randrange(1,7)
        points.append(point)
        numbers = numbers - 1
    return points

def roll_result(total):  #计算结果
    isBig = 11 <= total <=18
    isSmall = 3<= total <=10
    if isBig:
        return  'Big'
    elif isSmall:
        return  'Small'

def start_game():  #开始游戏
    money = 1000
    while money > 0:
        print('<<<<< GAME STARTS! >>>>>')
        choices = ['Big','Small']
        your_choice = input('Big or Small :')
        money_bet = float(input('how much will you bet:'))
        if your_choice in choices:
            points = roll_dice()
            total = sum(points)
            youWin = your_choice == roll_result(total)
            if youWin:
                print('the points are',points,'you win!')
                money = money + money_bet
                print('your money is:',money)
            else:
                print('the points are',points,'you lose!')
                money =money - money_bet
                print('your money is:',money)
        else:
            print('invalid words')
            start_game()
    else:
        print('you have no money.game over!')  #没钱了就结束

start_game()


'''
def guesswhat():
    guess = input('big or small:')
    import  random  # 随机数
    point1 = random.randrange(1,7)
    point2 = random.randrange(1,7)
    point3 = random.randrange(1,7)
    point_list = [point1,point2,point3]

    if 11<=sum(point_list)<=18:
        result = 'big'
    else:
        result = 'small'

    if guess == result :
        print('the points are',point_list,"You win!")
        guesswhat()
    else:
        print('the points are',point_list,"You lose!")
        guesswhat()

guesswhat()
'''