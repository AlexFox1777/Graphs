from util import Stack, Queue  # These may come in handy

'''
Given two words (begin_word and end_word), and a dictionary's word list, return the shortest transformation sequence from begin_word to end_word, such that:
Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that begin_word is not a transformed word.
Note:
Return None if there is no such transformation sequence.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume begin_word and end_word are non-empty and are not the same.
'''

f = open("words.txt", "r")

words_list = f.read().split("\n")

f.close()

words = {}

for word in words_list:
    words[word] = word


def findTransformedWord(begin_word, end_word):
    # create transform word from begin_word
    # iterate through end_word
    # change one letter in transform word
    # if tw exists in words add to path
    # get the last word in a path and repeat

    stack = Stack()
    stack.push([begin_word])

    last = stack.pop()
    new_tw = list(last[-1])
    for l in range(len(end_word)):
        new_tw[l] = end_word[l]
        tw = ''.join(new_tw)
        if tw in words:
            last.append(tw)
            stack.push(list(last))
            if tw == end_word:
                return stack.stack[-1]
    return None


print(findTransformedWord("hit", 'cog'))
