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
    Comment_Urls = scrapy.Field() #评论页主页


