#!/usr/bin/env python

with open('python_6.seq.txt', 'r') as seq_original:
 for line in seq_original:
  line=line.rstrip()
 # print(line)
  line_split=line.split('\t')
 # print(line_split)
  
  seq_name=line_split[0]
  forward_seq=line_split[1].lower()
  
  reverse_seq=forward_seq[::-1]
  #print(reverse_seq)
  reverse_seq_1=reverse_seq.replace('a','T').replace('t','A')
  reverse_seq_2=reverse_seq_1.replace('c','G').replace('g','C')
  
  print(f'>{seq_name}\n{reverse_seq_2}')





