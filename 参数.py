#coding=utf-8

def trapezoid_area(base_up, base_down, height):
    return 1/2 * (base_up + base_down) * height

print(trapezoid_area(1,2,3))    #  位置参数计算梯形面积


def trapezoid_area(base_up, base_down, height):
    return 1/2 * (base_up + base_down) * height

print(trapezoid_area(base_up=1,base_down=2,height=3))    #  关键词参数计算梯形面积