# encoding=utf-8

# 感谢九茶<http://blog.csdn.net/bone_ace>提供的cookie函数

import base64
import os
import requests
import time
import json
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import logging
from yumdama import identify

IDENTIFY = 1  # 验证码输入方式:        1:看截图aa.png，手动输入     2:云打码
COOKIE_GETWAY = 0 # 0 代表从https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.18) 获取cookie   # 1 代表从https://weibo.cn/login/获取Cookie
dcap = dict(DesiredCapabilities.PHANTOMJS)  # PhantomJS需要使用老版手机的user-agent，不然验证码会无法通过
dcap["phantomjs.page.settings.userAgent"] = (
    "Mozilla/5.0 (Linux; U; Android 2.3.6; en-us; Nexus S Build/GRK39F) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
)
logger = logging.getLogger(__name__)
logging.getLogger("selenium").setLevel(logging.WARNING)  # 将selenium的日志级别设成WARNING，太烦人

"""
    输入你的微博账号和密码，可去淘宝买，一元5个。
    建议买几十个，实际生产建议100+，微博反爬得厉害，太频繁了会出现302转移。
"""
myWeiBo = [
    ('liujuan86088@163.com', 'c456123'),
    ('as81313477@163.com', 'huyong123'),
    ('qq547778876@163.com', 'huyong123'),
    ('yu4369986@163.com', 'huyong123'),
    ('a331256202@163.com', 'c456123')
]


def getCookie(account, password):
    if COOKIE_GETWAY == 0:
        return get_cookie_from_login_sina_com_cn(account, password)
    elif COOKIE_GETWAY ==1:
        return get_cookie_from_weibo_cn(account, password)
    elif COOKIE_GETWAY == 2:
        return get_cookie_from_weibo(account, password)
    else:
        logger.error("COOKIE_GETWAY Error!")

def get_cookie_from_login_sina_com_cn(account, password):
    """ 获取一个账号的Cookie """
    loginURL = "https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.18)"
    username = base64.b64encode(account.encode("utf-8")).decode("utf-8")
    postData = {
        "entry": "sso",
        "gateway": "1",
        "from": "null",
        "savestate": "30",
        "useticket": "0",
        "pagerefer": "",
        "vsnf": "1",
        "su": username,
        "service": "sso",
        "sp": password,
        "sr": "1440*900",
        "encoding": "UTF-8",
        "cdult": "3",
        "domain": "sina.com.cn",
        "prelt": "0",
        "returntype": "TEXT",
    }
    session = requests.Session()
    r = session.post(loginURL, data=postData)
    jsonStr = r.content.decode("gbk")
    info = json.loads(jsonStr)
    if info["retcode"] == "0":
        logger.warning("Get Cookie Success!( Account:%s )" % account)
        cookie = session.cookies.get_dict()
        return json.dumps(cookie)
    else:
        logger.warning("Failed!( Reason:%s )" % info["reason"])
        return ""


def get_cookie_from_weibo_cn(account, password):
    """ 获取一个账号的Cookie """
    try:
        browser = webdriver.PhantomJS(desired_capabilities=dcap)
        browser.get("https://weibo.cn/login/")
        time.sleep(1)

        failure = 0
        while u"微博" in browser.title and failure < 5:
            failure += 1
            browser.save_screenshot("/Users/WJY/Desktop/check_pic/aa.png") #存放验证码的位置
            username = browser.find_element_by_name("mobile")
            username.clear()
            username.send_keys(account)

            psd = browser.find_element_by_xpath('//input[@type="password"]')
            psd.clear()
            psd.send_keys(password)
            try:
                code = browser.find_element_by_name("code")
                code.clear()
                if IDENTIFY == 1:
                    code_txt = raw_input(u"请查看路径下新生成的aa.png，然后输入验证码:")  # 手动输入验证码
                else:
                    from PIL import Image
                    img = browser.find_element_by_xpath(u'//form[@method="post"]/div/img[@alt="请打开图片显示"]')
                    x = img.location["x"]
                    y = img.location["y"]
                    im = Image.open("aa.png")
                    im.crop((x, y, 100 + x, y + 22)).save("ab.png")  # 剪切出验证码
                    code_txt = identify()  # 验证码打码平台识别
                code.send_keys(code_txt)
            except Exception, e:
                pass

            commit = browser.find_element_by_name("submit")
            commit.click()
            time.sleep(3)
            if u"我的首页" not in browser.title:
                time.sleep(4)
            if u'未激活微博' in browser.page_source:
                print u'账号未开通微博'
                return {}

        cookie = {}
        if u"我的首页" in browser.title:
            for elem in browser.get_cookies():
                cookie[elem["name"]] = elem["value"]
            logger.warning("Get Cookie Success!( Account:%s )" % account)
        return json.dumps(cookie)
    except Exception, e:
        logger.warning("Failed %s!" % account)
        return ""
    finally:
        try:
            browser.quit()
        except Exception, e:
            pass

def get_cookie_from_weibo(username, password):
    driver = webdriver.Chrome()
    driver.get('https://weibo.cn')
    assert u"微博" in driver.title
    login_link = driver.find_element_by_link_text(u'登录')
    ActionChains(driver).move_to_element(login_link).click().perform()
    login_name = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "loginName"))
    )
    login_password = driver.find_element_by_id("loginPassword")
    login_name.send_keys(username)
    login_password.send_keys(password)
    login_button = driver.find_element_by_id("loginAction")
    login_button.click()
    cookie = driver.get_cookies()
    driver.close()
    return json.dumps(cookie)


def initCookie(rconn):
    """ 获取所有账号的Cookies，存入Redis。如果Redis已有该账号的Cookie，则不再获取。 """
    for weibo in myWeiBo:
        if rconn.get("Cookies:%s--%s" % (weibo[0], weibo[1])) is None:  #我这里不打算区分三个爬虫的cookie，直接都叫Cookies，对应下账号密码就行了
            cookie = getCookie(weibo[0], weibo[1])
            if len(cookie) > 0:
                rconn.set("Cookies:%s--%s" % (weibo[0], weibo[1]), cookie)
    cookieNum = "".join(rconn.keys()).count("Cookies")
    logger.warning("The num of the cookies is %s" % cookieNum)
    if cookieNum == 0:
        logger.warning('Stopping...')
        os.system("pause")

def updateCookie(accountText, rconn):
    """ 更新一个账号的Cookie """
    account = accountText.split("--")[0]
    password = accountText.split("--")[1]
    cookie = getCookie(account, password)
    if len(cookie) > 0:
        logger.warning("The cookie of %s has been updated successfully!" % account)
        rconn.set("Cookies:%s" % (accountText), cookie)
    else:
        logger.warning("The cookie of %s updated failed! Remove it!" % accountText)
        removeCookie(accountText, rconn)


def removeCookie(accountText, rconn):
    """ 删除某个账号的Cookie """
    rconn.delete("%s:Cookies:%s" % (accountText))
    cookieNum = "".join(rconn.keys()).count("Cookies")
    logger.warning("The num of the cookies left is %s" % cookieNum)
    if cookieNum == 0:
        logger.warning("Stopping...")
        os.system("pause")