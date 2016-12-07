NASDAQ_code = {         #又叫键值对
    'bidu':'baidu',     #键是唯一的，不可修改
    'sina':'sina',      #值就可变的，可为任何对象
}

NASDAQ_code['yoku'] = 'youku'    #插入单个值
print(NASDAQ_code)

NASDAQ_code.update({'fb':'facebook','tsla':'tesla'})    #插入多个键值对
print(NASDAQ_code)

del NASDAQ_code['fb']            #删除
print(NASDAQ_code)