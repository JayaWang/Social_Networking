# -*- coding: utf-8 -*-

import sqlalchemy
from sqlalchemy import create_engine
from With_DB import Mysql_DB
from items import WeiboTargetItem, WeiboCommentItem, WeiboPersonalItem

class WeiboCrawlPipeline(object):
    def __init__(self):
        self.db = Mysql_DB()

    def process_item(self, item, spider):
        if isinstance(item, WeiboTargetItem):
            try:
                if item["Tweet_Over"] == 'N':
                    sql = """insert into Tweet (Target_ID, Target_Name, Tweet_Time, Tweet_Content, Tweet_Transfer, Tweet_Liked, Tweet_Comment, Tweet_Platform, Tweet_GPS, Comment_Urls, Update_Time, Tweet_Over) VALUES ("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")"""%(item["Target_ID"].encode('utf-8', 'ignore'), item["Target_Name"].encode('utf-8', 'ignore'), item["Tweet_Time"].encode('utf-8', 'ignore'), item["Tweet_Content"].encode('utf-8', 'ignore'), item["Tweet_Transfer"], item["Tweet_Liked"], item["Tweet_Comment"], item["Tweet_Platform"].encode('utf-8', 'ignore'), item["Tweet_GPS"].encode('utf-8', 'ignore'), item["Comment_Urls"].encode('utf-8', 'ignore'), item["Update_Time"].encode('utf-8', 'ignore'), item["Tweet_Over"].encode('utf-8', 'ignore'))
                else:
                    sql = """update Tweet set Target_ID = "%s", Target_Name = "%s", Tweet_Time = "%s", Tweet_Content = "%s", Tweet_Transfer = "%s", Tweet_Liked = "%s", Tweet_Comment = "%s", Tweet_Platform = "%s", Tweet_GPS = "%s", Comment_Urls = "%s", Update_Time = "%s", Tweet_Over = "%s" """%(item["Target_ID"].encode('utf-8', 'ignore'), item["Target_Name"].encode('utf-8', 'ignore'), item["Tweet_Time"].encode('utf-8', 'ignore'), item["Tweet_Content"].encode('utf-8', 'ignore'), item["Tweet_Transfer"], item["Tweet_Liked"], item["Tweet_Comment"], item["Tweet_Platform"].encode('utf-8', 'ignore'), item["Tweet_GPS"].encode('utf-8', 'ignore'), item["Comment_Urls"].encode('utf-8', 'ignore'), item["Update_Time"].encode('utf-8', 'ignore'), item["Tweet_Over"].encode('utf-8', 'ignore'))+ """where Target_ID = '%s'"""%(item["Target_ID"].encode('utf-8', 'ignore'))
                self.db.Insert_MySQL(sql)
            except Exception as e:
                print '插入Target数据库错误' + str(e)
        elif isinstance(item, WeiboCommentItem):
            try:
                sql = """insert into Comment (Comment_ID, Comment_Name, Comment_Content, Comment_Time, Comment_Liked, Comment_Platform, Comment_Personal_Url, Tweet_Owner) VALUES ("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")"""%(item["Comment_ID"].encode('utf-8', 'ignore'), item["Comment_Name"].encode('utf-8', 'ignore'), item["Comment_Content"].encode('utf-8', 'ignore'), item["Comment_Time"].encode('utf-8', 'ignore'), item["Comment_Liked"], item["Comment_Platform"].encode('utf-8', 'ignore'), item["Comment_Personal_Url"].encode('utf-8', 'ignore'), item["Tweet_Owner"].encode('utf-8', 'ignore'))
                self.db.Insert_MySQL(sql)
            except Exception as e:
                print '插入Comment数据库错误' + str(e)
        elif isinstance(item, WeiboPersonalItem):
            try:
                sql = """insert into Personal (Personal_ID, Personal_Name, Personal_Tweet_Num, Personal_Fans, Personal_Follow_Num, Personal_Sex, Personal_City, Personal_Birth, Personal_Level, Personal_Sentiment, Personal_Introduce, Personal_Authentication) VALUES ("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")"""%(item["Personal_ID"].encode('utf-8', 'ignore'), item["Personal_Name"].encode('utf-8', 'ignore'), item["Personal_Tweet_Num"], item["Personal_Fans"], item["Personal_Follow_Num"], item["Personal_Sex"].encode('utf-8', 'ignore'), item["Personal_City"].encode('utf-8', 'ignore'), item["Personal_Birth"].encode('utf-8', 'ignore'), item["Personal_Level"].encode('utf-8', 'ignore'), item["Personal_Sentiment"].encode('utf-8', 'ignore'), item["Personal_Introduce"].encode('utf-8', 'ignore'), item["Personal_Authentication"].encode('utf-8', 'ignore'))
                self.db.Insert_MySQL(sql)
            except Exception as e:
                print '插入Personal数据库错误' + str(e)



