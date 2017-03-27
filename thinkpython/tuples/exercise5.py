def distance(word1,word2):
    assert len(word1)==len(word2)
    x=0
    for c1,c2 in zip(word1,word2):
        if c1!=c2:
            x=x+1
    return x
def metathesis_pairs(d):
    for anagrams in d.intervalues():
        for word1 in anagrams:
            if word1<word2 and distance(word1,word2)==2:
                print(word1,word2)

