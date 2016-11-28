import os
from collections import Counter


def find_complamentary(genome):
    reverse_table = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }

    complementary_string = ''
    for i in range(0, len(genome)):
        complementary_string = complementary_string + \
            reverse_table.get(genome[i])

    complementary_string = complementary_string[::-1]

    return complementary_string


if __name__ == "__main__":
    # argv = sys.stdin.read().splitlines()

    scriptDir = os.path.dirname(os.path.realpath(__file__))
    file = open(scriptDir + '/data.txt', 'r')
    genome = file.readline().strip()
    argv = [genome]

    result = find_complamentary(argv[0])
    print(result)