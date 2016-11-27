import sys
from collections import Counter
import os

def frequent_words(genome, k):
    frequency = []
    for i in range(0, len(genome) - k + 1):
        frequency.append(genome[i:(i + k)])

    result = Counter(frequency)

    result.items()
    occurences = [x[1] for x in result.items()]
    most_frequent = max(occurences)
    final_result = [x for x in result.items() if x[1] == most_frequent]

    return final_result


def find_clumps(genome, k, L, t):
    final_result = []
    box_starts = range(0, len(genome) - L + 1)
    for i in box_starts:
        box = genome[i: i + L]
        result = frequent_words(box, k)
        result = [x for x in result if x[1] >= t]
        final_result.extend([x[0] for x in result])

    return list(set(final_result))

if __name__ == "__main__":
    # argv = sys.stdin.read().splitlines()

    argv = []
    scriptDir = os.path.dirname(os.path.realpath(__file__))
    file = open(scriptDir + '/data.txt', 'r')
    genome = file.readline().strip()
    kint = file.readline().strip()

    argv= [genome, kint]

    clump_params = argv[1].split(" ")
    params = [argv[0]]
    params.extend(clump_params) 
    result = find_clumps(params[0], int(params[1]), int(params[2]), int(params[3]))
    print(' '.join(result))
