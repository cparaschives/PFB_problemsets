#!/usr/bin/env python
taxa='sapiens,erectus,neanderthalensis'
print(taxa)
print(type(taxa))
species=taxa.split(",")
print(species)
sorted_species=sorted(species)
print(sorted_species)
length_sorted_species=sorted(sorted_species, key=len)
print(length_sorted_species)


