import os
from collections import Counter

scriptDir = os.path.dirname(os.path.realpath(__file__))
print(scriptDir)

file = open(scriptDir + '/data.txt', 'r')

dna = file.readline().strip()

reverse_table = {
    'A': 'T',
    'T': 'A',
    'C': 'G',
    'G': 'C'
}

complementary_string = ''
for i in range(0, len(dna)):
    complementary_string = complementary_string + reverse_table.get(dna[i])


print(complementary_string[::-1])


complementary_string = complementary_string[::-1]

file2 = open(scriptDir + '/solution.txt', 'w')
file2.write(complementary_string)