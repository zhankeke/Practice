class cocacola:
    formula = ['caffeine','sugar','water','soda']  #类的属性

coke_for_me = cocacola()  #实例
coke_for_you = cocacola()

print(cocacola.formula)   #类属性的引用
print(coke_for_me.formula)
print(cocacola.formula)   #类的属性被所有类的实例共享

for element in coke_for_me.formula:
    print(element)

coke_for_China = cocacola()
coke_for_China.local_logo = '可口可乐'  #创建实例属性
print(coke_for_China.local_logo)       #打印实例属性引用结果