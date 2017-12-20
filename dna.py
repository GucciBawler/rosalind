'''
DNA.py

A script to count the occurence of the amino acids in a string of DNA.
'''

amino_count = {'A':0, 'C':0, 'G':0, 'T':0}

for amino in input():
	amino_count[amino] += 1


print_string = str()

for count in amino_count:
	print_string += str(amino_count[count])+' '

print(print_string.strip())
