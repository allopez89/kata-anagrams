def Anagrams(wordlist):
    anagrams = {}

    for word in range(len(wordlist)):
        lowercased = wordlist[word].lower()
        sortedWord = "".join(sorted(lowercased))
        if sortedWord in anagrams:
            anagrams[sortedWord].append(lowercased)
        else:
            anagrams[sortedWord] = [lowercased]

    return len(anagrams)


