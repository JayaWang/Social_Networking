# -*- coding: utf-8 -*-

#爬取目标人物的微博，第一次爬一整个月的，之后保持一个星期的更新
from scrapy.selector import Selector
from scrapy_redis.spiders import RedisSpider
from Weibo_Crawl.With_DB import Redis_DB, Mysql_DB
from Weibo_Crawl.items import WeiboTargetItem
import re
import datetime

class T_Spider(RedisSpider):
    name = 'TargetSpider'
    redis_key = 'Target_urls'

    def parse(self, response):
        selector = Selector(response)
        name = response.meta['sign0']
        sign_tweet = response.meta['sign1'] #标志位
        sign_time = 0
        try:
            U_ID = re.findall('\/u\/(\d+)', response.url)[0] #用户ID
        except Exception as e:
            print 'U_ID提取错误' + str(e)
        divs = selector.xpath('body/div[@class="c" and @id]') #当页的所有微博
        for div in divs:
            try:
                T_id = div.xpath('@id').extract_first()  # 微博id
                content = div.xpath('div/span[@class="ctt"]//text()').extract()  # 微博内容
                GPS = div.xpath('div/a/@href').extract()  # 定位坐标，注意是个链接，能直接用第三方标注在地图上
                liked = re.findall(u'赞\[(\d+)\]', div.extract())  # 点赞数
                transfer = re.findall(u'转发\[(\d+)\]', div.extract())  # 转载数
                comment = re.findall(u'评论\[(\d+)\]', div.extract())  # 评论数
                #comment_url = div.xpath('div/a[@class="cc"]/@href').extract() #评论页地址
                comment_url = 'https://weibo.cn/comment/' + str(T_id[2:]) + '?uid=' + str(U_ID) + '&page=1'
                tp = div.xpath('div/span[@class="ct"]/text()').extract()
                Up_time = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M') # 当前时间

                item = WeiboTargetItem()
                item["Target_ID"] = U_ID + "-" + T_id[2:]
                item["Target_Name"] = name
                item["Update_Time"] = Up_time #标记的时间是给下次做参照的
                if content:
                    item["Tweet_Content"] = " ".join(content).strip(u'[位置]')  # 去掉最后的"[位置]"
                else:
                    item["Tweet_Content"] = ''
                if GPS:
                    GPS = re.findall('center=([\d.,]+)', GPS[0]) #把坐标提取出来
                    if GPS:
                        item["Tweet_GPS"] = GPS[0]
                    else:
                        item["Tweet_GPS"] = ''
                if liked:
                    item["Tweet_Liked"] = int(liked[0])
                else:
                    item["Tweet_Liked"] = ''
                if transfer:
                    item["Tweet_Transfer"] = int(transfer[0])
                else:
                    item["Tweet_Transfer"] = ''
                if comment:
                    item["Tweet_Comment"] = int(comment[0])
                else:
                    item["Tweet_Comment"] = ''
                if comment_url:
                    item["Comment_Urls"] = comment_url
                else:
                    item["Comment_Urls"] = ''
                if tp:
                    tp = tp[0].split(u'来自')
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
                    else:
                        item["Tweet_Platform"] = ''
                    try:
                        m1 = Mysql_DB()
                        sql = 'select Update_Time from Tweet where "' + str(U_ID) + '-' + str(T_id[2:]) + '" in (Target_ID)'
                        sign_tweet_tmp = m1.Query_MySQL(sql)
                        if sign_tweet_tmp == ():
                            sign_comment = 'N'
                            sign_tweet_uptime = 'no_time'
                        else:
                            sign_comment = 'Y'
                            sign_tweet_uptime = sign_tweet_tmp[0][0]
                    except Exception as e:
                        print '判断sign_comment错误' + str(e)
                    if sign_comment:
                        item["Tweet_Over"] = sign_comment
                    else:
                        item["Tweet_Over"] = ''
                r1 = Redis_DB(0) #评论相关扔到db0
                comment_url_sign = comment_url + '|||' + str(sign_tweet_uptime.encode('utf-8', 'ignore')) + sign_comment #前面是地址,|||后是更新时间,[-1]是标志位,判断comment里是否启用更新时间
                r1.Insert_Redis('Comment_urls', comment_url_sign)
                yield item
            except Exception as e:
                print ('抓取页面内容错误' + str(e))
        if sign_time == 0:
            try:
                url_next = selector.xpath(
                    u'body/div[@class="pa" and @id="pagelist"]/form/div/a[text()="下页"]/@href').extract()
                if url_next:
                    url_all = url_next[0] + '|||' + name + sign_tweet
                    r0 = Redis_DB(0) #翻页爬微博扔到db0里
                    r0.Insert_Redis('Target_urls', url_all)
            except Exception as e:
                print ('插入redis队列错误' + str(e))

    def Date_Measure(self, date):
        try:
            if u'年' in date:
                return 100 #随便写个大于7的
            elif u'月' in date:
                YMD = datetime.datetime.now().strftime('%Y-%m-%d').split('-')
                now = datetime.datetime(int(YMD[0]), int(YMD[1]), int(YMD[2]))
                a = re.findall(u'(\d+)月(\d+)日', date)
                old = datetime.datetime(int(YMD[0]), int(a[0][0]), int(a[0][1]))
                b = now - old
                try:
                    c = re.findall('(\d*)\sday', str(b))[0]
                except:
                    pass
                return int(c)
            else: #今天的帖子
                return 0
        except Exception as e:
            print '日期测量错误' + str(e)
