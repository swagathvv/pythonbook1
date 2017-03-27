def no_e(word):
    for letter in word:
        if letter =='e':
            return False
    return True
def has_no_e():
    fin = open('words.txt')
    for words in fin:
        word = words.strip()
        if no_e(word):
            print word
