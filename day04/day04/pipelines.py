# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json

class DoubanPipeline:
    def process_item(self, item, spider):
        jsonStr = json.dumps(dict(item),ensure_ascii=False)
        with open("films.txt","w",encoding="utf_8") as f:
            f.write(jsonStr)
        return item
