from functools import reduce
import re

from numpy.random import f

# map and reduce
"""
def add(x,y,f):
    return f(x) + f(y)
print(add(-5,6,abs))

def f(x):
    return x * x 

r = map(f,[1,2,3,4,5,6,7,8,9])
print(list(map(str,[1,2,3,4,5,6,7,8,9])))

def add(x,y):
    return x + y
print(reduce(add,[1,3,5,7,9]))

def fn(x,y):
    return x * 10 + y
print(reduce(fn,[1,3,5,7,9]))

def char2num(s):
    degits = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8 ,'9':9}
    return degits[s]
print(reduce(fn,map(char2num,'13579')))

def normalize(name):
    return name.capitalize()
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

def prod(L):
    return reduce(lambda x,y: x*y, L )
print(prod([3,5,7,9]))

def str2float(s):
    degits = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8 ,'9':9}
    def fn(s):
        return degits[s]
    def char2num(s):
        s1 = reduce(lambda x,y: x * 10 + y, map(fn, s))
        return s1
    I = s.find('.')
    sl = s[:I]
    sr = s[I+1:]
    offset = 0.1 ** len(sr)
    result = char2num(sl) + offset * char2num(sr)
    return result

print(str2float('123.456'))
"""

# fliter
"""
def is_odd(n):
    return n % 2 == 1

print(list(filter(is_odd,[1,2,3,4,5,6,7,8,9])))

def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty,['A','','B',None,' '])))

def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x : x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)

L = []
for n in primes():
    if n < 1000:
        L.append(n)
    else:
        break
print(L)

def is_palindrome(n):
    s = str(n)
    
    '''#第一种方法
    l = len(s)
    if l == 1:
        return True
    i = 0
    while i < l / 2:
        if s[i] == s[l-i-1]:
            i = i + 1
        else:    
            return False
    return True
    '''

    if s[::] == s[::-1]:
        return s
    else:
        return None


output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')
"""

# sorted
"""
print(sorted([36,5,-12,9,-21]))
print(sorted([36,5,-12,9,-21], key = abs))
print(sorted(['bob', 'about', 'Zoo', 'Credit']))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key = str.lower))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key = str.lower, reverse = True))
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]
print(sorted(L, key = by_name))
def by_score(t):
    return t[-1]
print(sorted(L, key = by_score))
"""

# 返回函数
"""
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

print(lazy_sum(1,3,5,7,9)())

def count():
    fs = []
    for i in range(1,4):
        def f():
            print(i*i)
            return i*i
        fs.append(f)
    return fs

f1,f2,f3 = count()
print(f1)
print(f1())
print(f2())
print(f3())

def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1,4):
        fs.append(f(i))
    return fs
f1,f2,f3 = count()
print(f1)
print(f1())
print(f2())
print(f3())

def inc():
    x = 0
    def fn():
        return x + 1
    return fn

f = inc()
print(f())
print(f())

def inc():
    x = 0
    def fn():
        nonlocal x
        x = x + 1
        return x
    return fn

f = inc()
print(f())
print(f())

def createCounter():
    x = 0
    def counter():
        nonlocal x
        x = x + 1
        return x 
    return counter

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
"""

# 匿名函数
"""
print(list(map(lambda x: x*x, [1,2,3,4,5,6,7,8,9])))

f = lambda x: x*x
print(f(5))

def build(x,y):
    return lambda: x*x+y*y

b = build(1,2)
print(b)
print(b())

L = list(filter(lambda n: n%2==1, range(1,20)))
print(L)
"""

# 装饰器Decorator
"""
# def now():
#     print('2018')
# f = now
# f()
# print(now.__name__)
# print(f.__name__)

def log(func):
    def wrapper(*args, **kwargs):
        print('call %s():' %func.__name__)
        return func(*args, **kwargs)
    return wrapper

@log
def now():
    #print('2018')
    return '2018'

print(now())
print(now.__name__)
#print(log(now)())

def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' %(text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    return '2018'

print(now())
print(now.__name__)

import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('call %s():' %func.__name__)
        return func(*args, **kwargs)
    return wrapper

@log
def now():
    return '2018'

print(now())
print(now.__name__)


import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('%s %s():' %(text, func.__name__))
            return func(*args, **kwargs)
        return wrapper
    return decorator

@log('execute')
def now():
    return '2018'

print(now())
print(now.__name__)

import time

def metric(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('%s executed in %s ms' % (func.__name__, 10.24))
        return func(*args, **kwargs)
    return wrapper

@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
"""
"""
import functools
import time, datetime

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('begin call @%s' %datetime.datetime.now())
        func(*args, **kwargs)
        print('end call @%s' %datetime.datetime.now())
    return wrapper

@log
def spendTime():
    time.sleep(0.2)

spendTime()
"""
"""
import functools, datetime, time

def log(text = None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if not isinstance(text, str):
                print('begin call @%s' %datetime.datetime.now())
                func(*args, **kwargs)
                print('end call @%s' %datetime.datetime.now())
            else:
                print('begin %s @%s' %(text, datetime.datetime.now()))
                func(*args, **kwargs)
                print('end %s @%s' %(text,datetime.datetime.now()))
        return wrapper
    if isinstance(text, str):
        return decorator
    else:
        return decorator(text)

@log
def spendTime():
    time.sleep(0.2)

spendTime()
@log('dooooo')
def spendTime():
    time.sleep(0.2)

spendTime()
"""

import functools
# 偏函数 Partial function
print(int('12345'))
print(int('12345', base = 8))
print(int('12345', 16))

def int2(x,base=2):
    return int(x, base)

print(int2('10000', 10))

int2 = functools.partial(int, base=2)
print(int2('10000'))

kw = {'base':2}
print(int('10000',**kw))