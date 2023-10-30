#!/usr/bin/env python
line_count=0
with open('python_6.fastq', 'r') as object_file: 
 for line in object_file:
  line=line.rstrip()
  line_count=line
  if line_count>0:
   print(line_count)

