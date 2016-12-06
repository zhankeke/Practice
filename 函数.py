#coding=utf-8

def g2kg(g):
    return str(g/1000) + 'kg'

print(g2kg(2000))  # g2kg



def pythagorean_theorem(a,b):
    return  'the right triangle third side\'s length is {}'.format((a**2 +b**2)**(1/2))

print(pythagorean_theorem(3,4)) #  直角三角形斜边长