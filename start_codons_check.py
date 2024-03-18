import re
import os
from Bio import SeqIO
from Bio.Seq import Seq

#mitochondrial invertebrate start codons from ncbi
alt_codons = ['ATA','ATT','ATC','GTG','TTG']

mito_genes = ['ATP6', 'ATP8', 'CYTB', 'COX1', 'COX2', 'COX3', 'FORF', 'HORF', 'MORF', 'NAD1', 'NAD2', 'NAD3', 'NAD4', 'NAD4L', 'NAD5', 'NAD6']

def codons_of_three(input):	
	if (len(record.seq)/3 % 1) > 0:
		print("warning: "+ input.id + " has an unusual length")
		w = 1
	else:
		w = 0
	return w, len(record.seq)/3	

current_directory = os.getcwd()
files_in_directory = os.listdir(current_directory)

alternative_dict = {}
for gene in mito_genes:
	lookup = str('_'+gene+'_')		
	gene_files = [file for file in files_in_directory if lookup in file and file.endswith('.fasta')]
	print(gene)
	if len(gene_files) == 0:
		continue
	#how many of them have a weird length  
	weird_length = 0	
	length_tot = []
	for file in gene_files:
		record = SeqIO.read(file,"fasta")
		cot = codons_of_three(record)
		length_tot.append(cot[1])		
		weird_length = weird_length + cot[0]
	weird_length_fraction = weird_length/len(gene_files)
	print(weird_length_fraction, max(length_tot))
	alternative_dict[gene] = {}	
	for alternative in alt_codons:	
		my_dict = {i: 0 for i in range(1, int(max(length_tot))+1)}	
		for file in gene_files:
			record = SeqIO.read(file,"fasta")		
			matches = re.finditer(alternative,str(record.seq))
			positions = [match.end() for match in matches]
			pos_corr = [(element // 3) for element in positions]
			for x in pos_corr:
				my_dict[x] = my_dict[x] + 1
		alternative_dict[gene][alternative] = my_dict



