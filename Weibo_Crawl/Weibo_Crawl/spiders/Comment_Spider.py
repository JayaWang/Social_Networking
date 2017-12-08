# -*- coding: utf-8 -*-

#爬取评论页的具体评论内容，并且提供评论者个人主页地址
from scrapy.selector import Selector
from scrapy_redis.spiders import RedisSpider
from Weibo_Crawl.items import WeiboCommentItem
import re
from scrapy import Request
import datetime
from Weibo_Crawl.With_DB import Redis_DB

class C_Spider(RedisSpider):
    name = 'CommentSpider'
    redis_key = 'Comment_urls' #查看了，格式都一样，page做翻页

    def parse(self, response):
        selector = Selector(response)
        Up_Time = response.meta['sign0'] #上一次更新评论区的时间
        sign_comment = response.meta['sign1'] #更新标志位
        divs = selector.xpath('body/div[@class="c" and @id]')  # 当页的所有评论
        sign_time = 0
        try:
            Tweet_Owner = selector.xpath('body/div[@id="M_"]/div[1]/a[1]/text()').extract()
        except Exception as e:
            print '微博作者提取错误' + str(e)
        for div in divs:
            try:
                Comment_ID = div.xpath('a[1]/@href').extract() #这个id有脏的链接，但是可以直接拼着用
                Comment_Name = div.xpath('a[1]/text()').extract()
                Comment_Content = div.xpath('span[@class="ctt"]/text()').extract()
                Comment_Liked = re.findall(u'赞\[(\d+)\]', div.extract())  # 点赞数
                tp = div.xpath('span[@class="ct"]/text()').extract()
                item = WeiboCommentItem()
                if Comment_ID:
                    item["Comment_ID"] = Comment_ID[0]
                    personal_url = 'https://weibo.cn' + str(Comment_ID[0])
                    item["Comment_Personal_Url"] = personal_url
                else:
                    item["Comment_Personal_Url"] = ''
                    personal_url = ''
                if Tweet_Owner:
                    item['Tweet_Owner'] = Tweet_Owner[0]
                else:
                    item['Tweet_Owner'] = ''
                if Comment_Name:
                    item["Comment_Name"] = Comment_Name[0]
                else:
                    item["Comment_Name"] = ''
                if Comment_Content:
                    if Comment_Content[0] == u'回复':
                        more_content = div.xpath('span[@class="ctt"]/text()[last()]').extract() #回复后面的内容
                        all_content = Comment_Content[0] + '|||' + more_content[0]
                        item["Comment_Content"] = all_content
                    else:
                        item["Comment_Content"] = Comment_Content[0]
                else:
                    item["Comment_Content"] = ''
                if Comment_Liked:
                    item["Comment_Liked"] = int(Comment_Liked[0])
                else:
                    item["Comment_Liked"] = ''
                if tp:
                    tp = tp[0].split(u'来自') #单纯的时间
                    item["Comment_Time"] = tp[0].replace(u"\xa0", "")
                    # 做个爬取的判断，判断还要不要翻页
                    if sign_comment == 'Y':
                        if div.xpath('/span[@class="kt"]/text()').extract() == False: #对热门贴的时间不做判断
                            if self.Date_Measure(Up_Time, tp[0]) > 0: #老的
                                sign_time +=1
                            else:
                                pass
                    else:
                        pass
                    if len(tp) == 2:  # 保证有平台
                        item["Comment_Platform"] = tp[1].replace(u"\xa0", "")
                    else:
                        item["Comment_Platform"] = ''
                print item["Comment_ID"].encode('utf-8', 'ignore'), item["Comment_Name"].encode('utf-8', 'ignore'), item["Comment_Content"].encode('utf-8', 'ignore'), item["Comment_Time"].encode('utf-8', 'ignore'), item["Comment_Liked"], item["Comment_Platform"].encode('utf-8', 'ignore'), item["Comment_Personal_Url"].encode('utf-8', 'ignore')
                yield item
                r2 = Redis_DB(0)  # 个人信息扔到db0
                r2.Insert_Redis('Personal_urls', personal_url)
            except Exception as e:
                print '抓取评论页面错误' + str(e)
        if sign_time == 0:
            try:
                url_next = selector.xpath(
                    'body/div[@id="pagelist"]/form/div/a[1]/@href').extract()
                if url_next:
                    r1 = Redis_DB(0) #评论页扔到db0里
                    url = 'https://weibo.cn' + url_next[0] + '|||' + Up_Time + sign_comment
                    r1.Insert_Redis('Comment_urls', url)
            except Exception as e:
                print ('插入redis队列错误' + str(e))

    def Date_Measure(self, Up_Time, Comment_Time):
        if u'年' in Comment_Time:
            return 1  # 随便写个大于0的
        elif u'月' in Comment_Time:
            Up_Time = Up_Time.split('-')
            upt = datetime.datetime(int(Up_Time[0]), int(Up_Time[1]), int(Up_Time[2]), int(Up_Time[3]), int(Up_Time[4]))
            a = re.findall(u'(\d+)月(\d+)日\s(\d+):(\d+)', Comment_Time)
            cmt = datetime.datetime(int(Up_Time[0]), int(a[0][0]), int(a[0][1]), int(a[0][2]), int(a[0][3]))
            b = upt - cmt
            a = str(b)[0]
            if a == '-':
                return -1
            else:
                return 1
        else:  # 今天的帖子
            return -1





