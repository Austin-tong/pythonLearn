#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np

"""
classmate=['michal', 'bob', 'tracy']
print(classmate)
print(len(classmate))
print(classmate[-1])
classmate.append('adam')
classmate.insert(1,'jack')
classmate.pop(1)
print(classmate)
"""
"""
age = int(input())
if age > 18:
    print('your age is ',age)
    print('adult')
else:
    print('your age is',age)
    print('teenager')

classmate=['michal', 'bob', 'tracy']
for name in classmate:
    print(f'hello,{name}!')

sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum = sum + x
print(sum)

sum = 0
for x in range(101):
    sum = sum + x
print(sum)

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n-2
print(sum)
"""
"""
d = {('a','b',['c']):100, 'michael' : 95, 'bob': 75, 'tracy': 85}
print(d['michael'])
d['michael'] = 67
print(d)
print('thomas' in d)
print(d.pop('bob'))
print(d)

s = set([1,2,3,1,2,3,4,5,6,7,8,9,('a','b')])
s.add(10)
s.remove(1)
s0 = set([1,2,3,4,5,6,7,11,12])
print(s | s0)
"""