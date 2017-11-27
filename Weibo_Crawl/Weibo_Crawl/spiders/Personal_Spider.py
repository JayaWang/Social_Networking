# -*- coding: utf-8 -*-

#爬取个人信息的爬虫，每个用户只爬一次，注意去重
from scrapy.selector import Selector
from scrapy_redis.spiders import RedisSpider
from With_DB import Redis_DB
from scrapy import Request
from items import WeiboTargetItem
import re

class P_Spider(RedisSpider):
    name = 'PersonalSpider'
    redis_key = 'Personal_urls'

