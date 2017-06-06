with open ('word_list.txt', 'r') as word_list:
    used_words = word_list.read().split(',')
    
print (len(used_words))