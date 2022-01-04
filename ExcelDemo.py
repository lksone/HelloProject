#!/usr/bin/python
# -*- coding: UTF-8 -*-

from os.path import isfile
from openpyxl import load_workbook

class ExcelToDict:
    """
    将excel 转换为字段对象的方式
    """
    def __init__(self,file_dir,title_row=0):
        self.file_dir = file_dir
        self.title_row = title_row
        self.data_dirt={}
        self.work_book = None

    def open_object(self):
        """
        打开工作簿对象
        :return:
        """
        valid = isfile(self.file_dir)
        if not valid:
            raise 
