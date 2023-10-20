#!/usr/bin/env python
numbers=[101,2,15,22,95,33,2,27,72,15,52]
even_numbers=[]
odd_numbers=[]
for number in numbers:
 if(number%2==0):
  print(number)
  even_numbers.append(number)
 else:
  print(number)
  odd_numbers.append(number)
print(even_numbers)
print(odd_numbers)

even_numbers.sort()
print(even_numbers)


print(sum(even_numbers))
print(sum(odd_numbers))









 
