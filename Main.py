def main():
	vocab = raw_input()
	while(vocab != ""):
		print "The string '" + vocab + "' contains " + str(count(vocab.upper())) + " palindromes."
		vocab = raw_input()

def count(vocab):
	list = []
	for i in range(1, len(vocab) + 1):
		for s in range(0, len(vocab) + 1 - i):
			if (verify(vocab[s : s + i])) and (vocab[s : s + i] not in list):
				list.append(vocab[s : s + i])

	return len(list)


def verify(vocab):
	if len(vocab) == 1 or len(vocab) == 0:
		return True

	if vocab[0] != vocab[len(vocab) - 1]:
		return False

	return verify(vocab[1 : len(vocab) - 1])


#this is used to initialize a main function
if __name__ == "__main__":
	main();