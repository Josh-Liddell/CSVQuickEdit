# import re
import pandas as pd


def numCells(df):
    return df.size


def mostPopular(df):
    wordlist = df.values.flatten().tolist() 
    populrDict = {}
    for word in wordlist:
        word = str(word)
        word = word.lower()
        if word in populrDict:
            populrDict[word] += 1
        else:
            populrDict[word] = 1

    top3 = []
    for i in range(3):
        maxname = max(populrDict, key=populrDict.get)
        top3.append((maxname, populrDict[maxname]))
        del populrDict[maxname]
    return top3












# .txt file anaylsis


# using this function to obtain list of words excluding all possible puctuation varieties
# def splitSentence(sentence): 
#     words = re.findall(r'\b\w+\b', sentence)
#     return words

# def wordCount(contents):
#     wordlist = contents.split()
#     return len(wordlist)

# def numCharacters(contents): # not including spaces
#     num = 0
#     contents = list(contents)
#     for x in contents:
#         if x != ' ':
#             num += 1
#     return num


