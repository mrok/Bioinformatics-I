import os
import sys
import operator
import functools

NUCLEOTIDES = ('A', 'C', 'G', 'T')


def convert_input_to_profile(strands):
    profile = {}
    row = 0
    for nucleotide in NUCLEOTIDES:
        profile[nucleotide] = [float(val) for val in strands[row].split(' ')]
        row += 1

    return profile


def calc_probability(pattern, profile):
    parts = []
    column = 0

    for nucleotide in pattern:
        parts.append(profile[nucleotide][column])
        column += 1

    prob = functools.reduce(operator.mul, parts, 1)
    return prob


def find_most_probable_kmer(text, k, profile):
    probability = 0
    kmer = ''
    for i in range(0, len(text) - k + 1):
        pattern = text[i:i + k]
        current_probability = calc_probability(pattern, profile)
        if current_probability > probability:
            probability = current_probability
            kmer = pattern

    return kmer

if __name__ == "__main__":
    # argv = sys.stdin.read().splitlines()    
    
    script_directory = os.path.realpath(os.path.dirname(__file__))
    file = open(script_directory + '/data.txt', 'r')

    lines = [line.strip() for line in file.readlines()]

    text = lines[0]
    k = int(lines[1])
    profile = convert_input_to_profile(lines[2:])
    result = find_most_probable_kmer(text, k, profile)

    print(result)
