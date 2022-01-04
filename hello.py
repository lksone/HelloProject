#!/usr/bin/env python
# -*- coding: utf-8 -*-

# from __future__ import print_function
#
# count = 11
# a = 11.1
# print(count+a)

#元组
tuple =('1231',123,12,12,32,123,10.12)
tinytuple = (123,'tom')

print(tuple)
print(tinytuple)
print(tinytuple[1])
print(tuple[1:3])

#dict 字典

dict = {}
dict['one'] = "this is one"
dict[2] = "this is two"

print(dict['one'])
print(dict.keys())
print(dict.values())
print(dict)

# 复杂数据

numbers = [12,37,5,43,8,3]
even=[]
odd=[]
for a in numbers:
    print(a)
while len(numbers) >0:
    number = numbers.pop()
    if(number % 2 ==0):
        even.append(number)
    else:
        odd.append(number)
print(even)
print(odd)
