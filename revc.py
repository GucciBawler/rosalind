'''
REVC.py

A script that generates the reverse complement of a string.
'''

translation = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}

revc = str()

for nucleic in input()[::-1]:
	revc += translation[nucleic]
	
print(revc)
