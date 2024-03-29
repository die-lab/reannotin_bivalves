# reannotin_bivalves
A dive into bivalves mitochondrial oddity

After having accurately found mitochondrial genomes of a large number of bivalves (following Maeda et al. 2021 and others), I've downloaded them using ncbi tools.
The starting file, dataset.txt, looked like this:

|nc_codes| order| family| species| typo|
|--------|------|-------|--------|-----|
|NC_008451	|Adapedonta	|Hiatellidae	|Hiatella arctica|	SMI|
|NC_016665	|Adapedonta	|Solenidae	|Solen grandis	|SMI|
|NC_017616	|Adapedonta	|Solenidae	|Solen strictus	|SMI|
|NC_020787|	Arcoida	|Arcidae	|Scapharca broughtonii	|SMI|
|KF750628	|Arcoida	|Arcidae	|Scapharca kagoshimensis	|SMI|
|KJ607173	|Arcoida	|Arcidae	|Tegillarca granosa	|SMI|
|NC_008452|	Cardiida	|Cardiidae	|Acanthocardia tuberculata|	SMI|
|KY780363 |Cardiida	|Donacidae	|Donax semistriatus	|Female|
|OR416184 |	Cardiida	|Donacidae	|Donax semistriatus	|Male|

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

