from time import perf_counter as timer

def Anagrams(wordlist):
    anagrams = {}

    for word in range(len(wordlist)):
        lowercased = wordlist[word].lower()
        sortedWord = "".join(sorted(lowercased))
        if sortedWord in anagrams:
            anagrams[sortedWord].append(lowercased)
        else:
            anagrams[sortedWord] = [lowercased]

    return anagrams


filename = "src\wordlist.txt"
file = open(filename, "r")
lines = file.readlines()
words = []

for word in lines:
    words.append(word.replace("\n", ""))
start = timer()
anagrams = Anagrams(words)
# for ana in anagrams:
#     if len(anagrams[ana]) > 1:
#         print(anagrams[ana])
end = timer()
print(end - start)



