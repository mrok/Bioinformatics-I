import os
import sys
import random
import functools
import operator

NUCLEOTIDES = ('A', 'C', 'G', 'T')

# functions copied from other file, stepik.org allows to upload single
# file only


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


def create_profile_with_pseudocount(strands):
    length = len(strands[0])
    # 4 is added because assumption that each nucleotide appears at least once
    amount = len(strands) + 4
    profile = {
        'A': [],
        'C': [],
        'G': [],
        'T': []
    }

    for column in range(0, length):
        nucleotide_in_column = [strand[column] for strand in strands]
        for nucleotide in NUCLEOTIDES:
            freq = (1 + nucleotide_in_column.count(nucleotide)) / amount
            profile[nucleotide].append(freq)

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
    kmer = text[:k]
    for i in range(0, len(text) - k + 1):
        pattern = text[i:i + k]
        current_probability = calc_probability(pattern, profile)
        if current_probability > probability:
            probability = current_probability
            kmer = pattern

    return kmer


# problem solution

def random_kmers(dnas, k):
    # build motifs from randomly chosen kmers
    motifs = []
    dna_length = len(dnas[0])
    for dna in dnas:
        start = random.randint(0, dna_length - k)
        motif = dna[start:start + k]
        motifs.append(motif)

    return motifs


def randomize_motif_search(k, t, dnas):
    motifs = random_kmers(dnas, k)
    best_motifs = motifs.copy()

    while True:
        profile = create_profile_with_pseudocount(motifs)
        motifs = []

        for dna in dnas:
            next_motif = find_most_probable_kmer(dna, k, profile)
            motifs.append(next_motif)

        best_motifs_score = score_motifs(best_motifs)
        motif_score = score_motifs(motifs)
        if motif_score < best_motifs_score:
            best_motifs = motifs.copy()
        else:
            return {'motifs': best_motifs, 'score': best_motifs_score}


def randomize_motif_search_multi_run(k, t, dnas, cycles):
    # cycles define how many attempts of finding the best motfi must be
    # performed
    best_score = float("inf")
    motifs = None
    for i in range(0, cycles):
        result = randomize_motif_search(k, t, dnas)
        if result['score'] < best_score:
            print(str(i) + " score: " + str(result['score']))            
            best_score = result['score']
            motifs = result['motifs']

    return motifs


if __name__ == "__main__":
    # argv = sys.stdin.read().splitlines()    
    script_dir = os.path.realpath(os.path.dirname(__file__))

    file = open(script_dir + '/data.txt', 'r')
    lines = [line.strip() for line in file.readlines()]

    [k, t] = lines[0].split(' ')
    dnas = lines[1:]

    result = randomize_motif_search_multi_run(int(k), int(t), dnas, 1000)
    result = "\n".join(result)

    print(result)
