def word_count(words):
	wordcount = {}
	for word in words.split():
		if word not in wordcount:
			wordcount[word] = 1
		else:
			wordcount[word] += 1

	return wordcount
