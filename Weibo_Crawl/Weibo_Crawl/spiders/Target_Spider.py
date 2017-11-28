# -*- coding: utf-8 -*-

#爬取目标人物的微博，第一次爬一整个月的，之后保持一个星期的更新
from scrapy.selector import Selector
from scrapy_redis.spiders import RedisSpider
from With_DB import Redis_DB, Mysql_DB
from items import WeiboTargetItem
import re
import datetime

class T_Spider(RedisSpider):
    name = 'TargetSpider'
    redis_key = 'Target_urls'

    def parse(self, response):
        selector = Selector(response)
        last = re.findall('\|\|\|(.*)', response.url) #末尾信息
        name = last[:-1]
        sign_tweet = last[-1] #用来做翻页程度的标志，N就翻一个月，Y就更新一周内的
        sign_time = 0
        U_ID = re.findall('(\d+)/profile', response.url)[0] #用户ID
        divs = selector.xpath('body/div[@class="c" and @id]') #当页的所有微博
        for div in divs:
            try:
                T_id = div.xpath('@id').extract_first()  # 微博id
                content = div.xpath('div/span[@class="ctt"]//text()').extract()  # 微博内容
                GPS = div.xpath('div/a/@href').extract()  # 定位坐标，注意是个链接，能直接用第三方标注在地图上
                liked = re.findall('赞\[(\d+)\]'.decode('utf8'), div.extract())  # 点赞数
                transfer = re.findall('转发\[(\d+)\]'.decode('utf8'), div.extract())  # 转载数
                comment = re.findall('评论\[(\d+)\]'.decode('utf8'), div.extract())  # 评论数
                #comment_url = div.xpath('div/a[@class="cc"]/@href').extract() #评论页地址
                comment_url = 'https://weibo.cn/comment/' + str(T_id[2:]) + '?uid=' + str(U_ID) + '&page=1'
                tp = div.xpath('div/span[@class="ct"]/text()').extract()
                Up_time = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M') # 当前时间

                item = WeiboTargetItem()
                item["Target_ID"] = U_ID + "-" + T_id
                item["Target_Name"] = name
                item["Update_Time"] = Up_time #标记的时间是给下次做参照的
                if content:
                    item["Tweet_Content"] = " ".join(content).strip('[位置]'.decode('utf8'))  # 去掉最后的"[位置]"
                if GPS:
                    GPS = re.findall('center=([\d.,]+)', GPS[0]) #把坐标提取出来
                    if GPS:
                        item["Tweet_GPS"] = GPS[0]
                if liked:
                    item["Tweet_Liked"] = int(liked[0])
                if transfer:
                    item["Tweet_Transfer"] = int(transfer[0])
                if comment:
                    item["Tweet_Comment"] = int(comment[0])
                if comment_url:
                    item["Comment_Urls"] = comment_url[0]
                if tp:
                    tp = tp[0].split('来自'.decode('utf8'))
                    item["Tweet_Time"] = tp[0].replace(u"\xa0", "")
                    #做个爬取的判断，判断还要不要翻页
                    if sign_tweet == 'Y':
                        if self.Date_Measure(tp[0]) <7:
                            pass
                        else:
                            sign_time += 1
                    else:
                        if self.Date_Measure(tp[0]) <30:
                            pass
                        else:
                            sign_time += 1
                    if len(tp) == 2: #保证有平台
                        item["Tweet_Platform"] = tp[1].replace(u"\xa0", "")
                    try:
                        m1 = Mysql_DB()
                        sql = 'select Update_Time from Tweet where "' + str(U_ID) + '-' + str(T_id) + '" in (Target_ID)'
                        sign_tweet_tmp = m1.Query_MySQL(sql)
                        if sign_tweet_tmp[0] == 'Empty':
                            sign_comment = 'N'
                        else:
                            sign_comment = 'Y'
                    except Exception as e:
                        print '判断sign_comment错误' + str(e)
                    if sign_comment:
                        item["Tweet_Over"] = sign_comment
                yield WeiboTargetItem
                r1 = Redis_DB(1) #评论相关扔到db1
                comment_url_sign = comment_url + '|||' + str(sign_tweet_tmp[0]) + sign_comment #前面是地址,|||后是更新时间,[-1]是标志位,判断comment里是否启用更新时间
                r1.Insert_Redis('Comment_urls', comment_url_sign)
            except Exception as e:
                print ('抓取页面内容错误' + str(e))
        if sign_time == 0:
            try:
                url_next = selector.xpath(
                    'body/div[@class="pa" and @id="pagelist"]/form/div/a[text()="下页"]/@href'.decode('utf8')).extract()
                if url_next:
                    r0 = Redis_DB(0) #翻页爬微博扔到db0里
                    r0.Insert_Redis('Target_urls', url_next)
            except Exception as e:
                print ('插入redis队列错误' + str(e))

    def Date_Measure(self, date):
        if '年' in date:
            return 100 #随便写个大于7的
        elif '月' in date:
            YMD = datetime.datetime.now().strftime('%Y-%m-%d').split('-')
            now = datetime.datetime(YMD[0], YMD[1], YMD[2])
            a = re.findall('(\d+)月(\d+)日', date)
            old = datetime.datetime(YMD[0], a[0][0], a[0][1])
            b = now - old
            try:
                c = re.findall('(\d*)\sday', str(b))[0]
            except:
                pass
            return int(c)
        else: #今天的帖子
            return 0

