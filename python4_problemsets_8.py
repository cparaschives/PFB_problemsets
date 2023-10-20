#!/usr/bin/env python
import sys
start_value=sys.argv[1]
end_value=sys.argv[2]
print(start_value, end_value)
print(type(start_value))
start_value_int=int(start_value)
end_value_int=int(end_value)
print(type(start_value_int))
print(type(end_value_int))
numbers=range(start_value_int,end_value_int)
print(list(numbers))
for number in numbers:
 if number%2==1:
  print(number)
  number=number+1



