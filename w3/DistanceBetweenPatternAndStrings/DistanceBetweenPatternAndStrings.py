import os
import sys

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


def calc_hamming_distance_from_many_words(pattern, strands):
    # sum of distances between Pattern and all strings in Dna
    distances = [calc_hamming_distance(pattern, dna) for dna in strands]
    distnace = sum(distances)

    return distnace



if __name__ == "__main__":
    # argv = sys.stdin.read().splitlines()

    script_directory = os.path.realpath(os.path.dirname(__file__))
    file = open(script_directory + '/data.txt', 'r')

    lines = [line.strip() for line in file.readlines()]

    pattern = lines[0]
    strands = lines[1].split(' ')

    result = calc_hamming_distance_from_many_words(pattern, strands)
    print(result)
