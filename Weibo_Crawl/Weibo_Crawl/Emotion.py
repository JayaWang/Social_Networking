# -*- coding: utf-8 -*-

#将热门评论做情感分析，根据热评加权评价歌曲的情感取向，使用百度AI的SDK

from With_DB import Mysql_DB
from aip import AipNlp
import re
from opencc import OpenCC

class Emotion(object):
    def __init__(self):
        APP_ID = '10362966'  # '你的 App ID'
        API_KEY = 'nQWiWR6DzjXsfYjW1yyVy8TB'  # '你的 Api Key'
        SECRET_KEY = 'WpjMdNWYv6TSg2psofaGt4LNW366tvnj'  # '你的 Secret Key'
        self.db = Mysql_DB()
        self.aip = AipNlp(APP_ID, API_KEY, SECRET_KEY)
        self.trans = OpenCC('t2s') #模式设置为繁体-简体

    def Get_Sentence(self):
        sql = "select id, Comment_Content from comment where over = 'N' limit " + str(100)
        try:
            Sentence_list = self.db.Query_MySQL(sql)  # 读取数据库，获取step行列
            for i in Sentence_list:  # 执行YYY修改命令,看看参照什么来做基准
                self.update_db(i[0])
            return Sentence_list
        except Exception as e:
            print ('query_db函数执行错误' + str(e))

    def update_db(self, i):
        changeY_sql = "update comment set over = 'Y' where id = " + str(i)
        try:
            self.db.Insert_MySQL(changeY_sql)
        except Exception as e:
            print ('改变YY错误' + str(e))

    def Get_Analyse(self):
        sentence_list = self.Get_Sentence()
        r = re.compile(ur"[\u0000-\u4dff,\u9fa6-\uffff]")  # 删除除了中文以外的一切
        for i in sentence_list:
            try:
                simple = self.trans.convert(i[1])
                #print i[1].strip().encode('utf-8', 'ignore')
                result = self.aip.sentimentClassify(simple.strip().encode('utf-8', 'ignore'))
                #print result
                '''print result['items'][0]['positive_prob'] #属于积极类别的概率
                print result['items'][0]['confidence'] #分类的置信度
                print result['items'][0]['negative_prob'] #属于消极类别的概率
                print result['items'][0]['sentiment'] #情感极性分类结果，0为负面，1为中性，2为正面'''
                s = str(result['items'][0]['sentiment'])
                p = str(result['items'][0]['positive_prob'])
                n = str(result['items'][0]['negative_prob'])
                c = str(result['items'][0]['confidence'])
                sql = "update comment set sentiment = %s, positive_prob = %s, negative_prob = %s, confidence = %s"%(s, p, n, c) + " where id = " + str(i[0])
                self.db.Insert_MySQL(sql)
            except Exception as e:
                print('辣鸡百度转码又TM错误了,看老子的' + str(e))
                try:
                    simple = self.trans.convert(i[1])
                    re_s = r.sub(',', simple)
                    result = self.aip.sentimentClassify(re_s.strip().encode('utf-8', 'ignore'))
                    s = str(result['items'][0]['sentiment'])
                    p = str(result['items'][0]['positive_prob'])
                    n = str(result['items'][0]['negative_prob'])
                    c = str(result['items'][0]['confidence'])
                    sql = "update comment set sentiment = %s, positive_prob = %s, negative_prob = %s, confidence = %s"%(s, p, n, c) + " where id = " + str(i[0])
                    self.db.Insert_MySQL(sql)
                except Exception as e:
                    print ('草，老子没辙了' + str(e))

if __name__ == '__main__':
    a = Emotion()
    for i in range(2832): #2832
        a.Get_Analyse()
        print '第' + str(i) + '次完成了'


