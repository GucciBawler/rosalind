'''
hamm.py

A script that calculates the Hamming distance between two strings.
'''

strand_1, strand_2 = input(), input()
Hamming = 0

for i in range(len(strand_1)):
	if strand_1[i] != strand_2[i]:
		Hamming += 1

print(Hamming)
