import os


def pattern_count(dna, test):
    count = 0
    testLength = len(test)
    for i in range(0, len(dna) - testLength):
        comparedPart = dna[i:(i + testLength)]
        if (comparedPart == test):
            count = count + 1

    return count


scriptDir = os.path.dirname(os.path.realpath(__file__))
print(scriptDir)

file = open(scriptDir + '/data.txt', 'r')

dna = file.readline().strip()
test = file.readline().strip()

print(pattern_count(dna, test))
