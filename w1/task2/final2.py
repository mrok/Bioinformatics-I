import sys
import os
from collections import Counter

def pattern_count(genome, pattern):
    count = 0
    pattern_length = len(pattern)
    iter = range(0, len(genome) - pattern_length + 1)
    for i in iter:
        comparedPart = genome[i:(i + pattern_length)]
        if (comparedPart == pattern):
            count = count + 1

    return count

def frequent_words(genome, k):
    frequency = []
    for i in range(0, len(genome) - k + 1):
        frequency.append(genome[i:(i+k)])

    result = Counter(frequency)
    
    result.items()
    occurences = [x[1] for x in result.items()]
    most_frequent = max(occurences)
    
    final_result = [x[0] for x in result.items() if x[1] == most_frequent]

    return final_result    

if __name__ == "__main__":
    # argv = sys.stdin.read().splitlines()
    argv = []
    scriptDir = os.path.dirname(os.path.realpath(__file__))    
    file = open(scriptDir + '/data.txt', 'r')
    genome = file.readline().strip()
    k = file.readline().strip()
    argv.append(genome)
    argv.append(k)

    result = frequent_words(argv[0], int(argv[1]))
    print(' '.join(result))   