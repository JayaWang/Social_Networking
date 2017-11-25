# -*- coding: utf-8 -*-

import scrapy
from scrapy_redis.spiders import RedisSpider

class T_Spider(RedisSpider):
    name = "TargetSpider"
    redis_key = 'Target_urls'

    def parse(self, response):
        pass



