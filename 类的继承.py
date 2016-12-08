class cocacola:
    calories =140
    sodium = 45
    caffeine = 34
    ingredients =[
        'high fructose corn syrup',
        'caffeine'
    ]
    def __init__(self,logo_name):
        self.local_logo = logo_name  #用输入的数据赋值

    def drink(self):
        print('you got {} cal energy'.format(self.calories))
        print('you got {} mg caffeine'.format(self.caffeine))


class caffeine_free(cocacola):   #类的继承
    caffeine = 0
    ingredients = [
        'high fructose corn syrup',
    ]

coke_a = caffeine_free('cocacola-free')
print(coke_a.local_logo)
coke_a.drink()