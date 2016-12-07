num_list =[6,2,7,4,1,3,5]
letters = ['a','b','c']
print(sorted(num_list))    #按照长短、大小、英文字母顺序排序,不改变原有列表
print(sorted(num_list,reverse=True))   #倒序

for num_list,letters in zip(num_list,letters):  #组合
    print(letters,'is',num_list)


