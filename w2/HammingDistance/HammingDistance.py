import sys
import os


def calc_hamming_distance(word1, word2):
    distance = 0

    assert len(word1) == len(word2)

    for i in range(0, len(word1)):
        if word1[i] != word2[i]:
            distance += 1

    return distance

if __name__ == "__main__":
    # argv = sys.stdin.read().splitlines()

    argv = []
    scriptDir = os.path.dirname(os.path.realpath(__file__))
    file = open(scriptDir + '/data.txt', 'r')
    word1 = file.readline().strip()
    word2 = file.readline().strip()

    argv = [word1, word2]
    result = calc_hamming_distance(argv[0], argv[1])
    print(result)
