class cocacola():
    formula = ['caffeine','sugar','water','soda']
    def __init__(self):              #初始化，不需要引用都可以执行
        self.local_logo = '可口可乐'

coke =cocacola()
print(coke.local_logo)