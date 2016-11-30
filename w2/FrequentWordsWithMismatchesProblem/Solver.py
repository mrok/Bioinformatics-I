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
        return pattern
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

# solution of the problem


def group_genome_words(genome, k):
    words = {}
    for i in range(0, len(genome) - k + 1):
        box = genome[i: i + k]
        words[box] = words.get(box, 0) + 1

    return words


def count_box_occurences_with_mismatch(words, pattern, d):
    neighbors = find_neighbors(pattern, d)
    occurences = 0
    for neighbor in neighbors:
        occurences += words.get(neighbor, 0)

    return occurences


def find_frequent_word_with_mismatch(genome, k, d):
    # lets group all words from genome first
    words = group_genome_words(genome, k)

    result = []
    max_occurences = 0
    for pattern, amount in words.items():
        occurences = count_box_occurences_with_mismatch(words, pattern, d)

        if occurences == max_occurences:
            result.append(pattern)

        if occurences > max_occurences:
            result = [pattern]
            max_occurences = occurences

    return result

if __name__ == "__main__":
    # argv = sys.stdin.read().splitlines()

    argv = []
    scriptDir = os.path.dirname(os.path.realpath(__file__))
    file = open(scriptDir + '/data.txt', 'r')
    genome = file.readline().strip()
    k, d = file.readline().strip().split(' ')

    argv = [genome, k, d]
    result = find_frequent_word_with_mismatch(
        argv[0], int(argv[1]), int(argv[2]))

    result = ' '.join(map(str, result))

    print(result)

    file2 = open(scriptDir + '/solution.txt', 'w')
    file2.write(result)
