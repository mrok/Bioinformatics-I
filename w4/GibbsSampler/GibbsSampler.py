import os
import sys
import random
import functools
import operator

NUCLEOTIDES = ('A', 'C', 'G', 'T')

# functions copied from other file, stepik.org allows to upload single
# file only


def create_profile_with_pseudocount(motifs):
    length = len(motifs[0])
    # 4 is added because assumption that each nucleotide appears at least once
    amount = len(motifs) + 4
    profile = {
        'A': [],
        'C': [],
        'G': [],
        'T': []
    }

    for column in range(0, length):
        nucleotide_in_column = [motif[column] for motif in motifs]
        for nucleotide in NUCLEOTIDES:
            freq = (1 + nucleotide_in_column.count(nucleotide)) / amount
            profile[nucleotide].append(freq)

    return profile


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


def calc_probability(pattern, profile):
    parts = []
    column = 0

    for nucleotide in pattern:
        parts.append(profile[nucleotide][column])
        column += 1

    prob = functools.reduce(operator.mul, parts, 1)
    return prob

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


def random_best_motif(dna, profile, k):
    # return k-length motif from dna selected in weighted random process  
    data = {}
    weights = []
    for i in range(0, len(dna) - k + 1):
        kmer = dna[i:i + k]
        prob = calc_probability(kmer, profile)
        data[i] = {'kmer': kmer,
                   'prob': prob
                   }
        weights.append(prob)

    # time to perform weighted random
    randomed_value = random.uniform(0, sum(weights))
    prob_sum = 0
    for i in range(0, len(weights)):
        prob_sum += weights[i]
        if randomed_value < prob_sum:
            return data[i]['kmer']


def gibbs_sampler(dnas, k, t, N):
    motifs = random_kmers(dnas, k)
    best_motifs = motifs.copy()
    best_motifs_score = score_motifs(best_motifs)

    for i in range(0, N):

        processed_row = random.randint(0, t - 1)
        del motifs[processed_row]

        profile = create_profile_with_pseudocount(motifs)

        next_motif = random_best_motif(dnas[processed_row], profile, k)
        motifs.insert(processed_row, next_motif)

        motif_score = score_motifs(motifs)
        if motif_score < best_motifs_score:
            best_motifs = motifs.copy()
            best_motifs_score = motif_score

    print (best_motifs_score)        
    return best_motifs


def main():
    # argv = sys.stdin.read().splitlines()
    script_dir = os.path.realpath(os.path.dirname(__file__))

    file = open(script_dir + '/data.txt', 'r')
    lines = [line.strip() for line in file.readlines()]

    [k, t, N] = lines[0].split(' ')
    dnas = lines[1:]

    result = gibbs_sampler(dnas, int(k), int(t), int(N))
    result = "\n".join(result)

    print(result)
    file2 = open(script_dir + '/solution.txt', 'w')
    file2.write(result)    
    


if __name__ == "__main__":
    main()
