#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time

ticks =time.time()
print(ticks)
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))

#格式化时间戳转化为时间
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

#将时间格式化为时间戳
a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))

#获取日历

import calendar

#显示的是日历格式的代码
cal = calendar.month(2016,2)
print(cal)
