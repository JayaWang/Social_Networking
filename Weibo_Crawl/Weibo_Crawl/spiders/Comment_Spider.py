# -*- coding: utf-8 -*-

#爬取评论页的具体评论内容，并且提供评论者个人主页地址
from scrapy.selector import Selector
from scrapy_redis.spiders import RedisSpider
from items import WeiboCommentItem
import re
from scrapy import Request
import datetime

class C_Spider(RedisSpider):
    name = 'CommentSpider'
    redis_key = 'Comment_urls' #查看了，格式都一样，page做翻页

    def parse(self, response):
        selector = Selector(response)
        Up_Time = response.url[-10:] #这里先暂定，到时候在redis队列的url里加入信息
        try:
            pass
        except Exception as e:
            pass
