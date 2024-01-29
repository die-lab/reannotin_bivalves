# reannotin_bivalves
A dive into bivolves mitochondrial oddity

After having accurately found mitochondrial genomes of a large number of bivalves (following Maeda et al. 2021 and others), I've downloaded them using ncbi tools.

'esearch -db nuccore -query NC_008451 | efetch -format gb >> all.gb'

And processed this large genbank file using  a custom python script (extracting_feature_v4.py), to obtain protein and nucleotide sequences.
