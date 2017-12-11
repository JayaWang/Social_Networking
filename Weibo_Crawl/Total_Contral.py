# -*- coding: utf-8 -*-

#统筹迟几天再做，先处理人工选定的微博数据
from Weibo_Crawl.With_DB import Redis_DB

'''commentlist = ['https://weibo.cn/comment/FxOfQdiA4?uid=1914100420&rl=0&page=400',
               'https://weibo.cn/comment/FwHPOe9Kc?uid=1914100420&rl=0&page=400',
               'https://weibo.cn/comment/FvFsS0JZW?uid=1914100420&rl=0&page=400',
               'https://weibo.cn/comment/FvkUDhD8V?uid=1914100420&rl=0&page=400',
               'https://weibo.cn/comment/FtzCXosjN?uid=1914100420&rl=0&page=400',
               'https://weibo.cn/comment/FtwaBAEGv?uid=1914100420&rl=0&page=400',
               'https://weibo.cn/comment/FsupvAEoA?uid=1914100420&rl=0&page=400',
               'https://weibo.cn/comment/FxQrSpxtf?uid=1563815015&rl=0&page=400',
               'https://weibo.cn/comment/FuXNanECs?uid=1563815015&rl=0&page=400',
               'https://weibo.cn/comment/FsvbyaXRa?uid=1563815015&rl=0&page=400',
               'https://weibo.cn/comment/FtD5KyGQU?uid=1563815015&rl=0&page=400',
               'https://weibo.cn/comment/FuEkynIFm?uid=3125046087&rl=0&page=400',
               'https://weibo.cn/comment/Fsv4uwESM?uid=3125046087&rl=0&page=400',
               'https://weibo.cn/comment/Fx1fhfSxr?uid=1880246651&rl=0&page=400',
               'https://weibo.cn/comment/FwKHXbmoz?uid=1880246651&rl=0&page=400',
               'https://weibo.cn/comment/FwHn8xV94?uid=1880246651&rl=0&page=400',
               'https://weibo.cn/comment/FsrOenUgq?uid=6182961391&rl=0&page=400',
               'https://weibo.cn/comment/FwMEsmCoh?uid=6292896728&rl=0&page=400',
               'https://weibo.cn/comment/FvFF6ykgZ?uid=2609400635&rl=0&page=400',
               'https://weibo.cn/comment/FuCN3h9I5?uid=2609400635&rl=0&page=400',
               'https://weibo.cn/comment/Fssu5nBci?uid=1648887267&rl=0&page=400',
               'https://weibo.cn/comment/FvGVeeYne?uid=1713031610&rl=0&page=400',
               'https://weibo.cn/comment/FvISk9FAS?uid=1288640027&rl=0&page=400',
               'https://weibo.cn/comment/FssBY9QlK?uid=1343887012&rl=0&page=400',
               'https://weibo.cn/comment/FssfN0l99?uid=3800468188&rl=0&page=400',
               'https://weibo.cn/comment/FwJ7PwDiE?uid=1309248901&rl=0&page=400',
               'https://weibo.cn/comment/FwIjQqZQB?uid=1763990660&rl=0&page=400',
               'https://weibo.cn/comment/FtxlTEEd1?uid=1715351501&rl=0&page=400',
               'https://weibo.cn/comment/FsrzyzqXD?uid=1567261593&rl=0&page=400',
               'https://weibo.cn/comment/FwLXdlcd4?uid=1307418975&rl=0&page=400',
               'https://weibo.cn/comment/FvkYZAt0h?uid=5241260567&rl=0&page=400',
               'https://weibo.cn/comment/Fv1XvxW9l?uid=5241260567&rl=0&page=400',
               'https://weibo.cn/comment/FuBphCgtl?uid=5241260567&rl=0&page=400',
               'https://weibo.cn/comment/FtAqQhB8w?uid=1235919683&rl=0&page=400',
               'https://weibo.cn/comment/FtvRIiieY?uid=1235919683&rl=0&page=400',
               'https://weibo.cn/comment/FtnfvcoW8?uid=1235919683&rl=0&page=400',
               'https://weibo.cn/comment/FtvRAxQAR?uid=1302929461&rl=0&page=400',
               'https://weibo.cn/comment/Ftw9VE82u?uid=2703557921&rl=0&page=400',
               'https://weibo.cn/comment/FtzJHwibO?uid=1305651895&rl=0&page=400',
               'https://weibo.cn/comment/Ftxfj3wq6?uid=1305651895&rl=0&page=400',
               'https://weibo.cn/comment/Ftvt4wZEU?uid=1305651895&rl=0&page=400',
               'https://weibo.cn/comment/FvGM4kBgq?uid=1391230884&rl=0&page=400',
               'https://weibo.cn/comment/FvlBNvoyI?uid=1646469930&rl=0&page=400',
               'https://weibo.cn/comment/FuKdk9puC?uid=1646469930&rl=0&page=400',
               'https://weibo.cn/comment/FuzH0rLuM?uid=1646469930&rl=0&page=400',
               'https://weibo.cn/comment/FuAjQFPnd?uid=1506711913&rl=0&page=400',
               'https://weibo.cn/comment/FuJDtb8o4?uid=1773061573&rl=0&page=400',
               'https://weibo.cn/comment/FuAKN6ymt?uid=1773061573&rl=0&page=400',
               'https://weibo.cn/comment/FuDqJz8ph?uid=2687827715&rl=0&page=400',
               'https://weibo.cn/comment/FwHQGi1gF?uid=1757744065&rl=0&page=400',
               'https://weibo.cn/comment/FvDAXjNKR?uid=1497874613&rl=0&page=400',
               'https://weibo.cn/comment/FwMcAAy2c?uid=1246229612&rl=0&page=400',
               'https://weibo.cn/comment/FxQDtlXmC?uid=2286552551&rl=0&page=400',
               'https://weibo.cn/comment/FxQ78r0MK?uid=2286552551&rl=0&page=400',
               'https://weibo.cn/comment/FxLIDpIlz?uid=2286552551&rl=0&page=400'] #抓评论主页'''

commentlist = [
    'https://weibo.cn/comment/FyI6CBc5S?uid=1195300800&rl=0&page=200',
    'https://weibo.cn/comment/FyOt97bDN?uid=1195300800&rl=0&page=200',
    'https://weibo.cn/comment/FyPw16hLW?uid=1195300800&rl=0&page=200',
    'https://weibo.cn/comment/FyTKr9sj1?uid=1195300800&rl=0&page=200',
    'https://weibo.cn/comment/FyTKXFGLP?uid=1195300800&rl=0&page=200',
    'https://weibo.cn/comment/FyTNstQWN?uid=1195300800&rl=0&page=200',
    'https://weibo.cn/comment/FyTRyCWKI?uid=1195300800&rl=0&page=200',
    'https://weibo.cn/comment/FyTYwC5YG?uid=1195300800&rl=0&page=200',
    'https://weibo.cn/comment/FyUbRpYTW?uid=1195300800&rl=0&page=200',
    'https://weibo.cn/comment/FyX7cAcGw?uid=1195300800&rl=0&page=200',
    'https://weibo.cn/comment/FyXecqwyM?uid=1195300800&rl=0&page=200',
    'https://weibo.cn/comment/FyXgS8JQG?uid=1195300800&rl=0&page=200',
    'https://weibo.cn/comment/Fz0kREGx6?uid=1195300800&rl=0&page=200',
    'https://weibo.cn/comment/Fz0TS1wns?uid=1195300800&rl=0&page=200',
    'https://weibo.cn/comment/Fz12Jllhx?uid=1195300800&rl=0&page=200',
    'https://weibo.cn/comment/Fz1shdTRH?uid=1195300800&rl=0&page=200',
    'https://weibo.cn/comment/Fz2Sn6sbI?uid=1195300800&rl=0&page=200',
    'https://weibo.cn/comment/Fz6Ehz4I1?uid=1195300800&rl=0&page=200',
    'https://weibo.cn/comment/Fz6GWFx0w?uid=1195300800&rl=0&page=200',
    'https://weibo.cn/comment/Fz78Ov6ZI?uid=1195300800&rl=0&page=200',
    'https://weibo.cn/comment/Fz7L44hJ5?uid=1195300800&rl=0&page=200',
    'https://weibo.cn/comment/Fz824DMwr?uid=1195300800&rl=0&page=200',
    'https://weibo.cn/comment/Fz9b3solv?uid=1195300800&rl=0&page=200',
    'https://weibo.cn/comment/Fz9bAg9tg?uid=1195300800&rl=0&page=200',
    'https://weibo.cn/comment/Fza95a8G0?uid=1195300800&rl=0&page=200',
    'https://weibo.cn/comment/FzaozuE0c?uid=1195300800&rl=0&page=200',
    'https://weibo.cn/comment/FzarIehN7?uid=1195300800&rl=0&page=200',
    'https://weibo.cn/comment/Fzb59tHF7?uid=1195300800&rl=0&page=200',
    'https://weibo.cn/comment/Fzb9bpXWW?uid=1195300800&rl=0&page=200',
    'https://weibo.cn/comment/Fzb9MFX9M?uid=1195300800&rl=0&page=200',
    'https://weibo.cn/comment/FzbdHgl9y?uid=1195300800&rl=0&page=200',
    'https://weibo.cn/comment/FzbfS1iU9?uid=1195300800&rl=0&page=200',
    'https://weibo.cn/comment/Fzbhl1XA4?uid=1195300800&rl=0&page=200',
    'https://weibo.cn/comment/FzbkS08oY?uid=1195300800&rl=0&page=200',
    'https://weibo.cn/comment/FzbC2EeoY?uid=1195300800&rl=0&page=200',
    'https://weibo.cn/comment/FzbILxZde?uid=1195300800&rl=0&page=200',
    'https://weibo.cn/comment/Fz98f7SDq?uid=1195300800&rl=0&page=200'
]

def Yanyuan():
    print 'begin'
    r0 = Redis_DB(0) #反正全部插入到db0里好了
    for i in commentlist:
        url = i + '|||notimeN'
        r0.Insert_Redis('Comment_urls', url)
    url0 = 'https://weibo.cn/u/5822309693?f=search_0|||ZRTGN'
    r0.Insert_Redis('Target_urls', url0)
    print 'end'

a = Yanyuan()
a
