import re

# using this function to obtain list of words excluding all possible puctuation varieties
def splitSentence(sentence): 
    words = re.findall(r'\b\w+\b', sentence)
    return words

def wordCount(contents):
    wordlist = contents.split()
    return len(wordlist)

def numCharacters(contents): # not including spaces
    num = 0
    contents = list(contents)
    for x in contents:
        if x != ' ':
            num += 1
    return num

# Returns of list that contains top 3 most common words and how many occurences for each
def mostPopular(contents):
    wordlist = splitSentence(contents)
    populrDict = {}
    for word in wordlist:
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

