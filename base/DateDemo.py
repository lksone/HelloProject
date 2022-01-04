#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time

def demo(str):
    print(str)

if __name__ == '__main__':
    #纳秒
    print(time.time_ns())
    #当前时间戳
    print("当前时间戳：",time.time())

    print(time.thread_time())


    print(time.localtime(time.time()))

    #格式化时间的对象
    print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))

    demo(1231)

