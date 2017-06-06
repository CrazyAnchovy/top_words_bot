import operator

print('imported operator')

with open ('word_list.txt', 'r') as word_list:
    used_words = word_list.read().split(',')

print('opened up the file and read it to make a list')

word_freq_dict = {}

print('word_freq_dict created')

for word in used_words:
    print(word)
    word_freq = used_words.count(word)
    word_freq_dict[word] = word_freq
    
print('list mapped to dict')
    



print(sorted(word_freq_dict.items(),reverse=True, key=operator.itemgetter(1)))