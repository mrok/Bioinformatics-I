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

if __name__ == "__main__":
    # argv = sys.stdin.read().splitlines()

    scriptDir = os.path.dirname(os.path.realpath(__file__))
    file = open(scriptDir + '/data.txt', 'r')
    genome = file.readline().strip()
    argv = [genome]

    result = pattern_to_number(argv[0])
    print(result)
