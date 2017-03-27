import urllib
user_input = raw_input("enter a 5-digit zipcode")
user_zipcode = urllib.urlopen('http://uszip.com/zip/' + user_input)

lines = user_zipcode.readlines()

name_line = lines[7]
name = name_line[7: -17]

text = ''

for line in lines:
    new_line = line.strip()
    for word in new_line:
        text += word

pop_index = text.find("Total population") + 25
pop_end_index = text.find("<", pop_index)
pop_text = text[pop_index: pop_end_index]

print "The population of %s is %s" % (name, pop_text)
