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
```

Process this large genbank file using  a custom python script (extracting_feature_v4.py), to obtain protein and nucleotide sequences.

```
python extracting_feature_v4.py
```

For some species, the genes have not been extracted from gb. Unknown reasons. Se who thery are at **missing_extraction.txt**.
```
