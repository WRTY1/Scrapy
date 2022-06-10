# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json

class DoubanPipeline(object):
    def open_spider(self,spider):
        self.items = []
    def process_item(self, item, spider):
        #jsonStr = json.dumps((item['films_name']),ensure_ascii=False).strip("[").replace("]","\n").replace(",","\n")
        #jsonStr = json.dumps(dict(item),ensure_ascii=False)
        #with open("films.json","a",encoding="utf_8") as f:
            #f.write(jsonStr)
            #f.write("\n")
        self.items.append(item)
        return item
    
    def close_spider(self,spider):
        #以下为json
        '''
        with open('films.json','w',encoding='utf-8') as f:
            f.write("{")
            self.items.sort(key = lambda i:i['no'])
            for item in self.items:
                cont = '{}\n'.format(str(item['films_name']).replace("'","\""))
                f.write(cont)
            f.write("}")
        '''
        #以下为csv
        with open('films.csv','w',encoding='utf-8') as f:
            self.items.sort(key = lambda i:i['no'])
            for item in self.items:
                cont = '{}\n'.format(str(item['films_name']).replace("'","").strip("[").strip("]"))
                f.write(cont)