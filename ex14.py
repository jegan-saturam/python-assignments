contents = open("extext.txt", "r")
wordseq = dict()
for line in contents:
	line = line.strip()
	line = line.lower()
	words = line.split(" ")
	for word in words:
		if word in wordseq:
			wordseq[word] = wordseq[word] + 1
		else:
			wordseq[word] = 1
for key in list(wordseq.keys()):
    print(key, ":", wordseq[key])