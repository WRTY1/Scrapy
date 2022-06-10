from scrapy.cmdline import execute
import sys
import os

# 保证终端执行  "scrapy", "crawl", "bd" 这个命令运行不出现路径问题！（可以不写！）
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
#with open("films.json","w",encoding="utf_8") as f:
            #f.write("")
execute(["scrapy", "crawl", "douban"])