#!/usr/bin/python
# -*- coding: UTF-8 -*-

import keyword

class demo:
    '''单行注释'''
    def __init__(self):
        name='',
        age='',
        sex = 0

    def getInfo(self):
        """
        输入的参数和
        :return:
        """
        print(self.name)


if __name__ == '__main__':
    """
    注释
    """
   # print(keyword.kwlist)
    #原生字符串表示不输出
    print(r'123132131\n123213')
    #转义换行
    print('fdsfdsafdsa\nfdsafd')


    """
    str(头下标：尾下标：步长)
    """
    str = "123456789"
    print(str[0:-1])
    #输出第一个字符
    print(str[0])
    print(str[:-1])


    print(str[2:])

    tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}

    print(type(tinydict.keys()))
    print(type(tinydict.values()))
    """
    输出key和value的值
    """
    for a in tinydict.keys():
        print(a)
    for b in tinydict.values():
        print(b)
