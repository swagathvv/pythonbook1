def avoids(word,forbiddenletter):
    fin=open('words.txt')
    for letter in forbiddenletter:
        if letter in word:
            return False
    return True
fin=open('words.txt')
def no_forbidden():
    forbiddenletter=raw_input('entre the forbidden letters')
    count=0
    for word in fin:
        if avoids(word.strip(),forbiddenletter):
            count= count+1
    return count

