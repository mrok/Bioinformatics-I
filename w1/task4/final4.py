import sys
import os
from collections import Counter


def find_occurences(genome, pattern):
    positions = []

    for i in range(0, (len(genome) - len(pattern) + 1)):
        tested = genome[i:i + len(pattern)]
        if tested == pattern:
            positions.append(i)

    return positions

if __name__ == "__main__":
    # argv = sys.stdin.read().splitlines()
    scriptDir = os.path.dirname(os.path.realpath(__file__))
    file = open(scriptDir + '/data.txt', 'r')
    pattern = file.readline().strip()
    genome = file.readline().strip()
    argv = [pattern, genome]

    result = find_occurences(argv[1], argv[0])
    print(' '.join([str(x) for x in result]))
