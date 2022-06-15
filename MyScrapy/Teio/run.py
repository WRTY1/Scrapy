from scrapy.cmdline import execute
import os,sys
nowPath=os.path.dirname(os.path.abspath(__file__))
sys.path.append(nowPath)
execute(["scrapy", "crawl", "TeioSpider"])