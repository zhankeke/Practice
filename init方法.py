class cocacola():
    formula = ['caffeine','sugar','water','soda']
    def __init__(self,logo_name):
        #初始化，不需要引用都可以执行
        for element in self.formula:
            print('has {}'.format(element))

        self.local_logo = logo_name

coke = cocacola('可口可乐')
print(coke.local_logo)
