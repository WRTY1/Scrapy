
from gc import callbacks
from operator import itemgetter
from pkgutil import extend_path
from pkg_resources import yield_lines
import scrapy

from Teio.items import TeioItem


class TeiospiderSpider(scrapy.Spider):
    name = 'TeioSpider'
    rootUrl = 'https://rickschanze.github.io'
    no = 1
    def start_requests(self):
        startUrl = r"https://rickschanze.github.io/2022/02/11/%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84%E4%B8%8E%E7%AE%97%E6%B3%95/2022-02-11-%E9%9D%99%E6%80%81%E9%93%BE%E8%A1%A8/"
        item = TeioItem()
        item["urlList"] = []
        yield scrapy.Request(startUrl,callback=self.parse,meta={'item':item})
    def parse(self, response):
        item = response.meta['item']
        if(self.no == 1): 
            extenUrl = response.xpath("//div[@class = 'prev-post pull-full']/a/@href").extract()
            item["urlList"].append(response.xpath("//div[@class = 'prev-post pull-full']/a/img/@src").extract())
        else: 
            extenUrl = response.xpath("//div[@class = 'prev-post pull-left']/a/@href").extract()
            item["urlList"].append(response.xpath("//div[@class = 'prev-post pull-left']/a/img/@src").extract())
        print(self.no)
        self.no+=1
        if(not self.no >= 10):
        #if(len(extenUrl)):
            url = (self.rootUrl + extenUrl[0]).replace("\t","")
            print(url)
            print(item)
            yield scrapy.Request(url=url,callback=self.parse,meta={'item':item})
        else:
            print("finished:",item)
            yield item

    '''
    def parse(self, response):
        item = TeioItem()
        #item["number"] = response.xpath("//div[@class = 'prev-post pull-left']/a/img/@src").extract()
        extenUrl = response.xpath("//div[@class = 'prev-post pull-full']/a/@href").extract()
        print(self.no)
        self.no+=1
        if(self.no >= 5):return item
        if(len(extenUrl)):
            url = (self.rootUrl + extenUrl[0]).replace("\t","")
            print(url)
            yield scrapy.Request(url=url,callback=self.parse,meta={'item':item})
        else:
            extenUrl = response.xpath("//div[@class = 'prev-post pull-left']/a/@href").extract()
        if(len(extenUrl)):
            url = (self.rootUrl + extenUrl[0]).replace("\t","")
            print(url)
            yield scrapy.Request(url=url,callback=self.parse,meta={'item':item})


        #else:
            #return item
            '''