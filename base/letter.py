#!/usr/bin/python
# -*- coding: UTF-8 -*-



if __name__ == '__main__':
    for letter in 'python':
        if (letter == 'h'):
            #跳出循环
            break
        print('当前字母%s'%letter)

    for letter in 'python':
        #终止当前的值
        if(letter == 'h'):
            continue
        print('当前的字符%s'%letter)

    # pass 保证程序额结构和完整性

    for letter in 'python':
        if(letter == 'h'):
            pass
            print('pass 并不影响后续代码的输出')
        print('当前的字符--%s'%letter)