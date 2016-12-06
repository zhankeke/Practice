#coding=utf-8

'''
file = open('/Users/zhankeke/Desktop/text.txt','w')
file.write('hello world')  #open函数
'''

'''
def text_create(name,msg):  #创建文件
    desktop_path = '/Users/zhankeke/Desktop/'
    full_path = desktop_path + name +'.txt'
    file = open(full_path,'w')
    file.write(msg)
    file.close()
    print('Done')
text_create('Hello','hello world')
'''

'''
def text_filter(word,censored_word = 'lame',changed_word = 'Awesome'):
    return  word.replace(censored_word,changed_word)
print(text_filter('Python is lame'))   #敏感词过滤函数
'''

def text_create(name,msg):
    desktop_path = '/Users/zhankeke/Desktop/'
    full_path = desktop_path + name +'.txt'
    file = open(full_path,'w')
    file.write(msg)
    file.close()

def text_filter(word,censored_word = 'lame',changed_word = 'Awesome'):
    return  word.replace(censored_word,changed_word)

def censored_text_create(name,msg):
    clean_msg = text_filter(msg)
    text_create(name,clean_msg)
censored_text_create('Try','lame!lame!lame!')
print('Done')