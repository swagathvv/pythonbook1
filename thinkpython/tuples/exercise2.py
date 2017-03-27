def random(words):
    t=[]
    for word in words:
       t.append((len(word),random.random(),word))
    t.sort(reverse=True)
    res=[]
    for length,_,word in t:
        res.append(word)
    return res

