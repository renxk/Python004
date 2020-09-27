import scrapy

from scrapy.selector import Selector

from maoyan.items import MaoyanItem

class MaoyanSpidersSpider(scrapy.Spider):
    name = 'maoyan_spiders'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/']


    def start_requests(self):
        url = 'https://maoyan.com/films?showType=3&offset=0'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print('开始解析数据:')
        movies = Selector(response=response).xpath('//div[@class="movie-hover-info"]')
        for movie in movies:
            title = movie.xpath('./div[@class="movie-hover-title"][1]/span/text()').extract_first().strip()
            type = movie.xpath('./div[@class="movie-hover-title"][2]/text()')[1].extract().strip()
            time = movie.xpath('./div[@class="movie-hover-title movie-hover-brief"]/text()')[1].extract().strip()

            item = MaoyanItem()
            item['name'] = title
            item['type'] = type
            item['time'] = time
            yield item