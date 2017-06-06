# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from datetime import datetime

class ImdbPipeline(object):
    def open_spider(self, spider):
        name = str(datetime.now())
        name = name[:13].replace(' ', '_')
        name = name.replace('-', '_')
        self.file = open('imdb_'+name+'.json', 'ab')
        self.file.write("[\n")
    def close_spider(self, spider):
        self.file.write("]")
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + ",\n"
        self.file.write(line)
        return item

