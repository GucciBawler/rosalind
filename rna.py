'''
rna.py

A script that translates a DNA string in RNA.
'''

RNA_string = str()

for nucleic in input():
	if nucleic == 'T':
		RNA_string += 'U'
	else:
		RNA_string += nucleic
		
return(RNA_string)
