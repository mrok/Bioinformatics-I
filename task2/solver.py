import os
from collections import Counter

def pattern_count(dna, test):
    count = 0
    testLength = len(test)
    for i in range(0, len(dna) - testLength):
        comparedPart = dna[i:(i + testLength)]
        if (comparedPart == test):
            count = count + 1

    return count

def frequentWords(dna, amount):
    frequency = []
    for i in range(0, len(dna) - amount):
        frequency.append(dna[i:(i+amount)])

    result = Counter(frequency)
    
    result.items()
    occurences = [x[1] for x in result.items()]
    most_frequent = max(occurences)
    
    final_result = [x[0] for x in result.items() if x[1] == most_frequent]

    return final_result

scriptDir = os.path.dirname(os.path.realpath(__file__))
print(scriptDir)

file = open(scriptDir + '/data2.txt', 'r')

dna = file.readline().strip()
amount = int(file.readline().strip())

result = frequentWords(dna, amount)
print(' '.join(result)) 
