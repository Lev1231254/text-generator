import re
from random import choices
import numpy as np



FILE_NAME = 'Harry Potter and the Sorcerers Stone.txt'
SENTENCE_LENGTH = 13
file = open(FILE_NAME, mode='r')
text = file.read()
words = np.array(re.split(r'\W+', text))
if words[-1] == '': words = words[:-1]


def setWeights(str):
    probs = {}
    summ = 0

    for i in range(len(words) - 1):
        word, nextWord = words[i], words[i+1]
        if word == str:
            if nextWord in probs: probs[nextWord] += 1
            else: probs[nextWord] = 1
            summ += 1

    if summ == 0: return None

    return probs

def chooseNextWord(word):
    probs = setWeights(word)

    keys = list(probs.keys())
    values = list(probs.values())


    
    word = choices(keys, weights=values, k=1)
    return word[0]


#main loop
message = ''
while message != 'end':
    message = input()
    
    if message != 'end' and message in words:
        currentWord = message
        output = currentWord + ' '
        for i in range(SENTENCE_LENGTH-1):
            try:
                nextWord = chooseNextWord(currentWord)
                output += nextWord + ' '
                currentWord = nextWord
            except:
                pass
        print(output)


file.close()