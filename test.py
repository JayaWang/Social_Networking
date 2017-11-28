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

import datetime
YMD = datetime.datetime.now().strftime('%m-%d-%H-%M').split('-')
print YMD

import re
date = '11月25日'
old = re.findall('(\d+)月(\d+)日', date)
print old[0][0], old[0][1]
import re
text ='<span class="tc">微博[308]</span><a href="/1784609372/follow">关注[85]</a><a href="/1784609372/fans">粉丝[511]</a>'

tweet_num = re.findall('微博\[(\d*)\]', text)[0]
fans = re.findall('粉丝\[(\d*)\]', text)[0]
follow_num = re.findall('关注\[(\d*)\]', text)[0]
print tweet_num, fans, follow_num
url = 'https://weibo.cn/u/5457837135'
ID = re.findall('/u/(\d+)', url)[0] #用户ID
print ID

for i in [1,2,3,4,5,6,7,8]:
    if i in [2,4,6,8]:
        continue
    print i'''

a = 'qwertyui'
print a[2:]
