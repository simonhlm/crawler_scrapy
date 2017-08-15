# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs
import csv

class RecruitPipeline(object):

    def process_item(self, item, spider):
        with codecs.open('result.csv','a',encoding='utf-8') as self.f:
            headers = [ k for k in item]
            my_writer = csv.DictWriter(self.f, fieldnames = headers)
            #for x in item:
            my_writer.writerow(item)
                #self.f.write(item[x])
            #self.f.write('\n')
        return item
