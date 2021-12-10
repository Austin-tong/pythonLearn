#!/usr/bin/env python
# -*- coding: utf-8 -*-

# abs(100,2)
# print(hex(255))

import math
"""
def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

def move(x,y,step,angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx,ny
x,y = move(100,100,60,math.pi/6)

def quadratic(a,b,c):
    en = math.sqrt(b**2 - 4 * a * c)
    if en > 0:
        return((-b + en)/2*a , (-b - en)/2*a)
    elif en == 0:
        return -b / 2*a
    else:
        return
print(quadratic(2,3,1))
print(quadratic(1,3,-4))
"""
"""
def power(x,n=2):
    x0 = x
    for i in range(n-1):
        x = x * x0
    return x
print(power(5))

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc(1,2,3))

def person(name, age, **kw):
    return print('name:',name,'age:',age,'other',kw)

print(person('michael', 30, gender = 'm', job = 'engineer'))

def mul(*numbers):
    x = 1
    for i in numbers:
        x = x * i
    return x
print(mul(5,6,7,9))
"""
'''
def fact(n):
    if n == 1:
        return 1
    else:
        return fact(n-1) * n
'''
def fact(n):
    return fact_iter(n,1)

def fact_iter(num,product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

print(fact(5))
#汉诺塔
def move(n,a,b,c):
    x = 0
    if n == 1:
        print(a,'->',c)
        # return x == x+1
    else:
        move(n-1,a,c,b)
        print(a,'->',c)
        #return x == x+1
        move(n-1,b,a,c)
    #print(x)

move(3,'A','B','C')