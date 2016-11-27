import sys
import os
from collections import Counter

reverse_table = {
    'A': 'T',
    'T': 'A',
    'C': 'G',
    'G': 'C'
}


def reverse_complement(genome):
    complementary_string = ''
    for i in range(0, len(genome)):
        nucleotide = reverse_table.get(genome[i])
        complementary_string = complementary_string + nucleotide

    return complementary_string[::-1]

if __name__ == "__main__":
    # argv = sys.stdin.read().splitlines()
    scriptDir = os.path.dirname(os.path.realpath(__file__))
    file = open(scriptDir + '/data.txt', 'r')
    genome = file.readline().strip()
    argv = [genome]

    result = reverse_complement(argv[0])
    print(result)
