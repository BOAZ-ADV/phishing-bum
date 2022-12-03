# aug based RD
# hyper-parameter : w = 0.1
w = 0.1


# p = 삭제 확률
def random_deletion(words, p):

	if len(words) == 1:
		return words

	new_words = []
	for word in words:
		r = random.uniform(0, 1)

		if r > p:
			new_words.append(word)

	if len(new_words) == 0:
		rand_int = random.randint(0, len(words) - 1)
		return [words[rand_int]]

	return new_words


def RD(df):
	
    for i in range(len(df)):
        df.iloc[i,0] = ' '.join(random_deletion(df.iloc[i,0].split(' '),w))

    return df