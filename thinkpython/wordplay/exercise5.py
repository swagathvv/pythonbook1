def uses_all(word,string):
    for char in string:
        if char not in word:
            return False
    return True

