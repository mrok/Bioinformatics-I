import sys
from collections import Counter
import os

# It is better(faster) because frequency array is not calculated for each window,
# but it is constructed from previous array by subtracting first element and adding
# last element of the next window

def compute_frequencies(genome, k):
    frequencies = {}

    for i in range(len(genome) - k + 1):
        pattern = genome[i: i + k]
        frequencies[pattern] = frequencies.get(pattern, 0) + 1

    return frequencies


def find_clumps(genome, k, L, t):
    initial_window = genome[0:L]
    initial_frequencies = compute_frequencies(initial_window, k)

    final_result = [key for key, value in initial_frequencies.items() if value >= t]
    frequencies = initial_frequencies
    for i in range(1, len(genome) - L + 1):
        if (i % 100000 == 1):
            print(i)
        beggining = genome[i - 1:i - 1 + k]
        end = genome[i + L - k:i + L]

        frequencies[beggining] -= 1
        frequencies[end] = frequencies.get(end, 0) + 1
        if (frequencies[beggining] == 0):
            del frequencies[beggining]

        final_result.extend([key for key, value in frequencies.items() if value >= t])

    final_result = list(set(final_result))
    return final_result

if __name__ == "__main__":
    # argv = sys.stdin.read().splitlines()

    argv = []
    scriptDir = os.path.dirname(os.path.realpath(__file__))
    file = open(scriptDir + '/data.txt', 'r')
    genome = file.readline().strip()
    kint = file.readline().strip()

    argv = [genome, kint]

    clump_params = argv[1].split(" ")
    params = [argv[0]]
    params.extend(clump_params)
    result = find_clumps(params[0], int(params[1]), int(params[2]), int(params[3]))
    print(' '.join(result))
    print(len(result))    
