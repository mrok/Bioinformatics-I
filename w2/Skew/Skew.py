import sys
import os


def skew(genome):
    result = [0]
    previous_value = 0

    for i in range(0, len(genome)):
        nucleotide = genome[i]
        if nucleotide == 'C':
            previous_value -= 1
        if nucleotide == 'G':
            previous_value += 1

        result.append(previous_value)

    return map(str, result)

if __name__ == "__main__":
    # argv = sys.stdin.read().splitlines()

    argv = []
    scriptDir = os.path.dirname(os.path.realpath(__file__))
    file = open(scriptDir + '/data.txt', 'r')
    genome = file.readline().strip()

    argv = [genome]
    result = skew(argv[0])
    print(' '.join(result))
