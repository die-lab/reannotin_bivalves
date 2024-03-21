from Bio import SeqIO
from Bio.Seq import Seq
import sys

genbank_file = sys.argv[1]
genes_name_list = { 'ATP6':['ATP6', 'ATPASE 6'], 'ATP8':['ATP8'], 'CYTB':['COB','CYTB'], 'COX1':['COI','COX1','COXI'], 'COX2':['COII','COX2','COXII'], 'COX3':['COIII','COX3','COXIII'], 'FORF':['F-ORF', 'FORF'], 'HORF':['HORF'], 'MORF':['M-ORF', 'MORF'],'NAD1':['NAD1','ND1'],'NAD2':['NAD2', 'ND2'],'NAD3':['NAD3','ND3'],'NAD4':['NAD4', 'ND4'],'NAD4L':['NAD4L', 'ND4L','NDL'],'NAD5':['NAD5', 'ND5'],'NAD6':['NAD6', 'ND6']}
genes_name_list = { 'ATP6':['ATP6', 'ATPASE 6','ATP SYNTHASE F0 SUBUNIT 6','ATP SYNTHASE SUBUNIT 6','ATP SYNTHETASE SUBUNIT 6','ATPASE SUBUNIT 6'], 'ATP8':['ATP SYNTHASE F0 SUBUNIT 8','ATP8','TRUNCATED ATP SYNTHASE F0 SUBUNIT 8','ATP SYNTHASE SUBUNIT 8'], 'CYTB':['COB','CYTB','CYTOCHROME B'], 'COX1':[',CYTOCHROME C OXIDASE SUBUNIT 1','COI','COX1','COXI','CYTOCHROME C SUBUNIT I','CYTOCHROME C OXIDASE SUBUNIT I'], 'COX2':['CYTOCHROME C OXIDASE SUBUNIT 2','COII','COX2','COXII','CYTOCHROME C SUBUNIT II','CYTOCHROME OXIDASE C SUBUNIT 2','CYTOCHROME C OXIDASE SUBUNIT II'], 'COX3':['CYTOCHROME C OXIDASE SUBUNIT III','CYTOCHROME C OXIDASE SUBUNIT 3','COIII','COX3','COXIII','CYTOCHROME OXIDASE C SUBUNIT 3','CYTOCHROME C SUBUNIT III'], 'FORF':['F-ORF', 'FORF','F-SPECIFIC ORF PROTEIN','F ORF'], 'HORF':['HORF','H OPEN READING FRAME'], 'MORF':['M-SPECIFIC MORF PROTEIN','M-ORF', 'MORF','M-SPECIFIC ORF PROTEIN','M-ORF PROTEIN','M-ORF1','M-ORF2','MORF21'],'NAD1':['NAD1','ND1','NADH DEHYDROGENASE SUBUNIT 1'],'NAD2':['NAD2', 'ND2','NADH DEHYDROGENASE SUBUNIT 2'],'NAD3':['NAD3','ND3','NADH DEHYDROGENASE SUBUNIT 3'],'NAD4':['NAD4', 'ND4','NADH DEHYDROGENESE SUBUNIT 4','NADH DEHYDROGENASE SUBUNIT 4'],'NAD4L':['NADH DEHYDROGENASE SUBUNIT 4L','NADH DEHYDROGENASE SUBUNIT L','NAD4L', 'ND4L','NDL'],'NAD5':['NAD5', 'ND5','NADH DEHYDROGENASE SUBUNIT 5'],'NAD6':['NADH DEHYDROGENASE SUBUNIT 6','NAD6', 'ND6']}

notes_dict = {}
for gene in genes_name_list.keys():
    print(gene)
    notes_dict[gene] = {}
    for record in SeqIO.parse(genbank_file, 'genbank'):
        species_db = dict(zip(list(genes_name_list), [[] for i in list(genes_name_list)]))
        gene_complete_check = []
        for feature in record.features:
            if feature.type == 'CDS':
                gene_name = feature.qualifiers.get('gene', [''])[0].upper()
                gene_name_corr = gene_name
                for i in genes_name_list:
                    if gene_name in genes_name_list[i]:
                        gene_name_corr = i
                    else:
                        gene_name_corr = gene_name
                gene_name = gene_name_corr
                note = feature.qualifiers.get('note', [''])[0].upper()
                if len(note) > 0:
                    notes_dict[gene][record.id] = note
                    print(str(record.id) + notes_dict[gene][record.id])


     	

