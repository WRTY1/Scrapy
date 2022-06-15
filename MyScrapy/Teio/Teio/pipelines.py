# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class TeioPipeline(object):
    def process_item(self,item,spider):
        with open('urlList.csv','w',encoding='utf-8') as f:
            for cout in item["urlList"]:
                f.write(''.join(cout))
                f.write(',')
        return item