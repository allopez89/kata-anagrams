from time import perf_counter as timer
def Anagrams(wordlist):
    if all(type(n) == str for n in wordlist):
        anagrams = {}

        for word in range(len(wordlist)):
            lowercased = wordlist[word].lower()
            sortedWord = "".join(sorted(lowercased))
            if sortedWord in anagrams:
                anagrams[sortedWord].append(lowercased)
            else:
                anagrams[sortedWord] = [lowercased]
        
        return len([ana for ana in anagrams if len(anagrams[ana]) > 1])
    else:
        return "The list must contain strings!"

def ReadFile(filename):
    file = open(filename, "r")
    lines = file.readlines()
    words = []

    for word in lines:
        words.append(word.replace("\n", ""))
    return words
    
def Timer():
    start = timer()
    Anagrams(ReadFile("src\wordlist.txt"))
    end = timer()
    print(end - start)
    
