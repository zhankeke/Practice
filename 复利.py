amount = float(input('amount:'))  #资金
rate = float(input('rate:'))  #利率
time = float(input('time:'))  #时间
year = 1

while year <= time:
    print('year '+str(year)+'：$'+str((1+rate)**year*amount))
    year = year + 1
else:
    print('finish!')
