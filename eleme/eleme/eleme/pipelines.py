# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import MySQLdb.cursors
from scrapy import log
import scrapy
from twisted.enterprise import adbapi


class InsertItemPipe(object):
    def __init__(self, dbargs):
        self.dbargs = dbargs
    
    def open_spider(self,spider):
        self.dbpool = adbapi.ConnectionPool('MySQLdb', **(self.dbargs))
        
    def close_spider(self,spider):
        self.dbpool.close()
        
    @classmethod
    def from_crawler(cls,crawler):
        settings = crawler.settings
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
        return cls(dbargs)
        
    def process_item(self, item, spider):
        self.dbpool.runInteraction(self.insertTitleSql,item)
        return item
    
    def insertTitleSql(self, tx,item):
                
        sql = "insert into eleme"
        sql_insert = sql + "(name,address,recent_order_num,rating,url,imageUrl) values(%s,%s,%s,%s,%s,%s)"
        
        tx.execute(sql_insert,(item['name'],item['address'], 
                               item['recent_order_num'],item['rating'],item['url'],item['imageUrl']))
