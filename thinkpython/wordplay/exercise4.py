fin=open('words.txt')
def uses_only(word,string):
    for char in word:
        if char not in string:
            return False
    return True
