def numAxis(df):
    return df.shape[0], df.shape[1]

def numCells(df):
    return df.size


def mostPopular(df):
    wordlist = df.values.flatten().tolist() 
    populrDict = {}
    for word in wordlist:
        word = str(word)
        word = word.lower()
        if word != '':
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