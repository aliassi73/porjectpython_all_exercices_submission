import string
def counttheworlds(text):
    text = text.lower()
    for p in string.punctuation:   
        text = text.replace(p,"")  
    words = text.split()
    wordnum = {}
    for word in words:
        if word in wordnum:
            wordnum[word] += 1
        else:
            wordnum[word] = 1
    return wordnum
text = "Ai is the future, The future is now."
print(counttheworlds(text))           

