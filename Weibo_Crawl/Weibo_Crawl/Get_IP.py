# -*- coding: utf-8 -*-

from With_DB import Mysql_DB

class Proxy(object):
    def __init__(self):
        self.db = Mysql_DB()

    def GetIP(self):  # 先委屈下放sql里，之后想办法放到redis里去管理
        sql = "SELECT ip, port FROM proxys WHERE id >= ((SELECT MAX(id) FROM proxys)-(SELECT MIN(id) FROM proxys)) * RAND() + (SELECT MIN(id) FROM proxys)  LIMIT 1"
        try:
            ip_middle = self.db.Query_MySQL(sql)
            ip = str(ip_middle[0][0]) + ':' + str(ip_middle[0][1])
            ip_ok = "http://" + ip
            return ip_ok
        except Exception as e:
            print ('读取代理ip错误' + str(e))
