# -*- coding: utf-8 -*-

'a test module'

__author__ = 'rui tong'

import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print('hello world')
    elif len(args) == 2:
        print('hello %s' % args[1])
    else:
        print('too many args')

def _private_1(name):
    return 'hello,%s' % name

def _private_2(name):
    return 'hi,%s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)

if __name__ == '__main__':
    print(greeting('ton'))
    print(sys.path)