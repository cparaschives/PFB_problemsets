#!/usr/bin/env python
import sys
dictionary={}
for seq_file in sys.argv[1:]:

# in the shell,when calling the sys.argv:
# 1. see how the files are seen: echo sequence_homology.py ss_rand5-200* (* is for everything that comes after ss_rand5-200)
# 2. call sys.argv (./sequence_homology.py ss_rand5-200*) 
# print(seq_file)

 with open(seq_file,'r') as file_1:
   for line in file_1:
     line=line.rstrip()
     if(line.startswith('random')): 
      break
# break is needed to say that I only want the first line
 line_split=line.split('\t')
 perc_id=line_split[2]
 align_len=line_split[3]
 evalue=line_split[-2]
 matrix=seq_file.split('_')[-1]
 matrix=matrix.split('.')[0]
 dictionary[matrix]={perc_id, align_len,evalue}
 print(dictionary)

#print(matrix, perc_id, align_len,evalue)

# or we can do this using regular expresssion:
# import re at the beginning
#matrix=re.sub('.txt',"", matrix)




  
 
