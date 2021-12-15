
import collections as cc
import os, argparse


# Point = namedtuple('Point', ['x', 'y'])
# p = Point(1,2)

# print(p.x, p.y)

# Circle = namedtuple('Circle', ['x', 'y', 'r'])

# q = cc.deque(['a','b','c'])
# q.append('x')
# q.appendleft('y')
# print(q)

# dd = cc.defaultdict(lambda:'N/A')
# dd['key1'] = 'abc'
# print(dd['key1'],dd['key2'])

# d = dict([('a',1), ('b',2), ('c',3)])
# od = cc.OrderedDict([('a',1), ('b',2), ('c',3)])
# print(d,od)

"""
class LastUpdatedOrderedDict(cc.OrderedDict):

    def __init__(self,capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity
    
    def __setitem__(self,key,value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('delete:', (last[0], last[1]))
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        cc.OrderedDict.__setitem__(self,key,value)

fifo = LastUpdatedOrderedDict(5)
for i in range(10):
    fifo[i] = i
    fifo[i] = i+1
"""

defaults = {
    'color': 'red',
    'user': 'guest'
}

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args()
command_line_args = { k:v for k,v in vars(namespace).items() if v}

combined = cc.ChainMap(command_line_args, os.environ, defaults)

print('color=%s' %combined['color'])
print('user=%s' %combined['user'])

c = cc.Counter()
# for ch in 'programming':
#     c[ch] = c[ch] + 1
c.update('programming')
print(c)
c.update('hello')
print(c)