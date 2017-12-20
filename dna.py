'''
dna.py

A script to count the occurence of the amino acids in a string of DNA.
'''

nucleic_count = {'A':0, 'C':0, 'G':0, 'T':0}

for nucleic in input():
	nucleic_count[nucleic] += 1


print_string = str()

for count in nucleic_count:
	print_string += str(nucleic_count[count])+' '

print(print_string.strip())
