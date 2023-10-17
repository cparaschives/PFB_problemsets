#!/usr/bin/env python3
import sys
number=sys.argv[1]
number=int(number)
if number<0:
 message='negative'
 print(message)
elif number>0:
 message='positive'
 print(message)
else:
 print('=0')

