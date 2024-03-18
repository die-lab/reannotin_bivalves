# reannotin_bivalves
A dive into bivalves mitochondrial oddity

<h2>preparing datasets</h2>
I have searched for mitochondrial genomes on ncbi by command line, using the below command.
But of course it will be better to have a file in which you have many different classes (like bivalves, gastropods, cefalopods, mammifera...) and you download everithing and parse it directly to files.
But you need first to check if you find many mitochondrial genome using that type of query on the browser.
```
for class in $(cat metazoa*); do esearch -db nuccore -query "("$class"[Organism] AND mitochondrion[All Fields] AND complete[All Fields]" | efetch -format gb >> $class'.gb'; done 
```
Now, extract every gene's sequence (nucleotides and protein) from gb files using custom python script **extracting_feature_v6.py**, and move them to separate directories.
```
for gb_file in $(ls *.gb); do python extracting_feature_v6.py $gb_file; mkdir ${gb_file%.gb}_extraction; mv *.fasta ${gb_file%.gb}_extraction; done
```
We have to work differently on nucleotides and ptoteic sequence, so I keep it apart.
```
for i in *_extraction; do cd $i; mkdir $i'_nucl'; mkdir $i'_prot'; mv *_nucl.fasta $i'_nucl'; mv *_prot.fasta $i'_prot'; cd ..; done
```
<h2>alternatives codons</h2>
I retrieve alternative start codons from [ncbi indications] (https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi#SG5-)
