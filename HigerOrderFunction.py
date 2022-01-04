#!/usr/bin/python
# -*- coding: UTF-8 -*-


def f(x):
    return x*x
#直接为list赋值
r = map(f,[3,2,3,4,2,12,1,32,1])

print(list(r))


L =[]
for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    L.append(f(n))
print(L)