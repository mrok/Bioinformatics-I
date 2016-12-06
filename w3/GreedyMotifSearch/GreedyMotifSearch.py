import os
import sys
import operator
import functools

NUCLEOTIDES = ('A', 'C', 'G', 'T')

# functions copied from other file, stepik.org allows to upload single
# file only


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
    kmer = text[:k]
    for i in range(0, len(text) - k + 1):
        pattern = text[i:i + k]
        current_probability = calc_probability(pattern, profile)
        if current_probability > probability:
            probability = current_probability
            kmer = pattern

    return kmer


def calc_hamming_distance(pattern1, pattern2):
    # word1.length > word2.length
    # d(GATTCTCA, GCAAAGACGCTGACCAA) = 3.

    def find_distance(string1, string2):
        assert len(string1) == len(string2)
        distance = 0

        for i in range(0, len(string1)):
            if string1[i] != string2[i]:
                distance += 1

        return distance

    assert len(pattern2) >= len(pattern1)

    sub_words = []

    pattern1_length = len(pattern1)
    for i in range(0, len(pattern2) - pattern1_length + 1):
        sub_words.append(pattern2[i:i + pattern1_length])

    result = {word: find_distance(word, pattern1) for word in sub_words}
    minimum = min(result.values())

    return minimum


def calc_hamming_distance_from_many_words(patterns, dnas):
    # sum of distances between Pattern and all strings in Dna
    distances = [calc_hamming_distance(patterns, dna) for dna in dnas]
    distnace = sum(distances)

    return distnace

# problem solution


def find_consensus(motif):
    length = len(motif[0])
    amount = len(motif)
    consensus = [None] * length

    for column in range(0, length):
        nucleotide_in_column = [strand[column] for strand in motif]
        max_freq = 0
        for nucleotide in NUCLEOTIDES:
            freq = nucleotide_in_column.count(nucleotide) / amount
            if freq > max_freq:
                consensus[column] = nucleotide
                max_freq = freq

    return ''.join(consensus)


def score_motifs(motif):
    consensus = find_consensus(motif)
    result = calc_hamming_distance_from_many_words(consensus, motif)

    return result


def create_profile(strands):
    length = len(strands[0])
    amount = len(strands)
    profile = {
        'A': [],
        'C': [],
        'G': [],
        'T': []
    }

    for column in range(0, length):
        nucleotide_in_column = [strand[column] for strand in strands]
        for nucleotide in NUCLEOTIDES:
            freq = nucleotide_in_column.count(nucleotide) / amount
            profile[nucleotide].append(freq)

    return profile


def greedy_motif_search(dnas, k, t):
    best_motifs = [dna[0:k] for dna in dnas]

    for i in range(0, len(dnas[0]) - k + 1):
        motifs = [dnas[0][i:i + k]]
        for j in range(1, t):
            profile = create_profile(motifs)
            next_motif = find_most_probable_kmer(dnas[j], k, profile)
            motifs.append(next_motif)
        if score_motifs(motifs) < score_motifs(best_motifs):
            best_motifs = motifs[:]

    return best_motifs


if __name__ == "__main__":
    # argv = sys.stdin.read().splitlines()

    script_directory = os.path.realpath(os.path.dirname(__file__))
    file = open(script_directory + '/data.txt', 'r')

    lines = [line.strip() for line in file.readlines()]

    [k, t] = lines[0].split(' ')
    dnas = lines[1:]
    result = greedy_motif_search(dnas, int(k), int(t))

    result = ' '.join(result)

    print(result)
    file2 = open(script_directory + '/solution.txt', 'w')
    file2.write(result)    
