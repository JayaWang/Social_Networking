# -*- coding: utf-8 -*-

import scrapy

class WeiboTargetItem(scrapy.Item):
    Target_ID = scrapy.Field() #用户id-微博id
    Target_Name = scrapy.Field() #名字
    Tweet_Time = scrapy.Field() #发布时间
    Tweet_Content = scrapy.Field() #内容
    Tweet_Transfer = scrapy.Field() #转发数
    Tweet_Liked = scrapy.Field() #点赞数
    Tweet_Comment = scrapy.Field() #评论数
    Tweet_Platform = scrapy.Field() #发布设备
    Tweet_GPS = scrapy.Field() #发布地理位置
    Comment_Urls = scrapy.Field() #评论页主页
    Update_Time = scrapy.Field() #爬取本条的时间，用于做评论增量的判断
    Tweet_Over = scrapy.Field() #给target和comment参考

class WeiboCommentItem(scrapy.Item):
    Comment_ID = scrapy.Field() #评论者ID
    Comment_Name = scrapy.Field() #评论者名字
    Comment_Content = scrapy.Field() #评论内容
    Comment_Time = scrapy.Field() #评论时间
    Comment_Liked = scrapy.Field() #评论点赞数
    Comment_Platform =scrapy.Field() #发布设备
    Comment_Personal_Url =scrapy.Field() #评论者个人主页

class WeiboPersonalItem(scrapy.Item):
    Personal_ID = scrapy.Field() #用户ID
    Personal_Name = scrapy.Field() #名字
    Personal_Tweet_Num = scrapy.Field() #微博数
    Personal_Fans = scrapy.Field() #粉丝数
    Personal_Follow_Num = scrapy.Field() #关注数
    Personal_Sex = scrapy.Field() #性别
    Personal_City = scrapy.Field() #城市
    Personal_Birth = scrapy.Field() #生日
    Personal_Level = scrapy.Field() #等级
    Personal_Sentiment = scrapy.Field() #感情状况
    Personal_Introduce = scrapy.Field() #简介
    Personal_Authentication = scrapy.Field() #认证
    Personal_Tags = scrapy.Field() #标签



