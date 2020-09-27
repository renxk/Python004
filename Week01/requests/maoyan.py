import requests
import random
from bs4 import BeautifulSoup
import os
import csv

user_agents = [
    'Mozilla/5.0 (Linux; Android 6.0.1; Moto G (4)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Mobile Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15'
]


class maoyan_spider:
    def __init__(self):
        self.url = 'https://maoyan.com/films?offset=0'
        self.pageSize = 30
        self.request_header = {}
        self.fileName = 'requests_movice.csv'

    def clearFile(self):
        if os.path.exists(self.fileName):
            os.remove(self.fileName)
        with open(self.fileName, 'w', encoding='utf-8', newline='') as fh:
            csv_writer = csv.writer(fh)
            csv_writer.writerow(['名称', '类型', '上映时间'])

    def getUserAgent(self):
        return random.choice(user_agents)


    def getMaoYanHtml(self):
        # if os.path.exists('maoyan.html'):
        #     with open('maoyan.html', 'r') as fh:
        #         html = fh.read()
        #         return (200, html)

        self.request_header['User-Agent'] = self.getUserAgent()
        response = requests.get(self.url, headers = self.request_header);
        if (response.status_code == 200):
            # with open('maoyan.html', 'w') as fh:
            #     fh.write(response.text)
            return (200, response.text)
        else:
            return (response.status_code, response.reason)

    def parsingHtml(self, htmlContent = ''):
        bs = BeautifulSoup(htmlContent, 'html.parser')
        moveList = bs.find_all('div', attrs={'class' : 'movie-info'})
        for item in moveList:
            # print(item)
            name = item.find("div", attrs={"class" : "title"}).text
            type = item.find('div', attrs = {'class' : 'actors'}).text
            time = item.find('div', attrs = {'class' : 'show-info'}).text
            self.saveMoviesData(name=name, type=type, time=time)

    def saveMoviesData(self, name ='', type = '', time = ''):
        print('电影名称:' + name)
        print('电影类型:' + type)
        print('上映时间:' + time)
        print('=' * 20)
        with open(self.fileName, 'a', encoding='utf-8', newline='') as fh:
            csv_writer = csv.writer(fh)
            csv_writer.writerow([name, type, time])

    def manage(self):
        self.clearFile()
        (code, result) = self.getMaoYanHtml()
        if code == 200:
            self.parsingHtml(result)
        else:
            print(result)

if __name__ == '__main__':
    maoyan_spider().manage()
