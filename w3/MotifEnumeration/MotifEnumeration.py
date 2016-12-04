import os
import itertools

# functions copied from other file, stepik.org allows to upload single
# file only

NUCLEOTIDES = ['A', 'T', 'C', 'G']


def calc_hamming_distance(word1, word2):
    distance = 0

    assert len(word1) == len(word2)

    for i in range(0, len(word1)):
        if word1[i] != word2[i]:
            distance += 1

    return distance


def find_neighbors(pattern, d):
    if d == 0:
        return [pattern]
    if len(pattern) == 1:
        return NUCLEOTIDES

    result = set()
    rest = pattern[1:]
    suffix_neighbors = find_neighbors(rest, d)
    for text in suffix_neighbors:
        if calc_hamming_distance(text, rest) < d:
            for acid in NUCLEOTIDES:
                result.add(acid + text)
        else:
            result.add(pattern[0:1] + text)

    return result


def extrakt_kmers(genome, k):
    patterns = []
    for i in range(0, len(genome) - k + 1):
        box = genome[i: i + k]
        patterns.append(box)

    return list(set(patterns))


def add_patterns_neighbors(patterns, d):
    result = list(patterns)
    for pattern in patterns:
        result.extend(find_neighbors(pattern, d))

    return list(set(result))


def has_pattern_with_mismatch(genome, pattern, d):
    pattern_len = len(pattern)
    for i in range(0, len(genome) - pattern_len + 1):
        box = genome[i: i + pattern_len]
        if calc_hamming_distance(box, pattern) <= d:
            return True

    return False

# problem solution


def motif_enumeration(dnas, k, d):
    result = {}
    requested_occurences = len(dnas)

    # find all k-mers in all dna string  
    patterns = [extrakt_kmers(dna, k) for dna in dnas]
    patterns = itertools.chain.from_iterable(patterns)
    patterns = list(set(patterns))

    # find all neighbors of previously found k-mers
    patterns = [find_neighbors(pattern, d) for pattern in patterns]
    patterns = itertools.chain.from_iterable(patterns)
    patterns = list(set(patterns))


    for pattern in patterns:
        result[pattern] = 0
        for dna in dnas:
            if has_pattern_with_mismatch(dna, pattern, d):
                result[pattern] += 1

    result = [key for key, value in result.items() if value == requested_occurences]

    return result


if __name__ == "__main__":
    script_directory = os.path.dirname(os.path.realpath(__file__))
    file = open(script_directory + '/data.txt', 'r')
    lines = [line.strip() for line in file.readlines()]

    [k, d] = lines[0].split(' ')
    result = motif_enumeration(lines[1:], int(k), int(d))
    result = ' '.join(result)

    print(result)
