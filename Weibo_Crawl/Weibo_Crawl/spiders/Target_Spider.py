# -*- coding: utf-8 -*-

from scrapy.selector import Selector
from scrapy_redis.spiders import RedisSpider
from With_DB import Redis_DB
from items import WeiboTargetItem
import re

class T_Spider(RedisSpider):
    name = "TargetSpider"
    redis_key = 'Target_urls'

    def parse(self, response):
        selector = Selector(response)
        name = response.meta['name'] #名字
        ID = re.findall('(\d+)/profile', response.url)[0] #目标人物ID
        divs = selector.xpath('body/div[@class="c" and @id]') #当页的所有微博id
        for div in divs:
            try:
                items = WeiboTargetItem()
                id = div.xpath('@id').extract_first()  # 微博id
                content = div.xpath('div/span[@class="ctt"]//text()').extract()  # 微博内容
                gps = div.xpath('div/a/@href').extract()  # 定位坐标，注意是个链接，能直接用第三方标注在地图上
                liked = re.findall('赞\[(\d+)\]'.decode('utf8'), div.extract())  # 点赞数
                transfer = re.findall('转发\[(\d+)\]'.decode('utf8'), div.extract())  # 转载数
                comment = re.findall('评论\[(\d+)\]'.decode('utf8'), div.extract())  # 评论数
                comment_url = re.findall('https://weibo.cn/comment/(.*)', div.extract()) #评论页地址--------
                tp = div.xpath('div/span[@class="ct"]/text()').extract()
                time = tp.split("&nbsp;")[0] #时间
                platform = tp.split("&nbsp;")[1] #平台

                tweetsItems["_id"] = ID + "-" + id
                tweetsItems["ID"] = ID
                if content:
                    tweetsItems["Content"] = " ".join(content).strip('[位置]'.decode('utf8'))  # 去掉最后的"[位置]"
                if cooridinates:
                    cooridinates = re.findall('center=([\d.,]+)', cooridinates[0])
                    if cooridinates:
                        tweetsItems["Co_oridinates"] = cooridinates[0]
                if like:
                    tweetsItems["Like"] = int(like[0])
                if transfer:
                    tweetsItems["Transfer"] = int(transfer[0])
                if comment:
                    tweetsItems["Comment"] = int(comment[0])
                if others:
                    others = others[0].split('来自'.decode('utf8'))
                    tweetsItems["PubTime"] = others[0].replace(u"\xa0", "")
                    if len(others) == 2:
                        tweetsItems["Tools"] = others[1].replace(u"\xa0", "")
                yield tweetsItems
            except Exception, e:
                pass

        url_next = selector.xpath(
            'body/div[@class="pa" and @id="pagelist"]/form/div/a[text()="下页"]/@href'.decode('utf8')).extract()
        if url_next:
            yield Request(url=self.host + url_next[0], callback=self.parse_tweets, dont_filter=True)





