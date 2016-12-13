import os
import itertools
import sys

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


# problem solution


def find_median_string(k, dnas):
    distance = float("inf")
    patterns = itertools.product('ACGT', repeat=k)
    median = ''

    for pattern in patterns:
        pattern = ''.join(pattern)
        current_distance = calc_hamming_distance_from_many_words(pattern, dnas)
        if distance > current_distance:
            distance = current_distance
            median = pattern

    return median


def find_all_median_string(k, dnas):
    distance = float("inf")
    patterns = itertools.product('ACGT', repeat=k)
    medians = []

    for pattern in patterns:
        pattern = ''.join(pattern)
        current_distance = calc_hamming_distance_from_many_words(pattern, dnas)

        if distance == current_distance:
            medians.append(pattern)            

        if distance > current_distance:
            distance = current_distance
            medians = [pattern]


    return ' '.join(medians)


if __name__ == "__main__":
    script_directory = os.path.dirname(os.path.realpath(__file__))
    file = open(script_directory + '/data.txt', 'r')

    lines = file.readlines()

    k = int(lines[0].strip())
    dnas = [dna.strip() for dna in lines[1:]]

    result = find_all_median_string(k, dnas)
    print(result)
