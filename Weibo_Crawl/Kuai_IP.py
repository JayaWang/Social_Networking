# -*- coding: utf-8 -*-

from Weibo_Crawl.With_DB import Mysql_DB
import requests
import json
import time
import base64

class Push_ip(object):
    def __init__(self):
        self.db = Mysql_DB()

    def push_ip(self):
        url = 'http://dps.kuaidaili.com/api/getdps/?orderid=991275393123488&num=20&ut=1&format=json&sep=1'
        get_ip = requests.get(url)
        ip_list = json.loads(get_ip.text)['data']['proxy_list']
        i = 1060
        for ip in ip_list:
            try:
                sql = """update proxys set ip = '%s' where id = '%s'"""%(str(ip), str(i))
                self.db.Insert_MySQL(sql)
                i += 1
            except Exception as e:
                print '插入ip错误' + str(e)

if __name__ == "__main__":
    while True:
        print 'begin get'
        a = Push_ip()
        a.push_ip()
        print 'start sleep'
        time.sleep(600)



