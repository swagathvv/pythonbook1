count=0
count=0
fin= open('words.txt')
for line in fin:
	if len(line)>=20:
		line=line.strip()
		print(line)
		count=count+1
	count1=count1+1

