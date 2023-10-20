#!/usr/bin/env python
my_list=['a','bb','ccc']
list_copy=my_list
print(my_list)
my_list.append('dddd')
print(my_list)
print(list_copy)

my_list2=['a','bb','ccc']
list2_copy=my_list2.copy()
print(my_list2)
list2_copy.append('dddd')
print(my_list2)
print(list2_copy)

