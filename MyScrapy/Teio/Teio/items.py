# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
class TeioItem(scrapy.Item):
    # define the fields for your item here like:
    urlList = scrapy.Field()
    nextUrl = scrapy.Field()
    #extendUrl = scrapy.Field()