# -*- coding: utf-8 -*-
import MySQLdb
import re
import redis

class time_aa(object):
    def __init__(self):
        self.db = Mysql_DB()

    def Get_Sentence(self):
        sql = "select id, Comment_Time from comment where Tweet_Owner = 1195300800 limit " + str(1)
        try:
            Sentence_list = self.db.Query_MySQL(sql)  # 读取数据库，获取step行列
            for i in Sentence_list:  # 执行YYY修改命令,看看参照什么来做基准
                self.update_db(i[0], i[1])
        except Exception as e:
            print ('query_db函数执行错误' + str(e))

    def update_db(self, i, time):
        if u'分钟前' in time:
            b = re.findall(u'(\d+)分钟前', time)[0]
            m = 60 - int(b)
            new_time = '今天 11:' + str(m)
            changeY_sql = "update comment set over = 'YYYYY', Comment_Time = " + new_time + " where id = " + str(i)
            try:
                self.db.Insert_MySQL(changeY_sql)
            except Exception as e:
                print ('改变YY错误' + str(e))

if __name__ == "__main__":
    a = time_aa()
    for i in range(1):
        a.Get_Sentence()
        print '第' + str(i) + '次结束'


class Mysql_DB(object):
    def __init__(self):
        host = '127.0.0.1'
        user = 'root'
        password = '228228'
        db_name = 'Weibo'  #到时候这里改一下mysql就行了
        try:
            self.db_conn = MySQLdb.connect(host, user, password, db_name, charset="utf8")
        except Exception as e:
            print ('数据库连接错误' + str(e))
        else:
            pass

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

class Redis_DB(object):
    def __init__(self, db_num):
        try:
            self.r = redis.Redis(host='127.0.0.1', port=6379, db=db_num)
        except Exception as e:
            print ('连接Redis失败' + str(e))

    def Insert_Redis(self, key, url):
        try:
            self.r.lpush(key, url)
        except Exception as e:
            print ('左插入Redis错误' + str(e))

    def Query_Redis(self, key):
        try:
            self.r.get(key)
        except Exception as e:
            print ('读取redis错误' + str(e))
