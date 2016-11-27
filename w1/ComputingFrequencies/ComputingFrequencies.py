import sys
from collections import Counter
import os


def symbol_to_number(symbol):
    mapping = {
        'A': 0,
        'C': 1,
        'G': 2,
        'T': 3
    }

    return mapping.get(symbol)


def pattern_to_number(pattern):
    if len(pattern) == 1:
        return symbol_to_number(pattern)

    last_symbol = pattern[-1:]
    new_pattern = pattern[:-1]

    result = 4 * pattern_to_number(new_pattern) + symbol_to_number(last_symbol)

    return result


def compute_frequencies(genome, k):
    frequencies = [0 for i in range(4 ** k)]

    for i in range(len(genome) - k + 1):
        pattern = genome[i: i + k]
        index = pattern_to_number(pattern)
        frequencies[index] += 1

    return frequencies


if __name__ == "__main__":
    # argv = sys.stdin.read().splitlines()

    scriptDir = os.path.dirname(os.path.realpath(__file__))
    file = open(scriptDir + '/data.txt', 'r')
    genome = file.readline().strip()
    k = file.readline().strip()
    argv = [genome, k]

    result = compute_frequencies(argv[0], int(argv[1]))
    result = ' '.join(map(str, result))

    print(result)

    file2 = open(scriptDir + '/solution.txt', 'w')
    file2.write(result)
