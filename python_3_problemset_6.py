#!/usr/bin/env python
dna='ATGCAGGGGAAACATGATTCAGGAC'
dna_replace=dna.replace('T', 'a').replace('C','g')
print(dna_replace)
dna_replace2=dna_replace.replace('A','t').replace('G','c')
print(dna_replace2)
dna_upper=dna_replace2.upper()
print(dna_upper)
print(dna_upper[::-1])









