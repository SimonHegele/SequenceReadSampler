# SequenceReadSampler

A small tool to help you with generating toy samples for testing software tools for bioinformatics.

### Example:

Filtering paired-end illumina reads from a mouse liver RNAseq<br>
(https://www.ncbi.nlm.nih.gov/sra/?term=SRR5273704)<br>
for reads that minimap2 aligns to chromosome 1 of the GRCm39 mouse genome assembly<br>
(https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_000001635.27/)

1. Mapping
   
`minimap2 -x sr -t 1 GCF_000001635.27_GRCm39_genomic.fna SRR5273704_1.fastq SRR5273704_2.fastq > mappings.paf`

2. Filtering
   
`python3 filter.py SSRR5273704_1.fastq SRR5273704_chr1_1.fastq NC_000067.7`

`python3 filter.py SSRR5273704_2.fastq SRR5273704_chr1_2.fastq NC_000067.7`

### Remarks:

Only tested for .paf output from single threaded minimap2.
It is important to only use a single thread because then the order of the mappings corresponds to the order of the query sequences from the input file.

