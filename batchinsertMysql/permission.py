#!/usr/bin/python
# -*- coding: UTF-8 -*-


import pymysql
import random
import time
import json

class Sqldriver(object):
    # 初始化属性,相当于consumt
    def __init__(self):
        self.host = '10.32.16.12'
        self.port = 3306
        self.user = 'root'
        self.password = '1qaz@WS'
        self.database = 'jeecg-boot'

    # 连接数据库
    def Connect(self):
        self.db = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.database,
            charset='utf8'
        )

    # 插入数据
    def insert(self, userId, permissionId, type):
        try:
            # 连接数据库
            self.Connect()
            # 创建游标
            global cursor
            cursor = self.db.cursor()
            # sql命令
            sql = "INSERT INTO `upms_user_permission` (`user_id`, `permission_id`, `type` )VALUES( %s, %s, %s )"
            # 执行sql语句
            cursor.execute(sql, (userId, permissionId, type))
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            self.db.commit()
            self.db.close()

    # 数据生成并调用数据插入方法
    def data_make(self,permissionId):
        userId = 15567
        permissionId = permissionId
        type = 1
        self.insert(userId, permissionId, type)
    def json_formate_select(self,cursor:pymysql.cursors.Cursor):
        """
        转换pymysql select * from reset to formate
        :param cursor:
        :return:
        """
        keys =[]
        for column in cursor.description:
            keys.append(column[0])
        key_numbers=[]
        for row in cursor.fetchall():
            item = dict()
            #设置数据字典
            for q in range(key_numbers):
                item[keys[q]] = row[q]



if __name__ == '__main__':
    db = Sqldriver()
    for record in range(260,390):
        db.data_make(record)

