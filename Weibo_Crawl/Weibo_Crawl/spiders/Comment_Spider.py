# -*- coding: utf-8 -*-

#爬取评论页的具体评论内容，并且提供评论者个人主页地址
from scrapy.selector import Selector
from scrapy_redis.spiders import RedisSpider
from items import WeiboCommentItem
import re
from scrapy import Request
import datetime
from With_DB import Redis_DB

class C_Spider(RedisSpider):
    name = 'CommentSpider'
    redis_key = 'Comment_urls' #查看了，格式都一样，page做翻页

    def parse(self, response):
        selector = Selector(response)
        last = re.findall('\|\|\|(.*)', response.url)  # 末尾信息
        Up_Time = last[:-1] #上一次更新评论区的时间
        sign_comment = last[-1] #更新标志位
        divs = selector.xpath('body/div[@class="c" and @id]')  # 当页的所有评论
        sign_time = 0
        for div in divs:
            try:
                Comment_ID = div.xpath('a[1]/@href') #这个id有脏的链接，但是可以直接拼着用
                Comment_Name = div.xpath('a[1]/text()').extract[0]
                Comment_Content = div.xpath('span[@class="ctt"]/text()').extract()[0]
                Comment_Liked = re.findall('赞\[(\d+)\]'.decode('utf8'), div.extract())  # 点赞数
                tp = div.xpath('span[@class="ct"]/text()').extract()

                item = WeiboCommentItem()
                if Comment_ID:
                    item["Comment_ID"] = Comment_ID
                    personal_url = 'https://weibo.cn' + str(Comment_ID)
                    item["Comment_Personal_Url"] = personal_url
                if Comment_Name:
                    item["Comment_Name"] = Comment_Name
                if Comment_Content:
                    item["Comment_Content"] = Comment_Content
                if Comment_Liked:
                    item["Comment_Liked"] = Comment_Liked
                if tp:
                    tp = tp[0].split('来自'.decode('utf8'))
                    item["Comment_Time"] = tp[0].replace(u"\xa0", "")
                    # 做个爬取的判断，判断还要不要翻页
                    if sign_comment == 'Y':
                        if self.Date_Measure(Up_Time, tp[0]) > 0: #老的
                            sign_time +=1
                        else:
                            pass
                    else:
                        pass
                    if len(tp) == 2:  # 保证有平台
                        item["Comment_Platform"] = tp[1].replace(u"\xa0", "")
                yield WeiboCommentItem
                r2 = Redis_DB(2)  # 个人信息扔到db2
                r2.Insert_Redis('Personal_urls', personal_url)
            except Exception as e:
                print '抓取评论页面错误' + str(e)
        if sign_time == 0:
            try:
                url_next = selector.xpath(
                    'body/div[@id="pagelist"]/form/div/a[1]/@href').extract()
                if url_next:
                    r1 = Redis_DB(1) #评论页扔到db1里
                    url = 'https://weibo.cn' + url_next
                    r1.Insert_Redis('Comment_urls', url)
            except Exception as e:
                print ('插入redis队列错误' + str(e))

    def Date_Measure(self, Up_Time, Comment_Time):
        if '年' in Comment_Time:
            return 100 #随便写个大于0的
        elif '月' in Comment_Time:
            Up_Time = Up_Time.split('-')
            upt = datetime.datetime(Up_Time[0], Up_Time[1], Up_Time[2], Up_Time[3], Up_Time[4])
            a = re.findall('(\d+)月(\d+)日\s(\d+):(\d+)', Comment_Time)
            cmt = datetime.datetime(Up_Time[0], a[0][0], a[0][1], a[0][2], a[0][3])
            b = upt - cmt
            if 'day' in str(b):
                return -1
            else:
                return 1
        else: #今天的帖子
            return -1




