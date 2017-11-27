# -*- coding: utf-8 -*-

#爬取个人信息的爬虫，每个用户只爬一次，注意去重
from scrapy.selector import Selector
from scrapy_redis.spiders import RedisSpider
from items import WeiboPersonalItm
import re
from scrapy import Request
import datetime

class P_Spider(RedisSpider):
    name = 'PersonalSpider'
    redis_key = 'Personal_urls' #url为个人主页，之后会跳到info

    def parse(self, response):
        selector = Selector(response)
        try:
            text = ";".join(selector.xpath('body/div[@class="u"]/div[@class="tip2]//text()"').extract())
            tweet_num = re.findall('微博\[(\d*)\]', text)[0]
            follow_num = re.findall('关注\[(\d*)\]', text)[0]
            fans = re.findall('粉丝\[(\d*)\]', text)[0]
            ID = re.findall('/u/(\d+)', response.url)[0] #用户ID
            info_url = 'https://weibo.cn/' + str(ID) + '/info'
            yield Request(url=info_url, callback=self.parse_info, meta={'tweet_num':tweet_num, 'follow_num':follow_num, 'fans':fans})
        except Exception as e:
            print '爬个人主页错误' + str(e)

    def parse_info(self, response):
        selector = Selector(response)
        ID = re.findall('(\d+)/info', response.url)[0] #用户ID
        tweet_num = response.meta['tweet_num']
        follow_num = response.meta['follow_num']
        fans = response.meta['fans']
        try:
            text1 = ";".join(selector.xpath('body/div[@class="c"]//text()').extract())  #为啥要join下？
            name = re.findall('昵称[：:]?(.*?);'.decode('utf8'), text1)
            sex = re.findall('性别[：:]?(.*?);'.decode('utf8'), text1)
            city = re.findall('地区[：:]?(.*?);'.decode('utf8'), text1)
            introduction = re.findall('简介[：:]?(.*?);'.decode('utf8'), text1)
            birthday = re.findall('生日[：:]?(.*?);'.decode('utf8'), text1)
            sentiment = re.findall('感情状况[：:]?(.*?);'.decode('utf8'), text1)
            level = re.findall('会员等级[：:]?(.*?);'.decode('utf8'), text1)
            authentication = re.findall('认证[：:]?(.*?);'.decode('utf8'), text1)
            #还有个标签，先放着，等下再想想

            item = WeiboPersonalItm()
            item["Personal_ID"] = ID
            item["Personal_Tweet_Num"] = tweet_num
            item["Personal_Follow_Num"] = follow_num
            item["Personal_Fans"] = fans
            if name and name[0]:
                item["Personal_Name"] = name[0].replace(u"\xa0", "")
            if sex and sex[0]:
                item["Personal_Sex"] = sex[0].replace(u"\xa0", "")
            if city and city[0]:
                city = city[0].replace(u"\xa0", "").split(" ")
                item["Personal_City"] = city[0] #只要省份就够了
                '''if len(city) > 1:
                    item["Personal_City"] = city[1]'''
            if introduction and introduction[0]:
                item["Personal_Introduce"] = introduction[0].replace(u"\xa0", "")
            if birthday and birthday[0]:
                try:
                    birthday = datetime.datetime.strptime(birthday[0], "%Y-%m-%d")
                    item["Personal_Birth"] = birthday - datetime.timedelta(hours=8)
                except Exception:
                    item['Personal_Birth'] = birthday[0]  # 有可能是星座，而非时间
            if sentiment and sentiment[0]:
                item["Personal_Sentiment"] = sentiment[0].replace(u"\xa0", "")
            if level and level[0]:
                item["Personal_Level"] = level[0].replace(u"\xa0", "")
            if authentication and authentication[0]:
                item["Personal_Authentication"] = authentication[0].replace(u"\xa0", "")

            yield WeiboPersonalItm
        except Exception as e:
            print '爬取个人资料页错误' + str(e)
