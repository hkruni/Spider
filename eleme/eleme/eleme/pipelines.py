# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import Image
from genericpath import getsize
import time

import MySQLdb.cursors
from scrapy import log
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from twisted.enterprise import adbapi
from scrapy.exceptions import DropItem


#最先执行from_crawler，然后执行__init__，再执行open_spider，关闭时执行close_spider
class InsertItemPipe(object):
    def __init__(self, dbargs):
        print 'InsertItemPipe_init'
        self.dbargs = dbargs
    
    #当spider刚启动时，这个方法被调用
    def open_spider(self,spider):
        print 'open_spider'
        self.dbpool = adbapi.ConnectionPool('MySQLdb', **(self.dbargs))
    #当spider最终关闭时，这个方法被调用
    def close_spider(self,spider):
        print 'close_spider'
        self.dbpool.close()
        
    @classmethod
    def from_crawler(cls,crawler):
        print 'InsertItemPipe from_crawler'
        settings = crawler.settings
        print settings
        dbargs = dict(
                      host=settings['MYSQL_HOST'],
                      db=settings['MYSQL_DBNAME'],
                      user=settings['MYSQL_USER'],
                      passwd=settings['MYSQL_PASSWD'],
                      port=settings['MYSQL_PORT'],
                      charset='utf8',
                      cursorclass = MySQLdb.cursors.DictCursor,
                      use_unicode= True,
                      )
        print dbargs
        return cls(dbargs)
        
    def process_item(self, item, spider):
        self.dbpool.runInteraction(self.insertTitleSql,item)
        return item
    
    def insertTitleSql(self,tx,item):
                
        sql = "insert into eleme"
        sql_insert = sql + "(name,address,recent_order_num,rating,url,imageUrl) values(%s,%s,%s,%s,%s,%s)"
        
        tx.execute(sql_insert,(item['name'],item['address'], 
                               item['recent_order_num'],item['rating'],item['url'],item['imageUrl']))
        
        
        
        
class ElemeImagesPipe(ImagesPipeline):
    def get_media_requests(self, item, info):
        #请求回去每张图片
        yield scrapy.Request(item['imageUrl'])
            
    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        return item
