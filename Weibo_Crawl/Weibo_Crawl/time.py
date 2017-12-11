# -*- coding: utf-8 -*-

from With_DB import Mysql_DB
import re

class time(object):
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
    a = time()
    for i in range(1):
        a.Get_Sentence()
        print '第' + str(i) + '次结束'

