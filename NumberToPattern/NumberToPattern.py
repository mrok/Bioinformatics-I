import sys
from collections import Counter
import os


def number_to_symbol(number):
    mapping = ['A', 'C', 'G', 'T']

    return mapping[number]


def number_to_pattern(number, k):
    if k == 1:
        return number_to_symbol(number)

    quotient = number // 4
    remainder = number % 4

    symbol = number_to_symbol(remainder)
    part_pattern = number_to_pattern(quotient, k-1) 
    
    return part_pattern + symbol    

if __name__ == "__main__":
    # argv = sys.stdin.read().splitlines()

    scriptDir = os.path.dirname(os.path.realpath(__file__))
    file = open(scriptDir + '/data.txt', 'r')
    number = file.readline().strip()
    k = file.readline().strip()
    argv = [number, k]

    result = number_to_pattern(int(argv[0]), int(argv[1]))
    print(result)
