import sys
import os


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

if __name__ == "__main__":
    # argv = sys.stdin.read().splitlines()

    argv = []
    scriptDir = os.path.dirname(os.path.realpath(__file__))
    file = open(scriptDir + '/data.txt', 'r')
    pattern = file.readline().strip()
    d = file.readline().strip()
    argv = [pattern, d]

    result = find_neighbors(argv[0], int(argv[1]))
    result = '\n'.join(result)
    print(result)

    file2 = open(scriptDir + '/solution.txt', 'w')
    file2.write(result)
