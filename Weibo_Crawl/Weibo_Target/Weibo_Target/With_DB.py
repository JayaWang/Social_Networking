# -*- coding: utf-8 -*-

import MySQLdb
import redis

class All_DB(object):
    def __init__(self):
        host = '127.0.0.1'
        user = 'root'
        password = '228228'
        db_name = 'Distributed_NTES'  #到时候这里改一下mysql就行了
        try:
            self.db_conn = MySQLdb.connect(host, user, password, db_name, charset="utf8")
        except Exception as e:
            print ('数据库连接错误' + str(e))
        else:
            print '成功连接数据库'

        try:
            self.r = redis.Redis(host='127.0.0.1', port=6379, db=0)
        except Exception as e:
            print ('连接Redis失败' + str(e))

    def Insert_MySQL(self, sql_command): #Insert/Update
        try:
            db_cur = self.db_conn.cursor()
            db_cur.execute(sql_command)
            self.db_conn.commit()
        except Exception as e:
            print ('写入执行' + sql_command + '失败' + str(e))

    def Query_MySQL(self, sql_command):
        try:
            db_cur = self.db_conn.cursor()
            db_cur.execute(sql_command)
            data = db_cur.fetchall()
            return data
        except Exception as e:
            print ('读取执行' + sql_command + '失败' + str(e))

    def Insert_Redis(self, url):
        try:
            self.r.lpush('slave_urls', url)
        except Exception as e:
            print ('左插入Redis错误' + str(e))




