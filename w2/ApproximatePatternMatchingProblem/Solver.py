import sys
import os


def calc_hamming_distance(word1, word2):
    distance = 0

    assert len(word1) == len(word2)

    for i in range(0, len(word1)):
        if word1[i] != word2[i]:
            distance += 1

    return distance


def find_patter_with_mismatch(genome, pattern, d):
    result = []
    pattern_len = len(pattern)
    for i in range(0, len(genome) - pattern_len + 1):
        box = genome[i: i + pattern_len]
        if calc_hamming_distance(box, pattern) <= d:
            result.append(i)

    return result

if __name__ == "__main__":
    # argv = sys.stdin.read().splitlines()

    argv = []
    scriptDir = os.path.dirname(os.path.realpath(__file__))
    file = open(scriptDir + '/data.txt', 'r')
    pattern = file.readline().strip()
    genome = file.readline().strip()
    d = file.readline().strip()

    argv = [pattern, genome, d]
    result = find_patter_with_mismatch(argv[1], argv[0], int(argv[2]))
    result = map(str, result)
    result = ' '.join(result)
    print(result)

    file2 = open(scriptDir + '/solution.txt', 'w')
    file2.write(result)    
