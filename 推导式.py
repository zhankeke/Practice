'''
a = []
for i in range(1,11):
    a.append(i)
print(a)
'''

a = [i**2 for i in range(1,10)]       #列表的推导式
b = [i for i in range(1,11)]          #推导式可以节约时间
c = [j+1 for j in range(1,10)]
k = [n for n in range(1,10) if n%2==0]
z = [letter.lower() for letter in 'ABCDEFGHIGKLMN']  #大小写的转换
print(a)
print(b)
print(c)
print(k)
print(z)

d = {i:i+1 for i in range(4)}         #字典的推导式
e = {i:j for i,j in zip(range(1,6),'abcde')}
g = {i:j.upper() for i,j in zip (range(1,6),'abcde')}
print(d)
print(e)
print(g)
