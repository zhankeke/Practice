fruit = ['pineapple','pear']          #在某个位置插入元素
fruit.insert(1,'grape')
print(fruit[1])
print(fruit)

fruit[0:0]=['orange']                 #在最前面插入元素
print(fruit)

fruit.insert(100,'banana')            #超出长度，则在最后面插入元素
print(fruit)