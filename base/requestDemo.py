#!/usr/bin/python
# -*- coding: UTF-8 -*-


import requests



if __name__ == '__main__':
   baidu =  requests.get("https://www.baidu.com")
   print(baidu.json())