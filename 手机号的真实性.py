number=input('number:')
CN_mobile = \
    [134,135,136,137,138,139,150,151,152,157,158,159,182,183,184,187,188,147,178,1705]
CN_union = \
    [130,131,132,155,156,185,186,145,176,1709]
CN_telecom = \
    [133,153,180,181,189,177,1700]
import re  #正则

def num_indefy():
    if re.findall('[0-9]+',number):  #搜索string，以列表形式返回全部能匹配的子串
        while len(number) == 11:     #验证长度
            if number in CN_mobile or CN_union or CN_telecom:  #验证运营商
                print('We are sending verification code via text to your phone', number)
            else:
                print('no such a operator')
        else:
            print('invalid length,your number should be in 11 digits')
    else:
        print('input number please!')

num_indefy()

