for name in range(1,11):
    desktop_path = '/Users/zhankeke/Desktop/'
    full_path = desktop_path + str(name) +'.txt'
    file = open(full_path,'w')
    file.close()
    print('Done')
