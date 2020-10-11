# _*_ encoding:utf-8 _*_
# Author: renxk
# date: 2020/10/10 11:29 上午

"""
画图工具类登录
"""

import requests
from fake_useragent import UserAgent
from lxml import  etree
from time import *

class Processon:
    def __init__(self):
        self.ua = UserAgent()
        self.session = requests.session()

    def goto_page(self, url = '', referer = ''):
        headers = {
            'User-Agent': self.ua.random,
        }
        if len(referer) > 0:
            headers['Referer'] = referer

        #访问页面
        self.session.get(url=url, headers = headers)


    def login(self, referer = ''):
        headers = {
            'User-Agent' : self.ua.random,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        if len(referer) > 0:
            headers['Referer'] = referer

        #登录
        form_data = {
            'login_email' : '18581877141',
            'login_password' : 'rxk123456'
        }
        respons = self.session.post(
            url = 'https://processon.com/login',
            data = form_data,
            headers = headers
        )
        if respons.status_code == 200:
            return self.handle_login_data(html_content=respons.text)
        else:
            return (respons.status_code, respons.reason)

    def handle_login_data(self, html_content):
        html = etree.HTML(html_content)
        result = html.xpath('/html/head/title/text()')[0]
        if '登录' in result:
            error = "登录失败"
            try:
                result1 = html.xpath('//div[@class="error-tip email-error-tip"]/text()')
                if len(result1) > 0:
                    result1 = result1[0]
                    error = result1

                result2 = html.xpath('//div[@class="error-tip pass-error-tip"]/text()')
                if len(result2) > 0:
                    result2 = result2[0]
                    error = result2

                return (0, str(error))
            except Exception as error:
                print(error)
                return (0, '登录失败')

        return (200, '登录成功')

    def manage_logo(self):
        #进入首页
        home_url = 'https://processon.com'
        self.goto_page(url=home_url)
        sleep(1.0)
        #进入登录页面
        login_url = 'https://processon.com/login?f=index'
        self.goto_page(url=login_url, referer=home_url)
        sleep(1.0)
        (code, result) = self.login(referer=login_url)
        if code == 200:
            print('登录成功')
        else:
            print('登录失败:' + result)
if __name__ == '__main__':
    Processon().manage_logo()



