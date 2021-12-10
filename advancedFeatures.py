# -*- coding: utf-8 -*-
from collections.abc import Iterable
import os

# L = []
# for i in range(101):
#     L.append(i)
# print(L,'\n')

# print(L[:])

# def trim(str):
#     if len(str) == 0:
#         return ''
#     else:
#         i = 0
#         j = len(str)
#         while (str[i] == ' ') & (i < j):
#             i = i + 1
#         while str[j-1] == ' ':
#             j = j - 1
#         return str[i:j]
# def trim(s):
#     while s[:1] == ' ':
#         s = s[1:]
#     while s[-1:] == ' ':
#         s = s[0:-1]
#     return s

# if trim('hello  ') != 'hello':
#     print('测试失败!')
# elif trim('  hello') != 'hello':
#     print('测试失败!')
# elif trim('  hello  ') != 'hello':
#     print('测试失败!')
# elif trim('  hello  world  ') != 'hello  world':
#     print('测试失败!')
# elif trim('') != '':
#     print('测试失败!')
# elif trim('    ') != '':
#     print('测试失败!')
# else:
#     print('测试成功!')

# s = ''
# print(s[0:2])

# d = {'a': 1, 'b': 2, 'c': 3}
# for key,value in d.items():
#     print(key,value)
# for ch in 'ABC':
#     print(ch)
# print(isinstance('abc', Iterable))
# print(isinstance([1,2,3], Iterable))
# print(isinstance(123, Iterable))

# for i,value in enumerate(['a','b','c']):
#     print(i,value)

# def findMinAndMax(n):
#     min = n[0]
#     max = n[0]

#     for a in n:
#         if min > a :
#             min = a
#         if max < a :
#             max = a
#     return min,max


# if findMinAndMax([7]) != (7, 7):
#     print('测试失败!')
# elif findMinAndMax([7, 1]) != (1, 7):
#     print('测试失败!')
# elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
#     print('测试失败!')
# else:
#     print('测试成功!')


# print(list(range(1,11)))

# l = []
# for _ in range(1,11):
#     l.append(_ * _)
# print(l)

# print([x * x for x in range(1,11)])
# print([x * x for x in range(1,11) if x%2 == 0])
# print([m + n for m in 'ABC' for n in 'XYZ'])
# print([d for d in os.listdir('.')])
# d = {'x':'A', 'y':'B', 'z':'C'}
# print([k + '='+ v for k, v in d.items()])
# L = ['Hello', 'World', 'IBM', 'Apple']
# print([s.lower() for s in L])
# print([x if x%2 == 0 else -x for x in range(1,11)])
# L = ['Hello', 'World', 18, 'Apple', None]
# print([s.lower() for s in L if isinstance(s,str)])
# g = (x * x for x in range(10))
# for n in g : print(n)
# def fib(max):
#     n,a,b = 0,0,1
#     while n < max:
#         yield (b)
#         a,b = b,a+b
#         n = n+1
#     return 'done'
# # print(n for n in fib(10))
# for n in fib(10): print(n)

"""
def triangles():
    s = [1]
    yield s
    while True:
        s = list(map(lambda x,y:x+y, [0]+s,s+[0]))
    yield s

a = triangles()
for n in a:
    print(a)
"""
import time
def consumer(name):
    print("%s 准备学习啦" %name)
    while True:
        lesson = yield
        print("开始[%s]了，[%s]老师来讲课了"%(lesson,name))

def producer(name):
    c = consumer('A')
    c2 = consumer('B')
    c.__next__()
    c2.__next__()
    print('同学们开始上课了！')
    for i in range(10):
        time.sleep(1)
        print('到了两个同学')
        c.send(i)
        c2.send(i)

producer('A')
producer('B')