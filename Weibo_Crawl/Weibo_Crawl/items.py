# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WeiboTargetItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Target_Name = scrapy.Field() #名字
    Tweet_Time = scrapy.Field() #发布时间
    Tweet_Content = scrapy.Field() #内容
    Tweet_Forward = scrapy.Field() #转发数
    Tweet_Liked = scrapy.Field() #点赞数
    Tweet_Comment = scrapy.Field() #评论数
    Tweet_Platform = scrapy.Field() #发布设备
    Tweet_GPS = scrapy.Field() #发布地理位置
    Comment_Urls = scrapy.Field() #评论页主页

class WeiboCommentItem(scrapy.Item):
    Comment_Name = scrapy.Field() #评论者名字
    Comment_Content = scrapy.Field() #评论内容
    Comment_Time = scrapy.Field() #评论时间
    Comment_Liked = scrapy.Field() #评论点赞数
    Comment_Platform =scrapy.Field() #发布设备
    Comment_GPS = scrapy.Field() #发布地理位置
    Comment_Personal_Url =scrapy.Field() #评论者个人主页

class WeiboPersonalItm(scrapy.Item):
    Personal_Name = scrapy.Field() #名字
    Personal_Tweet_Num = scrapy.Field() #微博数
    Personal_Fans = scrapy.Field() #粉丝数
    Personal_Follow_Num = scrapy.Field() #关注数
    Personal_Sex = scrapy.Field() #性别
    Personal_City = scrapy.Field() #城市
    Personal_Grade = scrapy.Field() #等级
    Personal_Introduce = scrapy.Field() #简介
    Personal_Tags = scrapy.Field() #标签



