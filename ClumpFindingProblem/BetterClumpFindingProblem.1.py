import sys
from collections import Counter
import time
import os

# enumerating list is too slow 
# It is better(faster) because frequency array is not calculated for each window, 
# but it is constructed from previous array by subtracting first element and adding
# last element of the next window    

def digit_to_symbol(number):
    mapping = ['A', 'C', 'G', 'T']

    return mapping[number]


def number_to_pattern(number, k):
    if k == 1:
        return digit_to_symbol(number)

    quotient = number // 4
    remainder = number % 4

    symbol = digit_to_symbol(remainder)
    part_pattern = number_to_pattern(quotient, k-1) 
    
    return part_pattern + symbol    


def symbol_to_number(symbol):
    mapping = {
        'A': 0,
        'C': 1,
        'G': 2,
        'T': 3
    }

    return mapping.get(symbol)


def pattern_to_number(pattern):
    if len(pattern) == 1:
        return symbol_to_number(pattern)

    last_symbol = pattern[-1:]
    new_pattern = pattern[:-1]

    result = 4 * pattern_to_number(new_pattern) + symbol_to_number(last_symbol)

    return result


def compute_frequencies(genome, k):
    frequencies = [0 for i in range(4 ** k)]

    for i in range(len(genome) - k + 1):
        pattern = genome[i: i + k]
        index = pattern_to_number(pattern)
        frequencies[index] += 1

    return frequencies


def find_clumps(genome, k, L, t):
    initial_window = genome[0:L]
    initial_frequencies = compute_frequencies(initial_window, k)

    final_result = [ind for ind, x in enumerate(initial_frequencies) if x >= t]

    frequencies = initial_frequencies    
    start_time=time.time() #taking current time as starting time
    
    genome_length = len(genome)
    for i in range(1, genome_length - L + 1):
        if (i % 1000 == 1):
            end_time=time.time() #taking current time as starting time
            print(i)
            print(end_time - start_time)    
        beggining = genome[i-1:i-1+k] 
        end = genome[i+L-k:i+L]

        frequencies[pattern_to_number(beggining)] -= 1
        frequencies[pattern_to_number(end)] += 1        

        final_result.extend([ind for ind, x in enumerate(frequencies) if x >= t])

    final_result = list(set(final_result))    
    final_result = [number_to_pattern(x, k) for x in final_result] 

    return list(set(final_result))

if __name__ == "__main__":
    # argv = sys.stdin.read().splitlines()

    argv = []
    scriptDir = os.path.dirname(os.path.realpath(__file__))
    file = open(scriptDir + '/data1.txt', 'r')
    genome = file.readline().strip()
    kint = file.readline().strip()

    argv = [genome, kint]

    clump_params = argv[1].split(" ")
    params = [argv[0]]
    params.extend(clump_params)
    result = find_clumps(params[0], int(params[1]), int(params[2]), int(params[3]))
    print(' '.join(result))
