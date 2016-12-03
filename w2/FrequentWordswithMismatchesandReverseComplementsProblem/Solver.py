import sys
import os

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


def find_patterns_with_mismatch(genome, pattern, d):
    result = []
    pattern_len = len(pattern)
    for i in range(0, len(genome) - pattern_len + 1):
        box = genome[i: i + pattern_len]
        if calc_hamming_distance(box, pattern) <= d:
            result.append(i)

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

# problem solution


def find_word_with_mismatch(genome, k, d):
    # lets group all kmers from genome into patterns
    patterns = extrakt_kmers(genome, k)
    patterns_with_neighbors = add_patterns_neighbors(patterns, d)

    result = {}
    for pattern in patterns_with_neighbors:
        occurences = len(find_patterns_with_mismatch(genome, pattern, d))
        result[pattern] = occurences

    return result


def find_frequent_word_with_mismatch_and_reverse(genome, k, d):
    result1 = find_word_with_mismatch(genome, k, d)
    complamantary_strand = find_complamentary(genome)
    result2 = find_word_with_mismatch(complamantary_strand, k, d)

    # time to merge results
    for pattern, occurence in result2.items():
          result1[pattern] = result1.get(pattern, 0) + occurence

    maximum = max(result1.values())            
    result = [pattern for pattern, value in result1.items() if value == maximum]
    
    return result


if __name__ == "__main__":
    # argv = sys.stdin.read().splitlines()

    argv = []
    scriptDir = os.path.dirname(os.path.realpath(__file__))
    file = open(scriptDir + '/data.txt', 'r')
    genome = file.readline().strip()
    k, d = file.readline().strip().split(' ')

    argv = [genome, k, d]
    result = find_frequent_word_with_mismatch_and_reverse(
        argv[0], int(argv[1]), int(argv[2]))

    result = ' '.join(map(str, result))

    print(result)

    file2 = open(scriptDir + '/solution.txt', 'w')
    file2.write(result)
