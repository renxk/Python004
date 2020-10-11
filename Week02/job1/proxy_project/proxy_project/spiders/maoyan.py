import scrapy
from scrapy.selector import Selector

from proxy_project.items import ProxyProjectItem


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/films?showType=3&offset=0']

    def parse(self, response):
        print('开始解析数据:')
        movies = Selector(response=response).xpath('//div[@class="movie-hover-info"]')
        for movie in movies:
            title = movie.xpath('./div[@class="movie-hover-title"][1]/span/text()').extract_first().strip()
            type = movie.xpath('./div[@class="movie-hover-title"][2]/text()')[1].extract().strip()
            time = movie.xpath('./div[@class="movie-hover-title movie-hover-brief"]/text()')[1].extract().strip()

            item = ProxyProjectItem()
            item['name'] = title
            item['type'] = type
            item['time'] = time
            yield item