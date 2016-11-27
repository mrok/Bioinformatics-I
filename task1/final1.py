import sys


def pattern_count(genome, pattern):
    count = 0
    patternLength = len(pattern)
    iter = range(0, len(genome) - patternLength + 1)
    for i in iter:
        comparedPart = genome[i:(i + patternLength)]
        if (comparedPart == pattern):
            count = count + 1

    return count

def main(argv):
    result = pattern_count(argv[0], argv[1])
    print(result)
        

if __name__ == "__main__":
   main(sys.argv[1:])
