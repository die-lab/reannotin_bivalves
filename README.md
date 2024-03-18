# reannotin_bivalves
A dive into bivalves mitochondrial oddity

I have searched for mitochondrial genomes on ncbi by command line, using the below command.
But of course it will be better to have a file in which you have many different classes (like bivalves, gastropods, cefalopods, mammifera...) and you download everithing and parse it directly to files.
But you need first to check if you find many mitochondrial genome using that type of query on the browser.
'''
for class in $(cat metazoa*); do esearch -db nuccore -query "("$class"[Organism] AND mitochondrion[All Fields] AND complete[All Fields]" | efetch -format gb >> $class'.gb'; done 
'''
Now, extract every gene's sequence (nucleotides and protein) from gb files using custom python script **extracting_feature_v6.py**, and move them to separate directories.

'''
for gb_file in $(ls *.gb); do python extracting_feature_v6.py $gb_file; mkdir ${gb_file%.gb}_extraction; mv *.fasta ${gb_file%.gb}_extraction; done
'''

Be sure to read /n as the line separator with IFS, and to have ncbi tools on your conda env.

```
for x in $(awk '{print $1}' dataset.txt)'
do esearch -db nuccore -query $x | efetch -format gb >> all.gb
done

awk '{print $1}' dataset.txt > nc_codes.txt
sed 's/\t/__/g'dataset.txt | sed 's/ /_/g' >> dataset.notab.txt
```

Process this large genbank file using  a custom python script (extracting_feature_v4.py), to obtain protein and nucleotide sequences.

```
python extracting_feature_v4.py
```

For some species, the genes have not been extracted from gb. Unknown reasons. Se who thery are at **missing_extraction.txt**.
Rename files using the following loop.
```
for code in $(cat nc_codes.txt); do value=$(grep $code dataset.notab.txt); for file in $(ls $code*); do mv $file $value${file#$code}; done; done
```
Then replace the header inside each fasta file, to make it easier to get information from manual scrolling of alignment.
```
for fasta in *.fasta; do name=$(grep '>' $fasta); sed -i 's/'$name'/>'${fasta%.fasta}'/g' $fasta; done
```
Now parse it to a file for each genes. Use **list_mito_genes.txt**
```
for gene in $(cat list_mito_genes.txt); do cat all_genes_prot_headerOK/*'_'$gene'_'* > aligned_prot/$gene'_prot.fasta'; done
```

