import os
from collections import Counter


def find_complamentary(pattern):
    reverse_table = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }

    complementary_string = ''
    for i in range(0, len(pattern)):
        complementary_string = complementary_string + \
            reverse_table.get(pattern[i])

    complementary_string = complementary_string[::-1]

    return complementary_string


scriptDir = os.path.dirname(os.path.realpath(__file__))

file = open(scriptDir + '/data.txt', 'r')

pattern = 'CTTGATCAT'
genome = file.readline().strip()
patterns = [pattern]
positions = []

for i in range(0, (len(genome) - len(pattern) + 1)):
    tested = genome[i:i + len(pattern)]
    if tested in patterns:
        positions.append(i)

print(positions)

result = ' '.join(str(x) for x in positions)
file2 = open(scriptDir + '/solution.txt', 'w')
file2.write(result)