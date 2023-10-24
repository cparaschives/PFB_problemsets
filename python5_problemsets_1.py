#!/usr/bin/env python
dict={'book':'Hyperion','song':'Strunga','tree':'Oak','organism':'dog,cat,fish'}
print(dict['book'])
fav_thing='book'
print(dict[fav_thing])
print(dict['tree'])
fav_thing='organism'
print(dict[fav_thing])
for element in dict:
 value=dict[element]


