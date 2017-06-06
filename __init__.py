import praw
import string
import operator

reddit = praw.Reddit('top_words_bot')
comments = reddit.subreddit('all').comments(limit = 10000)

saved_comments = []
temp_word_list = []
count_temp = []

with open ('saved_comment_ids.txt', 'r') as saved_comment_ids:
    saved_comments = saved_comment_ids.read().split(',')


for comment in comments:
    if comment in saved_comments:    #don't reuse any comments(accuracy in freq.count)
        pass
    saved_comments.append(comment)
    with open ('saved_comment_ids.txt', 'a') as saved_comment_ids:
        saved_comment_ids.seek(0,2)
        saved_comment_ids.write(str(comment)+',')
    comment.body = ''.join(letter for letter in comment.body if letter not in string.punctuation)
    comment = comment.body.split(' ')
    for word in comment:
        word = word.lower()
        word.strip('\n')
        temp_word_list.append(word)

    
with open ('word_list.txt', 'a') as word_list:
    for word in temp_word_list:
        word_list.seek(0,2)
        try:
            word_list.write(str(word) +',')       
        except UnicodeEncodeError:
            pass



amount_of_comments_gathered = len(saved_comments)
    

print (amount_of_comments_gathered)

frequency_dict = {}

for word in temp_word_list:
    if word in count_temp:
        pass
    if word is ' ':
        pass
    if word is '':
        pass
    count_temp.append(word)
    count_check = temp_word_list.count(word)
    frequency_dict[word.encode()] = count_check


    

print(sorted(frequency_dict.items(), key=operator.itemgetter(1)))

"""
need to write the current dict into a file and learn how to update it
here: https://stackoverflow.com/questions/11026959/writing-a-dict-to-txt-file-and-reading-it-back
"""
