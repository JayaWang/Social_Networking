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
    print i

a = 'qwertyui'
print a[2:]
import re
a = 'http://www.baidu.com|||woshiwangjiayunY'
r = re.findall('\|\|\|(.*)', a)
print r[0][:-1]
for i in [1,2,3,4,5]:
    if i == 2:
        kk = 'Y'

print kk
import re
a = '<a href="/u/5817026063">用户5817026063</a>'
U_ID = re.findall('用户(\d*)', a)
print U_ID[0]
import datetime
import re
a = datetime.datetime(2017, 11, 27, 11, 11)
b = datetime.datetime(2017, 11, 27, 11, 11)
c = a - b
if 'day' in str(c):
    print 'a<b'
else:
    print 'a>b'


import re, datetime
date = 'Ong东仔 :有点儿张一山  举报   赞[0]  回复   11月27日 13:01 来自iPhone客户端'
a = re.findall('(\d+)月(\d+)日\s(\d+):(\d+)', date)
print a[0]
import re
import datetime
from lxml import etree
from scrapy import Selector
def a():
    selector = etree('<body><div class="tm"><a href="https://weibo.cn/msg/?unread=37"><span class="tmn">37</span>私信</a>&nbsp;&nbsp;<a href="https://weibo.cn/msg/clearAllUnread?type=dcm&amp;rl=0"><img src="https://h5.sinaimg.cn/upload/2016/12/30/125/5366.gif" alt="[X]"></a><br></div><div class="n" style="padding: 6px 4px;"><a href="https://weibo.cn/?tf=5_009" class="nl">首页<span class="tk">!</span></a>|<a href="https://weibo.cn/msg/?tf=5_010" class="nl">消息</a>|<a href="https://huati.weibo.cn" class="nl">话题</a>|<a href="https://weibo.cn/search/?tf=5_012" class="nl">搜索</a>|<a href="/u/5187664653?rand=4146&amp;p=r" class="nl">刷新</a></div><div class="c tip"><a href="http://m.weibo.cn" id="top" class="tl">手机微博触屏版,点击前往&gt;&gt;</a></div><div class="u"><table><tbody><tr><td valign="top"><a href="/5187664653/avatar?rl=0"><img src="http://tvax3.sinaimg.cn/crop.0.0.512.512.50/005F4Uyxly8fet0xr9thnj30e80e8jrx.jpg" alt="头像" class="por"></a></td><td valign="top"><div class="ut"><span class="ctt">邓超<img src="https://h5.sinaimg.cn/upload/2016/05/26/319/5338.gif" alt="V"><a href="http://vip.weibo.cn/?F=W_tq_zsbs_01"><img src="https://h5.sinaimg.cn/upload/2016/05/26/319/donate_btn_s.png" alt="M"></a>&nbsp;男/北京    &nbsp;    <a href="/attention/add?uid=5187664653&amp;rl=0&amp;st=20bb87">加关注</a></span><br><span class="ctt">认证：演员、导演邓超</span><br><span class="ctt" style="word-break:break-all; width:50px;"></span><br><a href="/im/chat?uid=5187664653&amp;rl=0">私信</a>&nbsp;<a href="/5187664653/info">资料</a>&nbsp;<a href="/5187664653/operation?rl=0">操作</a>&nbsp;<a href="/attgroup/special?fuid=5187664653&amp;st=20bb87">特别关注</a>&nbsp;<a href="http://new.vip.weibo.cn/vippay/payother?present=1&amp;action=comfirmTime&amp;uid=5187664653">送Ta会员</a></div></td></tr></tbody></table><div class="tip2"><span class="tc">微博[985]</span>&nbsp;<a href="/5187664653/follow">关注[219]</a>&nbsp;<a href="/5187664653/fans">粉丝[64057579]</a>&nbsp;<a href="/attgroup/opening?uid=5187664653">分组[1]</a>&nbsp;<a href="/at/weibo?uid=5187664653">@他的</a></div></div><div class="pmst"><span class="pms">&nbsp;微博&nbsp;</span><span class="pmsl">&nbsp;<a href="/5187664653/photo?tf=6_008">相册</a>&nbsp;</span></div><div class="pms">全部-<a href="/u/5187664653?filter=1">原创</a>-<a href="/u/5187664653?filter=2">图片</a>-<a href="/attgroup/opening?uid=5187664653">分组</a>-<a href="/5187664653/search?f=u&amp;rl=0">筛选</a></div><div class="c" id="M_FxloorAfE"><div><span class="ctt">12月22日 ​​​</span></div><div><a href="https://weibo.cn/mblog/pic/FxloorAfE?rl=0"><img src="http://wx2.sinaimg.cn/wap180/005F4Uyxgy1flz2m5m4cgj31dq1xgkjm.jpg" alt="图片" class="ib"></a>&nbsp;<a href="https://weibo.cn/mblog/oripic?id=FxloorAfE&amp;u=005F4Uyxgy1flz2m5m4cgj31dq1xgkjm">原图</a>&nbsp;<a href="https://weibo.cn/attitude/FxloorAfE/add?uid=5587613175&amp;rl=0&amp;st=20bb87">赞[222528]</a>&nbsp;<a href="https://weibo.cn/repost/FxloorAfE?uid=5187664653&amp;rl=0">转发[7501]</a>&nbsp;<a href="https://weibo.cn/comment/FxloorAfE?uid=5187664653&amp;rl=0#cmtfrm" class="cc">评论[10968]</a>&nbsp;<a href="https://weibo.cn/fav/addFav/FxloorAfE?rl=0&amp;st=20bb87">收藏</a><!---->&nbsp;<span class="ct">11月29日 17:15</span></div></div><div class="s"></div><div class="c" id="M_FwCObtcr9"><div><span class="cmt">转发了&nbsp;<a href="https://weibo.cn/dengchao">邓超</a><img src="https://h5.sinaimg.cn/upload/2016/05/26/319/5338.gif" alt="V"><img src="https://h5.sinaimg.cn/upload/2016/05/26/319/donate_btn_s.png" alt="M">&nbsp;的微博:</span><span class="ctt">我女儿主演的电影，请亲们疯狂转发，我会去你梦里当面致谢[doge] ​​​</span></div><div><a href="https://weibo.cn/mblog/pic/FwqSMhf5L?rl=0"><img src="http://wx3.sinaimg.cn/wap180/005F4Uyxgy1fls4yo443pj30tz195474.jpg" alt="图片" class="ib"></a>&nbsp;<a href="https://weibo.cn/mblog/oripic?id=FwqSMhf5L&amp;u=005F4Uyxgy1fls4yo443pj30tz195474">原图</a>&nbsp;<span class="cmt">赞[382037]</span>&nbsp;<span class="cmt">原文转发[23957]</span>&nbsp;<a href="https://weibo.cn/comment/FwqSMhf5L?rl=0#cmtfrm" class="cc">原文评论[10742]</a><!----></div><div><span class="cmt">转发理由:</span>不是到了今天，都不能完全理解这部电影的意义所在。真的要向这部电影的主创们致敬，以最郑重的方式。&nbsp;&nbsp;<a href="https://weibo.cn/attitude/FwCObtcr9/add?uid=5587613175&amp;rl=0&amp;st=20bb87">赞[207780]</a>&nbsp;<a href="https://weibo.cn/repost/FwCObtcr9?uid=5187664653&amp;rl=0">转发[3943]</a>&nbsp;<a href="https://weibo.cn/comment/FwCObtcr9?uid=5187664653&amp;rl=0#cmtfrm" class="cc">评论[4418]</a>&nbsp;<a href="https://weibo.cn/fav/addFav/FwCObtcr9?rl=0&amp;st=20bb87">收藏</a><!---->&nbsp;<span class="ct">11月24日 23:45</span></div></div><div class="s"></div><div class="c" id="M_FwqSMhf5L"><div><span class="ctt">我女儿主演的电影，请亲们疯狂转发，我会去你梦里当面致谢[doge] ​​​</span></div><div><a href="https://weibo.cn/mblog/pic/FwqSMhf5L?rl=0"><img src="http://wx3.sinaimg.cn/wap180/005F4Uyxgy1fls4yo443pj30tz195474.jpg" alt="图片" class="ib"></a>&nbsp;<a href="https://weibo.cn/mblog/oripic?id=FwqSMhf5L&amp;u=005F4Uyxgy1fls4yo443pj30tz195474">原图</a>&nbsp;<a href="https://weibo.cn/attitude/FwqSMhf5L/add?uid=5587613175&amp;rl=0&amp;st=20bb87">赞[382037]</a>&nbsp;<a href="https://weibo.cn/repost/FwqSMhf5L?uid=5187664653&amp;rl=0">转发[23957]</a>&nbsp;<a href="https://weibo.cn/comment/FwqSMhf5L?uid=5187664653&amp;rl=0#cmtfrm" class="cc">评论[10742]</a>&nbsp;<a href="https://weibo.cn/fav/addFav/FwqSMhf5L?rl=0&amp;st=20bb87">收藏</a><!---->&nbsp;<span class="ct">11月23日 17:23</span></div></div><div class="s"></div><div class="c" id="M_FvnuvfnKw"><div><span class="ctt">我当过英语课代表 ​​​</span>&nbsp;<a href="https://weibo.cn/attitude/FvnuvfnKw/add?uid=5587613175&amp;rl=0&amp;st=20bb87">赞[437521]</a>&nbsp;<a href="https://weibo.cn/repost/FvnuvfnKw?uid=5187664653&amp;rl=0">转发[4399]</a>&nbsp;<a href="https://weibo.cn/comment/FvnuvfnKw?uid=5187664653&amp;rl=0#cmtfrm" class="cc">评论[53977]</a>&nbsp;<a href="https://weibo.cn/fav/addFav/FvnuvfnKw?rl=0&amp;st=20bb87">收藏</a><!---->&nbsp;<span class="ct">11月16日 18:55</span></div></div><div class="s"></div><div class="c" id="M_Fv5P3ASct"><div><span class="ctt">你们穿高领毛衣勒脖子吗？ ​​​</span>&nbsp;<a href="https://weibo.cn/attitude/Fv5P3ASct/add?uid=5587613175&amp;rl=0&amp;st=20bb87">赞[318217]</a>&nbsp;<a href="https://weibo.cn/repost/Fv5P3ASct?uid=5187664653&amp;rl=0">转发[4925]</a>&nbsp;<a href="https://weibo.cn/comment/Fv5P3ASct?uid=5187664653&amp;rl=0#cmtfrm" class="cc">评论[37693]</a>&nbsp;<a href="https://weibo.cn/fav/addFav/Fv5P3ASct?rl=0&amp;st=20bb87">收藏</a><!---->&nbsp;<span class="ct">11月14日 21:56</span></div></div><div class="s"></div><div class="c" id="M_FuMTjwLnO"><div><span class="ctt">等等正面照[doge] ​​​</span></div><div><a href="https://weibo.cn/mblog/pic/FuMTjwLnO?rl=0"><img src="http://wx3.sinaimg.cn/wap180/005F4Uyxgy1flfmx5ehm3j32ba1og7wi.jpg" alt="图片" class="ib"></a>&nbsp;<a href="https://weibo.cn/mblog/oripic?id=FuMTjwLnO&amp;u=005F4Uyxgy1flfmx5ehm3j32ba1og7wi">原图</a>&nbsp;<a href="https://weibo.cn/attitude/FuMTjwLnO/add?uid=5587613175&amp;rl=0&amp;st=20bb87">赞[704674]</a>&nbsp;<a href="https://weibo.cn/repost/FuMTjwLnO?uid=5187664653&amp;rl=0">转发[13199]</a>&nbsp;<a href="https://weibo.cn/comment/FuMTjwLnO?uid=5187664653&amp;rl=0#cmtfrm" class="cc">评论[23903]</a>&nbsp;<a href="https://weibo.cn/fav/addFav/FuMTjwLnO?rl=0&amp;st=20bb87">收藏</a><!---->&nbsp;<span class="ct">11月12日 21:44</span></div></div><div class="s"></div><div class="c" id="M_FuEwD9AX4"><div><span class="ctt">等等，生日快乐[心] ​​​</span></div><div><a href="https://weibo.cn/mblog/pic/FuEwD9AX4?rl=0"><img src="http://wx3.sinaimg.cn/wap180/005F4Uyxgy1flelybor3zj307r0eugme.jpg" alt="图片" class="ib"></a>&nbsp;<a href="https://weibo.cn/mblog/oripic?id=FuEwD9AX4&amp;u=005F4Uyxgy1flelybor3zj307r0eugme">原图</a>&nbsp;<a href="https://weibo.cn/attitude/FuEwD9AX4/add?uid=5587613175&amp;rl=0&amp;st=20bb87">赞[975626]</a>&nbsp;<a href="https://weibo.cn/repost/FuEwD9AX4?uid=5187664653&amp;rl=0">转发[4161]</a>&nbsp;<a href="https://weibo.cn/comment/FuEwD9AX4?uid=5187664653&amp;rl=0#cmtfrm" class="cc">评论[35498]</a>&nbsp;<a href="https://weibo.cn/fav/addFav/FuEwD9AX4?rl=0&amp;st=20bb87">收藏</a><!---->&nbsp;<span class="ct">11月12日 00:26</span></div></div><div class="s"></div><div class="c" id="M_FuceP4MK6"><div><span class="ctt">陈赫到底经历了什么？ ​​​</span>&nbsp;[<a href="https://weibo.cn/mblog/picAll/FuceP4MK6?rl=1">组图共2张</a>]</div><div><a href="https://weibo.cn/mblog/pic/FuceP4MK6?rl=0"><img src="http://wx2.sinaimg.cn/wap180/005F4Uyxgy1flb538nhq4j307o04agls.jpg" alt="图片" class="ib"></a>&nbsp;<a href="https://weibo.cn/mblog/oripic?id=FuceP4MK6&amp;u=005F4Uyxgy1flb538nhq4j307o04agls">原图</a>&nbsp;<a href="https://weibo.cn/attitude/FuceP4MK6/add?uid=5587613175&amp;rl=0&amp;st=20bb87">赞[692691]</a>&nbsp;<a href="https://weibo.cn/repost/FuceP4MK6?uid=5187664653&amp;rl=0">转发[10841]</a>&nbsp;<a href="https://weibo.cn/comment/FuceP4MK6?uid=5187664653&amp;rl=0#cmtfrm" class="cc">评论[25270]</a>&nbsp;<a href="https://weibo.cn/fav/addFav/FuceP4MK6?rl=0&amp;st=20bb87">收藏</a><!---->&nbsp;<span class="ct">11月09日 00:25</span></div></div><div class="s"></div><div class="c" id="M_FuaEcdf5N"><div><span class="ctt">一个笨演员的自我修养<a href="https://weibo.cn/sinaurl?f=w&amp;u=http%3A%2F%2Ft.cn%2FRlYKgX8&amp;ep=FuaEcdf5N%2C5187664653%2CFuaEcdf5N%2C5187664653">安乐电影的秒拍视频</a> ​​​</span>&nbsp;<a href="https://weibo.cn/attitude/FuaEcdf5N/add?uid=5587613175&amp;rl=0&amp;st=20bb87">赞[200151]</a>&nbsp;<a href="https://weibo.cn/repost/FuaEcdf5N?uid=5187664653&amp;rl=0">转发[12479]</a>&nbsp;<a href="https://weibo.cn/comment/FuaEcdf5N?uid=5187664653&amp;rl=0#cmtfrm" class="cc">评论[12200]</a>&nbsp;<a href="https://weibo.cn/fav/addFav/FuaEcdf5N?rl=0&amp;st=20bb87">收藏</a><!---->&nbsp;<span class="ct">11月08日 20:22</span></div></div><div class="s"></div><div class="c" id="M_FtQGgc9mA"><div><span class="ctt">腿长到买不到裤子怎么办？ ​​​</span>&nbsp;<a href="https://weibo.cn/attitude/FtQGgc9mA/add?uid=5587613175&amp;rl=0&amp;st=20bb87">赞[316647]</a>&nbsp;<a href="https://weibo.cn/repost/FtQGgc9mA?uid=5187664653&amp;rl=0">转发[8460]</a>&nbsp;<a href="https://weibo.cn/comment/FtQGgc9mA?uid=5187664653&amp;rl=0#cmtfrm" class="cc">评论[53362]</a>&nbsp;<a href="https://weibo.cn/fav/addFav/FtQGgc9mA?rl=0&amp;st=20bb87">收藏</a><!---->&nbsp;<span class="ct">11月06日 17:33</span></div></div><div class="s"></div><div class="pa" id="pagelist"><form action="/u/5187664653" method="post"><div><a href="/u/5187664653?page=2">下页</a>&nbsp;<input name="mp" type="hidden" value="99"><input type="text" name="page" size="2" style="-wap-input-format: &quot;*N&quot;"><input type="submit" value="跳页">&nbsp;1/99页</div></form></div><div class="pm"><form action="/search/" method="post"><div><input type="text" name="keyword" value="" size="15"><input type="submit" name="smblog" value="搜微博"><input type="submit" name="suser" value="找人"><br><span class="pmf"><a href="/search/mblog/?keyword=%E5%91%A8%E6%9C%AB%E6%97%B6%E5%85%89&amp;rl=0" class="k">周末时光</a>&nbsp;<a href="/search/mblog/?keyword=%E5%8C%97%E7%94%B5%E9%98%BF%E5%BB%96%E6%B2%99&amp;rl=0" class="k">北电阿廖沙</a>&nbsp;<a href="/search/mblog/?keyword=%E7%BB%99%E9%9D%92%E5%AE%87%E6%9C%80%E5%BC%BA%E5%BA%94%E6%8F%B4&amp;rl=0" class="k">给青宇最强应援</a>&nbsp;<a href="/search/mblog/?keyword=solo%E5%87%BA%E9%81%93%E5%87%86%E5%A4%87&amp;rl=0" class="k">solo出道准备</a>&nbsp;<a href="/search/mblog/?keyword=%E5%A4%A7%E5%BC%A0%E4%BC%9F%E8%87%B4%E6%95%AC%E7%99%BE%E4%BD%8D%E6%98%A5%E6%99%9A%E8%89%BA%E4%BA%BA&amp;rl=0" class="k">大张伟致敬百位春晚艺人</a></span></div></form></div><div class="cd"><a href="#top"><img src="https://h5.sinaimg.cn/upload/2017/04/27/319/5e990ec2.gif" alt="TOP"></a></div><div class="pms"> <a href="https://weibo.cn">首页<span class="tk">!</span></a>.<a href="https://weibo.cn/topic/240489">反馈</a>.<a href="https://weibo.cn/page/91">帮助</a>.<a href="http://down.sina.cn/weibo/default/index/soft_id/1/mid/0">客户端</a>.<a href="https://weibo.cn/spam/?rl=0&amp;type=3&amp;fuid=5187664653" class="kt">举报</a>.<a href="http://passport.sina.cn/sso/logout?r=https%3A%2F%2Fweibo.cn%2Fpub%2F%3Fvt%3D&amp;entry=mweibo">退出</a></div><div class="c">设置:<a href="https://weibo.cn/account/customize/skin?tf=7_005&amp;st=20bb87">皮肤</a>.<a href="https://weibo.cn/account/customize/pic?tf=7_006&amp;st=20bb87">图片</a>.<a href="https://weibo.cn/account/customize/pagesize?tf=7_007&amp;st=20bb87">条数</a>.<a href="https://weibo.cn/account/privacy/?tf=7_008&amp;st=20bb87">隐私</a></div><div class="c">彩版|<a href="http://m.weibo.cn/?tf=7_010">触屏</a>|<a href="https://weibo.cn/page/521?tf=7_011">语音</a></div><div class="b">weibo.cn[12-01 13:32]</div></body>')
    divs = selector.xpath('body/div[@class="c" and @id]') #当页的所有微博
    for div in divs:
        try:
            T_id = div.xpath('@id').extract_first()  # 微博id
            print T_id
            content = div.xpath('div/span[@class="ctt"]/text()').extract()  # 微博内容
            print content
            GPS = div.xpath('div/a/@href').extract()  # 定位坐标，注意是个链接，能直接用第三方标注在地图上
            print GPS
            liked = re.findall('赞\[(\d+)\]'.decode('utf8'), div.extract())  # 点赞数
            print liked
            transfer = re.findall('转发\[(\d+)\]'.decode('utf8'), div.extract())  # 转载数
            print transfer
            comment = re.findall('评论\[(\d+)\]'.decode('utf8'), div.extract())  # 评论数
            print comment
            #comment_url = div.xpath('div/a[@class="cc"]/@href').extract() #评论页地址
            #comment_url = 'https://weibo.cn/comment/' + str(T_id[2:]) + '?uid=' + str(U_ID) + '&page=1'
            tp = div.xpath('div/span[@class="ct"]/text()').extract()
            print tp
            Up_time = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M') # 当前时间
            print Up_time

            print '==================='
        except Exception as e:
            print '擦擦擦' + str(e)

a = a()
a


import datetime, re
def Date_Measure(date):
    try:
        if u'年' in date:
            return 100  # 随便写个大于7的
        elif u'月' in date:
            YMD = datetime.datetime.now().strftime('%Y-%m-%d').split('-')
            now = datetime.datetime(int(YMD[0]), int(YMD[1]), int(YMD[2]))
            a = re.findall('(\d+)月(\d+)日', date)
            old = datetime.datetime(int(YMD[0]), int(a[0][0]), int(a[0][1]))
            b = now - old
            try:
                c = re.findall('(\d*)\sday', str(b))[0]
            except:
                pass
            return int(c)
        else:  # 今天的帖子
            return 0
    except Exception as e:
        print '日期测量错误' + str(e)
a = Date_Measure('11月29日 17:15')
print a

a = ()
print (a == ())
'''

import re
url = 'https://weibo.cn/u/5187664653|||dcN'
last = re.findall('\|\|\|(.*)', url)  # 末尾信息
r = re.compile('\|\|\|.*')
newurl = r.sub('', url)
sign0 = last[0][:-1]
sign1 = last[0][-1]
print last
print sign0, sign1



