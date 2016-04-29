# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import redis


class GetGoogleStoreCategoryPipeline(object):

    def __init__(self):
        self.server = redis.Redis(host='localhost', port=6379)

    def process_item(self, item, spider):
        key = item['cat']
        name = "GoogleStoreCategory"
        value = 1
        self.server.hset(name, key, value)
        return item
