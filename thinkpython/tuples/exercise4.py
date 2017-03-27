def sig(s):
    t= list(s)
    t.sort()
    t=''.join(t)
    return t
def all_anagrams(filename):
    d={}
    for line in open(filename):
        word=line.strip().lower()
        t=sig(word)
        if t not in d:
            d[t]=[word]
        else:
            d[t].append(word)
    return d
def print_anagram(d):
    for v in d.values():
        if len(v)>1:
            print(len(v),v)
def print_anagram_inorder(d):
    t=[]
    for v in d.values():
        if len(v)>1:
            t.append((len(v),v)
    t.sort()
    for x in t:
        print(x)
#3
def length(d,n):
    res={}
    for word,anagrams in d.iteritems():
        if len(word)==n:
            res[word]=anagrams
    return res

