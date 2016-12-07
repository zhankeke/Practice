import string
path = '/Users/zhankeke/Documents/Python/Walden.txt'

with open(path,'r') as text:
    words = [raw_word.strip(string.punctuation).lower() for raw_word in text.read().split()]
    #去除连在一起的标点符号，转化成小写
    words_index = set(words)   #用集合去重
    counts_dict = {index:words.count(index) for index in words_index}


#以字典中的值排序
for word in sorted(counts_dict,key=lambda x: counts_dict[x],reverse= True):
    print('{} -- {} times'.format(word,counts_dict[word]))
