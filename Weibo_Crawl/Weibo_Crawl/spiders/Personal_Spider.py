# -*- coding: utf-8 -*-

#爬取个人信息的爬虫，每个用户只爬一次，注意去重
from scrapy.selector import Selector
from scrapy_redis.spiders import RedisSpider
from Weibo_Crawl.items import WeiboPersonalItem
import re
from scrapy import Request
import datetime

class P_Spider(RedisSpider):
    name = 'PersonalSpider'
    redis_key = 'Personal_urls' #url为个人主页，之后会跳到info

    def parse(self, response):
        selector = Selector(response)
        try:
            text = ";".join(selector.xpath('body/div[@class="u"]/div[@class="tip2"]').extract())
            tweet_num = re.findall(u'微博\[(\d*)\]', text)[0]
            follow_num = re.findall(u'关注\[(\d*)\]', text)[0]
            fans = re.findall(u'粉丝\[(\d*)\]', text)[0]
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
            name = re.findall(u'昵称[：:]?(.*?);', text1)
            sex = re.findall(u'性别[：:]?(.*?);', text1)
            city = re.findall(u'地区[：:]?(.*?);', text1)
            introduction = re.findall(u'简介[：:]?(.*?);', text1)
            birthday = re.findall(u'生日[：:]?(.*?);', text1)
            sentiment = re.findall(u'感情状况[：:]?(.*?);', text1)
            level = re.findall(u'会员等级[：:]?(.*?);', text1)
            authentication = re.findall(u'认证[：:]?(.*?);', text1)
            #还有个标签，先放着，等下再想想

            item = WeiboPersonalItem()
            item["Personal_ID"] = str(ID)
            item["Personal_Tweet_Num"] = int(tweet_num)
            item["Personal_Follow_Num"] = int(follow_num)
            item["Personal_Fans"] = int(fans)
            if name and name[0]:
                item["Personal_Name"] = name[0].replace(u"\xa0", "")
            else:
                item["Personal_Name"] = ''
            if sex and sex[0]:
                item["Personal_Sex"] = sex[0].replace(u"\xa0", "")
            else:
                item["Personal_Sex"] = ''
            if city and city[0]:
                city = city[0].replace(u"\xa0", "").split(" ")
                item["Personal_City"] = city[0] #只要省份就够了
                '''if len(city) > 1:
                    item["Personal_City"] = city[1]'''
            else:
                item["Personal_City"] = ''
            if introduction and introduction[0]:
                item["Personal_Introduce"] = introduction[0].replace(u"\xa0", "")
            else:
                item["Personal_Introduce"] = ''
            if birthday and birthday[0]:
                try:
                    birthday = datetime.datetime.strptime(birthday[0], "%Y-%m-%d")
                    item["Personal_Birth"] = str(birthday - datetime.timedelta(hours=8))
                except Exception:
                    item['Personal_Birth'] = birthday[0]  # 有可能是星座，而非时间
            else:
                item["Personal_Birth"] = ''
            if sentiment and sentiment[0]:
                item["Personal_Sentiment"] = sentiment[0].replace(u"\xa0", "")
            else:
                item["Personal_Sentiment"] = ''
            if level and level[0]:
                item["Personal_Level"] = level[0].replace(u"\xa0", "")
            else:
                item["Personal_Level"] = ''
            if authentication and authentication[0]:
                item["Personal_Authentication"] = authentication[0].replace(u"\xa0", "")
            else:
                item["Personal_Authentication"] = ''
            yield item
        except Exception as e:
            print '爬取个人资料页错误' + str(e)
