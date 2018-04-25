# -*- coding: utf-8 -*-
# namedtuple

from collections import namedtuple

point = namedtuple('Point', ['x', 'y'])
p = point(1, 2)
print('x,y: ', p.x, p.y)
# namedtuple('名称', [属性list]):
Circle = namedtuple('Circle', ['x', 'y', 'r'])

# deque
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：

from collections import deque

q = deque(['a', 'b', 'c'])
q.append('x')
print(q)
q.appendleft('y')
print(q)

# defaultdict

print('--------defaultdict: ')
# 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict
from collections import defaultdict

dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'

print(dd['key1'])
print(dd['key2'])

# OrderedDict

# dict key无序,需要创建有序dict的是时候,使用orderDict

print('--------OrderedDict: ')
from collections import OrderedDict

d = dict([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('x', 3)])
print('无序dict:', d)
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)

od = OrderedDict()
od['z'] = 1
od['y'] = 2
od['x'] = 3
# 按照插入的Key的顺序返回
print(list(od.keys()))


# 实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key

class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)


# Counter
print('--------Counter: ')
# 一个简单的计数器，例如，统计字符出现的个数
from collections import Counter

c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1

print(c)
