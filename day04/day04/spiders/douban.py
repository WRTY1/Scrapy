import time
import scrapy

from day04.items import DoubanItem

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['www.douban.com']
    #start_urls = ['https://movie.douban.com/top250?start=0&filter=']
    url = 'https://movie.douban.com/top250?start={}&filter='
    def start_requests(self):
        for i in range(0,250,25):
            url=self.url.format(i)
            self.offset = i/25+1
            yield scrapy.Request(
                url=url,
                callback=self.parse,
                cb_kwargs= {'no':i/25 +1}
            )

    def parse(self, response,no):
        films1_name = response.xpath('//div[@class="info"]/div/a/span[1]/text()').extract()
        item = DoubanItem() 
        item['no'] = no
        item['films_name'] = films1_name
        print(films1_name)
        return item
