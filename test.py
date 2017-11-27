# -*- coding: utf-8 -*-

'''import redis

r0 = redis.Redis(host='127.0.0.1', port=6379, db=0)
key = r0.keys()
print key[-1]

a = "09月16日 23:01&nbsp;来自iPhone 7 Plus"
print a.split("&nbsp;")[0]
print '---'
print a.split("&nbsp;")[1]
import re
a = '<a href="https://weibo.cn/comment/Fm8245xFU?uid=5187664653&amp;rl=0#cmtfrm" class="cc xh-highlight">评论[34281]</a>'
b = re.findall('(?<='<a href="').*?(?='评论\[(\d+)\]')', a)
print b
'''
import datetime
data = datetime.datetime.now().strftime('%Y-%m-%d')
a = datetime.datetime(3,1)
b = datetime.datetime(2,28)
print data
'''
import re
date = '11月25日'
old = re.findall('(\d+)月(\d+)日', date)
print old[0][0], old[0][1]'''

